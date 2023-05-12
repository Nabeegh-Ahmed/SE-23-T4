from flask import Flask,request,jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask_cors import CORS
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json



uri = "mongodb+srv://eeshafarrukh057:W2u2787rWG5CaYN@cluster0.opyxdoc.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)

print(client.list_database_names())
db= client.preferences
print(db.list_collection_names())
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
lp= client.labpref
lp.labpred.delete_many({})
result=lp.labpref.insert_many([
    {

            "name": "Mr None",
            "number": "123456789",
            "email": "qwertyuiop@gmail.com",
            "labName": ["Ai", "OR", "SE"],
            "preferredSlots": ["8:30-11:30", "11:30-2:30", "2:30-5:30"],
            "grade": ["A", "A", "A"],
            "cgpa": ["4", "4", "4"],
            "university": ["NU", "NU", "NU"]

    },
    {
        "name": "Ms. Jane Doe",
        "number": "987654321",
        "email": "janedoe123@gmail.com",
        "labName": ["ML", "CV", "NLP"],
        "preferredSlots": ["9:00-12:00", "1:00-4:00", "4:00-7:00"],
        "grade": ["A", "B", "A"],
        "cgpa": ["3.9", "3.7", "4.0"],
        "university": ["Harvard", "MIT", "Stanford"]
    },
    {
        "name": "Dr. John Smith",
        "number": "5551234567",
        "email": "johnsmith789@gmail.com",
        "labName": ["RL", "DL", "AI"],
        "preferredSlots": ["10:00-1:00", "2:00-5:00", "5:00-8:00"],
        "grade": ["A+", "A+", "A+"],
        "cgpa": ["4.0", "4.0", "4.0"],
        "university": ["UC Berkeley", "Carnegie Mellon", "Caltech"]
    }

])

db.preferences.delete_many({})
result=db.preferences.insert_many([
    {
            'name': 'Kashif Zafar',
            'courses': ['AI', 'AIP'],
            'non_preferred_timeslot': ['8:30AM-9:50AM','11:30AM-12:50PM'],
            'email': 'kashi.zafar@nu.edu.pk.com',
    },
    {
            'name': 'Muzamil Hasan Zaidi',
            'courses': ['Philosophy', 'Big Data Analytics'],
            'non_preferred_timeslot': ['11:30AM-12:50PM','8:30AM-9:50AM' ],
            'email': 'hoflolz@gmail.com',

    },
    {
            'name': 'Zulfiqar Ali Bhutto',
            'courses': ['Public Speaking', 'History'],
            'non_preferred_timeslot': ['1:00PM-2:20PM','8:30AM-9:50AM'],
            'email': 'bhuttojani@gmail.com',
    },
    {
            'name': 'Ahmad Zafar',
            'courses': ['PDC', 'CN'],
            'non_preferred_timeslot': ['2:00PM-3:20PM','1:00PM-2:20PM'],
            'email': 'ahmad1@gmail.com',
    }

])

tt=client.Timetable
tt.Timetable.delete_many({})
result=tt.Timetable.insert_many([
    {
        'day': 'Monday',
        'course': 'AI',
        'section': 'B',
        'instructor': 'Kashif Zafar',
        'timeslot': '8:30AM-9:50AM'
    },
    {#classes assigned at the same time
        'day': 'Monday',
        'course': 'AI',
        'section': 'A',
        'instructor': 'Kashif Zafar',
        'timeslot': '8:30AM-9:50AM'
    },
    {#non interest course
        'day': 'Monday',
        'course': 'DLD',
        'section': 'A',
        'instructor': 'Muzamil Hasan Zaidi',
        'timeslot': '8:30AM-9:50AM'

    },
    {#non preferred timings
        'day': 'Monday',
        'course': 'PDC',
        'section': 'C',
        'instructor': 'Ahmad Zafar',
        'timeslot': '2:00PM-3:20PM'
    },
    { #non interest course
        'day': 'Tuesday',
        'course': 'SE',
        'section': 'A',
        'instructor': 'Kashif Zafar',
        'timeslot': '10:00AM-11:20AM'
    },
    { #non preferred time
        'day': 'Tuesday',
        'course': 'History',
        'section': 'A',
        'instructor': 'Zulfiqar Ali Bhutto',
        'timeslot': '11:30AM-12:50PM'
    },
    {
        'day': 'Tuesday',
        'course': 'Philosophy',
        'section': 'A',
        'instructor': 'Muzamil Hasan Zaidi',
        'timeslot': '8:30AM-9:50AM'
    }
    ])

TIMESLOTS= {
    'Monday': [],
    'Tuesday': [],
    'Wednesday': [],
    'Thursday': [],
    'Friday': [],
    'Saturday': []
}
cursor=tt.Timetable.find({})
for d in cursor:
    day=d['day']
    ts=d['timeslot']
    TIMESLOTS[day].append(ts)
for day in TIMESLOTS:
    print(day, TIMESLOTS[day])
print(TIMESLOTS)
clashes=[] #list of clashes
classes=tt.Timetable.find({})
pref=db.preferences.find({})
# for preferences
for pref in pref:   # loop through all preferences
    instructor=pref["name"]
    nptime=pref["non_preferred_timeslot"]
    icourses=pref["courses"]

    # getting all classes for instructor
    classes=tt.Timetable.find({"instructor":instructor})

    for class_ in classes:
        course=class_["course"]
        timeslot=class_["timeslot"]
        section=class_["section"]
        day=class_['day']

        #checking for non preferred timeslot
        if timeslot in nptime:
            clash={'type': 'Non-preferred Timeslot','day': day, 'slots':timeslot,'course': course,'instructor': instructor, 'decription':f"{instructor} has been assigned non-preferred timeslot: {timeslot} for {course} course for section {section} on {class_['day']}" }
            clashes.append(clash)
        #checking for non preferred course
        if course not in icourses:
            clash = {'type': 'Non-preferred Course','day': day, 'slots':timeslot,'course': course,'instructor': instructor, 'decription': f"{instructor} has been assigned non-preferred course: {course} for section {section} on {class_['day']} at timeslot: {timeslot}"}
            clashes.append(clash)

for c in clashes:
   print(c)
labp=lp.labpref.find({})
#for lab pref
for pref in labp:   # loop through all preferences
    instructor=pref["name"]
    ptime=pref["preferredSlots"]
    icourses=pref["labName"]

    # getting all classes for instructor
    classes=tt.Timetable.find({"instructor":instructor})

    for class_ in classes:
        course=class_["course"]
        timeslot=class_["timeslot"]
        section=class_["section"]

        #checking for non preferred timeslot
        if timeslot not in ptime:
            clash={'type': 'Non-preferred Timeslot','slots':timeslot,'course': course,'instructor': instructor, 'decription':f"{instructor} has been assigned non-preferred timeslot: {timeslot} for {course} course for section {section} on {class_['day']}" }
            clashes.append(clash)
        #checking for non preferred course
        if course not in icourses:
            clash = {'type': 'Non-preferred Course', 'slots':timeslot, 'course': course,'instructor': instructor, 'decription': f"{instructor} has been assigned non-preferred course: {course} for section {section} on {class_['day']} at timeslot: {timeslot}"}
            clashes.append(clash)

for c in clashes:
   print(c)







# for time clashes
classes=tt.Timetable.find({})
for class_ in classes:#checking for classes for other sections and courses with same instructor same time
    instructor=class_["instructor"]
    day=class_["day"]
    timeslot=class_["timeslot"]
    course=class_["course"]
    section=class_["section"]
    for clash in tt.Timetable.find({'instructor': instructor, 'timeslot': timeslot,'day': day}):
        if clash['_id']!=class_['_id']:
            clash = {'type': 'Same Timeslot', 'slots': timeslot,'day': day,'course': course, 'instructor':instructor, 'decription': f"{instructor} has been assigned a timeslot clash for course: {course} for section {section} on {class_['day']} at timeslot: {timeslot}"}
            clashes.append(clash)

for c in clashes:
   print(c)


#resolving clashes

for clash in clashes:
    if clash['type']=='Non-preferred Timeslot':
        #looking for different time-slot
        instructor=clash['instructor']
        course = clash['course']
        day = clash['day']
        nptime = clash['slots']

        #find availability
        ts_available=[t for t in TIMESLOTS[day] if t not in nptime]

        #make sure new timeslot doesn't clash with exisitng
        clashF=True
        for ts in ts_available:
            class_clash=list(tt.Timetable.find({'day':day, 'timeslot':ts}))
            for cl in class_clash:
                if cl['instructor']==instructor:
                    clashF=True
                    break
                else:
                    clashF=False
            if not clashF:
                resolve= input(f"Do you want to resolve clash type {clash['type']} for {instructor} at time: {nptime} and day {day} for course {course} ")
                if resolve=='yes':
                    tt.Timetable.update_one(
                        {'day': day, 'timeslot': clash['slots'], 'course': course, 'section': section},
                        {'$set': {'timeslot': ts}}
                    )






app = Flask(__name__)
app.config['SECRET_KEY']="JKADSNFIASF09FWFKSFS"
app.config['MONGO_URI'] = "mongodb+srv://eeshafarrukh057:<W2u2787rWG5CaYN>@cluster0.opyxdoc.mongodb.net/?retryWrites=true&w=majority"

print(type(clashes))



jsonStr = json.dumps(clashes)

@app.route("/members")
def members():
    return jsonify(clashes)




if __name__ == '__main__':
    app.run(debug=True)
