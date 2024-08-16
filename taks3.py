import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

FILENAME = "tasks.json"

if os.path.exists(FILENAME):
    with open(FILENAME, "r") as file:
        tasks = json.load(file)
else:
    tasks = []

def save_tasks():
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

def create_task():
    title = simpledialog.askstring("Input", "Enter task title:")
    description = simpledialog.askstring("Input", "Enter task description:")
    if title and description:
        tasks.append({"title": title, "description": description, "completed": False})
        save_tasks()
        refresh_task_list()

def update_task():
    index = task_listbox.curselection()
    if index:
        index = index[0]
        title = simpledialog.askstring("Input", "Enter new task title:", initialvalue=tasks[index]["title"])
        description = simpledialog.askstring("Input", "Enter new task description:", initialvalue=tasks[index]["description"])
        if title and description:
            tasks[index] = {"title": title, "description": description, "completed": tasks[index]["completed"]}
            save_tasks()
            refresh_task_list()
    else:
        messagebox.showwarning("Warning", "No task selected.")

def delete_task():
    index = task_listbox.curselection()
    if index:
        tasks.pop(index[0])
        save_tasks()
        refresh_task_list()
    else:
        messagebox.showwarning("Warning", "No task selected.")

def mark_task():
    index = task_listbox.curselection()
    if index:
        index = index[0]
        tasks[index]["completed"] = not tasks[index]["completed"]
        save_tasks()
        refresh_task_list()
    else:
        messagebox.showwarning("Warning", "No task selected.")

def refresh_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✓" if task["completed"] else "✗"
        task_listbox.insert(tk.END, f"{task['title']} - {task['description']} [{status}]")

# Set up the GUI
root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

task_listbox = tk.Listbox(frame, width=50, height=10)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
scrollbar.config(command=task_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox.config(yscrollcommand=scrollbar.set)

button_frame = tk.Frame(root)
button_frame.pack(padx=10, pady=10)

create_button = tk.Button(button_frame, text="Create Task", command=create_task)
create_button.grid(row=0, column=0, padx=5, pady=5)

update_button = tk.Button(button_frame, text="Update Task", command=update_task)
update_button.grid(row=0, column=1, padx=5, pady=5)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=2, padx=5, pady=5)

mark_button = tk.Button(button_frame, text="Mark Complete/Incomplete", command=mark_task)
mark_button.grid(row=0, column=3, padx=5, pady=5)

refresh_task_list()
root.mainloop()
