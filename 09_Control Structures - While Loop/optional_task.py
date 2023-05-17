#Request to the user to enter a number between 1 and 100
num = int( input( 'Enter an integer positive number between 1 and 100: ' ) )

#Start a while loop that will keep triggering if the condition is true
while True:
    
    #If the number entered is not between 1 and 100, request to the user to enter a different number
    if num > 100 or num < 1:
        
        num = int( input( 'The number entered is not valid, try again: ' ) )
    
    #If the number entered is between 1 and 100 break the while loop
    else:
        
        break

#Compare if the number entered is even or odd
if num%2 == 0:
    
    #If the number is even multiply it by 2
    num = num*2

else:

    #Otherwise multiply it by 3 
    num = num*3

#Print out the result
print( num )
