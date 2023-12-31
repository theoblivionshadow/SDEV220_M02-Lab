'''
Author: Shadow R.
App Name: StudentQualifierApp.py
Purpose:
    App will take user input for student information to determine if student qualifies for the Dean's List or Honor Roll.
'''

# get user input for last name
lastName = input("Please enter student's last name: ")

#loop break condition variable
quit = "ZZZ"

while lastName != quit:
    #get user input for first name and GPA
    firstName = input("Please enter student's first name: ")
    gpa = float(input("Please enter student's GPA: "))
    
    #selection statement to determine student status
    if gpa >= 3.5:
        print(f"{firstName} {lastName} has made the Dean's List with a GPA of {gpa}.")
    elif gpa >= 3.25:
        print(f"{firstName} {lastName} has made the Honor Roll with a GPA of {gpa}.")
    else:
        print(f"{firstName} {lastName} didn't make the Honor Roll or Dean's List with a GPA of {gpa}. Keep studying!")
    #get last name from user to continue or exit loop
    lastName = input("Please enter student's last name: ")