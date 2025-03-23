from db_config import con
import tkinter as tk
from tkinter import messagebox

def remove_employee():
    remove_window = tk.Toplevel()
    remove_window.title("Remove Employee")
    remove_window.geometry("300x150")

    tk.Label(remove_window, text="Enter Employee ID to Remove").pack()
    emp_id_entry = tk.Entry(remove_window)
    emp_id_entry.pack()

    def delete():
        emp_id = emp_id_entry.get()
        cursor = con.cursor()
        cursor.execute("DELETE FROM employees WHERE id = %s", (emp_id,))
        con.commit()
        cursor.close()
        messagebox.showinfo("Success", "Employee Removed")
        remove_window.destroy()

    tk.Button(remove_window, text="Delete", command=delete).pack(pady=10)
