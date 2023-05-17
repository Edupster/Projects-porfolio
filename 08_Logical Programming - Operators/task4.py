#Request the user to enter an integer and save it in a variable
num=int(input('Enter an integer number:\n'))

#Determinate if the number is divisible by 2 and 5
if num%2==0 and num%5==0:
    print(f'{num} is divisible by 2 and 5')

#Determinate if the number is divisible by 2 or 5
elif num%2==0 or num%5==0:
    print(f'{num} is divisible by 2 or 5')

#Determinate if the number is not divisible by 2 or 5
elif num%2!=0 or num%5!=0:
    print(f'{num} is not divisible by 2 or 5')
