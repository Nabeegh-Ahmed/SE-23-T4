
def process_teachers_preferences(data):
     
    if isinstance(data, list):
        
        result = {}

        result["name"] = data[0]["name"]
        result["number"] = "0" + str(data[0]["number"])
        result["email"] = data[0]["email"]

        courses = []
        non_preferred_timeslot = []

        # Loop through each element in data
        for i in range(len(data)):
            courses.append(data[i]["courseName"]) 
            non_preferred_timeslot.append(data[i]["nonPreferredSlots"])

        result["courses"] = courses
        result["non_preferred_timeslot"] = non_preferred_timeslot

        return result
    
    else:
        
        result = {
            "name": data["name"],
            "number": data["number"],
            "email": data["email"],
            "courses": [],
            "non_preferred_timeslot": []
        }

        for course in data["courses"]:
            result["courses"].append(course["courseName"])
            result["non_preferred_timeslot"].append(course["nonPreferredSlots"])

        return result


    
def process_labinstructors_preferences(data):
   
    if isinstance(data,list):
        
        result = {}
        
        for key in data[0]:
            if key not in ['labName', 'preferredSlots', 'grade', 'cgpa', 'university']:
                result[key.lower()] = data[0][key]

        for key in ['labName', 'preferredSlots', 'grade', 'cgpa', 'university']:
            result[key.lower()] = [d[key] for d in data]

        result['number'] = '0' + str(data[0]['number'])

        return result
    
    else:
            result = {
        'name': data['name'],
        'number': data['number'],
        'email': data['email'],
        'labname': [lab['labName'] for lab in data['labs']],
        'preferredslots': [lab['preferredSlots'] for lab in data['labs']],
        'grade': [lab['grade'] for lab in data['labs']],
        'cgpa': [int(lab['cgpa']) for lab in data['labs']],
        'university': [lab['university'] for lab in data['labs']]
        }
            
            return result
        
