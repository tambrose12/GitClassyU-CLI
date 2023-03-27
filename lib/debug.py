import ipdb
from lib.db import *

# Course
# def __init__(self, name, level, course_credit):

bio = Course("Biology", 1000, 3)

# Student
# def __init__(self, first_name, last_name):

kim = Student("Kimberly", "Benton")


# Gradebook
# def __init__(self, course, student, grade):

g1 = Gradebook(bio, kim, 4.0)


ipdb.set_trace()
