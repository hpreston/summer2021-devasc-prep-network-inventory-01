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


    # Disconnect from network devices 
    for device in testbed.devices: 
        print(f"Disconnecting from device {device}.")
        testbed.devices[device].disconnect()

    # Build inventory report data structure 


    # Generate CSV file of data