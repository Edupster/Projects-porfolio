#Request to the user to enter the shape of the building
shape=input('Enter the shape of the building (Square, Rectangular or Round):\n')

#Request to the user the information needed to calculate the area based on the shape input and print out the result

if shape.upper()=='SQUARE':
    lenght=float(input("Enter the square's length in meters:\n"))
    area=round(lenght**2,2)
    print(f"The area that will be taken up by the fuondation of the {shape} building is: {area} m^2:\n")

if shape.upper()=='RECTANGULAR':
    lenght=float(input("Enter the Rectangle's Length in meters:\n"))
    whidth=float(input("Enter the Rectangle's Width in meters:\n"))
    area=round(lenght*whidth,2)
    print(f"The area that will be taken up by the foundation of the {shape} building is: {area} m^2:\n")

if shape.upper()=='ROUND':
    radius=float(input("Enter the Circle's Radius in meters:\n"))
    area=round(3.1416*radius**2,2)
    print(f"The area that will be taken up by the foundation of the {shape} building is: {area} m^2:\n")

