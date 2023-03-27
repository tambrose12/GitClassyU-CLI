# Phase-3-Project

A Course has many Students.
A Student can have many Courses.
A Gradebook belongs to one Student and one Class.

When you see a '#', this means the functionality will be related to the instance, a '.', the class.

Course#name
    returns a string that is the course's name

Course#level
    returns a number representing the level of the college course

Course#credits
    returns the number of credits the course is worth

Course.all
    returns a list of all Courses



Student#first_name
    returns string of student's first name

Student#last_name
    returns string of student's last name

Student#name
    returns the student's Full name



Gradebook#course
    returns the Course Instance associated with that grade

Gradebook#student
    returns the Student Instance associated with that grade

Gradebook#grade
    returns the number grade for that Student instance in that Course instance
