#
# Grant Bossa
# April 26, 2025
# Relational Database Programming Project
# SDEV 1200
#

# fmt: off
'''
# Instructions

* Write a program that performs CRUD operations on the Students table. 
Specifically, the program should allow the user to do the following: 
  - ___ Add a new student
  - ___ Search for an existing student 
  - ___ Update an existing student 
  - ___ Delete an existing student 
  - ___ Show a list of all students

When adding, updating, and deleting rows, be sure to enable foreign key enforcement. 

When adding a new student to the Students table, 
the user should only be allowed to select an existing student from the Departments table, 
and an existing department from the Departments table.
'''
# fmt: on

import sqlite3

choice = 0  # Menu choice
menu_exit = 6  # Menu exit


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
        execute_choice(choice, cur)

    # Commit the changes.
    conn.commit()

    # Close the connection.
    conn.close()


# The display_menu function displays a menu.
def display_menu():
    print("")
    print("                                    STUDENT TABLE MENU")
    print("----------------------------------------------------------------------")
    print("1 - Add a new student")
    print("2 - Search for an existing student")
    print("3 - Update an existing student")
    print("4 - Delete an existing student")
    print("5 - Show a list of all students")
    print("6 - EXIT")


# The get_menu_choice function displays the menu and gets the user's choice.
def get_menu_choice():
    display_menu()
    choice = int(input("Enter your choice: "))
    # Validate the choice
    while (choice < 1) or (choice > menu_exit):
        choice = int(input("Enter a valid choice: "))
    return choice


# Perform the action that the user selected.
def execute_choice(choice, cur):
    if choice == 1:  # Add a new student
        create_new_student(cur)
    elif choice == 2:  # Search for an existing student
        find_student(cur)
    elif choice == 3:  # Update an existing student
        update_student(cur)
    elif choice == 4:  # Delete an existing student
        delete_student(cur)
    elif choice == 5:  # Show a list of all students
        display_students(cur)

# The create_new_entry function adds input data into the Students table.
def create_new_student(cur):
    print("")
    print("Please add New Student Information")
    print("")
    new_name = input('Please enter the Name of the new Student: ')
    major_id = input("Please enter the Students Major ID ")
    dept_id = input("Please enter the Students Department ID ")
    
    cur.execute('''INSERT INTO Students (Name, MajorID, DeptID) 
                    VALUES (?, ?, ?)''', (new_name, major_id, dept_id,))
    
    # Add new record verification here
    # select new_name
    # if found - print Added, else print not added
    cur.execute('''SELECT * FROM Students WHERE Name = (?)''', (new_name,))
    display_students(cur, 1)

    
# the find_student function searches for a specific student in the Students table
def find_student(cur):
    print("")
    print("Please enter name of the Student you are looking for")
    print("")
    name = "%" + input('Please enter the Name of the Student to be found: ') + "%"
    
    cur.execute('''SELECT * FROM Students WHERE name LIKE (?)''', (name,))
    display_students(cur, 2)


def update_student(cur):
    print("")
    print("Which of the following students do you wish to change?")
    display_students(cur, 5)
    print("")
    select_id = input("Please enter the StudentID number of the Student you wish to change: ")
    new_name = input("Please enter the new name for the Student: ")
    major_id = input("Please enter the Students Major ID ")
    dept_id = input("Please enter the Students Department ID ")

    cur.execute('''UPDATE Students 
                SET name = (?), 
                MajorID = (?), 
                DeptID = (?) 
                WHERE StudentID = (?)''', (new_name, major_id, dept_id, select_id))
    cur.execute('''SELECT * FROM Students WHERE StudentID = (?)''', (select_id,))
    display_students(cur, 3)

def delete_student(cur):
    print("")

    print("Which of the following Students do you wish to delete?")
    display_students(cur, 5)

    select_id = input("Please enter the ID number of the record you wish to delete: ")

    cur.execute('''DELETE FROM Students WHERE StudentID = (?)''', (select_id))
    cur.execute('''SELECT * FROM Students WHERE StudentID = (?)''', (select_id,))
    display_students(cur, 4)

# The display_students function displays the contents of the Students table.
def display_students(cur, value=5):

    match value:
        case 1:
            title = "Created New Record:"
            results = cur.fetchall()
        case 2:
            title =  "Record Found Listing:"
            results = cur.fetchall()
        case 3:
            title =  "Record Updated Listing:"
            results = cur.fetchall()
        case 4:
            title =  "Record Deleted Listing:"
            results = cur.fetchall()
        case 5:
            title =  "Alphabetical Listing:"
            cur.execute('SELECT * FROM Students ORDER BY Name')
            results = cur.fetchall()

    print("")            
    print(title)
    print(f"{'Student ID':9} {'Name':^20} {'Major ID':^9} {'Dept ID':^9}")
    print(f"{'-------':9} {'------------------':20} {'-------':9} {'-------':9}")
    for row in results:
        student_id=row[0]
        name = row[1]
        majorID = row[2]
        deptID = row[3]
        print(f'{student_id:^9} {name:<20}{majorID:^9} {deptID:^9}')


# Call the main function ONLY if the file is being run as a standalone program.
if __name__ == "__main__":
    main()
