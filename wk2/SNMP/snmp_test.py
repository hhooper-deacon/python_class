#!/usr/bin/env python

import snmp_helper

COMMUNITY_STRING = "galileo"
SNMP_PORT = 161
HOST_LIST = list()
HOST_LIST.append("184.105.247.70")
HOST_LIST.append("184.105.247.71")

def PRINT_SNMP(snmp):
	output = snmp_helper.snmp_extract(snmp)
	print output

def GET_SNMP(device, OID):
	snmp_data = snmp_helper.snmp_get_oid(device, OID)
	PRINT_SNMP(snmp_data)

def ADD_DEVICE(host):
	OID = "1.3.6.1.2.1.1.5.0"
	OID_2 = "1.3.6.1.2.1.1.1.0"
	DEVICE = (host, COMMUNITY_STRING, SNMP_PORT)
	GET_SNMP(DEVICE, OID)
	GET_SNMP(DEVICE, OID_2)

for host in HOST_LIST:
	ADD_DEVICE(host)

