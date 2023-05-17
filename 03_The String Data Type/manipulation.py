#Request the user to enter a sentence
str_manip=input('Please enter a sentence:\n')
print('\n')
#Use the len method to determinate the length of the sentence and print out the result
print('The sentence length is :', len(str_manip))
print('\n')
#Determinate the last character of the sentence and use the .replace() method to replace with another character
print ("Replacing character letter for '&' in the whole sentence:"+str_manip.replace(str_manip[-1],'&'))
print('\n')
#Use the variable as a list to change the order of the characters backwards
print('Sentence backwards:'+str_manip[::-1])
print('\n')
#Use the string variable as a list of characters to slice it and create a new word with the first 3 and the last 2 characters
print ('Creating a new word with the first 3 and 2 last characters:'+str_manip[0:3:]+str_manip[len(str_manip)-2:len(str_manip):])

