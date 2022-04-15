# -*- coding: utf-8 -*-

myVariable = 5 #global variable 
def Greetings(n):#n will be called upon and filled with 4
   localVariable = 10 
   print("Hello")
   print(localVariable)
   newValue = n + n
   print(newValue)
   
def newFunction():
    Greetings(4)
   
def main(): #main will always begin the function call 
    print("My planet\n")
    Greetings(4) #this will call geeting as 4 and set it as n
    newFunction()
if __name__ == '__main__':
    main()

 
import math

def SquareRoot(n):
    
    result = math.sqrt(n)
    return result

def logarithm():
    pass

def main():
    
    result = SquareRoot(5)
    print(result)

if __name__=='__main__':
        main()
