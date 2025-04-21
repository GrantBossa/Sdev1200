#
# Grant Bossa
# April 19, 2025
# Phone Book Database Programming Project
# SDEV 1200
#

# Instructions

# fmt: off
'''
Write a program that creates a database named `phonebook.db`.
The database should have a table named `Entries`, with columns
for a person's name and phone number.

Next, write a CRUD application that lets the user
add rows to the `Entries` table,
look up a person's phone number,
change a person's phone number,
and delete specified rows.
'''
# fmt: on

import sqlite3

choice = 0  # Menu choice
menu_exit = 5  # Menu exit


# Main function
def main():
    global choice, menu_exit
    # Connect to the database.
    conn = sqlite3.connect("phonebook.db")

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
