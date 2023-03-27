from faker import Faker
from db import *
from db.models import Course
import random

def seed():
    print( "✨ creating courses ✨\n" )
    fake = Faker()
    course_names = set()
    while len( course_names ) < 20:
        course_name = fake.course_name()
        if course_name not in course_names:
            course_names.add( course_name )
    for course_name in course_names:
        course = Course(course_name)
        
    