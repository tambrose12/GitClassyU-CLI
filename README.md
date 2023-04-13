# Phase-3-Project

A Course has many Students.
A Student can have many Courses.
A Gradebook belongs to one Student and one Class.

![Screenshot 2023-04-13 at 3 36 51 PM](https://user-images.githubusercontent.com/112665601/231866847-b12142f6-d381-45b1-b9a1-c083f81f2f4f.png)
![Screenshot 2023-04-13 at 3 37 09 PM](https://user-images.githubusercontent.com/112665601/231866858-3bdced71-e52c-41ee-8577-2f784b6949a6.png)
![Screenshot 2023-04-13 at 3 38 38 PM](https://user-images.githubusercontent.com/112665601/231866891-54d73ab1-4ee3-4e77-85ff-1c53ad6f668e.png)
![Screenshot 2023-04-13 at 3 39 29 PM](https://user-images.githubusercontent.com/112665601/231866905-83f722e1-be37-4b32-8843-6fd54ae37616.png)
![Screenshot 2023-04-13 at 3 40 26 PM](https://user-images.githubusercontent.com/112665601/231866923-dc98408c-cfcc-4429-a270-b96762617d56.png)
![Screenshot 2023-04-13 at 3 40 51 PM](https://user-images.githubusercontent.com/112665601/231866939-c813cac2-fbbf-470f-8c11-fd5ad89bfd96.png)
![Screenshot 2023-04-13 at 3 41 16 PM](https://user-images.githubusercontent.com/112665601/231866957-075c1c3f-7f99-4405-b248-f67ec6bed175.png)


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

 
