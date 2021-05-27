#! /usr/bin/env python
"""
A basic network inventory generation script. 

Goal: 
 - Create a CSV inventory file 
    device name, software version, uptime, serial number

"""

from pyats.topology.loader import load
from genie.libs.parser.utils.common import ParserNotFound
from genie.metaparser.util.exceptions import SchemaEmptyParserError

def parse_command(device, command): 
    """
    Attempt to parse a command on a device with pyATS.
    In case of common errors, return best info possible.
    """

    print(f"Running command {command} on device {device.name}")
    try: 
        output = device.parse(command)
        return {"type": "parsed", "output": output}
    except ParserNotFound: 
        print(f"  Error: pyATS lacks a parser for device {device.name} with os {device.os}. Gathering raw output to return.")
    except SchemaEmptyParserError: 
        print(f"  Error: No valid data found from output from device {device.name}. Gathering raw output to return.")

    # device.execute runs command, gathers raw output, and returns as string
    output = device.execute(command)
    return {"type": "raw", "output": output}

def get_device_inventory(device, show_version, show_inventory): 
    """
    Given a testbed device and the output dictionaries, return the 
    required network inventory data for the device. Must consider 
    device OS and address raw/parsed output appropriately.

    return (device_name, device_os, software_version, uptime, serial_number)
    """

    # Common device details from testbed device
    device_name = device.name
    device_os = device.os

    # Build inventory report data structure 
    #   IOS / IOS XE
    #     software version: show version output ["output"]["version"]["version"]
    #     uptime:           show version output ["output"]["version"]["uptime"]
    #     serial:           show inventory output ["main"]["chassis"][MODEL]["sn"]
    #   IOS XR
    #     software version: show version output ["output"]["software_version"]
    #     uptime:           show version output ["output"]["uptime"]
    #     serial:           show inventory output ["output"]["module_name"][MODULE]["sn"]
    #   NXOS 
    #     software version: show version output ["output"]["platform"]["software"]["system_version"]
    #     uptime:           show version output ["output"]["platform"]["kernel_uptime"] : 
    #                                  {'days': 6, 'hours': 20, 'minutes': 48, 'seconds': 59}
    #     serial:           show inventory output ["output"]["name"]["Chassis"]["serial_number"]
    #   ASA
    #     software version: show version RAW output "Cisco Adaptive Security Appliance Software Version 9.12(2)"
    #     uptime:           show version RAW output "up 6 days 20 hours"
    #     serial:           show inventory output ["Chassis"]["sn"]

    if device.os in ["ios", "iosxe"]: 
        software_version = show_version[device.name]["output"]["version"]["version"]
        uptime = show_version[device.name]["output"]["version"]["uptime"]
        serial_number = None
        # serial_number = show_inventory[device.name]["main"]["chassis"][MODEL]["sn"]
    elif device.os == "nxos": 
        software_version = show_version[device.name]["output"]["platform"]["software"]["system_version"]
        uptime = show_version[device.name]["output"]["platform"]["kernel_uptime"]
        serial_number = show_inventory[device.name]["output"]["name"]["Chassis"]["serial_number"]
    elif device.os == "iosxr": 
        software_version = show_version[device.name]["output"]["software_version"]
        uptime = show_version[device.name]["output"]["uptime"]
        serial_number = None
        # serial_number = show_inventory[device.name]["output"]["module_name"][MODULE]["sn"]
    elif device.os == "asa": 
        software_version = None
        uptime = None
        serial_number = show_inventory[device.name]["output"]["Chassis"]["sn"]
    else: 
        return False

    return (device_name, device_os, software_version, uptime, serial_number)

# Script entry point
if __name__ == "__main__": 
    import argparse

    print("Creating a network inventory script.")

    # Load pyATS testbed into script 
    # Use argparse to determine the testbed file : https://docs.python.org/3/library/argparse.html
    parser = argparse.ArgumentParser(description='Generate network inventory report from testbed')
    parser.add_argument('testbed', type=str, help='pyATS Testbed File')
    args = parser.parse_args()

    # Create pyATS testbed object
    print(f"Loading testbed file {args.testbed}")
    testbed = load(args.testbed)

    # Connect to network devices 
    testbed.connect(log_stdout=False)
    print(f"Connecting to all devices in testbed {testbed.name}")


    # Run commands to gather output from devices 
    show_version = {}
    show_inventory = {}

    for device in testbed.devices: 
        print(f"Gathering show version from device {device}")
        show_version[device] = parse_command(testbed.devices[device], "show version")
        print(f"{device} show version: {show_version[device]}")

        print(f"Gathering show inventory from device {device}")
        show_inventory[device] = parse_command(testbed.devices[device], "show inventory")
        print(f"{device} show inventory: {show_inventory[device]}")


    # Disconnect from network devices 
    for device in testbed.devices: 
        print(f"Disconnecting from device {device}.")
        testbed.devices[device].disconnect()

    # Build inventory report data structure 
    print("Assembling network inventory data from output.")
    network_inventory = []
    for device in testbed.devices: 
        network_inventory.append(
            get_device_inventory(testbed.devices[device], show_version, show_inventory)
            )

    print(f"network_inventory = {network_inventory}")

    # Generate CSV file of data