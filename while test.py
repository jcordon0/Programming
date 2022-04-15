# -*- coding: utf-8 -*-
print('Basketball Simulator')

count = 0
baskets = 0
guess = 3

while baskets != 10:
    count += 1
    guess = int(input('Please guess a number between 1-5'))
    print (count)
    if (guess == 3):
        baskets += 1
print(count)
    #if (accumulator == 10):
        #break