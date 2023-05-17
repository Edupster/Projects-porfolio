#Request to the user to enter 3 numbers casting the values entered to integer data type and store them in variables
num_1=int(input('Please enter 1st number:\n'))
num_2=int(input('Please enter 2nd number:\n'))
num_3=int(input('Please enter 3rd number:\n'))
print('\n')
#Print out the sum of the 3 numbers entered using the + addition operator
print(f'Sum of all the numbers: {num_1+num_2+num_3}')
print('\n')
#Print out the result of the first number minus the second using the - subtraction operator
print(f'First number minus the second: {num_1-num_2}')
print('\n')
#Print out the result of the third number multiplied by the first number using the * multiplication operator
print(f'The third number multiplied by the first number: {num_3*num_1}')
print('\n')
#Print out the result of the sum of all three numbers divided by the third number using the + addition and * multiplication operators
print(f'The sum of all three numbers divided by the third number: {(num_1+num_2+num_3)/num_3}')
