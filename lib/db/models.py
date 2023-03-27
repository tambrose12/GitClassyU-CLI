from sqlalchemy import (PrimaryKeyConstraint, Column,
                        String, Integer, ForeignKey)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Course(Base):
    __tablename__ = "courses"
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    name = Column(String())
    level = Column(Integer(), default = 1000)
    credits = Column(Integer(), default = 4)

    def __repr__(self):
        return f"Id: {self.id}, " \
            + f"Name: {self.name}, " \
            + f"Level: {self.level}, " \
            + f"Credits: {self.credits} "


class Student(Base):
    __tablename__ = 'students'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    first_name = Column(String())
    last_name = Column(String())
    grade = Column(Integer())
    course_id = Column(Integer(), ForeignKey('courses.id'))

    def __repr__(self):
        return f"Id: {self.id}, " \
            + f"First Name: {self.first_name}, " \
            + f"Last Name: {self.last_name}, " \
            + f"Grade: {self.grade}, " \
            + f"Course: {self.course_id} "
