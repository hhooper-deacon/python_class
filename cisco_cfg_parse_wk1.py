#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse as ccp
from pprint import pprint as pp

with open("cisco_ipsec.txt") as f:
	my_cfg = ccp(f)

for obj in my_cfg.find_objects(r"crypto map CRYPTO"):
	pp("Object: " + str(obj) + " Val: " + str(obj.text))
	obj_child = obj.re_search_children(obj.text)
	for obj2 in obj_child:
		pp("Child: " + str(obj2))
