# -*- coding: utf-8 -*-
user_choice = input('Do you want to play a game?\n')
winning_number = 20
accumulator = 0

if (user_choice == "Yes" or user_choice == "yes" or user_choice == 'y'):
    print('\n')
    print('Lets Start:')
    print('Please enter a number between 1 and 50:')
else:
    print ("Okay, goodbye then.")
    
user_answer = int(input())

while user_answer != 20 or user_answer < 20 or user_answer > 20:
    accumulator += 1
    print('Try again please')
    if(user_answer == winning_number):
        print('You have won the grand prize, a trip to Hawaii!!') 
    elif(user_answer < 20 and user_answer >= 15):
        print('You have won a small prize, a 5$ gift card!')
    elif(user_answer < 26 and user_answer >= 21):
        print('You have won a small prize, a 5$ gift card!')
    elif(user_answer < 1 or user_answer > 50):
        print('Please choose a number between 1 and 50.') 
if (user_answer == 20):
    print(f"It took you {accumulator} tries.")
else:
    print('Sorry that is not correct, try again.') 