#
# Grant Bossa
# April 19, 2025
# Phone Book Database Programming Project
# SDEV 1200
#

# fmt: off
'''
# Instructions
Write a program that creates a database named `phonebook.db`.
The database should have a table named `Entries`, with columns
for a person's name and phone number.

Next, write a CRUD application that lets the user
add rows to the `Entries` table,
look up a person's phone number,
change a person's phone  number,
and delete specified rows.
'''
# fmt: on

import tkinter as tk
import tkinter.messagebox
import sqlite3

# Connect to the database.
conn = sqlite3.connect("phonebook.db")

# Get a database cursor.
cur = conn.cursor()


class MyGUI():
   global cur
      
   def __init__(self):

      # Create the main window.
      self.main_window = tk.Tk()
      self.main_window.title("Phone Book Database")
      self.main_window.geometry("400x500")


      var1 = tk.StringVar()
      label1 = tk.Label( self.main_window, textvariable=var1)
      var1.set("MENU")
      label1.pack()

      # Variable to store the selected value
      selected_option = tk.StringVar()
      selected_option.set("")  # Set initial value

      # Function to handle radio button selection
      def show_selection():
         choice = int(selected_option.get())
         print("Selected option:", choice)
         listbox.delete(0, tk.END)
         if choice == 1:  # Create new Entry in the `Entries` table
            create_new_entry(cur)
         elif choice == 2:  # Look up a person's phone number
            display_entries(cur)
         elif choice == 3:  # Change a person's phone number
            update_phone_number(cur)
         elif choice == 4:  # Delete specified rows.
            delete_entry(cur)    
         elif choice == 5:  # Show table rows.
            display_entries(cur)  

      # Create radio buttons
      radio_button1 = tk.Radiobutton(self.main_window, text="1 - Create new Entry", variable=selected_option, value="1", command=show_selection)
      radio_button2 = tk.Radiobutton(self.main_window, text="2 - Look up a person's phone number", variable=selected_option, value="2", command=show_selection)
      radio_button3 = tk.Radiobutton(self.main_window, text="3 - Change a person's phone number", variable=selected_option, value="3", command=show_selection)
      radio_button4 = tk.Radiobutton(self.main_window, text="4 - Delete specified rows", variable=selected_option, value="4", command=show_selection)
      radio_button5 = tk.Radiobutton(self.main_window, text="5 - Show table rows", variable=selected_option, value="5", command=show_selection)


      # Place radio buttons in the window
      radio_button1.pack(anchor = 'w')
      radio_button2.pack(anchor = 'w')
      radio_button3.pack(anchor = 'w')
      radio_button4.pack(anchor = 'w')
      radio_button5.pack(anchor = 'w')
      
      # Create two frames.
      self.button_frame = tk.Frame(self.main_window)
      self.info_frame = tk.Frame(self.main_window)

      label_output_title = tk.StringVar()
      label2 = tk.Label( self.info_frame, textvariable=label_output_title)

      listbox = tk.Listbox(self.info_frame, width=46)



      input_box = tk.Entry(window, width=30)
      input_box.pack(pady=10)

      submit_button = tk.Button(window, text="Submit", command=submit_text)
      submit_button.pack()


      # Create StringVar objects to display 
      # name, street, and city-state-zip
      self.name_value = tk.StringVar()
      self.phone_value = tk.StringVar()
      self.city_state_zip_value = tk.StringVar()

      # Create the label widgets associated with the StringVar objects.
      self.name_label = tk.Label(self.info_frame, textvariable=self.name_value)
      self.phone_label = tk.Label(self.info_frame, textvariable=self.phone_value)
      
      # Pack the labels.
      self.name_label.pack()
      self.phone_label.pack()
      
      # Create the button widgets.
      self.show_info_button = tk.Button(self.button_frame, text = "Show Info", command = self.show)
      self.quit_button = tk.Button(self.button_frame, text = "Quit", command = self.main_window.destroy)

      # Pack the buttons.
      self.show_info_button.pack(side="left")
      self.quit_button.pack(side='right')

      # Pack the frames.
      self.button_frame.pack()
      self.info_frame.pack()

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

        
         cur.execute('SELECT * FROM Entries ORDER BY PersonName')
         results = cur.fetchall()

         label_output_title.set(f"Alphabetical Listing:\n" +
                  f"{'Entry ID':9} {'Person':^20} {'Phone Number':>17}" )
         label2.pack(anchor = 'w')
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
            listbox.config(selectmode='multiple')
            listbox.insert(entry_id, f'{entry_id:^9} {person:<20} {phone:>17}' )
            
         listbox.pack()

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



      # Start the main loop.
      tk.mainloop()

  

   def show(self):
      self.name_value.set("Grant Bossa'")
      self.phone_value.set("123 Main St")
      self.city_state_zip_value.set("Green River, WY 12345")

# Main function
def main():
    # Create an instance of the MyGUI class.
    my_gui = MyGUI()

    # Commit the changes.
    conn.commit()

    # Close the connection.
    conn.close()


# Call the main function ONLY if the file is being run as a standalone program.
if __name__ == '__main__' :
    main()