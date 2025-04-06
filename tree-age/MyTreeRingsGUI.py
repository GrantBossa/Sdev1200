#
# Grant Bossa
# April 5, 2025
# Tree Age Programming Project
# SDEV 1200
#

# Instructions
"""
Counting the growth rings of a tree is a good way to tell the age of a tree.
Each growth ring counts as one year.
Use a Canvas widget to draw how the growth rings of a 5-year-old tree might look.
Then, using the create_text method, number each growth ring starting from the
center and working outward with the age in years associated with that ring.
"""

import tkinter as tk

class MyGUI:
    def __init__(self):
      # Create the main window.
      self.main_window = tk.Tk()
      self.main_window.title("Tree Growth Rings")
      self.main_window.geometry("350x370")

      # Create canvas widget
      self.canvas = tk.Canvas(self.main_window, width=300, height=300, bg="white")
      self.canvas.pack(pady=20)

      # Create the button frame and widgets.
      self.button_frame = tk.Frame(self.main_window)
      self.draw_button = tk.Button(
         self.button_frame, 
         text="Draw Rings", 
         command=self.draw_rings
      )
      self.quit_button = tk.Button(
         self.button_frame, 
         text="Quit", 
         command=self.main_window.destroy
      )

      # Pack the buttons and frame.
      self.draw_button.pack(side="left")
      self.quit_button.pack()
      self.button_frame.pack(side="bottom")

      # Start the main loop.
      tk.mainloop()

    def draw_rings(self):
        # Draw the growth rings
        self.center_x = 150
        self.center_y = 150
        self.max_radius = 100  # Max radius for outermost ring
        self.ring_width = self.max_radius // 5  # Width of each ring

        for year in range(5):
            self.radius = (year + 1) * self.ring_width
            self.canvas.create_oval(
               self.center_x - self.radius,
               self.center_y - self.radius,
               self.center_x + self.radius,
               self.center_y + self.radius,
               outline="brown",
               width=year + 1,
            )

            # Create text for each growth ring
            self.canvas.create_text(
               self.center_x + self.radius - 10,
               self.center_y,
               text=str(year + 1),
               fill="black",
               font=("Arial", 12),
            )


def main():
    # Create an instance of the MyGUI class.
    my_gui = MyGUI()


# Call the main function ONLY if the file is being run as a standalone program.
if __name__ == "__main__":
    main()
