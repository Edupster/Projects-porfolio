#Request to the user to enter an int positive number to calculate the times tables
num=int(input("Please a positive integer number to calculate it's times tables: "))

#Declare a for loop from 1 to 12 to calculate the times tables for the number entered above
for i in range (1,13):

    #Calculate the result of multiplying the loop iteration by the number entered 
    result=i*num

    #print out the result
    print(f'{num}x{i}={result}') 