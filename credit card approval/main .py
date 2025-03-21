class CreditCardPredictor:
    def __init__(self):
        self.min_age = 21
        self.min_income = 15000
        self.max_family_members = 5
        
    def preprocess_input(self, data):
        """Preprocess the input data."""
        # Convert gender to binary
        data['gender'] = 1 if data['gender'].lower() == 'male' else 0
        
        # Convert marital status to numeric
        marital_map = {
            'married': 1,
            'single': 0,
            'divorced': 2,
            'widowed': 3
        }
        data['marital_status'] = marital_map.get(data['marital_status'].lower(), 0)
        
        # Convert dwelling type to numeric
        dwelling_map = {
            'house': 0,
            'apartment': 0,
            'with parents': 1,
            'municipal apartment': 2,
            'rented apartment': 3,
            'office apartment': 4
        }
        data['dwelling_type'] = dwelling_map.get(data['dwelling_type'].lower(), 0)
        
        return data
    
    def predict(self, input_data):
        """Make prediction for credit card approval."""
        processed_data = self.preprocess_input(input_data)
        
        # Basic rule-based decision logic
        score = (
            processed_data['age'] >= self.min_age and
            processed_data['income'] >= self.min_income and
            processed_data['family_members'] <= self.max_family_members
        )
        
        # Additional scoring factors
        if processed_data['marital_status'] == 1:  # Married
            score = score and processed_data['income'] >= self.min_income * 0.8
        
        if processed_data['dwelling_type'] in [0, 2]:  # Owns home or municipal
            score = score and processed_data['income'] >= self.min_income * 0.9
            
        return "Approved" if score else "Not Approved"

def main():
    # Sample usage
    predictor = CreditCardPredictor()
    
    # Example application
    application = {
        'gender': 'Male',
        'age': 25,
        'marital_status': 'Single',
        'family_members': 2,
        'dwelling_type': 'house',
        'income': 50000
    }
    
    result = predictor.predict(application)
    print(f"Application Status: {result}")

if __name__ == "__main__":
    main()