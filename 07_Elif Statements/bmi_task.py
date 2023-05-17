#Request the user to enter their weight in kg and their height in m and save them in separate variables
weight=float(input('Please enter your weight in kg:\n'))
height=float(input('Please enter your height in m:\n'))
#Take the user's weight and height saved in the variables to calculate the bmi
BMI=round(weight/(height*height),2) #here we round the BMI result to 2 decimals to have a shorter number displayed when printing the BMI
if BMI >= 30:
    print(f'Your BMI is {BMI}, which means that you are obese')
elif BMI >= 25:
    print(f'Your BMI is {BMI}, which it means that you are overweight')
elif BMI >= 18.5:
    print(f'Your BMI is {BMI}, which it means that you are normal')
elif BMI < 18.5:
    print(f'Your BMI is {BMI}, which it means that you are underweight')