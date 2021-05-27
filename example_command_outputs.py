iosxe_show_version = {
    "type": "parsed",
    "output": {
        "version": {
            "xe_version": "16.11.01b",
            "version_short": "16.11",
            "platform": "Virtual XE",
            "version": "16.11.1b",
            "image_id": "X86_64_LINUX_IOSD-UNIVERSALK9-M",
            "label": "RELEASE SOFTWARE (fc2)",
            "os": "IOS-XE",
            "image_type": "production image",
            "compiled_date": "Tue 28-May-19 12:45",
            "compiled_by": "mcpre",
            "rom": "IOS-XE ROMMON",
            "hostname": "internet-rtr01",
            "uptime": "6 days, 20 hours, 49 minutes",
            "uptime_this_cp": "6 days, 20 hours, 50 minutes",
            "returned_to_rom_by": "reload",
            "system_image": "bootflash:packages.conf",
            "last_reload_reason": "Unknown reason",
            "license_level": "ax",
            "license_type": "N/A(Smart License Enabled)",
            "next_reload_license_level": "ax",
            "chassis": "CSR1000V",
            "main_mem": "2167316",
            "processor_type": "VXE",
            "rtr_type": "CSR1000V",
            "chassis_sn": "9D6J5QHY2PZ",
            "number_of_intfs": {"Gigabit Ethernet": "4"},
            "mem_size": {"non-volatile configuration": "32768", "physical": "3984308"},
            "disks": {
                "bootflash:.": {
                    "disk_size": "16162815",
                    "type_of_disk": "virtual hard disk",
                },
                "webui:.": {"disk_size": "0", "type_of_disk": "WebUI ODM Files"},
            },
            "curr_config_register": "0x2102",
        }
    },
}

iosxe_show_inventory = {
    "type": "parsed",
    "output": {
        "main": {
            "chassis": {
                "CSR1000V": {
                    "name": "Chassis",
                    "descr": "Cisco CSR1000V Chassis",
                    "pid": "CSR1000V",
                    "vid": "V00",
                    "sn": "9741BQ3XSZ5",
                }
            }
        },
        "slot": {
            "R0": {
                "rp": {
                    "CSR1000V": {
                        "name": "module R0",
                        "descr": "Cisco CSR1000V Route Processor",
                        "pid": "CSR1000V",
                        "vid": "V00",
                        "sn": "JAB1303001C",
                    }
                }
            },
            "F0": {
                "other": {
                    "CSR1000V": {
                        "name": "module F0",
                        "descr": "Cisco CSR1000V Embedded Services Processor",
                        "pid": "CSR1000V",
                        "vid": "",
                        "sn": "",
                    }
                }
            },
        },
    },
}

iosxr_show_version = {
    "type": "parsed",
    "output": {
        "operating_system": "IOSXR",
        "software_version": "6.3.1",
        "uptime": "6 days, 20 hours, 50 minutes",
        "image": "bootflash:disk0/xrvr-os-mbi-6.3.1/mbixrvr-rp.vm",
        "device_family": "IOS XRv Series",
        "processor": "Intel 686 F6M15S0",
        "processor_memory_bytes": "3145343K",
        "main_mem": "cisco IOS XRv Series (Intel 686 F6M15S0) processor with 3145343K bytes of memory.",
        "chassis_detail": "IOS XRv Chassis",
        "config_register": "0x2102",
        "rp_config_register": "0x2102",
    },
}

iosxr_show_inventory = {
    "type": "parsed",
    "output": {
        "module_name": {
            "0/0/CPU0": {
                "descr": "Route Processor type (16, 0)",
                "pid": "IOSXRV",
                "vid": "V01",
                "sn": "N/A",
            }
        }
    },
}


nxos_show_version = {
    "type": "parsed",
    "output": {
        "platform": {
            "name": "Nexus",
            "os": "NX-OS",
            "software": {
                "system_version": "9.2(3)",
                "system_image_file": "bootflash:///nxos.9.2.3.bin",
                "system_compile_time": "2/17/2019 5:00:00 [02/17/2019 15:07:27]",
            },
            "hardware": {
                "model": "Nexus9000 9000v",
                "chassis": "Nexus9000 9000v",
                "slots": "None",
                "rp": "None",
                "cpu": "Intel(R) Xeon(R) CPU E5-4669 v4 @ 2.20GHz",
                "memory": "8163960 kB",
                "processor_board_id": "9CUP5WOOV6M",
                "device_name": "dist-sw02",
                "bootflash": "3509454 kB",
            },
            "kernel_uptime": {"days": 6, "hours": 20, "minutes": 49, "seconds": 3},
            "reason": "Unknown",
        }
    },
}

nxos_show_inventory = {
    "type": "parsed",
    "output": {
        "name": {
            "Chassis": {
                "description": "Nexus9000 9000v Chassis",
                "slot": "None",
                "pid": "N9K-9000v",
                "vid": "V02",
                "serial_number": "9CUP5WOOV6M",
            },
            "Slot 1": {
                "description": "Nexus 9000v Ethernet Module",
                "slot": "1",
                "pid": "N9K-9000v",
                "vid": "V02",
                "serial_number": "9CUP5WOOV6M",
            },
            "Fan 1": {
                "description": "Nexus9000 9000v Chassis Fan Module",
                "slot": "None",
                "pid": "N9K-9000v-FAN",
                "vid": "V01",
                "serial_number": "N/A",
            },
            "Fan 2": {
                "description": "Nexus9000 9000v Chassis Fan Module",
                "slot": "None",
                "pid": "N9K-9000v-FAN",
                "vid": "V01",
                "serial_number": "N/A",
            },
            "Fan 3": {
                "description": "Nexus9000 9000v Chassis Fan Module",
                "slot": "None",
                "pid": "N9K-9000v-FAN",
                "vid": "V01",
                "serial_number": "N/A",
            },
        }
    },
}


asa_show_version = {
    "type": "raw",
    "output": '\r\nCisco Adaptive Security Appliance Software Version 9.12(2) \r\nFirepower Extensible Operating System Version 2.6(1.141)\r\nDevice Manager Version 7.12(2)\r\n\r\nCompiled on Fri 24-May-19 12:22 PDT by builders\r\nSystem image file is "boot:/asa9122-smp-k8.bin"\r\nConfig file at boot was "startup-config"\r\n\r\nedge-firewall01 up 6 days 20 hours\r\n\r\nHardware:   ASAv, 2048 MB RAM, CPU Xeon E5 series 2200 MHz,\r\nModel Id:   ASAv10\r\nInternal ATA Compact Flash, 8192MB\r\nSlot 1: ATA Compact Flash, 8192MB\r\nBIOS Flash Firmware Hub @ 0x0, 0KB\r\n\r\n\r\n 0: Ext: Management0/0       : address is 5254.0009.21e0, irq 10\r\n 1: Ext: GigabitEthernet0/0  : address is 5254.000c.8f3e, irq 11\r\n 2: Ext: GigabitEthernet0/1  : address is 5254.0002.00c6, irq 11\r\n\r\nLicense mode: Smart Licensing\r\nASAv Platform License State: Unlicensed\r\nActive entitlement: ASAv-STD-1G, enforce mode: Eval period\r\n*Memory resource allocation is more than the permitted limit.\r\n\r\nLicensed features for this platform:\r\nMaximum VLANs                     : 50             \r\nInside Hosts                      : Unlimited      \r\nFailover                          : Active/Active  \r\nEncryption-DES                    : Enabled        \r\nEncryption-3DES-AES               : Enabled        \r\nSecurity Contexts                 : 2              \r\nCarrier                           : Disabled       \r\nAnyConnect Premium Peers          : 2              \r\nAnyConnect Essentials             : Disabled       \r\nOther VPN Peers                   : 250            \r\nTotal VPN Peers                   : 250            \r\nAnyConnect for Mobile             : Disabled       \r\nAnyConnect for Cisco VPN Phone    : Disabled       \r\nAdvanced Endpoint Assessment      : Disabled       \r\nShared License                    : Disabled       \r\nTotal TLS Proxy Sessions          : 2              \r\nBotnet Traffic Filter             : Enabled        \r\nCluster                           : Disabled       \r\n\r\nSerial Number: 9ACJJ5Q1Q1X\r\n\r\nImage type          : Release\r\nKey version         : A\r\n\r\nConfiguration has not been modified since last system restart.',
}

asa_show_inventory = {
    "type": "parsed",
    "output": {
        "Chassis": {
            "description": "ASAv Adaptive Security Virtual Appliance",
            "pid": "ASAv",
            "vid": "V01",
            "sn": "9ACJJ5Q1Q1X",
        }
    },
}
