#
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

When adding, updating, and deleting rows, be sure to enable foreign key enforcement. 

When adding a new student to the Students table, 
the user should only be allowed to select an existing major from the Majors table, 
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
    print("                                    MAJOR TABLE MENU")
    print("----------------------------------------------------------------------")
    print("1 - Add a new major")
    print("2 - Search for an existing major")
    print("3 - Update an existing major")
    print("4 - Delete an existing major")
    print("5 - Show a list of all majors")
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
    if choice == 1:  # Add a new major
        create_new_major(cur)
    elif choice == 2:  # Search for an existing major
        find_major(cur)
    elif choice == 3:  # Update an existing major
        update_major(cur)
    elif choice == 4:  # Delete an existing major
        delete_major(cur)
    elif choice == 5:  # Show a list of all majors
        display_majors(cur)

# The create_new_entry function adds input data into the Majors table.
def create_new_major(cur):
    print("")
    print("Please add New Major Information")
    print("")
    new_name = input('Please enter the Name of the new Major: ')
    new_name = new_name.strip()
    if new_name != "":
        cur.execute('''INSERT INTO Majors (Name) 
                    VALUES (?)''', (new_name,))
    
        # if found - print Added, else print not added
        cur.execute('''SELECT * FROM Majors WHERE Name = (?)''', (new_name,))
        display_majors(cur, 1)

    
# the find_major function searches for a specific major in the Majors table
def find_major(cur):
    print("")
    print("Please enter the Major you are looking for")
    print("")
    name = "%" + input('Please enter the Name of the Major to be found: ') + "%"
    if name != "":
        cur.execute('''SELECT * FROM Majors WHERE name LIKE (?)''', (name,))
        display_majors(cur, 2)


def update_major(cur):
    print("")
    print("Which of the following majors do you wish to change?")
    display_majors(cur, 5)
    print("")
    select_id = input("Please enter the MajorID number of the Major you wish to change: ")
    select_id = select_id.strip()
    if select_id != "":
        new_name = input("Please enter the new name for the Major: ")
        new_name = new_name.strip()
        if new_name != "":
            cur.execute('''UPDATE Majors SET name = (?) WHERE MajorID = (?)''', (new_name, select_id))
            cur.execute('''SELECT * FROM Majors WHERE MajorID = (?)''', (select_id,))
            display_majors(cur, 3)

def delete_major(cur):
    print("")

    print("Which of the following Majors do you wish to delete?")
    display_majors(cur, 5)

    verify_choice = 0
    while verify_choice == 0:
        select_id = input("Please enter the ID number of the record you wish to delete: ")
        select_id = select_id.strip()
        if select_id != "":
            # If select_id is being used in Students Table, message that it cannot be deleted as it is in use
            cur.execute('''SELECT MajorID FROM Students WHERE DeptID = (?)''', (select_id,))
            results = cur.fetchone
            
            # If MajorID is not used in Students Table, Okay to delete
            if results == None: 
                cur.execute('''DELETE FROM Majors WHERE MajorID = (?)''', (select_id))
                cur.execute('''SELECT * FROM Majors WHERE MajorID = (?)''', (select_id,))
                display_majors(cur, 4)
                verify_choice = 1
            # If MajorID is used in Students Table, message that it cannot be deleted 
            else:
                print(f'\033[1mMajor ID cannot be deleted because it is in use in the Students Table.\033[0m')
        else:
            verify_choice=1


# The display_majors function displays the contents of the Majors table.
def display_majors(cur, value=5):

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
            cur.execute('SELECT * FROM Majors ORDER BY Name')
            results = cur.fetchall()

    print("")            
    print(title)
    print(f"{'Major ID':9} {'Name':^20}")
    print(f"{'-------':9} {'------------------':20}")
    for row in results:
        major_id=row[0]
        name = row[1]
        print(f'{major_id:^9} {name:<20}')

# Verify that the value is a valid MajorID
def verify_major(cur, value):
    cur.execute('''SELECT * FROM Majors WHERE MajorID = (?)''', (value,))
    results = cur.fetchone()
    print(f"value {value}, {results}, {results[0]} - {results[1]}")
    if results == None:
        return False
    else:
        return True


        
    
# Call the main function ONLY if the file is being run as a standalone program.
if __name__ == "__main__":
    main()
