"""Follow these steps:
● Create a new Python file in this folder called list_types.py.
● Imagine you want to store the names of three of your friends in a list of
strings. Create a list variable called friends_names, and write the syntax to
store the full names of three of your friends.
● Now, write statements to print out the name of the first friend, then the
name of the last friend, and finally the length of the list.
● Now, define a list called friends_ages that stores the age of each of your
friends in a corresponding manner, i.e., the first entry of this list is the age
of the friend named first in the other list."""

#Declare an empty list that will contain the names entered by the user
friend_names=[]

#Request to the user to enter three different names
print("Enter the name of three of your friends: ")

#Start a for loop that will request and save in the empty list the three names entered by the user
for i in range(0,3):
  friend_names.append(input(f"Friend {i+1}: "))

print("\n")

#Print out the first and the last items in the list entering their positions in the lists, 0 for the first and -1 for the last
#Also, print out the size of the list. 
print(f"Your first friend entered was: {friend_names[0]}")
print(f"Your last friend entered was: {friend_names[-1]}")
print(f"The size your friends list is: {len(friend_names)}")

print("\n")

#Create another empty list to save the age for each person entered
friend_ages=[]

#Start a for loop to save each friend age in the same position than their names in the names list 
for i in range(0,3):
  friend_ages.append(input(f"Enter {friend_names[i]}'s age: "))

print("\n")

#Star a for loop to print out the information of each person (name and age), getting the information on the same position on both lists
for i in range(0,3):
  print(f"{friend_names[i]} is {friend_ages[i]} years old")
