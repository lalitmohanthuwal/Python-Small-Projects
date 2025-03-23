from db_config import con

def add_employee(name, department, salary):
    """Function to add an employee to the database."""
    sql = "INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)"
    
    try:
        with con.cursor() as cursor:
            cursor.execute(sql, (name, department, salary))
            con.commit()
    except Exception as err:
        print(f"Error: {err}")
