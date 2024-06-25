import tkinter as tk
from tkinter import messagebox

# Define button click event functions
def button_click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(value))

def clear_display():
    display.delete(0, tk.END)

def calculate_result():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error: Div by 0")
        messagebox.showerror("Error", "Division by zero is not allowed.")
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        messagebox.showerror("Error", "Invalid Input")

# Create main application window
app = tk.Tk()
app.title("Simple Calculator")

# Create display area
display = tk.Entry(app, font=('Arial', 20), bd=10, insertwidth=4, width=14, borderwidth=4)
display.grid(row=0, column=0, columnspan=4)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Arrange buttons in a grid
row_val = 1
col_val = 0
for button in buttons:
    if button == 'C':
        tk.Button(app, text=button, padx=20, pady=20, font=('Arial', 20), command=clear_display).grid(row=row_val, column=col_val)
    elif button == '=':
        tk.Button(app, text=button, padx=20, pady=20, font=('Arial', 20), command=calculate_result).grid(row=row_val, column=col_val)
    else:
        tk.Button(app, text=button, padx=20, pady=20, font=('Arial', 20), command=lambda value=button: button_click(value)).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the application
app.mainloop()
