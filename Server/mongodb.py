from flask import Flask, request, jsonify
from pymongo import MongoClient

# connect to MongoDB database
uri = "mongodb+srv://aminafarooq:<password>@cluster0.bamxcq1.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)

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
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# route for receiving course and lab data
@app.route('/clam/input', methods=['POST'])
def receive_input():
    course_data = [
        {
            'code': 'CSE101',
            'title': 'Introduction to Computer Science',
            'instructor': 'John Smith',
            'day': 'Monday',
            'time': '9:00 AM',
            'venue': 'Room 101',
            'labs': ['L01', 'L02'],
            'students': 50
        },
        {
            'code': 'CSE201',
            'title': 'Data Structures and Algorithms',
            'instructor': 'Jane Doe',
            'day': 'Wednesday',
            'time': '11:00 AM',
            'venue': 'Room 202',
            'labs': ['L03'],
            'students': 40
        }
    ]

    lab_data = [
        {
            'code': 'L01',
            'title': 'Introduction to Python',
            'instructor': 'John Smith',
            'day': 'Tuesday',
            'time': '1:00 PM',
            'venue': 'Lab 1',
            'students': 20
        },
        {
            'code': 'L02',
            'title': 'Introduction to Java',
            'instructor': 'John Smith',
            'day': 'Thursday',
            'time': '2:00 PM',
            'venue': 'Lab 2',
            'students': 25
        },
        {
            'code': 'L03',
            'title': 'Sorting Algorithms',
            'instructor': 'Jane Doe',
            'day': 'Friday',
            'time': '10:00 AM',
            'venue': 'Lab 3',
            'students': 15
        }
    ]

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
    instructor_collection = db['instructors']

    courses = course_collection.find({'instructor': None})
    instructor = instructor_collection.find_one({'name': instructor_name})

    for course in courses:
        # check if the instructor is available at the course time and day
        if course['day'] in instructor['availability'] and course['time'] in instructor['availability'][course['day']]:
            # check if the instructor has the course in their preference list
            if course['code'] in instructor['preference']:
                course_collection.update_one({'_id': course['_id']}, {'$set': {'instructor': instructor_name}})
                instructor_collection.update_one({'_id': instructor['_id']}, {'$push': {'courses': course['code']}})
                return jsonify({'message': 'Course assigned to instructor.'})

    return jsonify({'message': 'No available courses to assign.'})

#route for allocating labs to instructors
@app.route('/clam/allocate_labs', methods=['POST'])
def allocate_labs():
    instructor_name = request.json['instructor_name']
    lab_collection = db['labs']
    course_collection = db['courses']

    # Get the courses the instructor is teaching
    courses = list(course_collection.find({'instructor': instructor_name}, {'_id': 0, 'code': 1}))

    # Get the labs that are not yet assigned to an instructor
    labs = list(lab_collection.find({'instructor': None}, {'_id': 0}))

    # If there are no labs to assign, return a message
    if len(labs) == 0:
        return jsonify({'message': 'No unassigned labs to allocate.'})

    # Assign each lab to the instructor based on their preferences and availability
    for lab in labs:
        # Check if the lab is for one of the instructor's courses
        if lab['code'] in [course['code'] for course in courses]:
            # Check if the lab is at a time the instructor is available
            if is_time_available(instructor_name, lab['day'], lab['time']):
                # Assign the lab to the instructor
                lab_collection.update_one({'_id': lab['_id']}, {'$set': {'instructor': instructor_name}})

    return jsonify({'message': 'Labs allocated.'})

#route for allocating venues for courses and labs
@app.route('/clam/allocate_venues', methods=['POST'])
def allocate_venues():
    course_collection = db['courses']
    lab_collection = db['labs']
    venue_collection = db['venues']

    courses = course_collection.find()
    labs = lab_collection.find()

    for course in courses:
        # find an available venue for the course
        venue = venue_collection.find_one(
            {'day': course['day'], 'time': course['time'], 'capacity': {'$gte': course['students']}})
        if venue:
            # update the course with the allocated venue information
            course_collection.update_one({'_id': course['_id']}, {'$set': {'venue': venue['name']}})
            # reduce the capacity of the venue by the number of students enrolled in the course
            venue_collection.update_one({'_id': venue['_id']}, {'$inc': {'capacity': -course['students']}})

    for lab in labs:
        # find an available venue for the lab
        venue = venue_collection.find_one(
            {'day': lab['day'], 'time': lab['time'], 'capacity': {'$gte': lab['students']}})
        if venue:
            # update the lab with the allocated venue information
            lab_collection.update_one({'_id': lab['_id']}, {'$set': {'venue': venue['name']}})
            # reduce the capacity of the venue by the number of students enrolled in the lab
            venue_collection.update_one({'_id': venue['_id']}, {'$inc': {'capacity': -lab['students']}})

    return jsonify({'message': 'Venues allocated.'})
if __name__ == '__main__':
    app.run( port=8000, debug=True)
