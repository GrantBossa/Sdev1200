#
# Grant Bossa
# April 5, 2025
# Property Tax Programming Project
# SDEV 1200
#

# Instructions  
'''
A county collects property taxes on the assessment value of property, which is 60 percent of the property�s actual value. 
If an acre of land is valued at $10,000, its assessment value is $6,000. 
The property tax is then $0.75 for each $100 of the assessment value. 
The tax for the acre assessed at $6,000 will be $45.00. 
Write a GUI program that displays the assessment value and property tax when a user enters the actual value of a property.
'''

import tkinter as tk

class MyGUI:
   def __init__(self):
      # Create the main window.
      self.main_window = tk.Tk()
      self.main_window.title("Property Tax Valuation")
      self.main_window.geometry("250x200")

      # Create StringVar objects to display 
      # name, street, and city-state-zip
      text_variable = tk.StringVar()

      self.property_value = tk.StringVar()
      self.assesment_value = tk.StringVar()
      self.property_tax_value = tk.StringVar()

      # Create three frames.
      self.entry_frame = tk.Frame(self.main_window)
      self.button_frame = tk.Frame(self.main_window)
      self.info_frame = tk.Frame(self.main_window)

      # Create Entry widgets
      my_entry = tk.Entry(self.entry_frame, textvariable=text_variable)
      text_variable.set("Enter Property Value Here")

      # Pack the Entry widgets
      my_entry.pack()

      # Create the button widgets.
      self.calculate_button = tk.Button(self.button_frame, text = "Calculate Values", command = self.calculateValues)
      self.quit_button = tk.Button(self.button_frame, text = "Quit", command = self.main_window.destroy)

      # Pack the buttons.
      self.calculate_button.pack(side="left")
      self.quit_button.pack(side='right')      

      # Create the label widgets associated with the StringVar objects.
      self.property_label = tk.Label(self.info_frame, textvariable=self.property_value)
      self.assessment = tk.Label(self.info_frame, textvariable=self.assesment_value)
      self.property_tax_label = tk.Label(self.info_frame, textvariable=self.property_tax_value)

      # Pack the labels.
      self.property_label.pack()
      self.assessment.pack()
      self.property_tax_label.pack()

      # Pack the frames.
      self.entry_frame.pack()
      self.button_frame.pack()
      self.info_frame.pack()

      # Start the main loop.
      tk.mainloop()

   def calculateValues(self):
      self.property_value.set(my_entry.get())
      self.assesment_value.set("Assessment Value")
      self.property_tax_value.set("Property Tax Value")

def main():
    # Create an instance of the MyGUI class.
    my_gui = MyGUI()

# Call the main function ONLY if the file is being run as a standalone program.
if __name__ == '__main__' :
    main()