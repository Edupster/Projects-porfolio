#Request to the user to enter 3 items
product1=input('Please enter your first shopping item:\n') 
product2=input('Please enter your second shopping item:\n')
product3=input('Please enter your third shopping item:\n')
print('\n')
#Request to the user the prices for each item and cast the information entered to be stored as integer values in new variables
product_price1=int(input('Please enter the price of the first shopping item:\n'))
product_price2=int(input('Please enter the price of the second shopping item:\n'))
product_price3=int(input('Please enter the price of the third shopping item:\n'))
print('\n')
#Calculate the total price of the 3 items
total=product_price1+product_price2+product_price3
#Calculate the average price of the 3 items, rounding the result to 2 decimals and store the result in a new variable 
avrg=round(total/3,2)
#Print the final statement including the values stored in the variables
print(f'The Total of {product1},{product2},{product3} together is {total} and the average price of the items is {avrg}.')

