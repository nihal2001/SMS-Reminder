'''
Gets information from API and stores it
'''

import json
import requests
from canvasapi import Canvas

# Canvas API URL
API_URL = "https://canvas.vt.edu"
# Canvas API key
API_KEY = "4511~vZrrov6HR0ZVZNKkf4IdEOz0U8h5BHuMiPxcOko0z4yIAF7dF67mLMUXfmX4ZSgE"

headers = {'Authorization': 'Bearer %s' % API_KEY}

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

#Gets classes currently enrolled in
def getClasses():
    my_Courses = requests.get("https://canvas.vt.edu/api/v1/courses", 
        headers = headers, params = {'enrollment_state':'active', 'include':['term']}).json() 
    current_Courses = []
    ##out_file = open("courses.json", "w")

    current_Courses = []
    for course in my_Courses:
        if (course['term']['name'] == "2022 Spring"):
            current_Courses.append(course['name'])
    ##json.dump(my_Courses, out_file, indent=6)
    ##out_file.close()ß
    return current_Courses

#Gets assignmetns due soon
def getAssignments(classID):
    my_Assignments = requests.get("https://canvas.vt.edu/api/v1/courses/" + classID +"/assignments", 
        headers = headers, params = {'enrollment_state':'active', 'include':['term']}).json()
    out_file = open("classes.json", "w")
    json.dump(my_Assignments, out_file, indent=6)
    out_file.close()
    return my_Assignments

def getCalender():
    events = requests.get("https://canvas.vt.edu//api/v1/calendar_events", 
        headers = headers).json()
    print(events)
    
getCalender()
