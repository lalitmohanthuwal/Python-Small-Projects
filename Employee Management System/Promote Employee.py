import mysql.connector
from main import con, check_employee
def promote_employee():
    emp_id = input("Enter Employee ID: ").strip()
    
    if not check_employee(emp_id):
        print("Employee does not exist. Please try again.")
        return

    try:
        increment = float(input("Enter salary increment: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    try:
        with con.cursor() as cursor:
            cursor.execute("SELECT salary FROM employees WHERE id=%s", (emp_id,))
            current_salary = cursor.fetchone()[0]
            new_salary = current_salary + increment

            cursor.execute("UPDATE employees SET salary=%s WHERE id=%s", (new_salary, emp_id))
            con.commit()
            print("Employee Promoted Successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()
