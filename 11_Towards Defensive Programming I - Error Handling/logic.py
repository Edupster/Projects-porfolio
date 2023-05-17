#The algorithm below will calculate the user's lucky numbers for the lottery requesting 
#to enter how many numbers can be entered per lotery ticket and the greatest number posible in the ticket
import random

n_nums=int(input("Enter how many numbers you are entering in your ticket: "))
numsRange=(input("Enter the greatest number you can pick up for your lucky numbers"))

luckyNums=[]

for i in range(0 n_nums):
a=random.randint(0,numsRange)

    while a in luckyNums
        a=random.randint(0,numsRange) 

    luckyNums_append(a)
        
print(luckyNums)

"This is the right algorithm"
"""import random

n_nums=int(input("Enter how many numbers you are entering in your ticket: "))
numsRange=int(input("Enter the greatest number you can pick up for your lucky numbers"))

luckyNums=[]

for i in range(0,n_nums):
    a=random.randint(0,numsRange)
    while a in luckyNums:
        a=random.randint(0,numsRange) 

    luckyNums.append(a)
        
print(luckyNums)
"""