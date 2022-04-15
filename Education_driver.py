# -*- coding: utf-8 -*-
import Education_class

def main():
    
    student_1 = studentClass()
    student_2 = studentClass()
    student_3 = studentClass()
    
    faculty_1 = facultyClass()
    faculty_2 = facultyClass()
    faculty_3 = facultyClass()
    
def studentClass():

    grades = int(input("Enter a grade value: "))
    gpa = int(input("Enter grade point average: ")) 
    tuition = int(input("Enter your tuition amount: "))
    
    grades.classStudent()
    gpa.classStudent()
    tuition.classStudent()
    
def facultyClass():

    major = input("Enter your major: ")
    salary = int(input("Enter your salary: ")) 
    lecture = input("Enter the class you lecture: ")
    
    major.getclassFaculty()
    salary.getclassFaculty()
    lecture.getclassFaculty()
    
if __name__ == '__main__':
    main()