# Countdown Timer

![Build Status](https://img.shields.io/github/workflow/status/adammirski/CountdownTimer/CI)
![License](https://img.shields.io/github/license/adammirski/CountdownTimer)

## Description
This program creates a countdown timer using Python’s tkinter library. The timer prompts the user to input the number of hours and minutes to start the countdown. The countdown is displayed in a graphical window with large digits, formatted as HH:MM:SS:MS. The timer includes a visual effect where the digits flash for 10 milliseconds every second, enhancing the user’s visual experience.

##Features:

	•	User Input: The program prompts the user to enter hours and minutes, ensuring that the input is valid (non-negative integers).
	•	Graphical Display: The countdown is displayed in a tkinter window with a large font size of 200 for clear visibility.
	•	Milliseconds Precision: The countdown updates every 100 milliseconds, showing hours, minutes, seconds, and milliseconds.
	•	Flashing Digits: The digits flash for 10 milliseconds every second, toggling visibility to create a blinking effect.

##Components:

	1.	CountdownApp Class:
	•	init Method: Initializes the main application window and calculates the total time in milliseconds.
	•	start_countdown Method: Handles the countdown logic, updating the display every 100 milliseconds, and implements the flashing effect.
	2.	is_valid_input Function: Validates the user input to ensure it consists of non-negative integers.
	3.	Main Block:
	•	Prompts the user for hours and minutes.
	•	Validates the input.
	•	Initializes and starts the CountdownApp.

##Usage:

	1.	Run the program.
	2.	Enter the desired hours and minutes for the countdown.
	3.	Observe the countdown in the graphical window, with digits flashing for 10 milliseconds every second.


