# -*- coding: utf-8 -*-
user_number = int(input('Enter a number:'))

if (user_number %2 and user_number > 0):
    print('That number is valid')
elif(user_number == 0):
        print('That number is not valid')
else:
    print('Goodbye')