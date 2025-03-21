def add_employee():
    Id = input("Enter Employee Id: ")

    # Checking if Employee with given Id already exists
    if check_employee(Id):
        print("Employee already exists. Please try again.")
        return
    
    else:
        Name = input("Enter Employee Name: ")
        Post = input("Enter Employee Post: ")
        Salary = input("Enter Employee Salary: ")

        # Inserting Employee details into the employees table
        sql = 'INSERT INTO employees (id, name, position, salary) VALUES (%s, %s, %s, %s)'
        data = (Id, Name, Post, Salary)
        cursor = con.cursor()

        try:
            # Executing the SQL Query
            cursor.execute(sql, data)

            # Committing the transaction
            con.commit()
            print("Employee Added Successfully")
        
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            con.rollback()
        
        finally:
            # Closing the cursor
            cursor.close()