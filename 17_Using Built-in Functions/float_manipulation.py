#Imort the math libraries
import math 

#Declare an empty list to contain the numbers entered by the user
numbers=[]

#Request the user to enter 10 numbers
print("Enter 10 numbers")

#Start a for loop to insert 10 elements to the list "numbers" and append the numbers entered
for i in range(0,10):
    numbers.append(float(input("")))

#Use the sum function to sum the 10 numbers contained in the list and save the result in a variable
total=sum(numbers,0)

#Calculate the average of the numbers entered using the len() and round() functions. Save the result in a variable
average=round(total/len(numbers),2)

#Use the sorted() function to sort in ascending order the elements in the list "numbers"
nubers=sorted(numbers)

#Use the round() and len() functions to calculate the index in the sorted list that contains the median value
median_index=round((len(numbers)/2))-1

#Use the index of the median value to get the element from the list and save it in a variable
median=numbers[median_index]

#Use the max() function to get the maximum value in the list and print it out
print(max(numbers))

#Use the min() function to get the minimum value in the list and print it out
print(min(numbers))

#Print out the rest of the results
print(total)
print(average)
print(median)





