"""Follow these steps:
● Create a new Python file in this folder called loop1000.py.
● You are asked to print out all the numbers from 1 to 1000. Write 2 lines of
code in your file to print out all numbers from 1 to 1000.
● Once you've got this to work, add logic inside your loop to only print out
the numbers from 1 to 1000 that are even (i.e. divisible by 2). Remember
the modulo command — i.e., %. 10%5 will give you the remainder of 10
divided by 5. 10 divided by 5 equals 2 with a remainder of 0. Hence, this
statement returns 0. Any even number is a number that can be divided by
2 with no remainder."""

# Start a for loop to print all the numbers from 1 to 1000
for i in range(1,1001):

    #The following line has been commented to print only the even numbers
    #print(i)

    #If the "i" iteration from the for loop divided by two is equal to 0 then print the value "i" of the iteration ()
    if i%2==0:
        print(i)
