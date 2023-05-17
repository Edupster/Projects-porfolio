# Request to the user to input an integer number
num=int(input('Enter an integer number: '))

#Compare the number entered for the user and compare if the number is greater to 10 
if num>10:
    
#If the number entered is greater to 10 then start a 
# "For loop" for i from 0 to the numb entered and print as many times as the value of num is
    for i in range (num):
        print(num)

#Else, if the number is less or equal to 10 print out "Sorry, too small"     
else:
    print('Sorry, too small')