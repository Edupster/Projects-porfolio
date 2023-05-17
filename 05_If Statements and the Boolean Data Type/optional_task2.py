#Request the user to answer Y/N to the questions related to the hotter_than20, day of the week and sunny day, store the answers in separate variables 
hotter_than20=input("Is today's average hotter_than20 above 20°? (Yes/No)\n")
weekend=input("Is today a weekend day? (Yes/No)\n")
sunny=input("Is it sunny today? (Yes/No)\n")
#Compare the Yes/No answers to transform the string variables into boolean variables
if hotter_than20.upper() == "YES":
    hotter_than20=True
if type(hotter_than20) != bool and hotter_than20.upper()=='NO':
    hotter_than20=False

if weekend.upper() == 'YES':
    weekend=True
if type(weekend) != bool and weekend.upper()=='NO':
    weekend=False

if sunny.upper() == 'YES':
    sunny=True
if type(sunny) != bool and sunny.upper()=='NO':
    sunny=False
#Use the boolean variables to determinate what the user should wear and print out the result
if hotter_than20==True:
    print('Today you should wear: short-sleeved shirt, ',end='')
if hotter_than20==False:
    print('Today you should wear: long-sleeved shirt, ',end='')
if weekend==True:
    print('shorts ',end='')
if weekend==False:
    print('jeans ',end='')
if sunny==True:
    print('and a cap')
if sunny==False:
    print('and a raincoat')
