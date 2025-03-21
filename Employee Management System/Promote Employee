def promote_employee():
    Id = input("Enter Employee's Id: ")

    # Checking if Employee with given Id exists
    if not check_employee(Id):
        print("Employee does not exist. Please try again.")
        return
    
    else:
        try:
            Amount = float(input("Enter increase in Salary: "))

            # Query to Fetch Salary of Employee with given Id
            sql_select = 'SELECT salary FROM employees WHERE id=%s'
            data = (Id,)
            cursor = con.cursor()

            # Executing the SQL Query
            cursor.execute(sql_select, data)

            # Fetching Salary of Employee with given Id
            current_salary = cursor.fetchone()[0]
            new_salary = current_salary + Amount

            # Query to Update Salary of Employee with given Id
            sql_update = 'UPDATE employees SET salary=%s WHERE id=%s'
            data_update = (new_salary, Id)

            # Executing the SQL Query to update salary
            cursor.execute(sql_update, data_update)

            # Committing the transaction
            con.commit()
            print("Employee Promoted Successfully")

        except (ValueError, mysql.connector.Error) as e:
            print(f"Error: {e}")
            con.rollback()

        finally:
            # Closing the cursor
            cursor.close()