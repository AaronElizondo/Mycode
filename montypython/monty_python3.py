#! /usr/bin/env python3
round = 0 # creating the round timer
answer = " "

while round < 3 and answer != "Brian":
    round =+ 1 # increase round by 1
    answer = input('Finish the movie title, "Mony Python\'s The Life of _____": ')
    if answer == "Brian": #logic to check if user gave correct answer
        print("Correct!")
    elif round == 3:
        print("Sorry, The answer was Brian.")
    else:
        print("Sorry. Try again!")
