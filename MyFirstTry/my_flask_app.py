from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# יצירת חיבור ל-MySQL
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

# פונקציה להוספת משתמש חדש לטבלה
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

# דף הבית של ההרשמה
@app.route('/')
def home():
    return render_template('register.html')  # לוודא שהקובץ register.html קיים

# טיפול בטופס ההרשמה
@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    
    connection = create_connection()
    if connection is not None and connection.is_connected():
        insert_user(connection, username, password)
        connection.close()
    
    return redirect(url_for('welcome'))

# לאחר ההרשמה, המשתמש יועבר לדף 'home.html'
@app.route('/welcome')
def welcome():
    print("Navigating to the welcome page")
    return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True, port=8080)

