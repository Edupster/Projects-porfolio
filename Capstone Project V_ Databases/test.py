Qty = "a"
flag = 0
while flag == 0:
    for i in Qty:
        if i in ["0","1","2","3","4","5","6","7","8","9",]:
            pass
        else:
            flag = 1
    if flag == 0:
        break
    if flag == 1:
        print("Please enter only integer numbers without spaces")
        Qty = input("Enter the book's Quantity")
        flag = 0
    
        
        