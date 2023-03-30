# Phase-3-Project

A Course has many Students.
A Student can have many Courses.
A Gradebook belongs to one Student and one Class.

Command Line Opens with a greeting to enter your Name.

With Name input Welcome message appears with options of main menu:

1. "C" to see a list of All Courses:
    -Once inside the course list - user has option of entering course number to see a list of students enrolled in selected course.
    -"C" will take the user back to main menu, "X" will exit the application

2. "E" to enroll as a student:
    -User will recieve a prompt to enter full name and application will enroll user in a course.
    -"C" will take the user back to main menu, "X" will exit the application

3. "S" to see a list of all students at the university:
    -Once in student list the user has the option of entering a student number to see what course that student is enrolled in. 
    -"C" will take the user back to main menu, "X" will exit the application

4. "G" to see the gradebook:
    -User will see a list of all students and their grade and their corresponding course information.

5. User my enter "secret" for a surprise 😉


Our code sorts through all the options with a combination of if, elif & while loops. Each different selection calls a corresponding function that sorts through our database to print out the information. Our Cli code is defined as a class that on the __init__ uses a session.query() to create the attribute self.course, self.students, self.grades to access the inforamtion needed for the functionality. 

 