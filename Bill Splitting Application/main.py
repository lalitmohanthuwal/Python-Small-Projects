from models.person import Person
from models.expense import Expense
from utils.calculator import calculate_settlements

def main():
    # Get group members
    print("Enter the names of people (one per line, empty line to finish):")
    people = []
    while True:
        name = input().strip()
        if not name:
            break
        people.append(Person(name))
    
    # Get expenses
    print("\nEnter expenses (format: description amount payer_name, empty line to finish):")
    expenses = []
    while True:
        expense_input = input().strip()
        if not expense_input:
            break
            
        try:
            desc, amount, payer_name = expense_input.rsplit(maxsplit=2)
            amount = float(amount)
            payer = next(p for p in people if p.name.lower() == payer_name.lower())
            
            expense = Expense(desc, amount, payer)
            expenses.append(expense)
            payer.add_payment(amount)
        except ValueError:
            print("Invalid input format. Please use: description amount payer_name")
            continue
    
    # Calculate total and shares
    total = sum(e.amount for e in expenses)
    for person in people:
        person.calculate_share(total, len(people))
    
    # Print summary
    print("\n=== Expense Summary ===")
    for expense in expenses:
        print(expense)
    
    print("\n=== Settlements ===")
    settlements = calculate_settlements(people)
    for settlement in settlements:
        print(f"{settlement['from']} pays ${settlement['amount']:.2f} to {settlement['to']}")

if __name__ == "__main__":
    main()