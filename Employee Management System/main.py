import mysql.connector


con = mysql.connector.connect(
    host="localhost", user="root", password="password", database="emp")
def check_employee(employee_id):
    # Query to select all rows from the employees table where id matches
    sql = 'SELECT * FROM employees WHERE id=%s'

    # Making cursor buffered to make rowcount method work properly
    cursor = con.cursor(buffered=True)
    data = (employee_id,)

    # Executing the SQL Query
    cursor.execute(sql, data)

    # Fetch the first row to check if employee exists
    employee = cursor.fetchone()

    # Closing the cursor
    cursor.close()

    # If employee is found, return True, else return False
    return employee is not None
def menu():
    while True:
        print("\nWelcome to Employee Management Record")
        print("Press:")
        print("1 to Add Employee")
        print("2 to Remove Employee")
        print("3 to Promote Employee")
        print("4 to Display Employees")
        print("5 to Exit")
        
        # Taking choice from user
        ch = input("Enter your Choice: ")

        if ch == '1':
            add_employee()
        elif ch == '2':
            remove_employee()
        elif ch == '3':
            promote_employee()
        elif ch == '4':
            display_employees()
        elif ch == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid Choice! Please try again.")