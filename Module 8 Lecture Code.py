# -*- coding: utf-8 -*-
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#searching for a value in the string
char = input("What letter would you like to search for? ")

if char in letters:
    print(f"the letter {char} was found in the string")

else:
    print("The letter was not found in the string")
    
print('------------------------------------------------')
#accessing a specific index value in the string
element = letters[5]
index = letters.index(char)
print(f'The element {element} is located at index {index}')
print('------------------------------------------------')
#concatenating strings
numbers = '123456'

combined = numbers + letters
print(combined)
print('------------------------------------------------')
#slicing strings
first_half = letters[0:13] 
second_half = letters[13:]
print(first_half, second_half)
print('------------------------------------------------')
#the FIND method
phrase = "99 Red balloons"
position = phrase.find("Red")

if position != -1:
    
    print(f"The word was contained at position {position}")

else:
    print("The word was not found")
print('------------------------------------------------')   
#determining the type of file by using the endswith substring
filename = input("")

if filename.endswith('.txt'):
    print("The file you are looking for is a text file")

else:
    print("The file is not a text file")
print('------------------------------------------------')    
#replacing values
newPhrase = phrase.replace("balloons", "apples")
print(newPhrase)
print('------------------------------------------------')
#converting the letters above into all lower case letters
result = letters.lower()
print(result)
print('------------------------------------------------')
#string testing methods
user_choice = input("Please enter a passphrase: ")

if user_choice.isalnum():
    print("The string is alphanumeric")
    
if user_choice.isdigit():
    print("The string contains only numbers")
    
if user_choice.isalpha():
    print("The string contains only letters")
    
if user_choice.islower():
    print("the string contains only lowercase letters")
print('------------------------------------------------')    
name = 'Juliet'
for ch in name:
    print(ch)
    
#LOOK AT THE BOTTOM OF PAGE 454.  WRITE THAT PROGRAM AND EXPLAIN TO ME WHAT IT'S DOING

#Programming Exercise in-class
#Use the instructions in Program 8-12 to calculate the average of each score using the StudentGradeBook.txt file I uploaded to Lab 2 on Blackoard
