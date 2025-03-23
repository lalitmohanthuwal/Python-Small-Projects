from db_config import con
import tkinter as tk
from tkinter import messagebox

def update_employee():
    emp_id = entry_id.get().strip()
    new_salary = entry_salary.get().strip()
    new_position = entry_position.get().strip()

    if not emp_id:
        messagebox.showwarning("Input Error", "Please enter Employee ID")
        return

    update_fields = []
    values = []

    if new_salary:
        update_fields.append("salary = %s")
        values.append(new_salary)

    if new_position:
        update_fields.append("position = %s")
        values.append(new_position)

    if not update_fields:
        messagebox.showwarning("Input Error", "Please enter at least one field to update")
        return

    values.append(emp_id)  # Employee ID as the last value

    try:
        cursor = con.cursor()
        sql = f"UPDATE employees SET {', '.join(update_fields)} WHERE id = %s"
        cursor.execute(sql, values)
        con.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Success", "Employee details updated successfully!")
        else:
            messagebox.showwarning("Error", "Employee ID not found")

        cursor.close()
    except Exception as e:
        messagebox.showerror("Database Error", str(e))

# Create GUI Window
def promote_employee():
    promote_window = tk.Toplevel()
    promote_window.title("Update Employee Details")
    promote_window.geometry("400x300")

    # Labels and Entry Fields
    tk.Label(promote_window, text="Employee ID (Required):", font=("Arial", 12)).pack(pady=5)
    global entry_id
    entry_id = tk.Entry(promote_window, font=("Arial", 12))
    entry_id.pack(pady=5)

    tk.Label(promote_window, text="New Salary (Optional):", font=("Arial", 12)).pack(pady=5)
    global entry_salary
    entry_salary = tk.Entry(promote_window, font=("Arial", 12))
    entry_salary.pack(pady=5)

    tk.Label(promote_window, text="New Position (Optional):", font=("Arial", 12)).pack(pady=5)
    global entry_position
    entry_position = tk.Entry(promote_window, font=("Arial", 12))
    entry_position.pack(pady=5)

    # Update Button
    btn_update = tk.Button(promote_window, text="Update Employee", font=("Arial", 12, "bold"), bg="green", fg="white", command=update_employee)
    btn_update.pack(pady=10)

    # Close Button
    btn_close = tk.Button(promote_window, text="Close", font=("Arial", 12), bg="red", fg="white", command=promote_window.destroy)
    btn_close.pack(pady=5)
