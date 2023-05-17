#Request to enter a sentence and save it in a variable
sentence=input("Enter a sentence: ")

#Create an empty list to save the result
sentence2=[]

#Start a for loop to determinate if the elements in the sentence entered have even indexes, if so 
#transform the elements with even indexes into upper characters. If the character's indexes are odd 
#ther's not any change applied on them. After the comparation append the results in the empty list.
for i in range(0,len(sentence)):

  if i%2==0:
    sentence2.append(sentence[i].upper())

  else:
    sentence2.append(sentence[i])

#Transform the list with the result into a string variable with the join method and print out the result
sentence2="".join(sentence2)
print(sentence2)