#Create a list with the name of the items in the menu
menu=["Ham Sandwich" , "Yogurt" , "Orange Juice" , "Crispies"]

#Crete a dictionary with the stock for each item using the names on the menu list as keys for each item in the dictionary
stock={"Ham Sandwich":5 , "Yogurt":3 , "Orange Juice":2 , "Crispies":2}

#Crete a dictionary with the price for each item using the names on the menu list as keys for each item in the dictionary
price={"Ham Sandwich":2 , "Yogurt":3 , "Orange Juice":4 , "Crispies":3}

#Declare a variable with initial value zero to save the total of the stock worth
stock_worth = 0

#Start a for loop to access to each value in the list with the items on the menu
for i in menu:

    #Calculate the stock worth for every element on the dictionaries "stock" and "price" accessing to their values with the key 
    #values saved in the list "menu". Save the result and accumulate the result for each item in the variable "stock_worth"
    stock_worth += stock[i] * price[i]

#Print out the result
print(stock_worth)