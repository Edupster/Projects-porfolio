from tabulate import tabulate


class Shoe:

    def __init__(self, country, code, product, cost, quantity):

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
    
    def get_cost(self):

        return self.cost

        '''
        Add the code to return the cost of the shoe in this method.
        '''

    def get_quantity(self):
        
        return self.quantity
        '''
        Add the code to return the quantity of the shoes.
        '''

    def __str__(self):

        return str(f"{self.country},{self.product},{self.cost},{self.code},{self.quantity}")

        '''
        Add a code to returns a string representation of a class.
        '''


shoe_list = []
#==========Functions outside the class==============
def update_inventory():
    f=open("inventory.txt" , "w")
    f.write("Country,Product,Cost,Code,Quantity")
    for shoe in shoe_list:
        f.write("\n"+shoe.__str__())
    f.close()

def read_shoes_data():
    shoe_list.clear()
    f=open("inventory.txt" , "r")
    for line in f:
        a=line.strip("\n").split(",")
        Shoe_1 = Shoe(a[0],a[1],a[2],a[3],a[4])
        shoe_list.append(Shoe_1)
    del shoe_list[0]
    f.close()
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''

def capture_shoes():
    country = input("Enter the Shoe's country: ")
    code = input("Enter the Shoe's code: ")
    product = input("Enter the Shoe's product: ")
    cost = input("Enter the Shoe's cost: ")
    quantity = input("Enter the Shoe's quantity: ")

    New_Shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(New_Shoe)
    update_inventory()
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

def view_all():
    table=[]
    table.append(["Country","Product","Cost","Code","Quantity"])
    for shoe in shoe_list:
        table.append(shoe.__str__().split(","))
    print(tabulate(table))



def re_stock():
    min = int(shoe_list[0].quantity)
    min_object_index = 0
    for i in range (len(shoe_list)):
        if int(shoe_list[i].quantity) < min:
            min = int(shoe_list[i].quantity)
            min_object_index = i
    print (f"{shoe_list[min_object_index].product} is the item with the lowest stock of {str(min)} pcs")
    
    while True:
        answer = input("Would you like to re-stock this item (yes/no): ")
        if answer.upper() == "YES":
            stock_quantity = int (input("Enter the new Quatity after re-stock: "))
            shoe_list[min_object_index].quantity = stock_quantity
            update_inventory()
            break

        elif answer.upper() == "NO":
            break

        else:
            print("Invalid answer!, try again")


    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

def seach_shoe():
    shoe_code= input("Enter the shoe Code: ")
    b = 0
    for shoe in shoe_list:
        if shoe.code == shoe_code:
            b = 1
            table=[]
            table.append(["Country","Product","Cost","Code","Quantity"])
            table.append(shoe.__str__().split(","))
            print(tabulate(table))
    if b == 0:
        print("Shoe Code not found!")
            
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

def value_per_item():
    table=[]
    table.append(["Product","Cost","Quantity","Value"])
    for shoe in shoe_list:
        value = round(int(shoe.get_cost())*int(shoe.quantity),2)
        table.append([shoe.product,shoe.get_cost(),shoe.quantity,value])
    print(tabulate(table))
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

def highest_qty():
    high_qty = 0
    hig_qty_object_index = 0
    for i in range (len(shoe_list)):
        if int(shoe_list[i].quantity) > high_qty:
            high_qty = int(shoe_list[i].quantity)
            hig_qty_object_index = i
    print (f"{shoe_list[hig_qty_object_index].product} is the item with the highest stock of {str(high_qty)} pcs. The item has been put on sale!")
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

read_shoes_data()
view_all()
highest_qty()
