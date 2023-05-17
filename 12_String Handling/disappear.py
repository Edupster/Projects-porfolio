#Request to enter a sentence and save it in a variable
sentence=input('Enter a sentence: ')

#Request to enter the characters that will be stripped from the sentence and save then in a variable
disappear=input("enter the characters you would like to remove separated by comas: ")

#Transform the variable with the characters that will be removed into a list
disappear=disappear.split(",")

#Declare an empty list that will have the same lenght than the sentence entered as a list
sentence_split=['']*len(sentence)

#Start a for loop that will compare the elements of the sentence entere with the characters selected to be removed
#if the element of the sentence entered is equal to any of characters to be removed, then the list with the sentence 
#will replace the element with an empty character
for i in range (0,len(sentence_split)):
   sentence_split[i]=sentence[i]
   for j in disappear:
        if sentence_split[i]==j:
           sentence_split[i]=""

#Transform the sentence as a list into a string variable again and print out the result
sentence_split="".join(sentence_split)
print(sentence_split)