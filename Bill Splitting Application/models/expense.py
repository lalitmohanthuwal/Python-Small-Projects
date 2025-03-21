from datetime import datetime

class Expense:
    def __init__(self, description, amount, paid_by):
        self.description = description
        self.amount = amount
        self.paid_by = paid_by
        self.date = datetime.now()
        
    def __str__(self):
        return f"{self.description}: ${self.amount:.2f} (Paid by {self.paid_by.name})"