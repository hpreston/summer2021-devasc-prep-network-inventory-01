# Summer 2021 DevNet Associate Preperation Webinar Series: Automating a Network Inventory with Python

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/hpreston/summer2021-devasc-prep-network-inventory-01)

This repository provides code and examples as part of a [DevNet Associate Certification Preparation Webinar Series](https://learningnetwork.cisco.com/s/article/devnet-associate-prep-program-in-one-place). The recording for this webinar, and others, can be found in the [DevNet Associate Prep Program Training Plan](https://learningnetwork.cisco.com/s/learning-plan-detail-standard?ltui__urlRecordId=a1c3i0000007q9cAAA&ltui__urlRedirect=learning-plan-detail-standard&t=1596603514739).

Slides from the webinar and discussions about the topic can be found in this [forum post from the Learning Network](https://learningnetwork.cisco.com/s/question/0D53i00001GCgmSCAT/devnet-associate-prep-automating-a-network-inventory-with-python?t=1623087847018).

### Automating a Network Inventory with Python

> It’s 3pm on Friday. You are already looking forward to your weekend and bingeing the latest season of your favorite show that just dropped. Your boss shows up and tells you he needs a full network inventory by Monday at 8am. He apologizes for ruining your weekend as he heads out to a concert. Can your newly learned network automation skills save your weekend?

## Using this repository 
If you'd like to explore the solution to the above use case yourself, here is everything you should need to know.  

### Lab/Sandbox Resources 
This example leverages the [Cisco NSO Reservable Sandbox from DevNet](https://devnetsandbox.cisco.com/RM/Diagram/Index/43964e62-a13c-4929-bde7-a2f68ad6b27c?diagramType=Topology).  You can reserve this sandbox for use with the [nso_sandbox_devices.xlsx](nso_sandbox_devices.xlsx) inventory spreadsheet.  

The network topology for the Sandbox can be seen with this [network diagram](NSO-Sandbox-Lab-Network-Topology.jpg).

If you have your own lab you'd like to try the network inventory script on, you will need to create your own inventory spreadsheet for your lab.  This use case shoudl support devices running Cisco IOS, IOS XE, IOS XR, NX-OS and ASA. 

### Creating the Python venv 
While other versions of Python will likley work, this use case was tested with Python 3.8.  It leverages [pyATS](https://developer.cisco.com/pyats) for interacting with network devices. 

```
# Create your Virtual Env
python3 -m venv venv
source venv/bin/activate
# Install the entire pyATS set of tools
pip install pyats[full]
# Install just the basics for this exercise
pip install pyats pyats.contrib genie
```

### Creating the pyATS Testbed File 
The pyATS YAML testbed is included with the GitHub repo, but you can create one from the Excel file with this command. 

```
pyats create testbed file \
--path nso_sandbox_devices.xlsx \
--output nso_sandbox_testbed.yaml
```

Some suggested improvements to the created testbed file include: 

* Move credentials from each device to testbed level
* `ASK{}` for Username as well as passwords

These changes are included in the [`improved_nso_sandbox_testbed.yaml`](improved_nso_sandbox_testbed.yaml) file. 

### Running the `network_inventory.py` script 
The [`network_inventory.py`](network_inventory.py) script in the repo should work and be ready to go.  

> Note: The sandbox credentials for devices are `cisco / cisco`

```
./network_inventory.py improved_nso_sandbox_testbed.yaml

# OUTPUT
Loading testbed file improved_nso_sandbox_testbed.yaml
Connecting to all devices in testbed improved_nso_sandbox_testbed
Gathering show version from device edge-firewall01
Running command show version on device edge-firewall01
  Error: pyATS lacks a parser for device edge-firewall01 with os asa. Gathering raw output to return.
Gathering show inventory from device edge-firewall01
Running command show inventory on device edge-firewall01
Gathering show version from device dist-rtr01
Running command show version on device dist-rtr01
Gathering show inventory from device dist-rtr01
Running command show inventory on device dist-rtr01
Gathering show version from device dist-rtr02
Running command show version on device dist-rtr02
Gathering show inventory from device dist-rtr02
Running command show inventory on device dist-rtr02
Gathering show version from device dist-sw01
Running command show version on device dist-sw01
Gathering show inventory from device dist-sw01
Running command show inventory on device dist-sw01
Gathering show version from device dist-sw02
Running command show version on device dist-sw02
Gathering show inventory from device dist-sw02
Running command show inventory on device dist-sw02
Gathering show version from device edge-sw01
Running command show version on device edge-sw01
Gathering show inventory from device edge-sw01
Running command show inventory on device edge-sw01
  Error: No valid data found from output from device edge-sw01. Gathering raw output to return.
Gathering show version from device internet-rtr01
Running command show version on device internet-rtr01
Gathering show inventory from device internet-rtr01
Running command show inventory on device internet-rtr01
Assembling network inventory data from output.
Writing inventory to file 2021-05-27-15-41- 13_improved_nso_sandbox_testbed_network_inventory.csv.
```

And it will create a CSV report that looks like 

```csv
device_name,device_os,software_version,uptime,serial_number 
edge-firewall01,asa,9.12(2),7 days 1 hour,9ACJJ5Q1Q1X 
core-rtr01,iosxr,6.3.1,"1 week, 1 hour, 10 minutes",N/A 
core-rtr02,iosxr,6.3.1,"1 day, 23 hours, 24 minutes",N/A 
dist-rtr01,iosxe,16.11.1b,"1 week, 1 hour, 9 minutes",9Y30J7X5QAC 
dist-rtr02,iosxe,16.11.1b,"1 week, 1 hour, 9 minutes",9741BQ3XSZ5 
dist-sw01,nxos,9.2(3),"7 days, 1 hours, 9 minutes",91FK5ZLK8FF 
dist-sw02,nxos,9.2(3),"7 days, 1 hours, 9 minutes",9CUP5WOOV6M 
edge-sw01,ios,15.2(CML,"4 hours, 52 minutes",N/A 
internet-rtr01,iosxe,16.11.1b,"1 week, 1 hour, 9 minutes",9D6J5QHY2PZ
```

## Following the development process 
If you'd like to see how the script was built, you can look at the commit log on the `network_inventory.py` file, or explore the files in the [`development-steps`](development-steps/) folder.  You'll find numbered files showing how the script was build, step by step, that you can run individually, or use as resources to create your own file.  

```
ls -l development-steps 
total 84
-rwxr-xr-x 1 hpreston hpreston  483 Jun  1 15:10 01_network_inventory.py
-rwxr-xr-x 1 hpreston hpreston  933 Jun  1 15:10 02_network_inventory.py
-rw-r--r-- 1 hpreston hpreston 1240 Jun  1 15:10 02a_network_inventory.py
-rw-r--r-- 1 hpreston hpreston 1744 Jun  1 15:10 03_network_inventory.py
-rw-r--r-- 1 hpreston hpreston 2463 Jun  1 15:10 03a_network_inventory.py
-rw-r--r-- 1 hpreston hpreston 2685 Jun  1 15:10 03b_network_inventory.py
-rw-r--r-- 1 hpreston hpreston 4031 Jun  1 15:10 04_network_inventory.py
-rw-r--r-- 1 hpreston hpreston 5989 Jun  1 15:10 04a_network_inventory.py
-rw-r--r-- 1 hpreston hpreston 6105 Jun  1 15:10 04b_network_inventory.py
-rw-r--r-- 1 hpreston hpreston 6432 Jun  1 15:10 04c_network_inventory.py
-rw-r--r-- 1 hpreston hpreston 6779 Jun  1 15:10 04d_network_inventory.py
-rw-r--r-- 1 hpreston hpreston 7148 Jun  1 15:10 04e_network_inventory.py
-rw-r--r-- 1 hpreston hpreston 7333 Jun  1 15:10 05_network_inventory.py
-rw-r--r-- 1 hpreston hpreston 7341 Jun  1 15:10 06_network_inventory.py
```

> Note: letters after a number indicate an improvement to the main step number, or a multi-stage development step.
