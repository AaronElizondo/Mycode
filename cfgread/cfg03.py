#! /usr/bin/env python3
#create file object in read mode
with open("vlanconfig.cfg", "r") as configfile:
    configlist= configfile.readlines()
print(configlist)
