#Request to the user to enter the name, age, eye colour and hair colour. Save this values in variables
name = input("Enter the person's name: ")
age = int(input("Enter the person's age: "))
eye_colour = input("Enter the person's eye colour: ")
hair_colour = input("Enter the person's hair colour: ")

#Declare the class Adult an initialize the instance properties
class Adult:
    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour
    
    #Define a method to print out that the person is old enough to drive
    def can_drive(self):
        print(f"{self.name} is old enough to drive")

#Define a sub class from the Adult that herderite the parent class properties
class Child(Adult):
    def __init__(self, name, age, eye_colour, hair_colour):
        super().__init__(name, age, eye_colour, hair_colour)
    
    #Override the  can_drive method from the parent class to print that the person is not old enough to drive
    def can_drive(self):
        print(f"{self.name} is not old enough to drive")
    
#if the person's age is greater or equal to 18 then create an object from the Adult class with the attributes entered 
# and call the method can_drive()
if age >= 18:
    new_person=Adult(name,age,eye_colour,hair_colour)
    new_person.can_drive()

#if the person's age is not greater or equal to 18 then create an object from the Child class with the attributes entered 
# and call the method can_drive()
else:
    new_person=Child(name,age,eye_colour,hair_colour)
    new_person.can_drive()

