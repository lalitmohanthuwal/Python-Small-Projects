import tkinter as tk
from tkinter import messagebox
from Add_Employee import add_employee
from display_employee import display_employees
from Promote_Employee import promote_employee
from remove_employee import remove_employee

# Create the main window
root = tk.Tk()
root.title("Employee Management System")
root.geometry("500x400")

# Title Label
label = tk.Label(root, text="Employee Management System", font=("Arial", 16, "bold"))
label.pack(pady=10)

# Function to add employee
def add_employee_ui():
    add_window = tk.Toplevel(root)
    add_window.title("Add Employee")
    add_window.geometry("300x200")

    tk.Label(add_window, text="Name").grid(row=0, column=0)
    tk.Label(add_window, text="Department").grid(row=1, column=0)
    tk.Label(add_window, text="Salary").grid(row=2, column=0)

    name_entry = tk.Entry(add_window)
    dept_entry = tk.Entry(add_window)
    salary_entry = tk.Entry(add_window)

    name_entry.grid(row=0, column=1)
    dept_entry.grid(row=1, column=1)
    salary_entry.grid(row=2, column=1)

    def submit():
        name = name_entry.get()
        dept = dept_entry.get()
        salary = salary_entry.get()
        add_employee(name, dept, salary)
        messagebox.showinfo("Success", "Employee Added Successfully")
        add_window.destroy()

    tk.Button(add_window, text="Add", command=submit).grid(row=3, column=1, pady=10)

# Buttons
tk.Button(root, text="Add Employee", command=add_employee_ui, width=20, height=2).pack(pady=5)
tk.Button(root, text="View Employees", command=display_employees, width=20, height=2).pack(pady=5)
tk.Button(root, text="Promote Employee", command=promote_employee, width=20, height=2).pack(pady=5)
tk.Button(root, text="Remove Employee", command=remove_employee, width=20, height=2).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit, width=20, height=2, bg="red").pack(pady=10)

root.mainloop()
