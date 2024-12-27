import tkinter as tk
from tkinter import ttk, messagebox
import requests

# OpenWeather API key (replace with your API key)
API_KEY = "000e2a2388116fa91e48cbb3090e4e1a"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Function to fetch weather data
def get_weather(location):
    try:
        params = {
            'q': location,
            'appid': API_KEY,
            'units': 'imperial'  # For Fahrenheit
        }
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Unable to fetch weather data: {e}")
        return None

# Function to display weather data
def display_weather():
    location = location_entry.get().strip()
    if not location:
        messagebox.showwarning("Input Error", "Please enter a location or ZIP code.")
        return

    weather_data = get_weather(location)
    if weather_data and weather_data.get("weather"):
        city = weather_data["name"]
        temp = weather_data["main"]["temp"]
        condition = weather_data["weather"][0]["description"].capitalize()
        result_label["text"] = f"Location: {city}\nTemperature: {temp}°F\nCondition: {condition}"
    else:
        result_label["text"] = "Weather data not found. Please try again."

# Tkinter GUI
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.configure(bg="#2E2E2E")

# Dark theme styling
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#2E2E2E", foreground="#FFFFFF", font=("Arial", 12))
style.configure("TEntry", fieldbackground="#555555", foreground="#FFFFFF")
style.configure("TButton", background="#444444", foreground="#FFFFFF", font=("Arial", 10))

# Widgets
header_label = ttk.Label(root, text="Weather App", font=("Arial", 16, "bold"))
header_label.pack(pady=10)

location_label = ttk.Label(root, text="Enter ZIP code or City:")
location_label.pack(pady=5)

location_entry = ttk.Entry(root, width=30)
location_entry.pack(pady=5)

search_button = ttk.Button(root, text="Get Weather", command=display_weather)
search_button.pack(pady=10)

result_label = ttk.Label(root, text="", font=("Arial", 12), anchor="center")
result_label.pack(pady=20)

# Run the application
root.mainloop()
