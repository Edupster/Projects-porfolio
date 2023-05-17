"""Create a new file in this folder called loop_lists.py.
● Inside it, define a list of strings of your 5 favourite movies.
● Now, loop over the list. For each item in the list, print out "Movie: " plus the
movie's name.
● Can you figure out how to print out Movie 1: <Movie 1's name>. Movie 2: ...
etc?
● HINT: YOU WILL NEED TO LOOK UP the enumerate command in Python
using a Google search. This command allows you to loop over a list
retaining both the item at every position and its index (i.e. position in the
list)."""

#Declare a list with your 5 favorite movies
favorite_movies=["Interestellar", "V for Vendeta", "Avatar", "Ironman", "Avengers"]

#Start a for loop to acces to each item in the list with your favorite movies and print out the name of each movie,
#adding at the begginig the string "Movie:"
for i in favorite_movies:
    print(f"Movie: {i}")

