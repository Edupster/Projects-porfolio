#Create an empty list that will contain the names entered
names=[]

#Request to the user to enter their pupil names
print('Enter the name of your pupils')

#Start a while loop that will keep triggering adding names to the list and will break only when the user types stop
while True:

    #The list names will add the names entered for the user and save them at the las position 
    names.append(input(''))

    #If the last element entered to the list is equal to 'stop', this element will be deleted from the list and the loop will break up after this
    if names[-1].upper()=='STOP':
        names.pop()
        break

#Print out the total number of pupils entered in the list checking how many elements are contained in the list
print(f"The total number of pupils in your class is {len(names)}")