import random
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb

def roll_dice():
    try:
        sides = int(dice_sides_entry.get())
        if sides < 2:
            result_label.config(text="Dice must have at least 2 sides.")
        else:
            result = random.randint(1, sides)
            result_label.config(text=f"You rolled: {result}")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Create main application window
app = tb.Window(themename="darkly")
app.title("Roller")
app.geometry("300x200")

# GUI Elements
frame = ttk.Frame(app, padding="20")
frame.pack(expand=True, fill="both")

dice_sides_label = ttk.Label(frame, text="Number of sides on the dice:")
dice_sides_label.pack(pady=5)

dice_sides_entry = ttk.Entry(frame, justify="center")
dice_sides_entry.pack(pady=5)

roll_button = ttk.Button(frame, text="Roll Dice", command=roll_dice)
roll_button.pack(pady=10)

result_label = ttk.Label(frame, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

# Run the application
app.mainloop()
