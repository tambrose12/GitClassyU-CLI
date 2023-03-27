from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer, ForeignKey)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = "courses"
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    name = Column(String())
    level = Column(Integer())
    credits = Column(Integer())

    def __repr__(self):
        return f"Id: {self.id}, " \
            + f"Name: {self.name}, " \
            + f"Level: {self.level}, " \
            + f"Credits: {self.credits}"

# class Student(Base):
#     __tablename__ = 'students'
#     __table_args__ = (PrimaryKeyConstraint('id'),)
    
#     id = Column(Integer())
#     first_name = Column(String())
#     last_name = Column(String())
#     course_id = Column(Integer(), ForeignKey('course.id'))