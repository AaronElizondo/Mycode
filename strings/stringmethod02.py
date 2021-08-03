#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

def main():
   """Run-time code"""
    # create a small string
    lilstring = "Alta3 Research offers classes on Python coding"
    newlist = lilstring.split(" ") #sperates string based off spaces to a list.
    print(newlist)

    #create a list of strings
    myiplist = ["192","168","0","12"]
    #set singleip as a result of joining list myiplist and the "."
    singleip = ".".join(myiplist)
    #display singleip
    print(singleip)

    #call our main fuction or it will stay in mem and not run.

    main()
