from tkinter import Tk, Listbox, Entry, Button, Scrollbar, END 
from tkinter import messagebox 
 
def add_contact(): 
    name = name_entry.get() 
    phone = phone_entry.get() 
    email = email_entry.get() 
 
    if name == "" or phone == "" or email == "": 
        messagebox.showwarning("Input Error", "Please fill all fields.") 
    else: 
        contact = f"{name} | {phone} | {email}" 
        listbox.insert(END, contact) 
        name_entry.delete(0, END) 
        phone_entry.delete(0, END) 
        email_entry.delete(0, END) 
 
def remove_contact(): 
    try: 
        selected_contact = listbox.curselection() 
        listbox.delete(selected_contact) 

 
    except IndexError: 
        messagebox.showwarning("Selection Error", "No contact selected.") 
 
root = Tk() 
root.title("Contact Book") 
 
# Labels for entry fields 
name_label = Button(root, text="Name:") 
name_label.pack() 
 
# Entry widgets for contact information 
name_entry = Entry(root, width=30) 
name_entry.pack() 
 
phone_label = Button(root, text="Phone:") 
phone_label.pack() 
 
phone_entry = Entry(root, width=30) 
phone_entry.pack() 
 
email_label = Button(root, text="Email:") 
email_label.pack() 
 
email_entry = Entry(root, width=30) 
email_entry.pack() 
 
# Button to add contact 
add_button = Button(root, text="Add Contact", command=add_contact) 
add_button.pack() 
 
# Button to remove contact 

 
remove_button = Button(root, text="Remove Contact", 
command=remove_contact) 
remove_button.pack() 
 
# Listbox to display contacts 
listbox = Listbox(root, width=50, height=10) 
listbox.pack() 
 
# Scrollbar for Listbox 
scrollbar = Scrollbar(root, orient="vertical", command=listbox.yview) 
scrollbar.pack(side="right", fill="y") 
listbox.config(yscrollcommand=scrollbar.set) 
 
root.mainloop()