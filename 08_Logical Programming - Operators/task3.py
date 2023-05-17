# Request to the user to enter the time their took to complete each event from the triathlon and save the information in a variable
total_time=float(input('Enter your Swimming time in minutes:\n'))
total_time+=float(input('Enter your Cycling time in minutes:\n'))
total_time+=float(input('Enter your Running time in minutes\n'))
#Round the total time variable to 2 decimals
total_time=round(total_time,2)

#Print out the total time
print(f"Yor total time for all the Triathlon's event is: {total_time}")

#Determinate based on the result of the total time if the user won an Award in the competition
if total_time<=100:
    print('You won the Provincial Colors')

elif total_time>100 and total_time<=105:
    print('You won the Provincial Half Colors')

elif total_time>105 and total_time<=110:
    print('You won the Provincial Scroll')

elif total_time>110:
    print("You don't qualify for an award")