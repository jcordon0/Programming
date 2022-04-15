# -*- coding: utf-8 -*-
#Lists are mutable, meaning the values inside them can be changed and/or overwritten
#Lists are dynamic, so we can add, subtract, append to them, and so on
def UnderstandingLists():
    myList = [5,6,7,8,9]

    myList2 = ['Sally', 'Lucy', 'Mike']
    
    myList3 = [1, 4.657, 'Daniel']    

    print(f'{myList}\n{myList2}\n{myList3}')
    
    print('\n--------------------------------')
    
    rangeList = list(range(5))
    rangeList_2 = list(range(1, 10, 2))
    
    print(f'{rangeList}\n{rangeList_2}')
    print('\n--------------------------------')
    
    listCopies = [1,2,3,'Copy'] * 5
    
    print(listCopies)
    print('\n--------------------------------')
    
def LoopingLists():
    
    numbers = [1,2,3,4,10]
        
    for values in numbers:
        
        print(values)
        
    print('\n---------------------------------')
    
    print(numbers[0], numbers[4])
    #this will give us an index out of range or index out of bounds error
    #print(numbers[5])
    
def AppendList():
    
    listA = [0,1,2,3,4,5]
    
    i = 6
    for number in range(0,3):
        listA.append(i)
        i += 1 #i -=2
    #listA[2] = 21
    print(listA)
    
def InsertLists():
    
    listB = [0,1,2,3,5,6,7]
    listB.insert(4,4)
    listB.insert(2,90)
    listB.remove(5) #removes the value not the index
    print(listB)
    
def LenFunction():
    
    numbers = [5, 9, 10, 456, 23, 8]
    
    length = len(numbers)
    print(length)
    print(numbers[5])
    
def Mutability():
    
    numbers = [5, 9, 10, 456, 23, 8]
    
    numbers[3] = 18
    
    print(numbers)
    
def ConcatenateLists():
    
    for i in range (0,1):
        myList_1 = [1, 2, 3, 4]
        myList_2 = [5, 6, 7, 8]
        list_3 = myList_1[0] + myList_2[0]
        list_4 = myList_1 *2
        print(list_4)
    
    result = myList_1 + myList_2
    
    print(result)
    
    print('\n--------------------------------')
    
    mtypesList = [1, 4.5, 'Sally']
    mtypesList2 = ['John']
    
    result = mtypesList + mtypesList2
    
    print(result)
    
    
def SortingLists():
    
    unsortedList = [10,0,4,8,16,1,2]
    
    unsortedList.sort()
    
    ascendingSort = unsortedList
    print(ascendingSort)
    
    ascendingSort.reverse()
    
    descendingSort = ascendingSort
    print(descendingSort)

def TwoDimentionalLists():
    
    studentScores = [['Greg', 100, 90],['Veronica', 96, 88],['Gandalf', 100, 100]]
    
    print(studentScores[0])
    print(studentScores[1])
    print(studentScores[2])
    
    for rows in studentScores:
        print('\n')
        for columns in rows:
            print(f'columns')
            
    for i in studentScores:
        i.insert(0, ['Greg', 0, 0])
        print(studentScores)
    
def ListSlicing():
    
    numbers = [ 5, 9, 14, 25, 40, 55]
    #length = len(numbers)
    last_half = numbers[3:6]
    print(last_half)
    
    first_half = numbers[0:3]
    print(first_half)
    
    from_to_end = numbers[2:]
    print(from_to_end)
    
    skipping = numbers[2:6:2]#[start, end + 1 (lenght +1), incements]
    print(skipping)
    
    newList = skipping + first_half
    print(newList)
    
def InOperator():
    
    passwordDatabase = ['password', '123456', 'admin', 'root', '000000']
    
    checkPass = input("Enter a password: ")
    
    if checkPass in passwordDatabase:
        
        print("Your password is in the known database")
    else:
        print("Good password")
#----------------------------------------------------------------------------------

def UnderstandingTuples():
    myTuple = (5,6,7,8,9)

    myTuple2 = ('yes',11,'x')

    #myTuple = myTuple2

    print(myTuple[2])
    
def Immutability():
    
    numbers = (5, 9, 10, 456, 23, 8)
    
    numbers[3] = 18
    
    print(numbers)
    
if __name__=='__main__':
    #AppendList()
    #InsertLists()
    #SortingLists()
    TwoDimentionalLists()
    #UnderstandingLists()
    #LoopingLists()
    #LenFunction()
    #Mutability()
    #ConcatenateLists()
    #ListSlicing()
    #InOperator()
    #UnderstandingTuples()
    #Immutability()