#!/usr/bin/env python3

#standard library imports
import os
#os allows for low level system commands
import zipfile
#tools to create, read, write,append and list a zip file

#functions to search for all files in a directory, and add them to our zip file
def zipdir(dirpath, zipfileobj):
    """does the work of writing data into our zipfile"""
    #os.walk() returs a 3-tuple or in lameeens terms 3 things
    #always in the order root,dirs,files
    for root,dirs,files in os.walk(dirpath):
        for file in files:# we only want to loos across the file component
            print(os.path.join(root,file))
            zipfileobj.write(os.path.join(root, file))
        return None #when we are done, no need to return any value
def main():
    """called at runtime"""
    dirpath = input("What directory are we archiving today? ")

    ## if the directory exists then we can start archiving
    if os.path.isdir(dirpath):
        zippedfn = input("What should we call the finished archive? ")
        ##zippedfn is the zipped file for the archive. what we want to call it when it is done
        with zipfile.ZipFile(zippedfn, "w", zipfile.ZIP_DEFLATED) as zipfileobj:
            #create a ip file object -- we are making a new zip file
            zipdir(dirpath, zipfileobj) #call to our function *look up to def zipdir(dirpath,zipfileobj*
    else:
        print("Run the script again when you have a valid directory to zip.\n")
main()
