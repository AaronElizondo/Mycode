#!/usr/bin/env python3

"""AaronElizondo | Alta3 student
    Printing dictionary data stored as lists to a screen"""

def main():
    """ On this farm there was a..."""

    #this is the data we want to loop across
    #it is a list containing 3 dictionaries
    farms = [{"name": "NE Farm", "agriculture":["sheep","cows","pigs","chickens","llamas","cats"]},{"name": "W Farm", "agriculture":["pigs","chickens","llamas"]},{"name": "SE Farm", "agriculture":["chicken","carrots","celery"]}]

    #each time throgh the loop fam will be equal to one of the dict within the list "farms"
    for farm in farms:
        #print(farm)
        print(farm.get("name", "Unknown Farm"), end=":\n")

        for agri in farm.get("agriculture"):
            print(" -", agri)
main()
