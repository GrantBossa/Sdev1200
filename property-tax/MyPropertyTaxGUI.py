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
      self.main_window.geometry("250x150")

      # Create StringVar objects to display 
      self.text_entry_variable = tk.StringVar()
      self.property_value = tk.StringVar()
      self.assessment_value = tk.StringVar()
      self.property_tax_value = tk.StringVar()

      # Create three frames.
      self.entry_frame = tk.Frame(self.main_window)
      self.button_frame = tk.Frame(self.main_window)
      self.info_frame = tk.Frame(self.main_window)

      # Create Entry widgets
      self.L1 = tk.Label(self.entry_frame, text="Enter Property Value")
      self.my_entry = tk.Entry(self.entry_frame, bd =5, textvariable=self.text_entry_variable)
      self.text_entry_variable.set("")

      # Pack the Entry widgets
      self.L1.pack( side = "left")
      self.my_entry.pack()

      # Create the button widgets.
      self.calculate_button = tk.Button(self.button_frame, text = "Calculate Values", command = self.calculateValues)
      self.quit_button = tk.Button(self.button_frame, text = "Quit", command = self.main_window.destroy)

      # Pack the buttons.
      self.calculate_button.pack(side="left")
      self.quit_button.pack(side="right")      

      # Create the label widgets associated with the StringVar objects.
      self.property_label = tk.Label(self.info_frame, textvariable=self.property_value)
      self.assessment = tk.Label(self.info_frame, textvariable=self.assessment_value)
      self.property_tax_label = tk.Label(self.info_frame, textvariable=self.property_tax_value)
      
      # Pack the frames.
      self.entry_frame.pack()
      self.button_frame.pack()
      self.info_frame.pack()

      # Start the main loop.
      tk.mainloop()

   def calculateValues(self):
      self.testproperty_value = float(self.my_entry.get())
      self.testassessment_value = float(self.testproperty_value) * 0.6
      self.testproperty_tax_value = float(self.testassessment_value) * .0075

      self.property_value.set(f"{"Property Value":<24} $ {self.testproperty_value:>10.2f}")
      self.assessment_value.set(f"{"Assessment Value":<20} $ {self.testproperty_value * 0.6:>10.2f}")
      self.property_tax_value.set(f"{"Property Tax":<25} $ {self.testassessment_value * .0075:>10.2f}")
      
      # Pack the labels.
      self.property_label.pack(anchor = 'w')
      self.assessment.pack(anchor = 'w')
      self.property_tax_label.pack(anchor = 'w')
      
def main():
    # Create an instance of the MyGUI class.
    my_gui = MyGUI()

# Call the main function ONLY if the file is being run as a standalone program.
if __name__ == '__main__' :
    main()