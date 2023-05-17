#Declare a sentence in a variable including a special character instead of spaces
sentence="The!quick!brown!fox!jumps!over!the!lazy!dog!."
#Replace the special character for space characters and print out the result
print(sentence.replace('!',' ')+'\n')
#Convert the sentence in low case to up case using .upper() method and print out the result
print(sentence.replace('!',' ').upper()+'\n')
#Use the negative indexes on the variable as a list to print the sentence backwards
print(sentence.replace('!',' ').upper()[::-1])