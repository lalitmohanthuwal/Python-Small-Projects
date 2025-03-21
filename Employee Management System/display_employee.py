import mysql.connector
from main import con

def display_employees():
    sql = "SELECT * FROM employees"
    try:
        with con.cursor() as cursor:
            cursor.execute(sql)
            employees = cursor.fetchall()

            if not employees:
                print("No employees found.")
                return

            print("\nEmployee Details:")
            print("=" * 40)
            for emp in employees:
                print(f"ID: {emp[0]}, Name: {emp[1]}, Post: {emp[2]}, Salary: {emp[3]}")
                print("-" * 40)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
