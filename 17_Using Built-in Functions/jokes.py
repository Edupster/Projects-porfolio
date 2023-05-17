#Import the random libraries
import random

#Declare a string list with jokes as the list's content
jockes=[" What time is it when the clock strikes 13? Time to get a new clock",
        "How does a cucumber become a pickle? It goes through a jarring experience",
        "Why can’t Elsa from Frozen have a balloon? Because she will",
        "Why did the kid bring a ladder to school? Because she wanted to go to high school.",
        "What did one volcano say to the other? I lava you.",
        "How do you talk to a giant? Use big words",
        "Why did the cookie go to the hospital? Because he felt crummy"]

#Use the random.randrange() and len() functions to pick up a random value in the range from 0 to the length of the 
#list and print out the joke contained in the list with that value as index
print(jockes[random.randrange(0,len(jockes))])
