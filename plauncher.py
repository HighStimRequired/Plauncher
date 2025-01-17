import tkinter as tk
from tkinter import ttk
import subprocess
import os

# Dynamically load scripts from the 'scripts' folder
script_folder = "scripts"

# Ensure the folder exists
if not os.path.exists(script_folder):
    os.makedirs(script_folder)

# Scan the folder for .py files
scripts = {
    f.replace(".py", "").capitalize(): os.path.join(script_folder, f)
    for f in os.listdir(script_folder)
    if f.endswith(".py")
}

# Function to run the script using subprocess
def run_script(script_name):
    try:
        subprocess.run(["python", scripts[script_name]])
    except Exception as e:
        log_label["text"] = f"Error: {e}"

# Function to calculate window size based on the number of scripts
def calculate_window_size():
    base_height = 100  # Base height for the window
    button_height = 40  # Height per button
    total_height = base_height + len(scripts) * button_height
    return max(total_height, 300)  # Minimum height of 300px

# GUI Setup
root = tk.Tk()
root.title("Plauncher")
root.geometry(f"400x{calculate_window_size()}")
root.configure(bg="#2E2E2E")

# Style
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", background="#444444", foreground="white", font=("Verdana", 10))
style.configure("TLabel", background="#2E2E2E", foreground="orange", font=("Verdana", 14))

# Title Label
title_label = ttk.Label(root, text="Plauncher", style="TLabel")
title_label.pack(pady=10)

# Script Buttons
for script_name in scripts.keys():
    button = ttk.Button(root, text=script_name, command=lambda name=script_name: run_script(name))
    button.pack(pady=5)

# Log Label
log_label = ttk.Label(root, text="", style="TLabel", wraplength=380)
log_label.pack(pady=10)

# Adjust window size dynamically
root.geometry(f"400x{calculate_window_size()}")

# Run the GUI
root.mainloop()
