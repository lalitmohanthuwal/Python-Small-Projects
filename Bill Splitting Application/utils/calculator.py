def calculate_settlements(people):
    # Calculate who owes whom
    settlements = []
    debtors = [p for p in people if p.owes > 0]
    creditors = [p for p in people if p.owes < 0]
    
    for debtor in debtors:
        while debtor.owes > 0.01:  # Account for floating point precision
            creditor = creditors[0]
            amount = min(debtor.owes, abs(creditor.owes))
            
            settlements.append({
                'from': debtor.name,
                'to': creditor.name,
                'amount': round(amount, 2)
            })
            
            debtor.owes -= amount
            creditor.owes += amount
            
            if abs(creditor.owes) < 0.01:
                creditors.pop(0)
                
    return settlements
