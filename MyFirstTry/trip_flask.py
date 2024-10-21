from flask import Flask, render_template

# Create Flask app
app = Flask(__name__)

# Define the homepage route
@app.route('/')
def home():
    return render_template('home.html')

# Define the add_trip route
@app.route('/add_trip')
def add_trip():
    return render_template('add_trip.html')

# Define the trip page route (Recommended places)
@app.route('/trip')
def trip():
    return render_template('trip.html')

# Run the app on the specified port
if __name__ == '__main__':
    app.run(debug=True, port=8080)
