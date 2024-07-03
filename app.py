from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('localhost', 27017)  # Assuming MongoDB is running on localhost:27017
db = client['travel_db']  # Replace 'travel_db' with your database name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customer', methods=['GET', 'POST'])
def customer():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        
        # Insert into MongoDB
        customers = db.customers
        customers.insert_one({'name': name, 'email': email})
        return 'Customer added successfully'

    return render_template('customer.html')

@app.route('/hotel', methods=['GET', 'POST'])
def hotel():
    if request.method == 'POST':
        # Get form data
        hotel_name = request.form['hotel_name']
        check_in_date = request.form['check_in_date']
        check_out_date = request.form['check_out_date']
        
        # Insert into MongoDB
        bookings = db.bookings
        bookings.insert_one({'hotel_name': hotel_name, 'check_in_date': check_in_date, 'check_out_date': check_out_date})
        return 'Hotel booking added successfully'

    return render_template('hotel.html')

@app.route('/places')
def places():
    # Query tourism places from MongoDB (if needed)
    # Example: Fetching places from a collection
    places_collection = db.places
    places_list = places_collection.find()
    
    # Render template with places data
    return render_template('places.html', places=places_list)

if __name__ == '__main__':
    app.run(debug=True)
