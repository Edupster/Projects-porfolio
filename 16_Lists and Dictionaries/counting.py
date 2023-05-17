#Request to enter a string and save it in a variable
word=input("Enter a string: ")

#Declare an empty dictionary to save the frequency
freq={}

#Start a for loop to compare the elements as a list in the string entered by the user 
for i in word:

    #if the "i" element in the string exist as a key in the dictionary then increase the value associated to the key
    if i in freq:
        freq[str(i)]+=1
    
    #Else, create the "i" element as a key in the dictionary with initial value equal to 1
    else:
        freq[i]=1

#Print out the dictionary
print(freq)
