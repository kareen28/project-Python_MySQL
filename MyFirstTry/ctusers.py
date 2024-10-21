import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # שם המשתמש שלך ל-MySQL
            password="kareen2mysql",  # הסיסמה שלך ל-MySQL
            database="example_database",  # הבסיס נתונים שכבר יצרת
            port=8808  # הפורט שהגדרת
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def create_table(connection):
    cursor = connection.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    );
    """
    try:
        print("Attempting to create table...")
        cursor.execute(query)
        print("Table 'users' created successfully!")
    except Error as e:
        print(f"The error '{e}' occurred")

# פתיחת חיבור
connection = create_connection()

# יצירת טבלה
if connection is not None and connection.is_connected():
    create_table(connection)
    connection.close()
    print("MySQL connection is closed.")
else:
    print("Failed to connect to the database.")
