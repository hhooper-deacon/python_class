#!/usr/bin/env python

import telnetlib
from time import sleep

user_name = "pyclass"
user_pass = "88newclass"
remote_host = "184.105.247.70"
remote_port = 23
remote_timeout = 180

remote_conn = telnetlib.Telnet(remote_host, remote_port, remote_timeout)

remote_conn.read_until("erna", remote_timeout)

remote_conn.write(user_name + "\n")

remote_conn.read_until("assw", remote_timeout)

remote_conn.write(user_pass + "\n")
sleep(2)

remote_conn.read_until("pynet-rtr1", remote_timeout)

remote_conn.write("show ip int brief\n")
sleep(3)

remote_out = remote_conn.read_very_eager()	

print remote_out

remote_conn.close()
