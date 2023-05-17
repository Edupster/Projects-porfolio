#Import math libraries
import math

#Open "input.txt" document in read mode 
f = open("input.txt", "r")

#Save all the "input.txt" content in a new variable
content = f.read(-1)

#Close "input.txt" file
f.close()

#Split the content extracted from the txt file using the split function and save the result 
#in a list with the content divided by lines
content = content.split("\n")

#Declare an empty list to append the operation contained in each line form "input.txt"
operation = []

#Declare an empty list to append the list of numbers contained in each line from "input.txt"
numbers = []

#Start a for loop to read each line contained in the list content
for i in content:
  
  #Slice the text in each element in the list "content" to separate the operation requested 
  # and the list of numbers for each operation. Append the result in the lists "operation" and "numbers"
  operation.append(i[0:3])
  numbers.append(i[4:])

#Declare an empty list to cast and append the numbers contained in the list "numbers"  
numbers_int=[]

#Declare an empty dictionary to add the the integer values of each line from "input.txt"
numbers_dic={}

#Start a for loop to read and cast every element in the list numbers to integer type and store
#the values in the dictionary
for i in range (0,len(numbers)):
  
  numbers_list1=numbers[i].split(',')
  
  for j in range(0,len(numbers_list1)):
    
    numbers_int.append(int(numbers_list1[j]))
    
  numbers_dic[i] = numbers_int
  
  numbers_int=[]


#Define a function to calculate the minimum value in a list of integer numbers
def my_min(list):
  
  #Order the list entered in the function's argument and sort it in ascending order
  list=sorted(list)
  
  #Retrun the first value in the sorted list which correspond to the minimum value
  return(list[0])

#Dedfine a function to calculate the maximum value in a list of integer numbers
def my_max(list):
  
  # #Order the list entered in the function's argument and sort it in ascending order
  list=sorted(list)
  
  #Retrun the last value in the sorted list which correspond to the maximum value
  return(list[-1])

#Define a function to calculate the average value in the list entered
def my_avg(list):
  
  #Calculate the average value in the list entered in the function's argument
  average=sum(list)/len(list)
  
  #Return the value for the average value
  return(average)

#Define a function to calculate a percentile in a list, this function takes as input arguments,
# a list of integer numbers and the value for the percentile to be calculated
def my_perc(list,perc):
  
  #Sort out the list entered in the function's argument in ascending order
  list=sorted(list)
  
  #Calculate the index of the value in the list that belongs to the percentile
  index=math.ceil((perc/100)*len(list))
  
  #Return the value in the list with the index calculated
  return(list[index-1])

#Open the "output.txt" file on write mode
f1 = open("output.txt", "w+")

#Start a for loop to call the list and dictionaries defined below and perform the operations
#calling to the functions created
for i in range(0,len(operation)):
  
  #Determinate the operation to perform saved on the list operation
  a = operation[i]
  
  #Depending on the operation to perform call the different functions declared write the 
  #result on the "output.txt" file
  if a == "min":
    
    result = my_min(numbers_dic[i])
    
    f1.write(f"The min of {numbers_dic[i]} is {result}\n")
    
  elif a == "max":
    
    result = my_max(numbers_dic[i])
    
    f1.write(f"The maxn of {numbers_dic[i]} is {result}\n")
    
  elif a == "avg":
    
    result = my_avg(numbers_dic[i])
    
    f1.write(f"The avg of {numbers_dic[i]} is {result}\n")
    
  elif "p" in a:
    
    percentil=int(a[1:3])
    
    result = my_perc(numbers_dic[i],percentil)
    
    f1.write(f"The {percentil}th percentil of {numbers_dic[i]} is {result}\n")

#Close the "output.txt" file
f1.close()
