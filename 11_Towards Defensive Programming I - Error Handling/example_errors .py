# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages, and find and fix the errors.
 
name = "Tim"

#Identation error (Delete spaces at the begining of the variable) and add a space atthe end of the word
surname = " Jones " 

#Cast the variable age to a string type 
age = "21"
 
#The string "is" has to be entered beween quotation marks and add a space at the end
full_message = name + surname +  "is "  + age + " years old"
 
print (full_message)