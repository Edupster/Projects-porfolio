#Request the user to enter their edge and save it in a variable
age=int(input('Please enter your age:\n'))

#Determinate if the user is over 18, between 16 and 18 or older 16, a print a statement based on the result
if age>=18:
    print('You are old enough!')
elif age>16 and age<18:
    print("Almost there")
elif age<16:
        print("You're just too young!")