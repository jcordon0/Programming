# -*- coding: utf-8 -*-
num = 40
#i = 40

for i in range (0,10):
    num += 1
    print(num, "\n")
    print(i)
    
for num in range (2,10,2):
    print(num, "\n")
    
for num in [1,2,3,4]:
    print(num, "\n")
    
print("------")
#numbers in range
for num in range(5):
    print(num, "\n")

for num in range(4,25,3):
    print(num, "\n")
    
    if num == 16:
        print("error")
        break
        #continue
        
#print in reverse order
for number in range (6,0,-1):
    print(number, "\n")
  
#user controlled for loops
end = int(input("Enter a number, a squared value will be displayed\n"))
print("Number\tSquared")
print("------")
for number in range (1, end + 1):
    square =number ** 2
    print(f"{number}\t\t {square}")
  
word = "dododododo"
for letter in word:
    print(letter)
    print(word)
    
for num in [1,5,8,12,15]:
    print(num)
    
for name in ["carl","sally","mike"]:
    print(name)
    
mylist = [1,5,8,14]

for mylist, i in enumerate(mylist):
    print(mylist, i)