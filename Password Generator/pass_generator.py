import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password using the specified length
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def on_generate():
    try:
        # Get the length from the entry widget
        length = int(entry.get())
        if length <= 0:
            raise ValueError("The length must be a positive integer.")
        
        # Generate the password
        password = generate_password(length)
        
        # Display the password
        result_label.config(text=f"Generated Password: {password}")
    except ValueError as ve:
        messagebox.showerror("Invalid Input", f"Error: {ve}")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
label = tk.Label(root, text="Enter the desired length of the password:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=on_generate)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
