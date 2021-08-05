#! /usr/bin/env python3
## EXPLORE READ
#create a file object in "r"ead mode
configfile= open("vlanconfig.cfg","r")

#display file to screen - .read()
print(configfile.read())
#closing file
print(configfile.close())

print("\n-------------------------------------\n")
## EXPLORE READLINES

configfile= open("vlanconfig.cfg","r")

#make a list of file lines -.readlines()
configlist= configfile.readlines()
print(configlist)

## iterate through config list
for x in configlist:
    print(x.strip())

#closing file since we are not using with
configfile.close()
