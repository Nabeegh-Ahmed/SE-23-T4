
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://theharism:zFgWhlb6z612sLzZ@cyberbasket.cpurxpb.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

def store_preferences(processed_data, collection_name):
    # Get a reference to the specified collection in the database
    db = client['mydatabase']
    collection = db[collection_name]
    
    result = collection.insert_one(processed_data)
    
    print(f"Inserted document with ID: {result.inserted_id}")
    
    
  #  CLAM
from flask import Flask, request, jsonify
from pymongo import MongoClient

# connect to MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['clam_db']

# define schema for course and lab data
course_schema = {
    'code': str,
    'title': str,
    'instructor': str,
    'day': str,
    'time': str,
    'venue': str,
    'labs': [str],
    'students': int
}

lab_schema = {
    'code': str,
    'title': str,
    'instructor': str,
    'day': str,
    'time': str,
    'venue': str,
    'students': int
}

# create Flask application
app = Flask(_name_)

# route for receiving course and lab data
@app.route('/clam/input', methods=['POST'])
def receive_input():
    course_data = request.json['courses']
    lab_data = request.json['labs']
    
    course_collection = db['courses']
    lab_collection = db['labs']
    
    for course in course_data:
        course_collection.insert_one(course)
        
    for lab in lab_data:
        lab_collection.insert_one(lab)
    
    return jsonify({'message': 'Data received.'})

# route for assigning courses to instructors
@app.route('/clam/assign_courses', methods=['POST'])
def assign_courses():
    instructor_name = request.json['instructor_name']
    course_collection = db['courses']
    
    courses = course_collection.find({'instructor': instructor_name})
    
    for course in courses:
        # assign the course to the instructor based on their preferences and availability
        pass
    
    return jsonify({'message': 'Courses assigned.'})

# route for allocating labs to instructors
@app.route('/clam/allocate_labs', methods=['POST'])
def allocate_labs():
    instructor_name = request.json['instructor_name']
    lab_collection = db['labs']
    
    labs = lab_collection.find({'instructor': instructor_name})
    
    for lab in labs:
        # allocate the lab to the instructor based on their preferences and availability
        pass
    
    return jsonify({'message': 'Labs allocated.'})

# route for allocating venues for courses and labs
@app.route('/clam/allocate_venues', methods=['POST'])
def allocate_venues():
    course_collection = db['courses']
    lab_collection = db['labs']
    
    courses = course_collection.find()
    labs = lab_collection.find()
    
    for course in courses:
        # allocate a suitable venue for the course based on its availability
        pass
    
    for lab in labs:
        # allocate a suitable venue for the lab based on its availability
        pass
    
    return jsonify({'message': 'Venues allocated.'})

if _name_ == '_main_':
    app.run(debug=True)
