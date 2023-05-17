"""Declare two variables, the first one is an accumulator (it will contain the addition of all the user entries) and 
the second one is a counter (it will count the number of repetitions the loop has been triggered)"""
num = 0
elements = 0

#Start a while loop that will remain asking for new entries unless the user enters -1 to break it
while True:
    
    num2 = int( input( "Enter an integer positive number, enter -1 to stop entering more numbers: " ) )

    #if the number entered is different to -1, the number entered will be summed to the accumulator and the counter will increase one value
    if num2 != -1:

        num = num+num2
        elements += 1

    #if the number entered is equal to -1 the while loop will break
    else:

        break

#Calculate the average 
average = num/elements

#Print out the average in the console
print( f'The average of the numbers entered is {average}' )