import mysql.connector

# Establish MySQL connection
con = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    user="root",
    password="lalit",
    database="hospital"
)

def check_employee(emp_id):
    """Check if an employee exists in the database."""
    sql = "SELECT COUNT(*) FROM employees WHERE id = %s"
    with con.cursor() as cursor:
        cursor.execute(sql, (emp_id,))
        return cursor.fetchone()[0] > 0
