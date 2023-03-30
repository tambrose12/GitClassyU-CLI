from sqlalchemy import (PrimaryKeyConstraint, Column,
                        String, Integer, ForeignKey)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import random

Base = declarative_base()

engine = create_engine('sqlite:///models.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


class Course(Base):
    __tablename__ = "courses"
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    name = Column(String())
    level = Column(Integer(), default=1000)
    credits = Column(Integer(), default=4)

    def __repr__(self):
        return f"Id: {self.id}, " \
            + f"Name: {self.name}, " \
            + f"Level: {self.level}, " \
            + f"Credits: {self.credits} "


class Student(Base):
    __tablename__ = 'students'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    name = Column(String())
    course_id = Column(Integer(), ForeignKey('courses.id'))

    def __repr__(self):
        return f"Id: {self.id}, " \
            + f"Name: {self.name}, " \
            + f"Course: {self.course_id} "


class Gradebook(Base):
    __tablename__ = 'gradebooks'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    student_name = Column(String())
    grade = Column(Integer(), default=random.randint(0, 4))
    course_name = Column(String())
    course_id = Column(Integer(), ForeignKey('courses.id'))
    student_id = Column(Integer(), ForeignKey('students.id'))

    def __repr__(self):
        # for c, s in session.query(Course, Student).filter(Course.id == Student.course_id).all():
        #     return ("ID: {} Name: {} Course Name: {} Grade: {}".format(
        #         s.id, s.name, c.name, grade=random.randint(0, 4)))

        return f"Id: {self.id}, " \
            + f"Student Name: {self.student_name}, " \
            + f"Grade: {self.grade}, " \
            + f"Course Name: {self.course_name} ," \
            + f"Course ID: {self.course_id} ," \
            + f"Student ID: {self.student_id}"
