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


    # Generate CSV file of data