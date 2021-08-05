#! /usr/bin/env python3

round = 0

while True:
    round = round + 1
    print('Finish the move title, "Monty Python\'s The life of _____')
    answer = input("Your guess---> ")
    if answer == 'Brian':
        print("Correct!")
        break
    elif round == 3:
        print("Sorry, The answer was Brian. Better luck next time. ")
        break
    else:
        print("Sorry! Try again!")

