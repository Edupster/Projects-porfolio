#Start a while loop to request the user to select one option from the menu displayed
while True:

    option = input("""Select an option:
    1 - Arithmetic result two numbers
    2 - View all the equations
    3 - Exit\n""")

    #if the user selects the option 1 execute the block to calculate an equation of two numbers
    if option == "1":

        #Use a try block in a while loop to verify if the number entered is an integer or float value, if an exception is triggered with a non-valid 
        #value then output the respective message and repeat the while loop, if a valid number is entered then break the loop and execute the next block
        while True:
            try:

                num1 = int(input("Enter your first number: "))
                num2 = int(input("Enter your second number: "))
                break

            except:
                print("Invalid information, please try again entering integer/float values")
        
        #Start a while loop to ask the user to enter an arithmetic symbol to calculate the result, if the user doesn't enter
        #a valid result then print the respective message and repeat the loop. Otherwise calculate the result of the two numbers entered depending 
        # the entered symbol, save it in a variable and break the loop
        while True:
            oper=input("Enter the operator symbol to calculate the result: ( + , - , x, / ): ")
            if oper == '+':
                result = num1+num2
                break

    
            elif oper == '-':
                result = num1-num2
                break
        
            elif oper == 'x':
                result = num1*num2
                break
    
            elif oper == '/':
                if num2==0:
                    print("Division by 0 is not allowed, try again!")
                
                    while True:

                        try:
                            num1=int(input("Enter your first number: "))
                            num2=int(input("Enter your second number: "))
                            break

                        except:
                            print("Invalid input value, please try again entering integer/float values")

                else:
                    result = round(num1/num2,2)
                    break
    
            else:
                print("You haven't entered a valid operator symbol, try again!")
        
        #Create a try block to open and write the equations entered in the system in a .txt file, if an exception 
        #is triggered due to a non-existent file then use se except block to create a .txt file to save the result
        try:
            f=open("results.txt","a")
            f.write (f'{num1} {oper} {num2} = {result}\n')
        except:
            f=open("results.txt","w+")
            f.write (f'{num1} {oper} {num2} = {result}\n')

        #Print out the result
        print(f'The result of the operation {num1} {oper} {num2} is: {result}')

    #if the user enters the option View all the equations then start a while loop that will ask to the user to enter
    #the file name with the equations, if the user doesn’t enter a valid file name (except) then display the respective message and 
    #ask to enter the filename again. If the filename is on the system, then print out the information in the file
    if option == "2":
        while True:
            try:
                filename=input("Enter the filename: ")
                f=open(filename+".txt", "r")
                print (f'Showing the equations contained in {filename}.txt are:\n')
                for line in f:
                    print(line)
                f.close
                break

            except:
                print("The filename entered doesn't exist!, try again with a different filename")
    
    #If the user enters the option 3 then break the main loop and finish the program
    if option == "3":
        break
        