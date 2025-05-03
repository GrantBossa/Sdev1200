#
# Grant Bossa
# April 26, 2025
# Relational Database Programming Project
# SDEV 1200
#

# fmt: off
'''
# Instructions

* Write a program that performs CRUD operations on the Departments table. 
Specifically, the program should allow the user to do the following:
  - ___ Add a new department 
  - ___ Search for an existing department 
  - ___ Update an existing department 
  - ___ Delete an existing department 
  - ___ Show a list of all departments 

When adding, updating, and deleting rows, be sure to enable foreign key enforcement. 

When adding a new student to the Students table, 
the user should only be allowed to select an existing department from the Departments table, 
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
        execute_choice(cur, choice)

    # Commit the changes.
    conn.commit()

    # Close the connection.
    conn.close()


# The display_menu function displays a menu.
def display_menu():
    print("")
    print("                                    DEPARTMENT TABLE MENU")
    print("----------------------------------------------------------------------")
    print("1 - Add a new department")
    print("2 - Search for an existing department")
    print("3 - Update an existing department")
    print("4 - Delete an existing department")
    print("5 - Show a list of all departments")
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
def execute_choice(cur, choice=0):
    if choice == 1:  # Add a new department
        create_new_department(cur)
    elif choice == 2:  # Search for an existing department
        find_department(cur)
    elif choice == 3:  # Update an existing department
        update_department(cur)
    elif choice == 4:  # Delete an existing department
        delete_department(cur)
    elif choice == 5:  # Show a list of all department
        display_departments(cur)


# The create_new_entry function adds input data into the Departments table.
def create_new_department(cur):
    print("")
    print("Please add New Department Information")
    print("")
    new_name = input('Please enter the Name of the new Department: ')
    new_name = new_name.strip()
    if new_name != "":
        cur.execute('''INSERT INTO Departments (Name) 
                    VALUES (?)''', (new_name,))
    
        # if found - print Added, else print not added
        cur.execute('''SELECT * FROM Departments WHERE Name = (?)''', (new_name,))
        display_departments(cur, 1)

    
# the find_major function searches for a specific department in the Departments table
def find_department(cur):
    print("")
    print("Please enter the Department you are looking for")
    print("")
    name = "%" + input('Please enter the Name of the Department to be found: ') + "%"
    
    cur.execute('''SELECT * FROM Departments WHERE name LIKE (?)''', (name,))
    display_departments(cur, 2)


def update_department(cur):
    print("")
    print("Which of the following majors do you wish to change?")
    display_departments(cur, 5)
    print("")
    select_id = input("Please enter the DeptID number of the Department you wish to change: ")
    select_id = select_id.strip()                  
    if select_id !="":
        new_name = input("Please enter the new name for the Department: ")
        new_name = new_name.strip()                 
        if new_name != "":
            cur.execute('''UPDATE Departments SET name = (?) WHERE DeptID = (?)''', (new_name, select_id))
            cur.execute('''SELECT * FROM Departments WHERE DeptID = (?)''', (select_id,))
            display_departments(cur, 3)

def delete_department(cur):
    print("")

    print("Which of the following Departments do you wish to delete?")
    display_departments(cur, 5)

    verify_choice = 0
    while verify_choice == 0:
        select_id = input("Please enter the ID number of the record you wish to delete: ")
        select_id = select_id.strip()
        if select_id != "":
            # If select_id is being used in Students Table, message that it cannot be deleted as it is in use
            cur.execute('''SELECT DeptID FROM Students WHERE DeptID = (?)''', (select_id,))
            results = cur.fetchone
            
            # If DeptID is not used in Students Table, Okay to delete
            if results == None: 
                cur.execute('''DELETE FROM Departments WHERE DeptID = (?)''', (select_id))
                cur.execute('''SELECT * FROM Departments WHERE DeptID = (?)''', (select_id,))
                display_departments(cur, 4)
                verify_choice = 1
            # If DeptID is used in Students Table, message that it cannot be deleted 
            else:
                print(f'\033[1mDepartment ID cannot be deleted because it is in use in the Students Table.\033[0m')
        else:
            verify_choice=1

# The display_departments function displays the contents of the Departments table.
def display_departments(cur, value=5):

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
            cur.execute('SELECT * FROM Departments ORDER BY Name')
            results = cur.fetchall()

    print("")            
    print(title)
    print(f"{'Dept ID':9} {'Name':^20}")
    print(f"{'-------':9} {'------------------':20}")
    for row in results:
        dept_id=row[0]
        name = row[1]
        print(f'{dept_id:^9} {name:<20}')


# Verify that the value is a valid DepartmentID
def verify_department(cur, value):
    cur.execute('''SELECT * FROM Departments WHERE DeptID = (?)''', (value,))
    results = cur.fetchone()
    print(f"value {value}, {results}, {results[0]} - {results[1]}")
    if results == None:
        return False
    else:
        return True


# Call the main function ONLY if the file is being run as a standalone program.
if __name__ == "__main__":
    main()
