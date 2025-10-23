import tkinter as tk
from tkinter import messagebox

def validate_fields(event=None):
    """Check if Name and Email are valid, then enable/disable Submit button."""
    name = name_entry.get().strip()
    email = email_entry.get().strip()

    # Basic validation checks
    if name and "@" in email:
        submit_btn.config(state="normal")  # Enable button
        status_label.config(text="All fields look good!", fg="green")
    else:
        submit_btn.config(state="disabled")  # Disable button
        status_label.config(text="Please enter valid details.", fg="red")

def submit_form():
    """Handle form submission."""
    name = name_entry.get().strip()
    email = email_entry.get().strip()

    if not name or "@" not in email:
        messagebox.showerror("Invalid Input", "Please fill in valid Name and Email.")
    else:
        messagebox.showinfo("Success", f"Form submitted successfully!\nName: {name}\nEmail: {email}")
        # Optionally clear fields after submit
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        submit_btn.config(state="disabled")
        status_label.config(text="Please enter details again.", fg="blue")

# Create main window
root = tk.Tk()
root.title("Dynamic Form with Enable/Disable States")
root.geometry("400x300")
root.config(bg="#f2f2f2")

# Heading
tk.Label(root, text="User Information Form", font=("Arial", 16, "bold"), bg="#f2f2f2").pack(pady=15)

# Name Label and Entry
tk.Label(root, text="Name:", font=("Arial", 12), bg="#f2f2f2").pack(anchor="w", padx=30)
name_entry = tk.Entry(root, width=40, font=("Arial", 12))
name_entry.pack(pady=5, padx=30)

# Email Label and Entry
tk.Label(root, text="Email:", font=("Arial", 12), bg="#f2f2f2").pack(anchor="w", padx=30)
email_entry = tk.Entry(root, width=40, font=("Arial", 12))
email_entry.pack(pady=5, padx=30)

# Status label for validation messages
status_label = tk.Label(root, text="Please fill in your details.", font=("Arial", 10), fg="red", bg="#f2f2f2")
status_label.pack(pady=10)

# Submit button (initially disabled)
submit_btn = tk.Button(root, text="Submit", font=("Arial", 12, "bold"), state="disabled",
                       bg="#4CAF50", fg="white", width=12, command=submit_form)
submit_btn.pack(pady=10)

# Bind key release event to both entry fields for real-time validation
name_entry.bind("<KeyRelease>", validate_fields)
email_entry.bind("<KeyRelease>", validate_fields)

root.mainloop()
