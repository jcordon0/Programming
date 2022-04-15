# -*- coding: utf-8 -*-
user_choice = input('Do you want to play a a game?\n')
user_name = input('Enter your name ')
user_age = int(input('Enter your age '))

if (user_choice.lower() == "Yes" or user_choice == "y"):
    print("Lets Start:")
else:
    print ("Goodbye")
    
print(f"Your name is {user_name} and your age is {user_age}")

  #if(userChoice == "y"):
      #print("Please enter yes or y")
     
#print('r to include \\ or figures')