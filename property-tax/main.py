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
Write a GUI program that displays the assessment value and property tax when a user enters the actual value of a property. '
'''
import MyPropertyTaxGUI

def main():
    # Create an instance of the MyGUI class.
    my_gui = MyPropertyTaxGUI.MyGUI()

# Call the main function ONLY if the file is being run as a standalone program.
if __name__ == '__main__' :
    main()