from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# חיבור ל-MySQL
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="kareen2mysql",
            database="example_database",
            port=8808
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

# יצירת הטבלה אם לא קיימת
def create_table(connection):
    cursor = connection.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS trips (
        id INT AUTO_INCREMENT PRIMARY KEY,
        location VARCHAR(255) NOT NULL,
        recommendation TEXT,
        restaurants TEXT,
        details TEXT
    );
    """
    try:
        cursor.execute(query)
        print("Table trips created successfully!")
    except Error as e:
        print(f"The error '{e}' occurred")

# הוספת טיול חדש לטבלה
def insert_trip(connection, location, recommendation, restaurants, details):
    cursor = connection.cursor()
    query = """
    INSERT INTO trips (location, recommendation, restaurants, details)
    VALUES (%s, %s, %s, %s);
    """
    try:
        cursor.execute(query, (location, recommendation, restaurants, details))
        connection.commit()
        print("Trip added successfully!")
    except Error as e:
        print(f"The error '{e}' occurred")

# דף הבית עם הצגת כל הטיולים
@app.route('/')
def home():
    connection = create_connection()
    create_table(connection)  # יצירת הטבלה אם לא קיימת
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM trips")
    trips = cursor.fetchall()
    connection.close()
    return render_template('home.html', trips=trips)

# דף הוספת טיול
@app.route('/add_trip', methods=['GET', 'POST'])
def add_trip():
    if request.method == 'POST':
        location = request.form['location']
        recommendation = request.form['recommendation']
        restaurants = request.form['restaurants']
        details = request.form['details']
        
        connection = create_connection()
        if connection is not None and connection.is_connected():
            insert_trip(connection, location, recommendation, restaurants, details)
            connection.close()
        
        return redirect(url_for('home'))
    
    return render_template('add_trip.html')  # אם לא נשלחה בקשה POST, להחזיר את הטופס

if __name__ == '__main__':
    app.run(debug=True, port=8080)
