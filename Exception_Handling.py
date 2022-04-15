# -*- coding: utf-8 -*-

#Global Variable
#result = 0

#Graceful Error Handling
def numbers():
    
    try: 
        number = open('C:\\Users\\JCord\\OneDrive\\Desktop\\Numbers.txt', 'r')
        read = number.readline()
        print(read)
        print(read + 1)
    except TypeError as err:
        print('Cannot add string to integer.')
        print("Error:", err)
        
def Gracefull():
    
    num_1 = int(input("Enter a number: "))
    num_2 = int(input("Enter another number: "))
    
    if num_2 != 0:
        
        print(int(num_1/num_2))
        
    else:
        
        print("You cannot divide a number by 0.")
    
#Explicit Error Handling
def ExceptionHandling():
    
    try:
        num_1 = int(input("enter a number: "))
        num_2 = int(input("Enter another number: "))
        
        #local variable
        result = num_1 / num_2
        
        print(int(result))
    #also, ZeroDivisionErro as err:    
    except ZeroDivisionError as err:
        
        print("You cannot divide by 0")
        print("Error:", err)
        
    #print(int(result))
    
def FileExceptions():
    
    #to catch all errors, just use except without an error type
    pass

if __name__=='__main__':
    
    #Gracefull()
    #ExceptionHandling()
    #FileExceptions()
    numbers()