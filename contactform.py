import tkinter as tk 
 
# Function to display the entered information 
def submit_form(): 
    name = name_entry.get() 
    email = email_entry.get() 
    message = message_text.get("1.0", "end-1c")  # Get text from the Text widget 
    print(f"Name: {name}\nEmail: {email}\nMessage: {message}") 
    result_label.config(text="Form Submitted Successfully!") 
 
# Create the main window 
root = tk.Tk() 
root.title("Contact Form") 
root.geometry("400x300") 
 
# Create Labels 
name_label = tk.Label(root, text="Name:") 
name_label.grid(row=0, column=0, pady=5, padx=5) 
 
email_label = tk.Label(root, text="Email:") 
email_label.grid(row=1, column=0, pady=5, padx=5) 
 
message_label = tk.Label(root, text="Message:") 
message_label.grid(row=2, column=0, pady=5, padx=5) 
 

 
 
# Create Entry widgets 
name_entry = tk.Entry(root) 
name_entry.grid(row=0, column=1, pady=5, padx=5) 
 
email_entry = tk.Entry(root) 
email_entry.grid(row=1, column=1, pady=5, padx=5) 
 
# Create Text widget for Message 
message_text = tk.Text(root, height=5, width=30) 
message_text.grid(row=2, column=1, pady=5, padx=5) 
 
# Create a Button widget 
submit_button = tk.Button(root, text="Submit", command=submit_form) 
submit_button.grid(row=3, column=1, pady=10) 
 
# Create a Label to show result 
result_label = tk.Label(root, text="") 
result_label.grid(row=4, column=0, columnspan=2) 
 
# Start the Tkinter event loop 
root.mainloop()

