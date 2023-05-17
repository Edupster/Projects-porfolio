#First we use the input function to require the initial value for our variables

num1=input('Enter the value for the first variable: \n')
num2=input('Enter the value for the second variable: \n')
print('\n')
#Here we print out the original arrange of our variables
print('num1: ', num1)
print('num2:', num2,'\n')

#Here we will declare a third variable that will help us to store the value of one of the variables that we want to swap
num3=num1
num1=num2
num2=num3

#After we swap the values we print out the variables again

print('num1: ', num1)
print('num2:', num2)



