#! /usr/bin/env python3
#parse keystone.common.wsgi and return the number of failed attempts

loginfail=0 # this is to start the counter and define it

keystone_file = open("/home/student/Mycode/attemptlogin/keystone.common.wsgi","r")
#keystone_file declares it and opens the file we want under read privledge
#turns the file into a list of lines in memory
keystone_file_lines=keystone_file.readlines()
#loop over the list of lines
for line in keystone_file_lines:
    #if this 'fail pattern' appears in the line...
    if "- - - - -] Authorization failed" in line:
        loginfail += 1 #this is the same as loginfail + 1 
print("The number of failed attempts is", loginfail)
keystone_file.close()
