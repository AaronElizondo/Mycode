#! /usr/bin/env python3

# opening warning
message = 'The movie is about to begin, we recommend '
#wrap connection in a float() to accept decimals as numbers
connection = float(input("What is your connection speed in Mbps?"))
# if a value is higher or equal to 25
if connection >= 25:
    message = message + 'setting video quality to 4k.'
elif connection >= 5:
    message = message + 'setting video quality to 1080p. '
elif connection >= 2:
    message = message + 'setting video quality to 720p. '
else:
    message = message + 'finding another access network. Sorry!'
print(message)
