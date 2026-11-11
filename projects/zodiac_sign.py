# Project 4: Zodiac Sign
# Given the birthdate and name of the person, create a Python program to determine the 
# corresponding zodiac sign based on the date.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import pandas as pd
from datetime import datetime


# creating Gui interface for the zodiac sign calculator

window = tk.Tk()
window.title("Zodiac Sign Calculator")

frame = tk.Frame(window)
frame.pack(padx=20, pady=20)

# Save User info
User_info = tk.LabelFrame(frame, text="User Information")
User_info.pack(padx=10, pady=10)

# Name and Birthdate input fields
tk.Label(User_info, text="Name:").grid(row=1, column=1, sticky="w")
name_entry = tk.Entry(User_info)
name_entry.grid(row=1, column=2, sticky="w")

# Year input fields 
year_label = tk.Label(User_info, text="Year (YYYY):").grid(row=2, column=1)
year_combox = ttk.Combobox(User_info, values=list(range(1900, 2026)))
year_combox.grid(row=2, column=2)

# Month input fields
month_label = tk.Label(User_info, text= "Month (MM):").grid(row=3, column=1)
month_combox = ttk.Combobox(User_info, values=list(range(1, 13)))
month_combox.grid(row=3, column=2)

# Day input fields
day_label = tk.Label(User_info, text="Day (DD):").grid(row=4, column=1)
day_combox = ttk.Combobox(User_info, values=list(range(1, 32)))
day_combox.grid(row=4, column=2)

# Submit button
submit_button = tk.Button(frame, text="Submit", command=lambda: main())
submit_button.pack(pady=10)

# Zodiac sign calculation function

def get_zodiac_sign(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    else:
        return None

# Main function to handle the calculation and data saving

def main():
    name = name_entry.get().strip()
    birthdate = f"{year_combox.get()}-{month_combox.get()}-{day_combox.get()}"

    # Validate the birthdate format and extract day and month
    try:
        birth_date = datetime.strptime(birthdate, "%Y-%m-%d")
        day = birth_date.day
        month = birth_date.month
    except ValueError:
        messagebox.showerror("Error", "Invalid birthdate format. Please enter a date in YYYY-MM-DD format.")
        return

    # Get the zodiac sign based on the day and month
    zodiac_sign = get_zodiac_sign(day, month)

    # Display the result and save the data to a CSV file using Pandas
    if zodiac_sign:
        messagebox.showinfo("Result", f"{name} is a {zodiac_sign}.")

        data = {
            "Name": [name],
            "Birthdate": [birthdate],
            "Zodiac Sign": [zodiac_sign]
        }
        # Create a DataFrame and save to CSV
        df = pd.DataFrame(data)
        file_name = "zodiac_signs.csv"
        file_exists = os.path.exists(file_name)
        # Save the DataFrame to CSV, appending if the file already exists
        df.to_csv(file_name, mode="a", index=False, header=not file_exists)
        messagebox.showinfo("Result", f"Data saved to {file_name} using Pandas.")
    else:
        messagebox.showerror("Error", "Invalid date or unable to determine zodiac sign.")


window.mainloop()

