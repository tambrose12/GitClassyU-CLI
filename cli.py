from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from lib.models import (Base, Course, Student, Gradebook)
import random
from rich.console import Console
from rich.table import Table


class CLI:
    def __init__(self, user_input):
        self.courses = [course for course in session.query(Course)]
        self.students = [student for student in session.query(Student)]
        self.grades = [grade for grade in session.query(Gradebook)]
        self.name = user_input
        self.start()

    def start(self):
        print(' ')
        print(f'🔥🔥🔥 Welcome To Git Classy University, {self.name} 🔥🔥🔥')
        print(' ')

        show_choices = False

        exit = False
        while exit == False:
            choice = input(
                f'✨Enter "C" to see a list of All Courses. Enter "E" to enroll as a student. Enter "S" to see a list of all students at the university. Enter "G" to see the gradebook. ✨ ')
            print(' ')
            if choice.lower() == "c":
                show_courses(self)
                show_choices = True
                new_choice = input(
                    "Enter course number to see students taking that course, or enter 'x' to continue without viewing students in a course: ")
                while show_choices == True:
                    if new_choice == "x" or new_choice == "X":
                        show_choices = False

                    elif new_choice == "1" or new_choice == "2" or new_choice == "3" or new_choice == "4" or new_choice == "5" or new_choice == "6" or new_choice == "7" or new_choice == "8" or new_choice == "9" or new_choice == "10" or new_choice == "11" or new_choice == "12" or new_choice == "13" or new_choice == "14" or new_choice == "15":
                        show_choices = False

                        selected_course_id = int(new_choice)
                        selected_students = session.query(
                            Student).filter_by(course_id=selected_course_id).all()
                        for index, student in enumerate(selected_students):
                            print(f'{index + 1}. {student.name}')

                        break
                    else:
                        show_choices = False
                        choice = input(
                            f'Type any key to get the continue or exit menu selection. ')
                        print(' ')

            elif choice.lower() == "s":
                show_students(self)
                show_choices = True
                new_choice = input(
                    "Enter student number to see course the student is enrolled in, or enter 'x' to continue: ")
                student_range = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34',
                                 '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70']

                while show_choices == True:
                    if new_choice == "x" or new_choice == "X":
                        show_choices = False

                    elif new_choice in student_range:
                        show_choices = False

                        selected_student_id = int(new_choice)
                        for s in self.students:
                            if s.id == selected_student_id:
                                students_course_id = s.course_id
                                courses_in = [
                                    c.name for c in self.courses if c.id == students_course_id]
                                print(f"{s.name} is enrolled in: {courses_in}")

                        break

            elif choice.lower() == "e":
                print(
                    "🔥 We are excited to have you! If you are ready to enroll, enter your full name below! 🔥")
                print(" ")
                add_student(self)

            elif choice.lower() == "g":
                print("All Students Grades Listed Below:")
                print(' ')
                show_grades(self)

            elif choice.lower() == "secret":
                print("🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥")
                print("🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🐍 We Love Python! 🐍🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥")
                print("🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥")
                print(" ")
                print(
                    "  🦨🦨 You have now completed the BloodOath to join the Lil' Stinkers Cult 🦨🦨 ")
                print(
                    "🧑‍🎤🐱🐱🧙‍♂️🕺🌮🍷 Our Benevolent Dictator For ✨LIFE✨ is Adam La Rosa 🧑‍🎤🐱🐱🧙‍♂️🕺🌮🍷")
                print("🔥🔥🔥🔥 🙇‍♂️🙇‍♂️🙇‍♂️🙇‍♂️🙇‍♂️🙇‍♂️🙇‍♀️🙇‍♀️🙇‍♀️🙇‍♀️🙇‍♀️🙇‍♀️🙇‍♂️🙇‍♂️🙇‍♂️🙇‍♀️🙇‍♂️🙇‍♂️🙇‍♂️🙇‍♀️🙇‍♀️🙇‍♀️🙇‍♀️🙇‍♀️🙇‍♀️🙇‍♂️🙇‍♂️🙇‍♂️🙇‍♂️🙇‍♂️🙇‍♂️ 🔥🔥🔥🔥")
                print("")

            print(' ')
            user_input = input(
                '🔥 Enter "C" to continue, or Enter "X" to exit application: ')
            print(' ')
            if user_input == "X" or user_input == 'x':
                exit = True

        printer(self.name)


def printer(user_input):
    print(' ')
    print(f'Thanks for checking out the classes we offer, {user_input}!')
    print(' ')


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


def add_student(self):
    name = input("Enter Your Full Name Here: ")
    student = Student(name=name, course_id=random.randint(1, 15))

    session.add(student)
    session.commit()

    self.students.append(student)
    print(f"🔥🔥🔥 Thank you for enrolling at GCU! 🔥🔥🔥")


def show_grades(self):
    print_grades(self.grades)


def print_grades(grades):

    table = Table(title="Gradebook")
    table.add_column("Student ID", style="magenta")
    table.add_column("Student", style="cyan", no_wrap=True)
    table.add_column("Grade", style="green")
    table.add_column("Course Name", justify="right", style="cyan")
    table.add_column("Course ID", style="cyan", no_wrap=True)

    print(' ')
    print('***Gradebook***')
    print('')
    for i, g in enumerate(grades):
        table.add_row(
            f"{i+1}", f"{g.student_name}",  f"{g.grade}",  f"{g.course_name}",  f"{g.course_id}")
    console = Console()
    console.print(table)
    print(' ')


if __name__ == '__main__':
    engine = create_engine('sqlite:///lib/models.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    user_input = input("Enter Your Name: ")
    CLI(user_input)
