#!/usr/bin/env python3
ipchk = input("Please enter an IP address: ") #this is the prompt for IP address

#a string tests as true
if ipchk == "192.168.70.1":
    print("Looks like the IP address of the Gateway was : " +ipchk + "This is not recommended.")
elif ipchk:
    print("Looks like the IP address was :" + ipchk)
else: # if nothing is provided
    print("...You didn't put anything")
