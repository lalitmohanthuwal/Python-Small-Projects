import mysql.connector
from main import con, check_employee
def remove_employee():
    emp_id = input("Enter Employee ID: ").strip()
    
    if not check_employee(emp_id):
        print("Employee does not exist. Please try again.")
        return

    sql = "DELETE FROM employees WHERE id=%s"

    try:
        with con.cursor() as cursor:
            cursor.execute(sql, (emp_id,))
            con.commit()
            print("Employee Removed Successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()
