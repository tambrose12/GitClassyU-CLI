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
# names = []
    # while len( names ) < 20:
    #     name = fake.name()
    #     if name not in names:
    #         names.add( name )
    # for name in names:
    #     student = Student(name)

        
if __name__ == '__main__':
    engine = create_engine('sqlite:///models.db')
    # Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session() 

    fake = Faker()
    names = []
    while len(names) < 20:
        n = fake.name()
        if n not in names:
            names.append(n)
    for n in names:
        student = Student(name = n)
        session.add(student)
        session.commit()



    # print(names)

    

    # bio = Course(name="Biology", level=1000, credits=4)
    # his = Course(name="History", level=1000, credits=3)

    # session.add_all([bio,his])
    # session.commit()