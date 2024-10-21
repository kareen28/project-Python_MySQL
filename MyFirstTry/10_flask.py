from flask import Flask, render_template

# יצירת Flask app
app = Flask(__name__)

# ניתוב לדף הבית
@app.route('/')
def home():
    return render_template('home.html')

# ניתוב להוספת טיול חדש
@app.route('/add_trip')
def add_trip():
    return render_template('add_trip.html')

# ניתוב לדף מקומות מומלצים
@app.route('/trip')
def trip():
    return render_template('trip.html')

# ניתוב לדף 10 טיולים מומלצים לחו"ל
@app.route('/recommended_trips')
def recommended_trips():
    return render_template('recommended_trips.html')

# הרצת האפליקציה
if __name__ == '__main__':
    app.run(debug=True, port=8080)
