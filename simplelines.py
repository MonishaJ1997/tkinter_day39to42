import tkinter as tk 
 
# Function to add note 
def add_note(): 
    title = entry.get() 
    note = text.get(1.0, tk.END).strip() 
     
    if title and note: 
        notes_list.insert(tk.END, f"Title: {title} - Note: {note}") 
        entry.delete(0, tk.END) 
        text.delete(1.0, tk.END) 
        label.config(text="Note added successfully!", fg="green") 

    else: 
        label.config(text="Please fill in both fields", fg="red") 
 
# Function to clear notes 
def clear_notes(): 
    text.delete(1.0, tk.END) 
 
# Function to delete selected note 
def delete_note(): 
    try: 
        note_index = notes_list.index(tk.ACTIVE) 
        notes_list.delete(note_index) 
    except Exception as e: 
        label.config(text="Select a note to delete", fg="red") 
 
root = tk.Tk() 
root.title("Simple Notes") 
 
# Entry widget for note title 
entry = tk.Entry(root, width=40) 
entry.pack(pady=10) 
 
# Label widget for instructions 
label = tk.Label(root, text="Enter title and note", font=("Arial", 14)) 
label.pack(pady=5) 
 
# Text widget for multi-line note input 
text = tk.Text(root, height=5, width=40) 
text.pack(pady=10) 

 
add_button = tk.Button(root, text="Add Note", command=add_note) 
add_button.pack(pady=5) 
 
clear_button = tk.Button(root, text="Clear Note", command=clear_notes) 
clear_button.pack(pady=5) 
 
delete_button = tk.Button(root, text="Delete Selected Note", 
command=delete_note) 
delete_button.pack(pady=5) 
 
# Listbox to show stored notes 
notes_list = tk.Listbox(root, height=10, width=50) 
notes_list.pack(pady=10) 
 
root.mainloop() 
