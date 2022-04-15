# -*- coding: utf-8 -*-
import sys

pizza_accumulator = 0
user_name = input("Please enter your name:\n")
user_answer = input("Do you want to order a pizza?\n")

if user_answer.lower() == "yes":
    print(f"\nHello {user_name}, \nWelcome to the Python Pizza Chooser!\n")
    print("You have three pizza options:\nPepperoni \nCheese \nSupreme")
else:
    print("Ok, thank you for using the Python Pizza Chooser!")
    sys.exit()

user_choice = input("Choose your pizza: ")
while user_choice == "Pepperoni" or "Cheese" or "Supreme":
    pizza_accumulator += 1
    user_verdict = input("Would you like to add a pizza? ")
    if user_verdict.lower() == "yes":
        print("\nPlease enter: \nPepperoni \nCheese \nSupreme")
        user_choice = input("Go ahead: ")
    else:
        print(f"\nThank you {user_name}\nThe {pizza_accumulator} pizza(s) you ordered will be ready in 30 minutes!")     
        break