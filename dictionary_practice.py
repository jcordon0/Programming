# -*- coding: utf-8 -*-
empty_dictionary = {}
loop = int(input("Number to loop: "))

for number in range(loop):
    
    key = input("Enter a car make: ")
    model = input("Enter the model:")
    empty_dictionary[key] = model
    
print(empty_dictionary)
print(key)
print(model)
