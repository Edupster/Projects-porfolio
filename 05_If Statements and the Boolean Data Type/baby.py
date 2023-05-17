#Request the user to enter the year they were born
year_of_birth=int(input('Please enter your year of birth:\n'))
#Determnate if the user is over or under 18 years old, if the user is older than 18 print out that is old enough to enter
if year_of_birth < 2004:
    print('Congratulations you are old enough!')
else:
    print('Unfortunatelly you are not old enough to enter')

