# -*- coding: utf-8 -*-

def Menu():
    
    answer = input("Would you like to enter a student into the gradebook? (Yes/No)\n") #input statement to continue or end with program
    if answer.lower() == "yes": # user answers, any answer other than yes ends program
        AddStudent() #calls AddStudent function
    else:
        print("Okay, goodbye.")
    
def AddStudent():
    
    grade_log = {} #creating an empty dictionary 
    students = int(input("\nHow many students are you adding?\n")) #user inputs number for amount of students (loops)
    
    for i in range(students): #range function to loop for how many students entered 
        
        print('-------------------------------------------')
        student_name = input("\nEnter student name: ") #input student name
        
        print('-------------------------------------------')
        
        grade_1 = int(input("\nEnter grade #1: ")) #input student grades
        
        while (grade_1 < 0) or (grade_1 > 100): #conditional statement to keep grades between 0-100 and loops back
            grade_1 = int(input("\nPlease enter a grade in the range of 0 - 100: "))
            print('-------------------------------------------')
            
        grade_2 = int(input("\nEnter grade #2: "))
        
        while (grade_2 < 0) or (grade_2 > 100): #inputs second grade and checks for 0-100
            grade_2 = int(input("\nPlease enter a grade in the range of 0 - 100: "))
            print('-------------------------------------------')
            
        grade_3 = int(input("\nEnter grade #3: "))
        
        while (grade_3 < 0) or (grade_3 > 100): #inputs third grate and checks for 0-100
            grade_3 = int(input("\nPlease enter a grade in the range of 0 - 100: "))
            print('-------------------------------------------')
            
        grade_log[student_name] = [grade_1, grade_2, grade_3] #sets up and populates the dictionary with the inputs
        keys = student_name #keys are going to be student names and have been set up right before 
        values = [grade_1, grade_2, grade_3] #values are going to be the 3 grades 
        
        print('\n')
        print(keys,'\n')
        print("Adding to local gradebook: ", grade_log)
        StudentGradeBook(keys, values) #passes one key pair value at a time to studentgradebook function
   
def StudentGradeBook(name, grade_value): #has different parameters than what addstudent() passes, but will sort them in order
    
    grade_book = {'Gina': [100, 90, 95], 'Tina': [90, 88, 94],} #dictionary already created needs to have element added
   
    grade_book[name] = grade_value # adds element to grade_book dictionary from passed values in addstudent()
    print('\nUpdated gradebook: ',grade_book) #will print the new dictionary with added element 
    
if __name__ == '__main__':
    Menu()