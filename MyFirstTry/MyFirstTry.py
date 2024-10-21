import mysql.connector

try:
    # יצירת חיבור לשרת MySQL על פורט 8808
    connection = mysql.connector.connect(
        host="localhost",  # אם השרת מקומי
        user="root",  # שם המשתמש שלך ל-MySQL
        password="kareen2mysql",  # הסיסמה שלך ל-MySQL
        port=8808  # הפורט שאת משתמשת בו (יש פסיק לפני השורה הזו!)
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # יצירת בסיס נתונים
        cursor.execute("CREATE DATABASE IF NOT EXISTS example_database")
        print("Database 'example_database' created successfully!")

        # שימוש בבסיס הנתונים שנוצר
        connection.database = "example_database"
        print(f"Now using database: {connection.database}")

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")
