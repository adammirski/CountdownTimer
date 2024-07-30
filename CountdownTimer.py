# Countdown Timer Program
# Author: Adam
# Date: 2024-07-30

import tkinter as tk
import time

class CountdownApp:
    def __init__(self, root, hours, minutes):
        # Initialize the main application window
        self.root = root
        self.root.title("Countdown Timer")
        
        # Create and pack the label to display the countdown
        self.label = tk.Label(root, text="", font=("Helvetica", 200))
        self.label.pack()
        
        # Calculate the total number of milliseconds from hours and minutes
        self.total_milliseconds = (hours * 3600 + minutes * 60) * 1000
        
        # Start the countdown
        self.start_countdown()

    def start_countdown(self):
        # If there is still time left
        if self.total_milliseconds >= 0:
            # Calculate hours, minutes, seconds, and milliseconds
            total_seconds, milliseconds = divmod(self.total_milliseconds, 1000)
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            
            # Format time as HH:MM:SS:MS
            time_format = f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds // 100:01}"
            
            # Update the label with the current time
            self.label.config(text=time_format)
            self.root.update()
            
            # Decrement the total milliseconds
            self.total_milliseconds -= 100
            
            # Call the function again after 100 milliseconds
            self.root.after(100, self.start_countdown)

def is_valid_input(hours, minutes):
    # Check if the hours and minutes input are valid
    return hours.isdigit() and minutes.isdigit() and int(hours) >= 0 and int(minutes) >= 0

if __name__ == "__main__":
    root = tk.Tk()
    
    # Prompt user for hours and minutes until valid input is provided
    while True:
        hours = input("Enter hours: ")
        minutes = input("Enter minutes: ")
        if is_valid_input(hours, minutes):
            hours = int(hours)
            minutes = int(minutes)
            break
        else:
            print("Invalid input. Please enter non-negative integer values for hours and minutes.")
    
    # Create the CountdownApp instance
    app = CountdownApp(root, hours, minutes)
    
    # Run the main event loop
    root.mainloop()
