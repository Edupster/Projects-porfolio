#Import the libraries needed for the math functions
import math
#Request the user to enter the lengths of three sides of a triangle
print('Provide the length of the three sides of a tiangle (a,b,c) below\n')
side_a=float(input("Enter the side 'a':\n"))
side_b=float(input("Enter the side 'b':\n"))
side_c=float(input("Enter the side 'c':\n"))
print('\n')
#Calculate the area of the triangle with the formula given and using the math library
s=((side_a+side_b+side_c)/2)
area=(math.sqrt(s*(s-side_a)*(s-side_b)*(s-side_c)))  
#Print the area of the triangle and round it out to 2 decimals
print(f'The area of the triangle is {round(area,2)}')