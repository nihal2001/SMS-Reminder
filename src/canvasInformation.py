'''
Gets information from API and stores it
'''

# Import the Canvas class
from canvasapi import Canvas

# Canvas API URL
API_URL = "https://canvas.vt.edu"
# Canvas API key
API_KEY = "4511~vZrrov6HR0ZVZNKkf4IdEOz0U8h5BHuMiPxcOko0z4yIAF7dF67mLMUXfmX4ZSgE"

headers = {'Authorization': 'Bearer %s' % API_KEY}

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

myCourses = canvas.get("https://canvas.vt.edu/api/v1/courses", headers=headers, params={'enrollment_state':'active', 'include':['term']}).json()
print(myCourses)