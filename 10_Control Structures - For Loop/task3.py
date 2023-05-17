#Declare a variable with the initial comparing value for the while loop
i=20

print("From 20 to 0")

# While i greater or equal to 0, print the value of i
while i>=0:
  print(i)

#After each iteration "i" will decrease one unit
  i+=-1

print("\n")
print("Even numbers from 0 to 20")

#Start a while cycle that will keep repeating while “I” is less or equal to 20
while i<=20:

#If the result of dividing "i" by 2 is equal to 0, then print out "i"
  if i%2==0:
    print(i)

#Increse "i" one unit at the end of the iteration
  i+=1

print("\n")
print("Chart with loop")

# Declare the variable b with initial value with the character "*"
b='*'

# Declare a for loop. For "j" in range 0 to 5 (the loop will repeat 5 times), and print out the value of "j" in each iteration
for j in range(0,5):
  print(b)

#Add a new character to the string variable b after each iteration
  b=b+'*'
