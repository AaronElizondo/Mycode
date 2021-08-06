#!/usr/bin/env python3

import zipfile

def main():
    zipcheck = input("What file do you want to check the zip status of? ")
    if zipfile.is_zipfile(zipcheck) :
        print("Yup that sure do be a 'zip' file.")
    else:
        print("Doesn't look like a 'zip' file to me")

if __name__== "__main__":
    main()
