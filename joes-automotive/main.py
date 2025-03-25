#
# Grant Bossa
# March 26, 2025
# Joe's Automotive Programming Project
# SDEV 1200
#
# Instructions  
'''
Joe’s Automotive performs the following routine maintenance services:
- Oil change—$30.00
- Lube job—$20.00
- Radiator flush—$40.00
- Transmission flush—$100.00
- Inspection—$35.00
- Muffler replacement—$200.00
- Tire rotation—$20.00

Write a GUI program with check buttons that allow the user to select any or all of these 
services. When the user clicks a button, the total charges should be displayed.
'''
import tkinter as tk
import tkinter.messagebox

class Joes_AutoGUI:
    def __init__(self):
        # Create the main window
        self.main_window = tk.Tk()
        self.main_window.title("Joe's Automotive")
        
        #create frames
        self.top_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)
        
        # Create checkbutton variables
        self.cb_oil_var = tk.IntVar()
        self.cb_lube_var = tk.IntVar()
        self.cb_radiator_var = tk.IntVar()
        self.cb_transmission_var = tk.IntVar()
        self.cb_inspection_var = tk.IntVar()
        self.cb_muffler_var = tk.IntVar()
        self.cb_tire_var = tk.IntVar()

        # Set variables to Zero
        self.cb_oil_var.set(0)
        self.cb_lube_var.set(0)
        self.cb_radiator_var.set(0)
        self.cb_transmission_var.set(0)
        self.cb_inspection_var.set(0)
        self.cb_muffler_var.set(0)
        self.cb_tire_var.set(0)

        # Create top frame checkbuttons
        self.cb1 = tk.Checkbutton(self.top_frame, 
                                  text = "Oil Change - $30.00", 
                                  variable = self.cb_oil_var)
        self.cb2 = tk.Checkbutton(self.top_frame, 
                                  text = "Lube Job - $20.00", 
                                  variable = self.cb_lube_var)
        self.cb3 = tk.Checkbutton(self.top_frame, 
                                  text = "Radiator Flush - $40.00", 
                                  variable = self.cb_radiator_var)
        self.cb4 = tk.Checkbutton(self.top_frame, 
                                  text = "Transmission Flush - $100.00", 
                                  variable = self.cb_transmission_var)
        self.cb5 = tk.Checkbutton(self.top_frame, 
                                  text = "Inspection - $35.00", 
                                  variable = self.cb_inspection_var)
        self.cb6 = tk.Checkbutton(self.top_frame, 
                                  text = "Muffler Replacement - $200.00", 
                                  variable = self.cb_muffler_var)                        
        self.cb7 = tk.Checkbutton(self.top_frame, 
                                  text = "Tire Rotation - $20.00", 
                                  variable = self.cb_tire_var)

        # pack the checkbuttons to set on screen
        self.cb1.pack(anchor="w")
        self.cb2.pack(anchor="w")
        self.cb3.pack(anchor="w")
        self.cb4.pack(anchor="w")
        self.cb5.pack(anchor="w")
        self.cb6.pack(anchor="w")
        self.cb7.pack(anchor="w")
        
        # Create the bottom frame buttons
        self.display_button = tk.Button(self.bottom_frame, 
                                        text = "Display Charges", 
                                        command = self.calculate)
        self.quit_button = tk.Button(self.bottom_frame, 
                                     text = "Quit", 
                                     command = self.main_window.destroy)
        
        # Pack the widgets in the bottom frame
        self.display_button.pack(side="left")
        self.quit_button.pack(side="left")
        
        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        # Enter the tkinter main loop
        tk.mainloop()

    # def show_info event function
    def calculate(self):
        # Create Total variable and set to zero
        self.total = 0.0

        # Determine total charges based on checkbuttons selected
        if self.cb_oil_var.get() == 1:
            self.total += 30.0
        if self.cb_lube_var.get() == 1:
            self.total += 20.0
        if self.cb_radiator_var.get() == 1:
            self.total += 40.0
        if self.cb_transmission_var.get() == 1:
            self.total += 100.0
        if self.cb_inspection_var.get() == 1:
            self.total += 35.0
        if self.cb_muffler_var.get() == 1:
            self.total += 200.0
        if self.cb_tire_var.get() == 1:
            self.total += 20.0

        # Display messagebox response
        tkinter.messagebox.showinfo("Total Charges", 
                        f"Your total charges = ${self.total:,.2f}")
        
 
        tk.mainloop()

if __name__ == "__main__":
    joes_auto = Joes_AutoGUI()