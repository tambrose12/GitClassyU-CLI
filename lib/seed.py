from faker import Faker
from db import *
from db.models import Course, Student
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import (Base, Course, Student)

# def seed():
    # print( "✨ creating students ✨\n" )
    # fake = Faker()
    # names = set()
    # while len( names ) < 20:
    #     name = fake.name()
    #     if name not in names:
    #         names.add( name )
    # for name in names:
    #     return Student(name)
        
if __name__ == '__main__':
    engine = create_engine('sqlite:///models.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session() 
    student = Student(name="vanessa")

    session.add(student)
    session.commit()

    bio = Course(name="Biology", level=1000, credits=4)
    his = Course(name="History", level=1000, credits=3)

    session.add_all([bio,his])
    session.commit()