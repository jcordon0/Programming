# -*- coding: utf-8 -*-
import sys

user_choice = input("Do you want to play a game?\n")
winning_number = 20
accumulator = 1

if (user_choice == "Yes" or user_choice == "y"):
    print("\n")
    print("Lets Start:")
    print("Please enter a number between 1 and 50:")
else:
    print ("Okay, goodbye then.")
    sys.exit()
   
user_answer = int(input("Enter your guess:\n"))
if(user_answer == winning_number):
    print(f"You guessed the correct number in {accumulator} attempt(s)!") 
    sys.exit()
while user_answer != 20:
    accumulator += 1
    user_answer = int(input())
    if(user_answer == 20):
        print("Correct!")
        print(f"You guessed the correct number in {accumulator} attempt(s)!")
        break
    elif (user_answer <= 25 and user_answer >= 15):
        print("You have guessed within the correct range.")
    elif (user_answer < 1 or user_answer > 50):
        print("Please choose a number between 1 and 50.")
    else:
        print("Sorry that is not correct, try again.")