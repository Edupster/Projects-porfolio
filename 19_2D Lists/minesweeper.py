#Define a new function that gets a grid as input information
def mines(grid):

    #Declare a new empty grid with the same dimensions that the input grid
    new_grid = [[None] * len(grid[0]) for _ in range(len(grid))]

    #Declare a counter to register every time there's a mine around the current position
    count = 0

    #Declare a for loop that access to each row in the grid entered
    for row in range(len(grid)):
        #Declare a for loop that accesses to each column in the grid entered
        for col in range(len(grid[row])):
            
            #if the element in the row and column in the loop contains a "#" symbol then assign that symbol
            #in the new grid at the same position
            if grid[row][col] == '#':
                new_grid[row][col]='#'

            #if the element in the row and column in the loop it's different to "#" symbol then execute the following
            #block
            else:

                #Analize all the values around the element in the loop, if there's a "#" symbol in any of the neighbour
                #values then the counter will increase one unit
                try:
                    if grid[row-1][col-1] == "#" and row-1>=0 and col-1>=0:
                        count += 1
                except:
                    pass
                
                try:
                    if grid[row][col-1] == "#" and col-1>=0:
                        count += 1
                except:
                    pass

                try:
                    if grid[row+1][col-1] == "#" and col-1>=0:
                        count += 1
                except:
                    pass
            
                try:
                    if grid[row-1][col] == "#" and row-1>=0:
                        count += 1
                except:
                    pass

                try:
                    if grid[row+1][col] == "#":
                        count += 1
                except:
                    pass
            
                try:
                    if grid[row-1][col+1] == "#" and row-1>=0:
                        count += 1
                except:
                    pass

                try:
                    if grid[row][col+1] == "#":
                        count += 1
                except:
                    pass

                try:
                    if grid[row+1][col+1] == "#":
                        count += 1
                except:
                    pass

                #Replace the element in the same position in the new grid with the value of the counter that represents
                #the number of "#" symbols around that position in the grid
                new_grid[row][col] = str(count)
            
            #Reset the counter
            count = 0
    
    #Start a for loop to print out the values in the new grid
    for i in range(len(new_grid)):
        print(new_grid[i])
    

mines([ ["-", "-", "-", "#", "#"],["-", "#", "-", "-", "-"],["-", "-", "#", "-", "-"],["-", "#", "#", "-", "-"],["-", "-", "-", "-", "-"] ])

