import tkinter as tk
from tkinter import messagebox
from datetime import datetime

appointments = []

def add_appointment():
    """Add an appointment to the list."""
    date = entry_date.get()
    time = entry_time.get()
    description = entry_description.get()
    try:
        datetime.strptime(date, "%Y-%m-%d")
        datetime.strptime(time, "%H:%M")
        appointments.append(f"{date} {time} - {description}")
        listbox_appointments.insert(tk.END, f"{date} {time}: {description}")
        entry_date.delete(0, tk.END)
        entry_time.delete(0, tk.END)
        entry_description.delete(0, tk.END)
    except ValueError:
        messagebox.showwarning("Warning", "Invalid date or time format. Use YYYY-MM-DD for date and HH:MM for time.")

# Create the main window
root = tk.Tk()
root.title("Appointment Scheduler")

# Create and place widgets
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

label_date = tk.Label(frame_input, text="Date (YYYY-MM-DD):")
label_date.pack()

entry_date = tk.Entry(frame_input)
entry_date.pack()

label_time = tk.Label(frame_input, text="Time (HH:MM):")
label_time.pack()

entry_time = tk.Entry(frame_input)
entry_time.pack()

label_description = tk.Label(frame_input, text="Description:")
label_description.pack()

entry_description = tk.Entry(frame_input, width=40)
entry_description.pack()

button_add = tk.Button(frame_input, text="Add Appointment", command=add_appointment)
button_add.pack(pady=5)

listbox_appointments = tk.Listbox(root, width=60, height=15)
listbox_appointments.pack(expand=True, fill=tk.BOTH)

# Start the main loop
root.mainloop()
