from faker import Faker
from db import *
from db.models import Course, Student
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import (Base, Course, Student)

        
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
trig = Course(name="Trigonometry", level=3000, credits=3)
chem = Course(name="Chemistry", level=1000, credits=3)
bus = Course(name="Business", level=1000, credits=2)
crim = Course(name="Criminal Justice", level=2000, credits=4)
cul = Course(name="Culinary", level=2000, credits=2)
law = Course(name="Law", level=4000, credits=4)
psych = Course(name="Psychology", level=2000, credits=3)
code = Course(name="Programming", level=3000, credits=4)
art = Course(name="Art", level=1000, credits=2)
phil = Course(name="Philosophy", level=3000, credits=3)
alg = Course(name="Algebra", level=1000, credits=3)
med = Course(name="Medicine", level=4000, credits=4)

session.add_all([trig, chem, bus, crim, cul, law, psych, code, art, phil, alg, med])
session.commit()