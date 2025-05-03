#
# Grant Bossa
# April 26, 2025
# Grant Bossa
# April 26, 2025
# Relational Database Programming Project
# SDEV 1200
#

# fmt: off
'''
# Instructions
* Write a program that performs CRUD operations on the Majors table. 
Specifically, the program should allow the user to do the following:
  - ___ Add a new major
  - ___ Search for an existing major 
  - ___ Update an existing major 
  - ___ Delete an existing major 
  - ___ Show a list of all majors 

* Write a program that performs CRUD operations on the Departments table. 
Specifi-cally, the program should allow the user to do the following:
  - ___ Add a new department 
  - ___ Search for an existing department 
  - ___ Update an existing department 
  - ___ Delete an existing department 
  - ___ Show a list of all departments 

* Write a program that performs CRUD operations on the Students table. 
Specifically, the program should allow the user to do the following: 
  - ___ Add a new student
  - ___ Search for an existing student 
  - ___ Update an existing student 
  - ___ Delete an existing student 
  - ___ Show a list of all students

When adding, updating, and deleting rows, be sure to enable foreign key enforcement. 

When adding a new student to the Students table, 
the user should only be allowed to select an existing major from the Departments table, 
and an existing department from the Departments table.
'''
# fmt: on

import sqlite3
import subprocess

choice = 0  # Menu choice
menu_exit = 5  # Menu exit


# Main function
def main():
    global choice, menu_exit
    # Connect to the database.
    conn = sqlite3.connect("student_info.db")

    # Get a database cursor.
    cur = conn.cursor()

    # Get the user's menu choice.
    while choice != menu_exit:
        choice = get_menu_choice()
        execute_choice(cur, choice)

    # Commit the changes.
    conn.commit()

    # Close the connection.
    conn.close()


# The display_menu function displays a menu.
def display_menu():
    print("")
    print("                                    MAIN MENU")
    print("----------------------------------------------------------------------")
    print("1 - Majors Table Menu")
    print("2 - Departments Table Menu")
    print("3 - Students Table Menu")
    print("4 - Create/Recreate Student Info DB")    
    print("5 - EXIT")


# The get_menu_choice function displays the menu and gets the user's choice.
def get_menu_choice():
    display_menu()
    choice = int(input("Enter your choice: "))
    # Validate the choice
    while (choice < 1) or (choice > menu_exit):
        choice = int(input("Enter a valid choice: "))
    return choice


# Perform the action that the user selected.
def execute_choice(cur, choice=0):
    if choice == 1:  # Go To Majors Table Menu
        subprocess.run(
            ["python", "crud_majors.py"], check=True)
    elif choice == 2:  # Go To Departments Table Menu
        subprocess.run(
            ["python", "crud_departments.py"], check=True)
    elif choice == 3:  # Go To Students Table Menu
        subprocess.run(
            ["python", "crud_students.py"], check=True)
    elif choice == 4:  # Create/Recreate Student Info DB
        print("!!!THIS WILL DELETE THE CURRENT DATABASE IF IT EXISTS!!!")
        verify_choice = input("Do you want to continue? Y/N ")
        if verify_choice.lower == "y":
            subprocess.run(
                ["python", "create_student_info_db.py"], check=True)   
            print("New database created")   
        else:
            print("Process Aborted, Database not created")  

# Call the main function ONLY if the file is being run as a standalone program.
if __name__ == "__main__":
    main()
