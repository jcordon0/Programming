# -*- coding: utf-8 -*-

def Database(student, grade_location, grade_value): # Passed variables from ChangingGrades()
    
    saved_database = []    #WE ARE CREATING AN EMPTY LIST HERE
    
    inFile = open(r'C:\Users\JCord\OneDrive\Desktop\StudentGradeBook.txt', 'r') #HERE WE ARE OPENING A FILE IN READ MODE
    
    for lines in inFile:    #WE ARE GOING TO LOOP THROUGH EVERY LINE IN THE FILE
        
        saved_database.extend(lines.split('\t'))    #WE ARE SAVING EACH ITEM SEPARATED WITH A TAB TO A LOCATION IN THE LIST
        
    print('\nPrevious gradebook:\n',saved_database) # Printing the saved database with the content read from .txt file
    
    print('\n------------------------------')
    inFile.close()  # closing the .txt file 
    
    if student in saved_database: # conditional statement comparing student name enterted and names in database created earlier
        
        student_index = saved_database.index(student) # assigning student_index to be the indexed name from the database
        student_index = student_index + grade_location # taking the indexed name and adding 1-3 depending on user input
        saved_database[student_index] = grade_value # within saved database we insert the new grade on the newly calucalated index
        
        print('Student:', student,'| Student Index: ', student_index) # printing student name with the correlated index
        print('Grade: ', grade_value,'| Grade Index: ', grade_location) # printing grade entered with associated index in student_index
        
    else:
        print("Student is not in the gradebook.") # if student not found in saved_database program ends
        
    with open(r'C:\Users\JCord\OneDrive\Desktop\StudentGradeBook.txt', 'w') as f: #OPEN THE FILE IN WRITE MODE
        
        for elements in saved_database:   #ITERATE THROUGH EVERY ELEMENT IN THE DATABASE
            
            f.write('%s\t' % elements) # concatenates strings to integers and tabs them for each number and name in saved_database
            
        f.close() 
        
        print("\nUpdated Gradebook:")
        print(saved_database)
        
def ChangingGrades():
    
    print("Gina: (100, 90, 80)\nTina: (10, 20, 30)\nRob: (50, 50, 50)") # created a representation of the .txt for user to undertand locations

    student = input("\nWhich student gradebook would you like to access? (Gina, Tina, Rob): ") # take user inputs for student to start index from
    grade_location = int(input("Which grade would you like to change? (1,2,3): ")) # once student is selected, user will choose which grade they intend to change
    
    while (grade_location >= 4) or (grade_location <=0): # looping statement in case user enters invalid indexes so they do not write over names
        print("\nPlease enter a grade betwen 1 - 3:")
        grade_location = int(input("\nWhich grade would you like to change? (1,2,3): ")) # which grade user wants to change within the gradebook
    
    grade_value = int(input(f'What would you like the new grade to be for {student}? (0-100): ')) # new grade that will replace old grade in specified location
    
    Database(student, grade_location, grade_value) # calling Database function and passing values that were input from user
    
if __name__=='__main__':

    ChangingGrades()