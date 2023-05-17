"""
Compulsory Task 1: 
------------------

Copy the code provided below to a new file named compulsory_task_1.py: 
1. Add another method in the Course class that prints the head office location: Cape Town
2. Create a subclass of the Course class named OOPCourse
3. Create a constructor that initialises the following attributes and assigns these values:
    --- "description" with a value "OOP Fundamentals"
    --- "trainer" with a value "Mr Anon A. Mouse"
4. Create a method in the subclass named "trainer_details" that prints what the 
   course is about and the name of the trainer by using the description and trainer attributes.
5. Create a method in the subclass named "show_course_id" that prints the ID number of the course: #12345
6. Create an object of the subclass called course_1 and call the following methods
   contact_details
   trainer_details
   show_course_id
   These methods should all print out the correct information to the terminal

Note: this task covers single inheritance. Multiple inheritance is also possible in Python and 
we encourage you to do some research on multiple inheritance when you have finished this course.
"""
class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"
    head_location = "Cape Town"


    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)
    
    def head_office_location(self):
        print("The head office location is: ", self.head_location)    


class OOPCourse (Course):
    description = "OOP Fundamentals"
    trainer = "Mr Anon A. Mouse"
    course_id_number = "#12345"

    def trainer_details(self):
        print(f"Course name: {self.description}, Course trainer: {self.trainer}")
        
    def show_course_id(self):
        print(f"Course ID is: {self.course_id_number}")

OOPCourse_1=OOPCourse()
OOPCourse_1.contact_details()
OOPCourse_1.trainer_details()
OOPCourse_1.show_course_id()