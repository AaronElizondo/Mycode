#!/usr/bin/env python3
# open file in read mode
dnsfile = open("dnsservers.txt", "r")
# create list of lines
dnslist = dnsfile.readlines()
# loop over lines
for server in dnslist: #in the for loop. for *server* doesn't need to be specified. can be any word.
    #print and end without a newline
    print(server, end="")
# close your file
dnsfile.close()

