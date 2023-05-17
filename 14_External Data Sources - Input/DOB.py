#Use the open function to open and create an object with the .txt file saved in the same working directory
f = open('DOB.txt', 'r+', encoding='utf-8')

#Create a variable to extract and save the name contained on each line of the object "f"
name=""

#Create an empty list to append the name saved in the variable "name"
names=[]

#Create a variable to save the index where the date of birth starts in each line on the object "f"
dob_index=0

#Create an empty list to append the days of birth contained on each line on "f"
dobs=[]

#Start a for loop to read each line on "f"
for line in f:

    #Start a for loop to read the content on each line of "f" as list
    for i in range(0,len(line)):

        #if the element "i" of the line on "f" is not equal to a numerical character then save the characters in the variable name 
        if line[i]!="0" and line[i]!="1" and line[i]!="2" and line[i]!="3" and line[i]!="4" and line[i]!="5" and line[i]!="6" and line[i]!="7" and line[i]!="8" and line[i]!="9":

                name += line[i]

        #Else (if the element "i" of the line on "f" is equal to a numerical character then get the position where the date of birth starts on the line and break the loop)        
        else:

            dob_index=i
            break
    
    #After reading the line and prosses the information on the line append the variable name in the list "names". Also, append the values in the list "dobs" from the line value "i" corresponding to the start of the 
    #date of birth up to the end of the line
    dobs.append(line[dob_index:len(line)])
    names.append(name)

    #After reading and appending name in "f" clear the variable "name" to save the next value
    name=""

#Close the reading of the .txt document
f.close ()

#Start two for loops to print out separated the values saved on the lists "names" and "dobs"
print("Names:")
for i in names:
    print(i)
print("\n")
print("Birth dates:")         
for i in dobs:
    print(i, end = '')



