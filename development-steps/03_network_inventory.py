#! /usr/bin/env python
"""
A basic network inventory generation script. 

Goal: 
 - Create a CSV inventory file 
    device name, software version, uptime, serial number

"""

from pyats.topology.loader import load

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
        show_version[device] = testbed.devices[device].parse("show version")
        print(f"{device} show version: {show_version[device]}")

        print(f"Gathering show inventory from device {device}")
        show_inventory[device] = testbed.devices[device].parse("show inventory")
        print(f"{device} show inventory: {show_inventory[device]}")


    # Disconnect from network devices 
    for device in testbed.devices: 
        print(f"Disconnecting from device {device}.")
        testbed.devices[device].disconnect()

    # Build inventory report data structure 


    # Generate CSV file of data