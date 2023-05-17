ragged_list = [ [ 1, 2, 3 ] ,
[ 4, 5 ],
[ 6 ],
[ 7, 8, 9, 10 ] ]

rows = len(ragged_list)
for row in range(rows):
    cols = len(ragged_list[row]) # now the number of cols depends on each row’s length
print("Row", row, "has", cols, "columns: ", end="")
for col in range(cols):
    print(ragged_list[row][col], " ", end="")
empty_grid=[["#"] * len(ragged_list[0]) for _ in range(len(ragged_list))]
print(empty_grid)
print(ragged_list[-1][-1])