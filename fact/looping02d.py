#!/usr/bin/env python3

#open file in read mode
with open("dnsservers.txt","r") as dnsfile:
    #indent to keep the dnsfile object open
    #loop across the lines in the field
    for svr in dnsfile:
        svr = svr.rstrip('\n') #this removes new line characters if they are present
        #lets make a if string for .org
        if svr.endswith('org'):
            with open("org-domain.txt", "a") as srvfile:
                srvfile.write(svr + "\n")
        elif svr.endswith('com'):
            with open("com-domain.txt", "a") as srvfile:
                srvfile.write(svr + "\n")
