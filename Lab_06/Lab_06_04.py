def Water_flow(terrain, r, c, rows, cols, current_height):
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return
    
    if terrain[r][c] == '0':
        return
    
    if int(terrain[r][c]) > current_height:
        return
    
    height_here = int(terrain[r][c])
    
    terrain[r] = terrain[r][:c] + '0' + terrain[r][c+1:]
    
    Water_flow(terrain, r+1, c, rows, cols, height_here)
    Water_flow(terrain, r-1, c, rows, cols, height_here)
    Water_flow(terrain, r, c+1, rows, cols, height_here)
    Water_flow(terrain, r, c-1, rows, cols, height_here)


print(" *** Water Flow ***")
data = input("Input rows,cols/data1,data2,.../start_row,start_col : ").split("/")
rows, cols = map(int, data[0].split(","))
terrain = data[1].split(",")
start_r, start_c = map(int, data[2].split(","))
if rows <= 0 or rows > 9 or cols <= 0 or cols > 9:
    print("Error: Rows and columns must be between 1 and 9")
elif start_c >= cols or start_r >= rows:
    print("Error: Start coordinates are out of grid bounds")
else:
    start_height = int(terrain[start_r][start_c])

    Water_flow(terrain, start_r, start_c, rows, cols, start_height)

    for row in terrain:
        print(row)

