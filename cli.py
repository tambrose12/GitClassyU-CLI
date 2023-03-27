from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from lib.db.models import (Base, Course, Student)



class CLI:
    def __init__(self, user_input):
        self.courses = [course for course in session.query(Course)]
        self.students = [student for student in session.query(Student)]
        self.name = user_input
        self.start()

    def start(self):
        print(' ')
        print(f'🔥🔥🔥 Welcome To Git Classy University {self.name} 🔥🔥🔥')
        print(' ')

        exit = False
        while exit == False:
            choice = input(
                f'Type "courses" to see a list of All Courses. Type "add" to add a course. Type "students" to see a list of all students at the university.: ')
            print(' ')
            if choice.lower() == "courses":
                show_courses(self)
            elif choice.lower() == "students":
                show_students(self)
            elif choice.lower() == "add":
                add_course(self)

            print(' ')
            user_input = input(
                '🔥Enter "c" to continue, or Enter "x" to exit application: ')
            print(' ')
            if user_input == "X" or user_input == 'x':
                exit = True

        printer(self.name)




def printer(user_input):
    print(' ')
    print(f'Thanks for checking out the classes we offer, {user_input}!')


def show_courses(self):
    print_courses(self.courses)


def print_courses(courses):

    print(' ')
    print('***Available Courses***')
    print('')
    for index, course in enumerate(courses):
        print(f'{index + 1}. {course.name}')

    print(' ')


def show_students(self):
    print_students(self.students)




def print_students(students):
    print(' ')
    print('***Our Current Students***')
    print('')
    for index, student in enumerate(students):
        print(f'{index + 1}. {student.name}')
    print(' ')


def add_course(self):
    name = input("Enter the New Course Name: ")
    level = input("Enter the Course Level: ")
    c_credits = input(
        "Enter the Number of Credits a Student gets for the course: ")
    course = Course(name=name, level=level, credits=c_credits)

    session.add(course)
    session.commit()

    self.courses.append(course)  





if __name__ == '__main__':
    engine = create_engine('sqlite:///models.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    user_input = input("Enter Your Name: ")
    CLI(user_input)



# meowmeow = "lol check it out we are wizards now"

# while meowmeow != 'x':
#     meowmeow = input('🔥')
#     if meowmeow == 'l':
#         print('we love python 🐍')
#     elif meowmeow != 'x':
#         print(f"{meowmeow} is not the exit")
