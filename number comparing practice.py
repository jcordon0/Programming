# -*- coding: utf-8 -*-
number_guessed = int(input('Please choose a number between 1-200:'))
print("\n")

if(number_guessed <= 200):
    if(number_guessed < 200 and number_guessed >= 150):
        print('You entered a value in the correct range')
        print('The number you chose is less than 200, but greater than 149.')
    elif(number_guessed < 150 and number_guessed >= 100):
        print('You entered a value in the correct range')
        print('It is less than 150 but greater than 99')
    elif(number_guessed < 100 and number_guessed >= 50):
        print('You entered a value in the correct range')
        print('The number you entered is less than 100 but greater than 49')
    elif(number_guessed < 50 and number_guessed >= 1):
        print('You entered a value in the correct range')
        print('The number you entered is less than 50 but greater than 0')
    elif(number_guessed < 0):
        print('The value you entered is not in the correct range')
        if(number_guessed == 0):
            print('The number you provided is 0')
        elif(number_guessed < 0):
            print('The number you guessed is less than 0')
else:
    print('You did not enter a value in the correct range')
    print('The number you guessed was greater than 200')