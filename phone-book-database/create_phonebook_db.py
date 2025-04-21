#
# Grant Bossa
# April 19, 2025
# Population Database Programming Project
# SDEV 1200
# 

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

def main():
    # Connect to the database.
    conn = sqlite3.connect('phonebook.db')

    # Get a database cursor.
    cur = conn.cursor()
    
    # Add the Entries table.
    add_entries_table(cur)
    
    # Commit the changes.
    conn.commit()
  
    # Close the connection.
    conn.close()

# The add_entries_table adds the Entries table to the database.
def add_entries_table(cur):
    # If the table already exists, drop it.
    cur.execute('DROP TABLE IF EXISTS Entries')

    # Create the table.
    cur.execute('''CREATE TABLE Entries (EntryID INTEGER PRIMARY KEY NOT NULL,
                                        PersonName TEXT,
                                        PhoneNumber varchar(10))''')

# Execute the main function.
if __name__ == '__main__':
    main()
