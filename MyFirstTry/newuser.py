import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # ?? ?????? ??? ?-MySQL
            password="kareen2mysql",  # ?????? ??? ?-MySQL
            database="example_database",  # ????? ?????? ???? ????
            port=8808  # ????? ??????
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def insert_user(connection, username, password):
    cursor = connection.cursor()
    query = """
    INSERT INTO users (username, password)
    VALUES (%s, %s);
    """
    try:
        cursor.execute(query, (username, password))
        connection.commit()
        print("User added successfully!")
    except Error as e:
        print(f"The error '{e}' occurred")

# ????? ????? ?-MySQL
connection = create_connection()

# ???? ?? ????? ?????? ?????
if connection is not None and connection.is_connected():
    insert_user(connection, "new_user", "secure_password")
    connection.close()
    print("MySQL connection is closed.")
else:
    print("Failed to connect to the database.")
