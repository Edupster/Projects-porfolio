#Request the user to enter an integer number
number=int(input('Please enter an integer number:\n'))
print('\n')
#compare if the number entered is odd or even based the remainder after dividing it by 2  and print out if the number is even or odd
if number %2 == 0:
    print('The number entered is even')

else:
    print('The number entered is odd')