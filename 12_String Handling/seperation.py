#Request to enter a sentence and save it in a variable
string=input("Enter a sentence: ")

#Detect the spacing characters in the sentence and use them to split the sentence into separated words in a list.
string=string.split(" ")

#Use a for loop to print the separated words saved in the list to print them one by one on the terminal
for i in string:
    print(i)
