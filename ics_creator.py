import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tkcalendar import DateEntry
from ics import Calendar, Event
from datetime import datetime, timedelta

def create_meeting(title, start_date, start_hour, start_minute, duration_minutes, location, description, output_file):
    start_time = datetime.combine(start_date, datetime.min.time()) + timedelta(hours=start_hour, minutes=start_minute)
    calendar = Calendar()
    event = Event()
    event.name = title
    event.begin = start_time
    event.end = start_time + timedelta(minutes=duration_minutes)
    event.location = location
    event.description = description
    calendar.events.add(event)
    with open(output_file, "w") as f:
        f.writelines(calendar)
    messagebox.showinfo("Success", f"Meeting created and saved to {output_file}")

def submit():
    title = title_entry.get()
    start_date = date_entry.get_date()
    start_hour = int(hour_entry.get())
    start_minute = int(minute_entry.get())
    duration_minutes = int(duration_entry.get())
    location = location_entry.get()
    description = description_entry.get()
    output_file = filedialog.asksaveasfilename(defaultextension=".ics", initialfile=title, filetypes=[("ICS files", "*.ics")])
    if output_file:
        create_meeting(title, start_date, start_hour, start_minute, duration_minutes, location, description, output_file)

root = tk.Tk()
root.title("ICS Meeting Creator")

tk.Label(root, text="Title").grid(row=0)
tk.Label(root, text="Date").grid(row=1)
tk.Label(root, text="Time (24-hour format)").grid(row=2)
tk.Label(root, text="Duration (minutes)").grid(row=3)
tk.Label(root, text="Location").grid(row=4)
tk.Label(root, text="Description").grid(row=5)

title_entry = tk.Entry(root)
date_entry = DateEntry(root, date_pattern='yyyy-mm-dd')
hour_entry = ttk.Spinbox(root, from_=0, to=23, width=5)
minute_entry = ttk.Spinbox(root, values=(0, 15, 30, 45), width=5)
duration_entry = tk.Entry(root)
location_entry = tk.Entry(root)
description_entry = tk.Entry(root)

title_entry.grid(row=0, column=1)
date_entry.grid(row=1, column=1)
hour_entry.grid(row=2, column=1, sticky='w')
minute_entry.grid(row=2, column=1, sticky='e')
duration_entry.grid(row=3, column=1)
location_entry.grid(row=4, column=1)
description_entry.grid(row=5, column=1)

tk.Button(root, text="Create Meeting", command=submit).grid(row=6, column=1)

root.mainloop()