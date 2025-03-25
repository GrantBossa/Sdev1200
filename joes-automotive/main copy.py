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
        self.main_window = tkinter.Tk()
        self.main_window.title("Joe's Automotive")
        window = tk.Tk()
        window.title("Joe's Automotive")
        window.geometry("300x300")

        hello = tk.Label(text="Hello world!")
        hello.pack()
        button = tk.Button(text="Click me!")
        button.pack()

        tk.mainloop()
'''
#-----------------------------------------------------------------
root = tk.Tk()
root.title("Radio Button Example")

# Variable to store the selected value
selected_option = tk.StringVar()
selected_option.set("option1")  # Set a default value

# Function to handle radio button selection
def show_selection():
    print("Selected option:", selected_option.get())

# Create radio buttons
radio_button1 = tk.Radiobutton(root, text="Option 1", variable=selected_option, value="option1", command=show_selection)
radio_button2 = tk.Radiobutton(root, text="Option 2", variable=selected_option, value="option2", command=show_selection)
radio_button3 = tk.Radiobutton(root, text="Option 3", variable=selected_option, value="option3", command=show_selection)

# Place radio buttons in the window
radio_button1.pack()
radio_button2.pack()
radio_button3.pack()

root.mainloop()

#-----------------------------------------------------------------


def show_selection():
    selected_options = [
        option for option, var in option_vars.items() if var.get() == 1
    ]
    print("Selected options:", ", ".join(selected_options))

window = tk.Tk()
window.title("Joe's Automotive")

options = ["$ 30.00 Oil Change", 
           "$ 20.00 Lube Job", 
           "$ 40.00 Radiator Flush", 
           "$100.00 Transmission Flush", 
           "$ 35.00 Inspection", 
           "$200.00 Muffler Replacement", 
           "$ 20.00 Tire Rotation"]

option_vars = {}

for option in options:
    var = tk.IntVar()
    option_vars[option] = var
    check_button = tk.Checkbutton(window, text=option, variable=var)
    check_button.pack(anchor="w")

select_button = tk.Button(window, text="Show Selection", command=show_selection)
select_button.pack()

window.mainloop()
'''
'''
#---------------------------------------------------
class Joes_AutoGUI:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()
        self.main_window.title("Joe's Automotive")

        #create frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        # Create checkbutton variables
        self.cb_oil_var = tkinter.IntVar()
        self.cb_lube_var = tkinter.IntVar()
        self.cb_radiator_var = tkinter.IntVar()
        self.cb_transmission_var = tkinter.IntVar()
        self.cb_inspection_var = tkinter.IntVar()
        self.cb_muffler_var = tkinter.IntVar()
        self.cb_tire_var = tkinter.IntVar()

        # Set variables to Zero
        self.cb_oil_var.set(0)
        self.cb_lube_var.set(0)
        self.cb_radiator_var.set(0)
        self.cb_transmission_var.set(0)
        self.cb_inspection_var.set(0)
        self.cb_muffler_var.set(0)
        self.cb_tire_var.set(0)

        # Create top frame checkbuttons
        self.cb1 = tkinter.Checkbutton(self.top_frame, 
                                  text = "Oil change...........$ 30.00", 
                                  variable = self.cb_oil_var)
        self.cb2 = tkinter.Checkbutton(self.top_frame, 
                                  text = "Lube job.............$ 20.00", 
                                  variable = self.cb_lube_var)
        self.cb3 = tkinter.Checkbutton(self.top_frame, 
                                  text = "Radiator flush.......$ 40.00", 
                                  variable = self.cb_radiator_var)
        self.cb4 = tkinter.Checkbutton(self.top_frame, 
                                  text = "Transmission flush...$100.00", 
                                  variable = self.cb_transmission_var)
        self.cb5 = tkinter.Checkbutton(self.top_frame, 
                                  text = "Inspection...........$ 35.00", 
                                  variable = self.cb_inspection_var)
        self.cb6 = tkinter.Checkbutton(self.top_frame, 
                                  text = "Muffler replacement..$200.00", 
                                  variable = self.cb_muffler_var)                        
        self.cb7 = tkinter.Checkbutton(self.top_frame, 
                                  text = "Tire rotation........$ 20.00", 
                                  variable = self.cb_tire_var)

        # pack the checkbuttons to set on screen
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()
        
        # Create the bottom frame buttons
        self.display_button = tkinter.Button(self.bottom_frame, 
                                        text = "Display Charges", 
                                        command = self.calculate)
        self.quit_button = tkinter.Button(self.bottom_frame, 
                                     text = "Quit", 
                                     command = self.main_window.destroy)
        
        # Pack the widgets in the bottom frame
        self.display_button.pack(side="left")
        self.quit_button.pack(side="left")
        
        # Enter the tkinter main loop
        tkinter.mainloop()

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
        
'''

if __name__ == "__main__":
    joes_auto = Joes_AutoGUI()