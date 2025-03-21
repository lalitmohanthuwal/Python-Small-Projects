def remove_employee():
    Id = input("Enter Employee Id: ")

    # Checking if Employee with given Id exists
    if not check_employee(Id):
        print("Employee does not exist. Please try again.")
        return
    
    else:
        # Query to delete employee from the employees table
        sql = 'DELETE FROM employees WHERE id=%s'
        data = (Id,)
        cursor = con.cursor()

        try:
            # Executing the SQL Query
            cursor.execute(sql, data)

            # Committing the transaction
            con.commit()
            print("Employee Removed Successfully")
        
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            con.rollback()
        
        finally:
            # Closing the cursor
            cursor.close()