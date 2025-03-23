from db_config import con
import tkinter as tk
from tkinter import ttk

def display_employees():
    display_window = tk.Toplevel()
    display_window.title("Employee List")
    display_window.geometry("600x400")

    # Title Label
    title_label = tk.Label(display_window, text="Employee List", font=("Arial", 14, "bold"))
    title_label.pack(pady=10)

    # Create a frame for the table
    frame = tk.Frame(display_window)
    frame.pack(pady=5, padx=5, fill="both", expand=True)

    # Create a treeview (table)
    tree = ttk.Treeview(frame, columns=("ID", "Name", "Department", "Salary"), show="headings")
    tree.heading("ID", text="ID", anchor="center")
    tree.heading("Name", text="Name", anchor="center")
    tree.heading("Department", text="Department", anchor="center")
    tree.heading("Salary", text="Salary", anchor="center")

    tree.column("ID", width=50, anchor="center")
    tree.column("Name", width=150, anchor="w")
    tree.column("Department", width=120, anchor="w")
    tree.column("Salary", width=100, anchor="center")

    # Add a scrollbar
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    
    tree.pack(fill="both", expand=True)

    # Fetch data from the database
    cursor = con.cursor()
    cursor.execute("SELECT * FROM employees")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

    cursor.close()

    # Close button
    close_button = tk.Button(display_window, text="Close", command=display_window.destroy, bg="red", fg="white", font=("Arial", 12))
    close_button.pack(pady=10)
