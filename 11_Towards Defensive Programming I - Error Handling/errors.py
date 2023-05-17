# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

#Add round brackets to contain the print function's arguments
print ("Welcome to the error program")

#Add round brackets to contain the print function's arguments and delete the wrong indentation
#at the beginning of the line
print ("\n")

#Delete indentation at the beginning of the line and replace the comparation symbol "=="
#with the assignment operator "=". 
ageStr = "24 years old" #I'm 24 years old.

#Remove indentation at the beginning of the line and strip no numerical information from ageStr
age = int(ageStr.strip(" years old"))

#Remove indentation at the beginning of the line and cast age to string type. Also ad a space after "I'm" and before "years old"
print("I'm " + str(age) + " years old.")

#Remove indentation at the beginning of the line and declare variable as integer type
three = 3

#Remove indentation at the beginning of the line 
answerYears = age + three

#Add round brackets to contain the print function's arguments and cast answerYears to string type
print ("The total number of years:" + str(answerYears))

#Correct the wrong reference to anwerYears variable
answerMonths = answerYears * 12

#Add round brackets to contain the print function's arguments and cast asnwerMonths to string type
print ("In 3 years and 6 months, I'll be " + str(answerMonths) + " months old")

#HINT, 330 months is the correct answer


