#Request to the user to enter a number and save it in a variable
num = int( input( 'Please enter an integer number:' ) )

#Declare a variable with initial value equal to 1, this variable will work as a counter
i = 1

#Start a while loop with the condition that will be repeating while the counter is less or equal to the number provided for the user
while i <= num:
    
#If the result of the counter divided by two is equal to zero then print the number
    if i%2 == 0:

        print( i )

#After each time the loop is triggered and the counter will increase one unit
    i += 1