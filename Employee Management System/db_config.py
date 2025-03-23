import mysql.connector

# Establish connection
con = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    user="root",
    password="lalit",
    database="lalit"
)

if con.is_connected():
    print("Connected to database")
else:
    print("Failed to connect to database")
