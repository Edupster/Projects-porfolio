#Open the file "input.txt" read the content in the file and save in in the object "f"
f = open("input.txt","r+")

#Declare the variables "characters”, “words", "lines" and "vowels" with initial values equal to zero.
#(This variables will serve as counters and accumulators)
characters=0
words=0
lines=0
vowel=0

#Start for loop to read all the lines in the object "f"
for line in f:

    #Each time the for loop reads a line increase the counter “lines” one unit
    lines+=1
    
    #Sume and save the result in the variable "characters" for the length of each line
    #(Considere that this algorithm count the space characters as any other character)
    characters+= len(line)

    #Start a for loop to get each character value with position "i" in each line
    for i in range(0,len(line)):

        #if the character "i" in each line is equal to the character space " " or the position "i" is equal to the last position in the line
        #Then increase one unit the counter words
        if line[i]==" " or i+1==len(line):
            words+=1
        
        #else if the character "i" in each line is equal to a vowel then increse the variable vowel one unit
        elif line[i].upper()=="A" or line[i].upper()=="E" or line[i].upper()=="I" or line[i].upper()=="O" or line[i].upper()=="U":
            vowel+=1

#Close the riding of the file "input.txt"
f.close()

#Print out the value of all the counters and accumulators
print (f"The number of characters in the file is: {characters}")
print (f"The number of words in the file is: {words}")
print(f"The number of lines in the file is: {lines}")
print(f"The number of vowel in the file is: {vowel}")