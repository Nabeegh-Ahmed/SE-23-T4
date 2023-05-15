import pandas as pd
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps
from flask import Flask, request, send_file
from flask_pymongo import PyMongo
import numpy as np
import io
# app = Flask(_name_)
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/timetable'
# mongo = PyMongo(app)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["timetable"]
mycol = mydb["tt"]
timetable = pd.read_excel(r'C:\Users\PC\Pictures\TimeTable.xlsx')
timetable.head()


def readtimetable():
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


readtimetable()


def read_from_mongodb():

    for x in mycol.find():
        print(x)
# read_from_mongodb()


def show_clashes():
    for i in range(len(timetable)):
        for j in range(len(timetable)):
            if (i != j and i < j):
                if (timetable.iloc[i, 3] == timetable.iloc[j, 3] and timetable.iloc[i, 4] == timetable.iloc[j, 4] and timetable.iloc[i, 2] == timetable.iloc[j, 2]):
                    print("clash between", timetable.iloc[i, 0],
                          "and", timetable.iloc[j, 0], "at", timetable.iloc[i, 3], "on", timetable.iloc[i, 4])


show_clashes()

# def show_clashes():
#     courses = list(mycol.find())
#     clashes = set()  # Use a set to store unique clashes
#     for i in range(len(courses)):
#         for j in range(i + 1, len(courses)):
#             if (
#                 i != j  # Avoid comparing a course with itself
#                 and courses[i]["time"] == courses[j]["time"]
#                 and courses[i]["day"] == courses[j]["day"]
#                 and courses[i]["venue"] == courses[j]["venue"]
#             ):
#                 clash = (
#                     courses[i]["courseName"],
#                     courses[j]["courseName"],
#                     courses[i]["time"],
#                     courses[i]["day"],
#                 )
#                 clashes.add(clash)  # Add the clash to the set

#     # Print the unique clashes
#     for clash in clashes:
#         print(
#             "Clash between",
#             clash[0],
#             "and",
#             clash[1],
#             "at",
#             clash[2],
#             "on",
#             clash[3],
#         )


# show_clashes()















