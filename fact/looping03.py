#! /usr/bin/env python3
# the UUID library allows us to generate UUID values.
import uuid
#this prompts for the number of UUIDs the user wants created.
howmany = int(input("How many UUIDs should be generated?"))

print("Generating UUIDs...")

for billy in range(howmany):
    print(uuid.uuid4())
