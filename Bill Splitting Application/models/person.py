class Person:
    def __init__(self, name):
        self.name = name
        self.total_paid = 0
        self.share = 0

    def add_payment(self, amount):
        self.total_paid += amount

    def calculate_share(self, total, num_people):
        self.share = total / num_people

    def balance(self):
        return self.total_paid - self.share

    def __repr__(self):
        return f"Person(name={self.name}, paid={self.total_paid}, share={self.share})"
