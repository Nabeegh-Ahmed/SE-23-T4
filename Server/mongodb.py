
from pymongo.mongo_client import MongoClient


uri = "mongodb://localhost:27017"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


# defining schema for the databases
# 1- Teacher
teacher_schema = {
    'name': str,
    'number': str,
    'email': str,
    'courses': [str],
    'non_preferred_timeslot': [str]
}

# 1- Lab Instructors
lab_instructor_schema = {
    'name': str,
    'number': str,
    'email': str,
    'labname': [str],
    'preferredslots': [str],
    'grade': [str],
    'cgpa': [float],
    'university': [str],
}

# Labs offered
lab_schema = {
    'lab_code': str,
    'name': str
}

# sections offered for each lab 
section_schema = {
    'section_name': str,
    'lab_code': str
}
# creating database 
db =  client["LabAllocation"]

# Collection names
instructor_collection = db['lab_instructor']
lab_collection = db['lab']
section_collection = db['section']

# a function that takes a lab code and returns the lab name
def return_Lab_name(val):
    lab = lab_collection.find_one({'lab_code': val})
    if lab:
        return lab['name']
    else:
        return None

# verify that if there is any section of a lab
def return_section_name(val):
    section = section_collection.find_one({'lab_code': val})
    if section:
        return section['section_name']
    else:
        return None
    
# a function that return the instructor name who have a hisghest grade in a particular lab
def return_instructor_name(labName):
    instructors = []
    grades = []
    cgpa = []

    # iterate over each document in the collection
    for doc in instructor_collection.find():
        lab_index = None
        instructor_grade = None
        instructor_cgpa = None

        # find the index where labName matches in the labname array
        if labName in doc['labname']:
            lab_index = doc['labname'].index(labName)

        # if lab_index is found, get the corresponding grade and cgpa from the grade and cgpa arrays
        if lab_index is not None:
            instructor_grade = doc['grade'][lab_index]
            instructor_cgpa = doc['cgpa'][lab_index]

        # if all the values are found, add the instructor name, grade, and cgpa to the respective lists
        if lab_index is not None and instructor_grade is not None and instructor_cgpa is not None:
            instructors.append(doc['name'])
            grades.append(instructor_grade)
            cgpa.append(instructor_cgpa)

    # check if instructors, grades, and cgpa lists are empty
    if not instructors or not grades or not cgpa:
        return None


    # sort the instructors, grades, and cgpa based on grades and then cgpa in ascending order
    sorted_data = sorted(zip(grades, cgpa, instructors), key=lambda x: (x[0], -x[1]))
    sorted_grades, sorted_cgpa, sorted_instructors = zip(*sorted_data)
    
    return list(sorted_instructors), list(sorted_grades), list(sorted_cgpa)


# Retrieve list of instructors,labs and sections
instructors = instructor_collection.find()
labs = lab_collection.find()
sections = section_collection.find()

for lab in labs:
    lab_Code = lab['lab_code']
    lab_Name = lab['name']
    print("\n*********\n")
    
for section in sections:
    section_Name = section['section_name']
    section_lab_Code = section['lab_code']

# Iterate through each instructor
for instructor in instructors:
    instructor_name = instructor['name']
    preferred_labs = instructor['labname']
    preferred_slots = instructor['preferredslots']
    grades = instructor['grade']
    cgpa = instructor['cgpa']

# grade hierarchy to know which instructor grade is higher inorder to assign lab to him
grade_hierarchy = {'A+': 7, 'A': 6, 'A-': 5, 'B+': 4, 'B': 3, 'B-': 2, 'C+': 1, 'C': 0, 'D+': -1, 'D': -2, 'F': -3}

# get the list of labs from the lab collection
labs = [lab['lab_code'] for lab in lab_collection.find()]
i = 0 
Allocated_Labs = [] # to check the lab going to assigned not in the list
Allocated_Sections = [] # to check the section going to assigned not in the list
# allocated_instructor consist of tuple of instructor name and a count of how many labs he is assigned.
Allocated_instructors = [] # to check the instructor going to assigned not in the list

for lab in labs:
    # get the first lab to last lab from the list on each iteration
    if len(labs) > 0:
        lab = labs[i]
        i+=1
        # verify that if there is any section of a lab
        if return_section_name(lab) not in Allocated_Sections:
                Allocated_Sections.append(return_section_name(lab))  # put it into allocated labs list
                # call the function with the labName
                print("Of Lab code : ",lab," having lab name :",return_Lab_name(lab))
                result = return_instructor_name(return_Lab_name(lab))

                # check if the result is None
                if result is None:
                  print("No instructors found for the lab:", return_Lab_name(lab))
                else:
                   instructors, grades, cgpa = result                # print the sorted instructors and grades
                for instructor, grade, cgpa_value in zip(instructors, grades, cgpa):
                    print("Instructor:", instructor)
                    print("Grade:", grade)
                    print("CGPA:", cgpa_value)
                    print()
        # find the instructor for the lab from the instructor list, having hisghest grade.
    else:
        print("No labs found.")
