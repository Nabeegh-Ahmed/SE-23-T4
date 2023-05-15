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
    {  # non interest course
        'name': 'Ahmad Ilahi',
        'courses': ['SE', 'AIP'],
        'non_preferred_timeslot': ['2:00PM-3:20PM', '1:00PM-2:20PM'],
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
    },
    {
        'name': 'Karim Zaidi',
        'courses': ['PDC', 'CN','SE'],
        'non_preferred_timeslot': ['2:00PM-3:20PM', '1:00PM-2:20PM'],
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
    {  # non interest course
        'day': 'Monday',
        'course': 'AI',
        'section': 'A',
        'instructor': 'Karim Zaidi',
        'timeslot': '1:00PM-2:20PM'

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
    {  # non interest course
        'day': 'Tuesday',
        'course': 'AI',
        'section': 'C',
        'instructor': 'Ahmad Ilahi',
        'timeslot': '2:00AM-3:20AM'
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
    if ts not in TIMESLOTS[day]:
        TIMESLOTS[day].append(ts)
for day in TIMESLOTS:
    print(day, TIMESLOTS[day])
print(TIMESLOTS)
clashes=[] #list of clashes

def findclashes(clashes):
    clashes.clear()
    classes = tt.Timetable.find({})
    pref = db.preferences.find({})



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
                clash={'type': 'Non-preferred Timeslot','day': day,'resolve':"",'section':section, 'slots':timeslot,'course': course,'instructor': instructor, 'decription':f"{instructor} has been assigned non-preferred timeslot: {timeslot} for {course} course for section {section} on {class_['day']}" }
                clashes.append(clash)
            #checking for non preferred course
            if course not in icourses:
                clash = {'type': 'Non-preferred Course','day': day,'resolve':"",'section':section, 'slots':timeslot,'course': course,'instructor': instructor, 'decription': f"{instructor} has been assigned non-preferred course: {course} for section {section} on {class_['day']} at timeslot: {timeslot}"}
                clashes.append(clash)





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
                clash={'type': 'Non-preferred Timeslot','slots':timeslot,'resolve':"",'section':section,'course': course,'instructor': instructor, 'decription':f"{instructor} has been assigned non-preferred timeslot: {timeslot} for {course} course for section {section} on {class_['day']}" }
                clashes.append(clash)
            #checking for non preferred course
            if course not in icourses:
                clash = {'type': 'Non-preferred Course','section':section,'resolve':"", 'slots':timeslot, 'course': course,'instructor': instructor, 'decription': f"{instructor} has been assigned non-preferred course: {course} for section {section} on {class_['day']} at timeslot: {timeslot}"}
                clashes.append(clash)

        # for time clashes
    classes = tt.Timetable.find({})
    for class_ in classes:  # checking for classes for other sections and courses with same instructor same time
        instructor = class_["instructor"]
        day = class_["day"]
        timeslot = class_["timeslot"]
        course = class_["course"]
        section = class_["section"]
        for clash in tt.Timetable.find({'instructor': instructor, 'timeslot': timeslot, 'day': day}):
            if clash['_id'] != class_['_id']:
                clash = {'type': 'Same Timeslot', 'section': section, 'slots': timeslot, 'resolve': "", 'day': day,
                         'course': course,
                         'instructor': instructor,
                         'decription': f"{instructor} has been assigned a timeslot clash for course: {course} for section {section} on {class_['day']} at timeslot: {timeslot}"}
                clashes.append(clash)


    return clashes

clashes= findclashes(clashes)
for c in clashes:
   print(c)

updatedd = list(clashes)
def resolve_clashes(updatedd):
    resolve=[]
    #resolving clashes
    count=-1
    for clash in updatedd:
        #updatedd = findclashes(updatedd)
        count=count+1
        if clash['type']=='Non-preferred Timeslot':
            #looking for different time-slot
            instructor=clash['instructor']
            course = clash['course']
            day = clash['day']
            section=clash['section']
            pr = db.preferences.find({"name": instructor})
            for p in pr:
                nptime=p['non_preferred_timeslot']


            time = clash['slots']

            #find availability
            ts_available=[t for t in TIMESLOTS[day] if t not in nptime]

            #make sure new timeslot doesn't clash with exisitng
            clashF=True
            for ts in ts_available:
                class_clash=list(tt.Timetable.find({'day':day, 'timeslot':ts}))
                for cl in class_clash:
                    if cl['instructor']==instructor:   #instructor already has class at this time
                        clashF=True
                        break
                    else:
                        clashF=False
                if not clashF:
                    tt.Timetable.update_one(
                        {'day': day, 'timeslot': clash['slots'], 'course': course, 'section': section},
                        {'$set': {'timeslot': ts}}
                    )

                    clashes[count]['resolve']= f"Clash type {clash['type']} for {instructor} at time: {time} and day {day} for course {course} and section {section} can be updated to new timeslot: {ts}"
                    #updatedd = findclashes(updatedd)
                    break


        elif clash['type'] == 'Non-preferred Course':
            instructor = clash['instructor']
            course = clash['course']
            section = clash['section']
            day = clash['day']
            pr = db.preferences.find({"name": instructor})
            for p in pr:
                nptime = p['non_preferred_timeslot']
                pref_c = p['courses']


            current_class= tt.Timetable.find({"instructor": instructor})


            time = clash['slots']


            clashR=False
            # find availability
            ts_available = [t for t in TIMESLOTS[day] if t not in nptime]
            class_avail=[c for c in tt.Timetable.find({}) if c['course'] in pref_c and c not in current_class and c['timeslot'] not in nptime]
            clashF=True
            # make sure new timeslot doesn't clash with exisitin
            for t in ts_available:
                for class_ in class_avail:
                    instructor2 = class_['instructor']
                    times=class_['timeslot']
                    dy=class_['day']
                    crs=class_['course']
                    sec=class_['section']

                    pr = db.preferences.find({"name": instructor2})
                    for p in pr:
                        nonptime = p['non_preferred_timeslot']
                        pref_cr = p['courses']

                    current_class = tt.Timetable.find({"instructor": instructor})
                    if time not in nonptime and course in pref_cr and dy == day:
                        for cr in current_class:
                            if cr['timeslot'] == times :
                              clashF=True
                              break
                            else:
                               clashF=False
                        if not clashF:
                            #resolve = input(f"Do you want to resolve clash type {clash['type']} for {instructor} at time: {time} and day {day} for course {course} ")
                            #if resolve == 'yes':
                            tt.Timetable.update_one(
                                {'day': day, 'timeslot': clash['slots'], 'course': course, 'section': section},
                                {'$set': {'instructor': instructor2}}
                            )
                            tt.Timetable.update_one(
                                {'day': dy, 'timeslot': times, 'course': crs, 'instructor': instructor2,
                                 'section': sec},
                                {'$set': {'instructor': clash['instructor']}}
                            )
                            clashes[count]['resolve'] = f"Class for {instructor} at {time} on {day} for course {course} {section} can be assigned to {instructor2} and class for {instructor2} at {times} on {dy} for  {crs} {sec} can be assigned to {instructor}"
                           # updatedd = findclashes(updatedd)
                            clashR = True
                            break
                if clashR==True:
                    break





        elif clash['type'] == 'Same Timeslot':   #find another slot thats
            instructor = clash['instructor']
            course = clash['course']
            day = clash['day']
            section=clash['section']
            pr = db.preferences.find({"name": instructor})
            for p in pr:
                nptime = p['non_preferred_timeslot']
                pref_c = p['courses']

            current_class = tt.Timetable.find({"instructor": instructor})
            time = clash['slots']

            # find availability
            ts_available = [t for t in TIMESLOTS[day] if t not in nptime]
            class_avail = [c for c in tt.Timetable.find({}) if c not in current_class and c['timeslot'] not in nptime]

            clashR=False
            # make sure new timeslot doesn't clash with exisitin
            for t in ts_available:
                for class_ in class_avail:   #other classes that in preferred timeslot and not already occupied
                    tt.Timetable.update_one(
                        {'day': day, 'timeslot': clash['slots'], 'course': course,'section': section},
                        {'$set': {'timeslot': class_['timeslot']}}
                    )
                    clashes[count]['resolve']=f" The timeslot for class for {instructor} at {clash['slots']} on {day} for {course} {section} can be changed to new timeslot: {class_['timeslot']}  "
                    clashR=True
                    break
                if clashR==True:
                   break

            #updatedd = findclashes(updatedd)


resolve_clashes(updatedd)

app = Flask(__name__)
app.config['SECRET_KEY']="JKADSNFIASF09FWFKSFS"
app.config['MONGO_URI'] = "mongodb+srv://eeshafarrukh057:<W2u2787rWG5CaYN>@cluster0.opyxdoc.mongodb.net/?retryWrites=true&w=majority"



for cl in clashes:
    if cl['resolve']=="":
        cl['resolve']="No resolution found"

jsonStr = json.dumps(clashes)

@app.route("/members")
def members():
    return jsonify(clashes)




if __name__ == '__main__':
    app.run(debug=True)
