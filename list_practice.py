# -*- coding: utf-8 -*-

#mutable Objects: Lists, Dictionaries, user-defined objects
listA = [0]
print (listA)
listB = listA
print (listB)
listB.append(1)
print (listA)
print (listB)

#immutable objects: Number (integers, and floating-point values), strings, booleans, tuples
print("---------\n")
numberA = 0
print(numberA)
numberB = numberA
print(numberB)
print(numberA)