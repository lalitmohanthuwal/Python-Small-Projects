import requests
import tkinter as tk
from tkinter import ttk, messagebox

def get_exchange_rate(from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['rates'].get(to_currency, None)
    return None

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = currency_map[from_currency_combo.get()]
        to_currency = currency_map[to_currency_combo.get()]
        
        if not from_currency or not to_currency:
            messagebox.showerror("Error", "Please select both currencies")
            return
        
        exchange_rate = get_exchange_rate(from_currency, to_currency)
        if exchange_rate:
            converted_amount = round(amount * exchange_rate, 2)
            result_label.config(text=f"Converted Amount: {converted_amount} {to_currency_combo.get()}")
        else:
            messagebox.showerror("Error", "Invalid currency or unable to fetch exchange rate")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount")

# Currency mapping with symbols
currency_map = {
    "$ USD": "USD",
    "€ EUR": "EUR",
    "£ GBP": "GBP",
    "₹ INR": "INR",
    "A$ AUD": "AUD",
    "C$ CAD": "CAD",
    "¥ JPY": "JPY",
    "¥ CNY": "CNY"
}

# GUI Setup
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")

tk.Label(root, text="Amount:").pack(pady=5)
amount_entry = tk.Entry(root)
amount_entry.pack(pady=5)

tk.Label(root, text="From Currency:").pack(pady=5)
from_currency_combo = ttk.Combobox(root, values=list(currency_map.keys()))
from_currency_combo.pack(pady=5)
from_currency_combo.set("$ USD")

tk.Label(root, text="To Currency:").pack(pady=5)
to_currency_combo = ttk.Combobox(root, values=list(currency_map.keys()))
to_currency_combo.pack(pady=5)
to_currency_combo.set("₹ INR")

convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="Converted Amount: ")
result_label.pack(pady=10)

root.mainloop()
