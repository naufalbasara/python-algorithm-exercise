def numCells(grid):
    count = 0

    for row_i in range(len(grid)):
        for col_i in range(len(grid[0])):
            current = grid[row_i][col_i]

            for index in range(max(0,row_i-1), min(row_i, row_i+2)):
                for j in range(max(0, col_i-1), min(col_i, col_i+2)):
                    count += 1
    return count

grid_rows = int(input().strip())
grid_columns = int(input().strip())

grid = []

for _ in range(grid_rows):
    grid.append(list(map(int, input().rstrip().split())))

result = numCells(grid)