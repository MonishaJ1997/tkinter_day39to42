import tkinter as tk
from tkinter import messagebox, filedialog
import sqlite3
import os

# ------------------------------
# Database setup
# ------------------------------
def init_db():
    """Initialize SQLite database and create table if not exists."""
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def fetch_tasks():
    """Fetch all tasks from the database."""
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_task_to_db(task):
    """Insert new task into database."""
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()

def update_task_in_db(task_id, new_task):
    """Update selected task."""
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET task = ? WHERE id = ?", (new_task, task_id))
    conn.commit()
    conn.close()

def delete_task_from_db(task_id):
    """Delete task from database."""
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

# ------------------------------
# GUI Functions
# ------------------------------
def refresh_task_list():
    """Refresh the Listbox to show current tasks."""
    task_listbox.delete(0, tk.END)
    for task in fetch_tasks():
        task_listbox.insert(tk.END, f"{task[0]}. {task[1]}")

def add_task():
    """Add new task."""
    task = task_entry.get().strip()
    if task:
        add_task_to_db(task)
        task_entry.delete(0, tk.END)
        refresh_task_list()
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

def update_task():
    """Update selected task."""
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Select a task to update!")
        return
    index = selected[0]
    task_text = task_listbox.get(index)
    task_id = int(task_text.split(".")[0])
    new_task = task_entry.get().strip()

    if new_task:
        update_task_in_db(task_id, new_task)
        task_entry.delete(0, tk.END)
        refresh_task_list()
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

def delete_task():
    """Delete selected task."""
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Select a task to delete!")
        return
    index = selected[0]
    task_text = task_listbox.get(index)
    task_id = int(task_text.split(".")[0])

    confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this task?")
    if confirm:
        delete_task_from_db(task_id)
        refresh_task_list()

def export_tasks():
    """Export tasks to a text file."""
    tasks = fetch_tasks()
    if not tasks:
        messagebox.showinfo("No Tasks", "No tasks to export!")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")],
        title="Save Task List"
    )
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(f"{task[0]}. {task[1]}\n")
        messagebox.showinfo("Export Successful", f"Tasks exported to:\n{file_path}")

def on_select(event):
    """Display selected task in Entry box for editing."""
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        task_text = task_listbox.get(index)
        task_entry.delete(0, tk.END)
        task_entry.insert(0, task_text.split(". ", 1)[1])

# ------------------------------
# Main GUI Setup
# ------------------------------
root = tk.Tk()
root.title("SQLite Todo Application")
root.geometry("450x450")
root.config(bg="#f0f0f0")

# Initialize database
init_db()

# Heading
tk.Label(root, text="📝 SQLite To-Do List", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333").pack(pady=10)

# Entry for tasks
task_entry = tk.Entry(root, width=40, font=("Arial", 12))
task_entry.pack(pady=10)

# Buttons
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Task", width=12, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"),
          command=add_task).grid(row=0, column=0, padx=5)

tk.Button(btn_frame, text="Update Task", width=12, bg="#2196F3", fg="white", font=("Arial", 10, "bold"),
          command=update_task).grid(row=0, column=1, padx=5)

tk.Button(btn_frame, text="Delete Task", width=12, bg="#f44336", fg="white", font=("Arial", 10, "bold"),
          command=delete_task).grid(row=0, column=2, padx=5)

tk.Button(btn_frame, text="Export to .txt", width=38, bg="#9C27B0", fg="white", font=("Arial", 10, "bold"),
          command=export_tasks).grid(row=1, column=0, columnspan=3, pady=10)

# Listbox for displaying tasks
task_listbox = tk.Listbox(root, width=50, height=12, font=("Arial", 12))
task_listbox.pack(pady=10)
task_listbox.bind("<<ListboxSelect>>", on_select)

# Load tasks initially
refresh_task_list()

root.mainloop()
