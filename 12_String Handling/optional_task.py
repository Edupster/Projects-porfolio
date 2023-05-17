#Enter a word and save it in a variable
word=input("Enter a word: ")

#Create an empty list with the same length than the word entered to save the word backwards
word_backwards=['']*len(word)

#Start a for loop to write the word in backwards in the empty list
for i in range(0,len(word)):
    word_backwards[i]=word[-i-1]

#Transfrom the word in bacwards from a list to a string with the method join
word_backwards="".join(word_backwards)

#Compare if the word entered and the word backwards are palindromes and print out the result
if word==word_backwards:
    print('Your word is a palindrome')
else:
    print('Your word is not a palindrome')