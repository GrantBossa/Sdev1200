#
# Grant Bossa
# April 26, 2025
# Relational Database Programming Project
# SDEV 1200
#

# fmt: off
'''
Update plans:
    1 menu for all operations
        select table to do processing on
        submenues will change with table selected
        Pass the table parameter to the function
# Instructions
* Write a program that performs CRUD operations on the Majors table. 
Specifically, the program should allow the user to do the following:
  - ___ Add a new major
  - ___ Search for an existing major 
  - ___ Update an existing major 
  - ___ Delete an existing major 
  - ___ Show a list of all majors 

* Write a program that performs CRUD operations on the Departments table. 
Specifically, the program should allow the user to do the following:
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
        execute_choice(choice, cur)

    # Commit the changes.
    conn.commit()

    # Close the connection.
    conn.close()


# The display_menu function displays a menu.
def display_menu():
    print("")
    print("                                    MENU")
    print("----------------------------------------------------------------------")
    print("1 - Create new Entry")
    print("2 - Look up a person's phone number")
    print("3 - Change a person's phone number")
    print("4 - Delete specified rows")
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
def execute_choice(choice, cur):
    if choice == 1:  # Create new Entry in the `Entries` table
        create_new_entry(cur)
    elif choice == 2:  # Look up a person's phone number
        display_entries(cur)
    elif choice == 3:  # Change a person's phone number
        update_phone_number(cur)
    elif choice == 4:  # Delete specified rows.
        delete_entry(cur)

# The create_new_entry function adds input data into the Entries table.
def create_new_entry(cur):
    print("")
    print("Please add New Entry Information in the format LastName, First Name")
    print("")
    new_name = input('Please enter the new Name: ')
    new_phone_number = input("Please enter the 10 digit Phone Number without formatting: ")

    cur.execute('''INSERT INTO Entries (PersonName, PhoneNumber)
        VALUES (?, ?)''', (new_name, new_phone_number))
    
# The display_entries function displays the contents of the Entries table.
def display_entries(cur):
    print("")

    print('Alphabetical Contents of phonebook.db/Entries table:')
    cur.execute('SELECT * FROM Entries ORDER BY PersonName')
    results = cur.fetchall()
    print(f"{'Entry ID':9} {'Person':^20} {'Phone Number':>17}")
    print(f"{'---------':9} {'--------------------':20} {'-----------------':17}")
    for row in results:
        entry_id=row[0]
        person = row[1]
        phone = row[2]
        if len(phone) == 10:
            phone = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
        elif len(phone) == 7:
            phone = f"{phone[:3]}-{phone[3:]}"
        else:
            "Invalid phone number format"         
        print(f'{entry_id:^9} {person:<20} {phone:>17}')


def update_phone_number(cur):
    print("")

    print("Which of the following numbers do you wish to change?")
    display_entries(cur)
    print("")
    select_id = input("Please enter the Entry ID number of the phone number you wish to change: ")
    new_phone_number = input("Please enter the 10 digit Phone Number without formatting: ")

    cur.execute('''UPDATE Entries SET PhoneNumber = (?) WHERE EntryID = (?)''', (new_phone_number, select_id))

def delete_entry(cur):
    print("")

    print("Which of the following records do you wish to delete?")
    display_entries(cur)

    select_id = input("Please enter the ID number of the record you wish to delete: ")

    cur.execute('''DELETE FROM Entries WHERE EntryID = (?)''', (select_id))

# Call the main function ONLY if the file is being run as a standalone program.
if __name__ == "__main__":
    main()
