#Request to the user to enter a year to start with 
start = int( input( "What year do you want to start with? "))

#Request to the user to enter how many years the script will verify if it's a leap year or not
end = int( input( "How many years do you want to check? "))

#Start a "for loop" where i will take the values in the range entered for the user (start and end)
for i in range(start, start+end):

#If the result of "i" divided by 4 is equal to 0, and "i" divided 100 is unequal to 0 then print the value of "i"
    if i%4==0 and i%100!=0:
        print(f"{i} is a leap year")

#Else If the result of "i" divided by 4 and 100 is equal to 0 then do the next verification
    elif i%4==0 and i%100==0:

#If "i" divided by 400 is equal to 0, then print the value of "i". Else print the value of "i" as a not leap year
        if i%400==0:
            print(f"{i} is a leap year")
    else:
        print(f"{i} isn't a leap year")
