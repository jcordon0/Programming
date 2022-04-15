# -*- coding: utf-8 -*-
loop = int(input("How many sets? "))
set1 = set()
set2 = set([1,5,6,8,7,10])

myList = []

for i in range(0, loop):
    value = int(input("Enter values: "))
    myList.append(value)

set1.update(myList)

set3 = set1.intersection(set2)

print(set1)
print(set3)
print(myList)