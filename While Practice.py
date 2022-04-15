# -*- coding: utf-8 -*-
descision = input('Do you want to play a game?')

if (descision.lower() == 'yes'):
    print('Good welcome')
    
    #descision = input('Do you want to continue')
    
    while(descision == 'yes'):
        print('I am repeating myself')
else:
    print('Have a nice day')

    
count = 10

num = 0

while count >= 1:
    print(count)
    count -= 1
    num += 1
    if count == 4:
        #break
        print('Error')
        continue 
    print('\n',num)
    #count = count -1