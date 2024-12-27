import tkinter as tk
from tkinter import ttk
import subprocess
import importlib

# Define your scripts here
scripts = {
    "Gaming Trivia": "scripts/multigame.py",
    "Weather": "scripts/weather.py",
    "Roller": "scripts/roller.py",
	"IcoMaker": "scripts/icomaker.py",
	"ImgThf": "scripts/imgthf.py",
	"Harmony": "scripts/harmony.py",
}

# Function to run the script using subprocess
def run_script(script_name):
    try:
        subprocess.run(["python", scripts[script_name]])
    except Exception as e:
        log_label["text"] = f"Error: {e}"

# Function to import and run the script as a module
def run_script_as_module(script_name):
    try:
        module_name = scripts[script_name].replace(".py", "")
        module = importlib.import_module(module_name)
        if hasattr(module, "main"):
            module.main()
        else:
            log_label["text"] = "Script does not have a main() function."
    except Exception as e:
        log_label["text"] = f"Error: {e}"

# GUI Setup
root = tk.Tk()
root.title("Plauncher")
root.geometry("400x300")
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

# Run the GUI
root.mainloop()
