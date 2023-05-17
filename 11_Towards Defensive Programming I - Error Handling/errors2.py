# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

#Add quotation marks to define the strings contained in the variable
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16

#The variable with the whole sentence cannot be defined adding variables among curly brackets, is necessary instead 
#to use the operator addition and add quotation marks. Also, cast number_of_teeth to an integer variable and swap it with animal type
full_spec = "This is a " +animal+"."+" It is a "+ animal_type + " and it has "+str(number_of_teeth)+ " teeth"

#Add round brackets to define the print's function arguments
print (full_spec)
