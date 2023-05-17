#Import the math package of functions
import math

#Request to the user to enter the calculation that they would like to perform (investment or bond)

print("Please enter the calculation you would like to perform from the options below:\n")
print("Investment  - To calculate the amount of interest you'll earn on your investment")
print("Bond        - to calculate the amount of interest you'll have to pay on a home loan\n")
#Save the user's selection on a variable
task=input('')

#Start the while loop that will ensure that the user enters a valid option, if the user enters an invalid option 
# the loop will keep triggering a message requesting for a valid option
while True:
    #If the users selected to calculate the investment, then run the block below requesting the information necessary to calculate the investment earn
    if task.upper()=='INVESTMENT':
        deposit=float(input('How much are you depositing?: '))
        interest_rate=float(input('Enter the interes rate (%): '))/100
        investment_time=int(input('How many years would you like to invest your money for?: '))
        #Request to the user if they would like to calculate a simple or compound interest and based on the answered execute the block corresponding 
        #to each interest calculation and print out the result. Also, the while loop will break at the end of each block
        interest=input("Would you like to do a 'simple' or 'compound' interest?: ")
        if interest.upper()=='SIMPLE':
            earn=round(deposit*(1+(interest_rate*investment_time)),2)
            print(f"The amount that you will earn with a simple interest rate of {interest_rate}, in {investment_time} year(s) time will be {earn}£ ")
        elif interest.upper()=='COMPOUND':
            earn=round(deposit*math.pow((1+interest_rate),investment_time),2)
            print(f"The amount that you will earn with a compound interest rate of {interest_rate}, in {investment_time} year(s) time will be {earn}£")
        break
    #Execute this block if the user's entered Bond as selected calculation to perfom
    elif task.upper()=='BOND':
        #Request to the user the informaton necesary to calculate the monthly payments and print out the result. Also, the loop will
        #be broke up at the end of this block
        present_value=float(input("What is the present value of the house: "))
        interest_rate=float(input('Enter the annual interest rate (%): '))/1200
        num_months=int(input("Enter the number of months over which the bond will be paid: "))
        monthly_pay=round((interest_rate*present_value)/(1-pow((1+interest_rate),-num_months)),2)
        print(f"Your Monthly repayments will be {monthly_pay}£")
        break
    #In case the user didn't enter a valid option this block will be executed indefinitetly in the loop until a valid option is entered

    else:
        print("You haven't entered a valid option")
        print("Please enter the calculation you would like to perform from the options below:\n")
        print("Investment  - To calculate the amount of interest you'll earn on your investment")
        print("Bond        - to calculate the amount of interest you'll have to pay on a home loan\n")
        task=input('')

