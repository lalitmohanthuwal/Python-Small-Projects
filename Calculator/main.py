import tkinter as tk
from tkinter import ttk
import math

def on_button_click(value):
    if value == "C":
        entry_var.set("")
    elif value == "CE":
        entry_var.set(entry_var.get()[:-1])
    elif value == "⌫":
        entry_var.set(entry_var.get()[:-1])
    elif value == "=":
        try:
            entry_var.set(eval(entry_var.get()))
        except:
            entry_var.set("Error")
    else:
        entry_var.set(entry_var.get() + str(value))

root = tk.Tk()
root.title("Modern Calculator")
root.geometry("400x500")
root.configure(bg="#1e1e1e")
root.resizable(True, True)  # Allow resizing

entry_var = tk.StringVar()

ttk.Style().configure("TButton", font=("Arial", 14), padding=10)

entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 24), bg="#282c34", fg="white", justify="right")
entry.pack(pady=20, padx=10, fill="both")

buttons = [
    ["%", "CE", "C", "⌫"],
    ["1/x", "x²", "√x", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["+/-", "0", ".", "="]
]

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(pady=10, fill="both", expand=True)

for r, row in enumerate(buttons):
    frame.rowconfigure(r, weight=1)
    for c, char in enumerate(row):
        frame.columnconfigure(c, weight=1)
        btn = tk.Button(frame, text=char, font=("Arial", 16), bg="#333", fg="white", relief="flat", command=lambda v=char: on_button_click(v))
        btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")  # Allow buttons to expand

root.mainloop()
