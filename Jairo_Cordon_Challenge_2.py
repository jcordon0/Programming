# -*- coding: utf-8 -*-
print("What is your name?:")

userName = input()

print("Please enter your date of birth in the following format: mm/dd/yyyy")

userDate = input()

print ("Your birthday is" " " + userDate + "")

print ("Please enter your birth year only:")
userYear = input()

result = 2022 - int(userYear) 
print (result)

print ("You are currently" " " + str(result) + " " "years old...\n")

print ("Your name is"" "+ userName +"."" ""You were born in" " " + userYear +"."" ""That makes you approximately" " "+ str(result) +" ""years old.")