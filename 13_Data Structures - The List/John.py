"""Follow these steps:
● Write a Python program called John.py that takes in a user’s input as a
string.
● While the string is not “John”, add every string entered to a list until “John”
is entered. This program basically stores all incorrectly entered strings in a
list where “John” is the only correct string.
● Print out the list of incorrect names.
● Example program run (what should show up in the Python Console when
you run it):
Enter your name : <user enters Tim>
Enter your name : <user enters Mark>
Enter your name: <user enters John>
Incorrect names: [‘Tim’, ‘Mark’]
● HINT: When testing your While loop, you can make use of .upper() or
.lower() to eliminate case sensitivity.
If you are having any difficulties, please feel free to contact our specialist team on
Discord for support"""

#Create an empty list that will contain the names entered by the user
name=[]

#Start a while loop that will request to the user to enter their name and will remain repeating unless the right name is entered (the right name is "john" )
while True:

    #Request to the user to enter their name and append it into the name list
    name.append(input("Enter your name: "))

    #If the name entered in the last position of the list is equal to the name "John" then delete that element from the list and print
    #out the rest of the names entered. Also, once this condition is true break the while loop
    if name[-1].upper()=="JOHN":
        name.pop()
        break

#print the list the names entered without the last element entered "John"
print(name)
