#Read the content in the .txt files and save their content in different objects "f1" "f2".
#Open to read and write another object "f3"
f1 = open("numbers1.txt","r")
f2 = open("numbers2.txt","r")
f3 = open("all_numbers.txt","w+")

#Start a loop to read and copy all the content from the object "f1" to the object "f3"
for line in f1:
    #Start a for loop to add an "," character after the last element copied to "f3" and keep the format needed
    for i in range(0,len(line)):
        if i == len(line)-1:
            f3.write(line[i]+", ")
        else:
            f3.write(line[i])

#Start a loop to read and copy all the content from the object "f2" to the object "f3"
for line in f2:
    f3.write(line)

#Create an empty list to contain all the numbers copied disordered in the object "f3"
list_disordered = []

#Enable the reading of the object "f3"
f3 = open("all_numbers.txt","r")

#Start a for loop read the content in the object "f3"
for line in f3:
    #Copy all the object's content in the list "list_disordered", keeping only the numerical values
    list_disordered=line.split(", ")

#Cast the list from a string list to a list of integers
list_disordered=list(map(int,list_disordered))

#Create an list "list_ordered" with the same size than the list "list_disordered" filled up with zeros
list_ordered=[0]*len(list_disordered)

#Declare a variable to determinate the position of each element in the ordered list
a = 0
#Start a for loop to ordinate the values from "list_disordered" and then replace the ordered values in "list_ordered"
for i in range(0,len(list_disordered)):
    
    #start a for loop to determinate the ordered position of each value from the list disordered
    for j in range(0,len(list_disordered)):

        #If the element "i" from the disordered list is bigger than the element "j" in the same list, then increase the variable "a" one unit,
        #The final value of "a" determinates after each iteration determinate the right position of the element "i" in the ordered list
        if list_disordered[i]>list_disordered[j]:
            a += 1
    list_ordered[a]=list_disordered[i]
    a = 0

#Enable the writing in the object "f3" to fill it up with the ordered list
f3 = open("all_numbers.txt","w")

#Start a for loop to get and write in "f3" the values from the ordered list
for i in range(0,len(list_ordered)):
    f3.write(str(list_ordered[i]) +", ")

#Close all the files previously opened
f1.close()
f2.close()
f3.close()




