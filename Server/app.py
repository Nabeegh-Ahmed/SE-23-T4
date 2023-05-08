from flask import Flask,request
import sys
import mongodb
from flask_cors import CORS
sys.path.append('./IPM')  #for importing module from IPM directory
from process_data import process_teachers_preferences,process_labinstructors_preferences #custom function

app = Flask(__name__) #default

CORS(app)

#function for recieving preferences in json format from client
@app.route('/uploadTeachersPreferences', methods=['POST'])
def readTeachersPreferences():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        preferences = request.get_json()
        processed_data = process_teachers_preferences(preferences)
        mongodb.store_preferences(processed_data, 'teachers_preferences')
        print(processed_data)
        return "Preferences Received"
    else:
        return 'Content-Type not supported!'

@app.route('/uploadLabInstructorsPreferences', methods=['POST'])
def readLabInstructorsPreferences():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        preferences = request.get_json()
        processed_data = process_labinstructors_preferences(preferences)
        mongodb.store_preferences(processed_data, 'lab_instructors_preferences')
        print(processed_data)
        return "Preferences Received"
    else:
        return 'Content-Type not supported!'