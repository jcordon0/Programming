# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 18:53:29 2022

@author: iburr
"""

myList = ["4", "5"]

userName = input("Please enter a username using alphanumeric values: ")
'''
if any(char in userName for char in myList):
    
    print("The number 4 or 5 was found in the username and it's not valid.")
    
else:
    
    print("Your username is valid")
    
'''  
for char in userName:
    
    for element in myList:
        
        if element == char:
            
            print("The value 4 or 5 was found in your userName")
            
    else:
            
        print("That's a good username")
        break
            
        
