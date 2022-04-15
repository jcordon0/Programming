# -*- coding: utf-8 -*-
myString = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
myNumbers = (1,2,3,4,5,6,7,8,9,0)

print(f'{myString} {myNumbers}')



print(myString[0:26:2])

length = len(myString)

print(length)

found = 'D'

if found in myString:
    print('The Letter D is in the string.')
    print(myString.index(found))
    print(myString[3])
    print(myString[12:26])
else:
    print('The letter is not in the string')
    
for element in myString:
    print(element)
    
#8.6 solution