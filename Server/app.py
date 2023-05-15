import pandas as pd
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps
from flask import Flask, request,jsonify, send_file,render_template
from flask_pymongo import PyMongo
import numpy as np
import io
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config['MONGO_URI'] = 'mongodb://localhost:27017/timetable'
mongo = PyMongo(app)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["timetable"]
mycol = mydb["tt"]




@app.route('/')
def home():
    return render_template('timetable.html')

@app.route('/api/import', methods=['POST'])
def import_timetable():
    file = request.files['file']
    timetable = pd.read_excel(file)
    for i in range(len(timetable)):

        courseName = str(timetable.iloc[i, 0])
        section = str(timetable.iloc[i, 1])
        venue = str(timetable.iloc[i, 2])
        time = str(timetable.iloc[i, 3])
        day = str(timetable.iloc[i, 4])

        mydict = {"courseName": courseName, "section": section,
                  "venue": venue, "time": time, "day": day}
        x = mycol.insert_one(mydict)
        print(x)
   
    return {'message': 'Timetable imported successfully'}


@app.route('/api/export')
def export_timetable():
    # Get all rows from the database
    cursor = mycol.find({})
    rows = [row for row in cursor]
    
    # Convert rows to a Pandas DataFrame
    df = pd.DataFrame(rows)
    
    # Save the DataFrame to an Excel file
    filepath = 'timetable.xlsx'
    df.to_excel(filepath, index=False)
    
    # Send the Excel file as a response
    return send_file(filepath, as_attachment=True)



@app.route('/api/timetable')
def get_timetable():
    timetable = mycol.find()
    timetable_list = []
    for row in timetable:
        row_dict = {
            "courseName": row["courseName"],
            "section": row["section"],
            "venue": row["venue"],
            "time": row["time"],
            "day": row["day"]
        }
        timetable_list.append(row_dict)
    return jsonify(timetable_list)




if __name__ == '__main__':
    app.run(port=3002)