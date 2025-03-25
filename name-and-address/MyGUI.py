#
# Grant Bossa
# March 23, 2025
# Name and Address Programming Project
# SDEV 1200
#
# Use comments liberally throughout the program.
# The code below was auto-generated.
# Delete unnecessary code.

import tkinter as tk

class MyGUI:
   def __init__(self):
      # Create the main window.
      self.main_window = tk.Tk()
      self.main_window.title("Name and Address")
      self.main_window.geometry("250x100")

      # Create StringVar objects to display 
      # name, street, and city-state-zip
      self.name_value = tk.StringVar()
      self.street_value = tk.StringVar()
      self.city_state_zip_value = tk.StringVar()

      # Create two frames.
      self.info_frame = tk.Frame(self.main_window)
      self.button_frame = tk.Frame(self.main_window)

      # Create the label widgets associated with the StringVar objects.
      self.name_label = tk.Label(self.info_frame, textvariable=self.name_value)
      self.street_label = tk.Label(self.info_frame, textvariable=self.street_value)
      self.city_state_zip_label = tk.Label(self.info_frame, textvariable=self.city_state_zip_value)

      # Pack the labels.
      self.name_label.pack()
      self.street_label.pack()
      self.city_state_zip_label.pack()

      # Create the button widgets.
      self.show_info_button = tk.Button(self.button_frame, text = "Show Info", command = self.show)
      self.quit_button = tk.Button(self.button_frame, text = "Quit", command = self.main_window.destroy)

      # Pack the buttons.
      self.show_info_button.pack(side="left")
      self.quit_button.pack(side='right')

      # Pack the frames.
      self.info_frame.pack()
      self.button_frame.pack()

      # Start the main loop.
      tk.mainloop()

   def show(self):
      self.name_value.set("Grant Bossa'")
      self.street_value.set("123 Main St")
      self.city_state_zip_value.set("Green River, WY 12345")

<<<<<<< HEAD
my_gui = MyGUI()
=======
# my_gui = MyGUI()
>>>>>>> ccd9c23 (In Progress)
'''
   # Create the entry widgets for the StringVar objects.
   self.name_entry = tk.Entry(self.info_frame, textvariable=self.name_value)
   self.street_entry = tk.Entry(self.info_frame, textvariable=self.street_value)
   self.city_state_zip_entry = tk.Entry(self.info_frame, textvariable=self.city_state_zip_value)

   # Pack the entry widgets.
   self.name_entry.pack(side=tk.LEFT)
   self.street_entry.pack(side=tk.LEFT))
   self.street_label.pack(side=tk.LEFT)
   self.city_state_zip_label.pack(side=tk.LEFT)

   # Create the entry widgets for the StringVar objects.
   self.name_entry = tk.Entry(self.info_frame, textvariable=self.name_value)
   self.street_entry = tk.Entry(self.info_frame, textvariable=self.street_value)
   self.city_state_zip_entry = tk.Entry(self.info_frame, textvariable=self.city_state_zip_value)

   # Pack the entry widgets.
   self.name_entry.pack(side=tk.LEFT)
   self.street_entry.pack(side=tk.LEFT)'
'''
<<<<<<< HEAD
=======

def main():
    # Create an instance of the MyGUI class.
    my_gui = MyGUI()
>>>>>>> ccd9c23 (In Progress)

# Call the main function ONLY if the file is being run as a standalone program.
if __name__ == '__main__' :
    main()