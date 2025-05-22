import mysql.connector
from mysql.connector import Error

# MySQL connection credentials
host = "example.com"
user = "musab"
password = "pass_here"
database = "db_here"

try:
    # Attempt to connect to the MySQL server
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    if connection.is_connected():
        print("[+] Successfully connected to the database!")
        connection.close()

except Error as e:
    print("[-] Failed to connect to the database.")
    print(f"Error: {e}")
