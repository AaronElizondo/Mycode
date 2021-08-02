#!/usr/bin/env python3
# Creates a list containing three items
my_list= [ "192.168.2.1", 5060, "UP"]

# display the first item in the list
print("The first item in the list is (IP): " + my_list[0])

# display the second item in the list
print("The second item in the list (port): " + str(my_list[1]) )

# display the third item in the list
print("The last item in the list (state): " + my_list[2] )


iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
# this is adding up the strings with the + operator
print("IP addresses: " +  iplist[3] + ", and " + iplist[4]) 

# this is using an f-string
print(f"IP addresses: {iplist[3]}, and {iplist[4]}")
