# Import the tabulate libraries to display results on charts
from tabulate import tabulate

#========The beginning of the class==========
class Shoe:

    '''
    In this function, you must initialise the following attributes:
        ● country,
        ● code,
        ● product,
        ● cost, and
        ● quantity.
    '''

    def __init__(self, country, product, cost, code, quantity):

        self.country = country
        self.product = product
        self.cost = cost
        self.code = code
        self.quantity = quantity

    
    def get_cost(self):
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return self.cost

    def get_quantity(self):
        '''
        Add the code to return the quantity of the shoes.
        '''
        return self.quantity
        

    def __str__(self):
        '''
        Add a code to returns a string representation of a class.
        '''
        return str(f"{self.country},{self.product},{self.cost},{self.code},{self.quantity}")

        

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def update_inventory():
    ''' 
    This function will update the information in inventory.txt getting the information
     from the updated list shoe_list and writing the new information in the .txt file'''

    try:
        f = open("inventory.txt" , "w")
        f.write("Country,Code,Product,Cost,Quantity")

        for shoe in shoe_list:
            f.write("\n"+shoe.__str__())
        f.close()

    except FileExistsError:
        print("inventory.txt file hasn't been found in the working directory, please make sure the file is in the right directory")



def read_shoes_data():

    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''

    shoe_list.clear()

    try:
        f = open("inventory.txt" , "r")

        for line in f:
            a = line.strip("\n").split(",")
            Shoe_1 = Shoe(a[0], a[1], a[2], a[3], a[4])
            shoe_list.append(Shoe_1)

        del shoe_list[0]
        f.close()

    except FileNotFoundError:
        print("inventory.txt file hasn't been found in the working directory, please make sure the file is in the right directory")
    


def capture_shoes():

    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

    country = input("Enter the Shoe's country: ")
    product = input("Enter the product's name: ")
    cost = input("Enter the Shoe's cost: ")
    code = input("Enter the Shoe's code: ")
    quantity = input("Enter the Shoe's quantity: ")

    New_Shoe = Shoe(country, product, cost, code, quantity)

    shoe_list.append(New_Shoe)

    print("The Shoes have been added to the inventory!")

    update_inventory()



def view_all():

    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

    table = []
    table.append(["Country","Product","Cost","Code","Quantity"])

    for shoe in shoe_list:
        table.append(shoe.__str__().split(","))

    print(tabulate(table))



def re_stock():

    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    try:
        min = int(shoe_list[0].get_quantity())
        min_object_index = 0

        for i in range (len(shoe_list)):
            if int(shoe_list[i].get_quantity()) < min:
                min = int(shoe_list[i].get_quantity())
                min_object_index = i

        print (f"{shoe_list[min_object_index].product} is the item with the lowest stock of {str(min)} pairs left")

        answer =""
        while answer.upper() != "NO":
            answer = input("Would you like to re-stock this item (yes/no): ")

            if answer.upper() == "YES":
                stock_quantity = int (input("Enter the new Quantity after re-stock: "))
                shoe_list[min_object_index].quantity = stock_quantity
                update_inventory()
                print(f"{shoe_list[min_object_index].product} has been re-stocked successfully!")
                break

            else:
                print("Invalid answer!, try again")

    except ValueError:
        print("Value Error, Please make sure all the quantity values from inventory.txt are integer or float values")
    


def search_shoe():

    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

    shoe_code = input("Enter the shoe Code: ")
    b = 0

    for shoe in shoe_list:
        if shoe.code == shoe_code:
            b = 1
            table = []
            table.append(["Country","Product","Cost","Code","Quantity"])
            table.append(shoe.__str__().split(","))
            print(tabulate(table))

    if b == 0:
        print("Shoe Code not found!")
            
    

def value_per_item():

    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    
    table = []
    table.append(["Product","Cost","Quantity","Value"])

    try:
        for shoe in shoe_list:
            value = round(int(shoe.get_cost())*int(shoe.get_quantity()),2)
            table.append([shoe.product,shoe.get_cost(),shoe.get_quantity(),value])

        print(tabulate(table))
    
    except ValueError:
        print("Value Error, Please make sure all the quantity and cost values from inventory.txt are integer or float values")
    


def highest_qty():

    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

    high_qty = 0
    hig_qty_object_index = 0

    try:
        for i in range (len(shoe_list)):
            
            if int(shoe_list[i].get_quantity()) > high_qty:
                high_qty = int(shoe_list[i].get_quantity())
                hig_qty_object_index = i

        print (f"{shoe_list[hig_qty_object_index].product} is the item with the highest stock of {str(high_qty)} pairs. The item has been marked to put on sale!")

    except ValueError:
        print("Value Error, Please make sure all the quantity values from inventory.txt are integer or float values")

    

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
option = ""

while option != "7":

    print("""Select an option from the menu:

1 - View all the stock
2 - Search Shoes
3 - Capture Shoes
4 - Re-Stock
5 - Put shoes on sale
6 - Check value per item in stock 
7 - Quit""")

    option = input("")

    if option == "1":
        read_shoes_data()
        view_all()
    
    elif option == "2":
        read_shoes_data()
        search_shoe()

    elif option == "3":
        read_shoes_data()
        capture_shoes()
    
    elif option == "4":
        read_shoes_data()
        re_stock()

    elif option == "5":
        read_shoes_data()
        highest_qty()
    
    elif option == "6":
        read_shoes_data()
        value_per_item()
    
    elif option == "7":
        print("Good Bye!")
    
    else:
        print("Invalid option!, try again")

