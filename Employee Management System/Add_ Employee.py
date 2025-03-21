import mysql.connector
from main import con, check_employee

def add_employee():
    emp_id = input("Enter Employee ID: ").strip()
    
    if check_employee(emp_id):
        print("Employee already exists. Please try again.")
        return
    
    name = input("Enter Employee Name: ").strip()
    post = input("Enter Employee Post: ").strip()
    try:
        salary = float(input("Enter Employee Salary: "))
    except ValueError:
        print("Invalid salary input. Please enter a valid number.")
        return

    sql = "INSERT INTO employees (id, name, position, salary) VALUES (%s, %s, %s, %s)"
    data = (emp_id, name, post, salary)
    
    try:
        with con.cursor() as cursor:
            cursor.execute(sql, data)
            con.commit()
            print("Employee Added Successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()
