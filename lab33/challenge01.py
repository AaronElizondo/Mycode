#!/usr/bin/env pyton3

API = "http://api.notify.org/astros.json"
# python3 -m pip intall requests
import requests

def main():

    #send an HTTP get request to our API
    resp=requests.get(API)
    # use the .json() method from the requests to get objects
    spacedata = resp.json()

    print(spacedata)

    print(f"in space there are curently {spacedata..get('number') people in space."}

if __name__== "__main__":
    main()
