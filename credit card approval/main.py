import tkinter as tk
from tkinter import messagebox

class CreditCardPredictor:
    def __init__(self):
        self.min_age = 21
        self.min_income = 15000
        self.max_family_members = 5

    def preprocess_input(self, data):
        """Preprocess the input data and validate it."""
        try:
            data['gender'] = 1 if data['gender'].strip().lower() == 'male' else 0

            marital_map = {'married': 1, 'single': 0, 'divorced': 2, 'widowed': 3}
            data['marital_status'] = marital_map.get(data['marital_status'].strip().lower(), 0)

            dwelling_map = {
                'house': 0, 'apartment': 0, 'with parents': 1,
                'municipal apartment': 2, 'rented apartment': 3, 'office apartment': 4
            }
            data['dwelling_type'] = dwelling_map.get(data['dwelling_type'].strip().lower(), 0)

            return data

        except KeyError as e:
            raise ValueError(f"Missing required field: {e}")

    def calculate_approval_score(self, data):
        """Calculate approval score based on predefined conditions."""
        if data['age'] < self.min_age or data['income'] < self.min_income:
            return False
        if data['family_members'] > self.max_family_members:
            return False
        if data['marital_status'] == 1 and data['income'] < self.min_income * 0.8:
            return False
        if data['dwelling_type'] in [0, 2] and data['income'] < self.min_income * 0.9:
            return False

        return True

    def predict(self, input_data):
        """Make prediction for credit card approval."""
        processed_data = self.preprocess_input(input_data)
        return "Approved" if self.calculate_approval_score(processed_data) else "Not Approved"


def submit_application():
    try:
        user_data = {
            'gender': gender_var.get(),
            'age': int(age_entry.get()),
            'marital_status': marital_var.get(),
            'family_members': int(family_entry.get()),
            'dwelling_type': dwelling_var.get(),
            'income': float(income_entry.get())
        }

        predictor = CreditCardPredictor()
        result = predictor.predict(user_data)
        messagebox.showinfo("Application Result", f"Your application is: {result}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid inputs.")

# GUI Setup
root = tk.Tk()
root.title("Credit Card Approval System")
root.geometry("400x400")

# Labels and Inputs
tk.Label(root, text="Gender:").pack()
gender_var = tk.StringVar()
tk.OptionMenu(root, gender_var, "Male", "Female").pack()

tk.Label(root, text="Age:").pack()
age_entry = tk.Entry(root)
age_entry.pack()

tk.Label(root, text="Marital Status:").pack()
marital_var = tk.StringVar()
tk.OptionMenu(root, marital_var, "Single", "Married", "Divorced", "Widowed").pack()

tk.Label(root, text="Number of Family Members:").pack()
family_entry = tk.Entry(root)
family_entry.pack()

tk.Label(root, text="Dwelling Type:").pack()
dwelling_var = tk.StringVar()
tk.OptionMenu(root, dwelling_var, "House", "Apartment", "With Parents", "Municipal Apartment", "Rented Apartment", "Office Apartment").pack()

tk.Label(root, text="Monthly Income:").pack()
income_entry = tk.Entry(root)
income_entry.pack()

tk.Button(root, text="Submit", command=submit_application).pack()

root.mainloop()
