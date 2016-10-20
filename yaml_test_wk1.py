#!/usr/bin/env python

import yaml
import json

my_list = range(10)

my_list.append("Test1")
my_list.append("Test2")
my_list.append("Test3")
my_list.append({})

my_list[-1]
my_list[-1]["ip_address_1"] = "1.1.1.1"
my_list[-1]["ip_address_1_pfx"] = "24"
my_list[-1]["ip_address_2"] = "2001::1"
my_list[-1]["ip_address_2_pfx"] = "64"
my_list[-1]["host_device_1"] = "Test Device"
my_list[-1]["host_device_1_plat"] = "Cisco"
my_list[-1]["host_device_1_os"] = "IOS"

#for i in my_list:
#	print i

with open("yaml_dump_wk1", "w") as f:
	f.write(yaml.dump(my_list, default_flow_style=False))

with open("json_dump_wk1", "w") as g:
	json.dump(my_list, g)
