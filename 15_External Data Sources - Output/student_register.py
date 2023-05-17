"""● We will write a program called student_register.py that allows students
to register for an exam venue.
● First, ask the user how many students are registering.
● Create a for loop that runs for that amount of students
● Each time the loop runs it needs to ask the next student to enter their ID
number.
● Write each of the ID numbers to a Text File called reg_form.txt
● Include a dotted line to sign because this document will be used as an
attendance register which the students will sign when they arrive at the
exam venue.
"""

#Request to the user to enter the number of students that will be registered for the exam
students_numb = int( input( "Enter the number of students that you are registering: "))

#Open and save as an object "f" the file in the same directory with name "reg_form.txt" and enable reading and writing with the command "r+""
f = open("reg_form.txt","w+")

#Start a for loop in the range from 0 to the number of students entered
for i in range(0,students_numb):
  
  #Each time the loop is triggered, request to the next student to enter their student ID and save it in the "ID" variable
  ID = input("Enter your student ID: ")
  
  #Write down the ID entered by the user in the "reg_form.txt" file with the write function with the format needed to be displayed later
  f.write("Student ID:"+ID+" Signature____________________"+"\n") 

#Close the .txt with the close function
f.close()

