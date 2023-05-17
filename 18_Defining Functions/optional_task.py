#Define a function to add two numbers. The function gets two integer values as input
def add_num(a,b):

    #Calculate the result of the addition of the two numbers entered in the input of the function
    result=a+b

    #Return the result of the addition
    return(result)

#Define a function to perform a subtraction of two numbers. The function gets two integer values as input
def subtract_num(a,b):
    
    #Calculate the result of the subtraction of the two numbers entered in the input of the function
    result=a-b

    #Return the result of the operation
    return(result)

#Define a new function to multiply two numbers. The function gets two integer values as input
def multiply_num(a,b):

    #Calculate the result of the multiplication of the two numbers entered in the argument of the function
    result=a*b

    #Return the result of the operation
    return(result)

#Define a variable to divide two numbers. The function gets two integer values as input
def divide_num(a,b):

    #Calculate the result of the division of the two values entered in the argument of the function
    result=a/b

    #Return the result of the operation
    return(result)

#Request to enter an option from the menu provided and save it in a variable
option=input("""Enter the number of the operation that you want to perform:\n
Option 1 - add
Option 2 - subtract
Option 3 - multiply
Option 4 - divide\n
:""")

print("\n")

#Compare the value entered by the user to select what option of the menu to perform

if option=="1":
    
    #If the option selected is add, then perform the operation requesting to the user to enter the two values
    #to input them in the function declared and calculate the result. Print out the result in the format desired
    print("a+b")
    a=int(input("Enter the value for a: "))
    b=int(input("Enter the value for b: "))
    print(f"{a} + {b} = {add_num(a,b)}")

if option=="2":

    #If the option selected is subtract, then perform the operation requesting to the user to enter the two values
    #to input them in the function declared and calculate the result. Print out the result in the format desired
    print("a-b")
    a=int(input("Enter the value for a: "))
    b=int(input("Enter the value for b: "))
    print(f"{a} - {b} = {subtract_num(a,b)}")

if option=="3":

    #If the option selected is multiply, then perform the operation requesting to the user to enter the two values
    #to input them in the function declared and calculate the result. Print out the result in the format desired
    print("a*b")
    a=int(input("Enter the value for a: "))
    b=int(input("Enter the value for b: "))
    print(f"{a} * {b} = {multiply_num(a,b)}")

if option=="4":

    #If the option selected is subtract, then perform the operation requesting to the user to enter the two values 
    #to input them in the function declared and calculate the result. Print out the result in the format desired
    print("a/b")
    a=int(input("Enter the value for a: "))
    b=int(input("Enter the value for b: "))
    print(f"{a} / {b} = {divide_num(a,b)}")

