#Create an algorithm that will request to the user to enter items from a store, if the user enter an item 
#that is not available the item will be removed and at the end the list will be printed out


#Compilation error Print instead of print function
Print("Enter the items you would like to order.\nEnter stop to stop entering more items. ")

#Logical error, the while loop can not exist without Boolean statements or with an initial Boolean value "False"
while False:
    a=input("")
    #Compilation error, uper instead of upper function
    a=a.uper()

    #Logical error, the items can no be append in a list that hasn't be declared
    cart.append()

    if "STOP" in cart:
        cart.pop()
        break

#Runtime error, -1 is not an index in the valid range for the list
for i in range(-1,len(cart)):

    #Runtime error if TV is on the list the item will be removed and the for loop will be out of the list range.
    #If TV is removed from the list is necessary to break the loop

    if cart[i]=="TV":
        print("TV is currently unavailable")
        cart.remove("TV")

print(f"The items in your list are : {cart}")



"""
cart=[]

print("Enter the items you would like to order.\nEnter stop to stop entering more items. ")
while True:
    a=input("")
    a=a.upper()
    cart.append(a)

    if "STOP" in cart:
        cart.pop()
        break

for i in range(0,len(cart)):
    if cart[i]=="TV":
        print("TV is currently unavailable")
        cart.remove("TV")
        break

print(f"The items in your list are : {cart}")"""