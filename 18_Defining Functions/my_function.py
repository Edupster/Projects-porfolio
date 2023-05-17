#Define a new function without input arguments to print out the days 
# of the week 
def days_week():

  #Declare a list that contain the days of the week
  days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  #Start a for loop to call the elements in the list "days" 
  for i in days:

    #Print out the "i" element from the list "days"
    print(i)

#Define a function that requests a string as input argument 
def hello(string):

  #Cast the sentence entered in the argument to a list. Use the spaces in the sentence to
  # split sentence's elements 
  string=string.split(" ")

  #Declare an empty list to save the output result
  new_string=[]

  #Start a for loop to compare the elements in the list with the sentence entered using 
  # the indexes for each value in the list
  for i in range(0,len(string)):
    
    #If the index "i" is an odd number, then append a "hello" in the empty list
    if i%2 != 0:
      new_string.append("Hello")

    #If the index "i" ins an even number, then append the "i" value from the list with the sentence
    else:
      new_string.append(string[i])
      
  #Cast the list with the output to a string variable using the join function and adding a space 
  # between each element in the list    
  new_string=" ". join(new_string)
  
  #Print out the result
  print(new_string)

#Call the function "days_week" on the terminal (it doesn't need any input argument)
days_week()

#Call the function "hello" on the terminal (it needs a sentence as input argument)
hello("This is my new function")

