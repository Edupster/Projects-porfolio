#Decalre 3 variables and assign them number values
num1=66
num2=1
num3=34

#Determinate between num1 and num2 which one is the greatest and print it out
if num1<num2:
    print(f'The greatest num between {num1} and {num2} is {num2}')
else:
    print(f'The greatest num between {num1} and {num2} is {num1}')

#Determinate if num1 is even or odd and print it out
if num1%2==0:
    print(f'{num1} is even')
else:
    print(f'{num1} is odd')

#Determinate with logical operations the order from lowest to greatest for num1, num2 and num3 and print out the result
if num1<num2 and num2<num3:
    print(f'The number entered in order from lowest to greatest is:\n{num1} {num2} {num3}')

elif num1<num3 and num3<num2:
    print(f'The number entered in order from lowest to greatest is:\n{num1} {num3} {num2}')

if num2<num3 and num3<num1:
    print(f'The number entered in order from lowest to greatest is:\n{num2} {num3} {num1}')

elif num2<num1 and num1<num3:
    print(f'The number entered in order from lowest to greatest is:\n{num2} {num1} {num3}')

if num3<num1 and num1<num2:
    print(f'The number entered in order from lowest to greatest is:\n{num3} {num1} {num2}')

elif num3<num2 and num2<num1:
    print(f'The number entered in order from lowest to greatest is:\n{num3} {num2} {num1}')
