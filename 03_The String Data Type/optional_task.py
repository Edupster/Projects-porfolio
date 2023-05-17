#Request to the user to enter their favorite restaurant and store in a variable as a string
fav_rest=input('Enter the name of your favourite restaurant:\n')
#Request to the user to enter their favorite number and store in a variable as an integer 
int_fav=int(input('Enter your favorite number:\n'))
print('\n')
#Print out the information entered with f' function 
print (f'Favourite restaurant: {fav_rest}')
print('\n')
print(f'Favourite number: {int_fav}')
print('\n')
#Cast the string variable with the favorite restaurant to an integer variable
fav_rest=int(fav_rest)

"""The variable fav_rest can't be cast to an integer variable since it contains a sentence and not numerical characters """