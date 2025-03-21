def display_employees():
    try:
        # Query to select all rows from the employees table
        sql = 'SELECT * FROM employees'
        cursor = con.cursor()

        # Executing the SQL Query
        cursor.execute(sql)

        # Fetching all details of all the Employees
        employees = cursor.fetchall()
        for employee in employees:
            print("Employee Id : ", employee[0])
            print("Employee Name : ", employee[1])
            print("Employee Post : ", employee[2])
            print("Employee Salary : ", employee[3])
            print("------------------------------------")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Closing the cursor
        cursor.close()