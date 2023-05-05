from flask import Flask,request
import sys
import mongodb
sys.path.append('./IPM')  #for importing module from IPM directory

from process_data import process_preferences #custom function

app = Flask(__name__) #default

#function for recieving preferences in json format from client
@app.route('/uploadPreferences', methods=['POST'])
def readPreferences():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        preferences = request.get_json()
        process_preferences(preferences)
        return "Preferences Received"
    else:
        return 'Content-Type not supported!'
    
    