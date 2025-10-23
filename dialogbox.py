import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

# ------------------------------
# Core Application Functions
# ------------------------------

def new_file():
    """Clear the text area and prompt for confirmation if unsaved work."""
    if text_area.get("1.0", tk.END).strip():  # if not empty
        confirm = messagebox.askyesnocancel("Unsaved Work", "Do you want to save your current work before creating a new file?")
        if confirm:  # Yes
            save_file()
        elif confirm is None:  # Cancel
            return
    text_area.delete("1.0", tk.END)
    root.title("Untitled - Custom Dialog App")

def open_file():
    """Prompt user for filename and open file content."""
    file_name = simpledialog.askstring("Open File", "Enter file name to open:")
    if file_name:
        if not file_name.endswith(".txt"):
            file_name += ".txt"
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                content = f.read()
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, content)
            root.title(f"{file_name} - Custom Dialog App")
            messagebox.showinfo("File Opened", f"Successfully opened {file_name}")
        except FileNotFoundError:
            messagebox.showerror("Error", f"File '{file_name}' not found!")

def save_file():
    """Prompt for filename and save content to file."""
    file_name = simpledialog.askstring("Save File", "Enter file name to save:")
    if file_name:
        if not file_name.endswith(".txt"):
            file_name += ".txt"
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(text_area.get("1.0", tk.END).strip())
        messagebox.showinfo("File Saved", f"File saved as {file_name}")
        root.title(f"{file_name} - Custom Dialog App")

def exit_app():
    """Confirm exit, optionally prompt to save before closing."""
    if text_area.get("1.0", tk.END).strip():  # has content
        confirm = messagebox.askyesnocancel("Exit Confirmation", "Do you want to save changes before exiting?")
        if confirm:  # Yes -> Save
            save_file()
        elif confirm is None:  # Cancel exit
            return
    confirm_exit = messagebox.askyesno("Exit Application", "Are you sure you want to exit?")
    if confirm_exit:
        root.destroy()

# ------------------------------
# UI Setup
# ------------------------------

root = tk.Tk()
root.title("Custom Dialog Boxes and Menu System")
root.geometry("600x400")
root.config(bg="#f4f4f4")

# ------------------------------
# Toolbar
# ------------------------------
toolbar = tk.Frame(root, bg="#ddd", height=40)
toolbar.pack(side="top", fill="x")

btn_new = tk.Button(toolbar, text="New", width=8, bg="#4CAF50", fg="white", command=new_file)
btn_new.pack(side="left", padx=5, pady=5)

btn_open = tk.Button(toolbar, text="Open", width=8, bg="#2196F3", fg="white", command=open_file)
btn_open.pack(side="left", padx=5, pady=5)

btn_save = tk.Button(toolbar, text="Save", width=8, bg="#FF9800", fg="white", command=save_file)
btn_save.pack(side="left", padx=5, pady=5)

# ------------------------------
# Menu Bar
# ------------------------------
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

# ------------------------------
# Text Area
# ------------------------------
text_area = tk.Text(root, wrap="word", font=("Arial", 12))
text_area.pack(fill="both", expand=True, padx=10, pady=10)

# ------------------------------
# Run the Application
# ------------------------------
root.protocol("WM_DELETE_WINDOW", exit_app)  # Handle close button
root.mainloop()
