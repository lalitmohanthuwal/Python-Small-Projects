import math
import tkinter as tk
from tkinter import messagebox

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def power(a, b):
    return a ** b

def sqrt(a):
    if a < 0:
        return "Error: Square root of negative number"
    return math.sqrt(a)

def sin(a):
    return math.sin(math.radians(a))

def cos(a):
    return math.cos(math.radians(a))

def tan(a):
    return math.tan(math.radians(a))

def perform_calculation():
    try:
        num1 = float(entry1.get()) if entry1.get() else None
        num2 = float(entry2.get()) if entry2.get() else None
        operation = operation_var.get()

        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)
        elif operation == "Power":
            result = power(num1, num2)
        elif operation == "Square Root":
            result = sqrt(num1)
        elif operation == "Sine":
            result = sin(num1)
        elif operation == "Cosine":
            result = cos(num1)
        elif operation == "Tangent":
            result = tan(num1)
        else:
            result = "Invalid operation"

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

# GUI setup
root = tk.Tk()
root.title("Scientific Calculator")

# Input fields
entry1 = tk.Entry(root, width=20)
entry1.grid(row=0, column=1, padx=10, pady=5)
entry2 = tk.Entry(root, width=20)
entry2.grid(row=1, column=1, padx=10, pady=5)

# Labels for inputs
tk.Label(root, text="First Number:").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Second Number:").grid(row=1, column=0, padx=10, pady=5)

# Dropdown for operations
operation_var = tk.StringVar(value="Add")
operations = ["Add", "Subtract", "Multiply", "Divide", "Power", "Square Root", "Sine", "Cosine", "Tangent"]
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.grid(row=2, column=1, padx=10, pady=5)
tk.Label(root, text="Operation:").grid(row=2, column=0, padx=10, pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=perform_calculation)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="Result: ", font=("Arial", 14))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
