from typing import Tuple

Grid = Tuple[Tuple[int, ...], ...]  # 0 = dead, 1 = alive

def next_generation(grid: Grid) -> Grid: # Heidy
    """Reassign Grid with a new mutable grid representing the next generation."""
    ...
# Heidy Salem
# 20230641
# Conway's Game of Life - Imperative Version

#Imperative Engine Functions
# next_generation()
#	It doesn’t receive a grid; it accesses the global grid and reassigns it
#	It doesn’t return a grid; it reassigns the global grid
#	It does all the operations line by line, so we have one function that does everything in the needed order


#Imperative Engine Execution Flow
#               next_generation()
#       |
#       ├─ Creates an empty grid
#       ├─ iterate over all rows (x)
#       │    └─ iterate over all columns (y)
#       │          └─  For each cell
#       │          	       ├─ Determine the current state of the current cell
#       │                 ├─ Count alive neighbors for the chosen cell
#       │                 ├─ Decide the new state based on the conditions
#       │                 └─ Put the new state inside the empty grid
#       │
#       └─ Replace the old grid with the new grid (reassign)

#Global Variables
# grid: 2D list of integers representing the grid (0 for dead, 1 for alive)
# rows_size: integer representing the size of rows of the grid
# columns_size: integer representing the size of columns of the grid

# create an empty grid
def create_empty_grid(rows_size, columns_size):
    grid = []  # to store the rows

    for _ in range(rows_size):
        row = []  # one row

        for _ in range(columns_size):
            row.append(0)  # add a cell with value 0 (dead)

        grid.append(row)  # add the row to the grid

    return grid

g = create_empty_grid(3, 4)
print(g)

def determine_each_cell_state(grid, rows, columns):
    state = []
    for _ in range(rows):
        row = []
        for _ in range(columns):
            if grid[rows][columns] == 0:
                state.append("dead")
            else:
                state.append("alive")
        state.append(row)
    return state

#Function to count alive neighbors for the chosen cell
def count_alive_neighbors(grid, rows, columns):
#intialize the count of alive neighbors
    alive_neighbors = 0
    count_alive_neighbors = []
    for _ in range(rows):
        row = []
        # in case of the cell in the corner the grid .
        #  will be out of index so we need to check the index of the cell
        # in case of the cell in the first row and first column
        if i == 0 and j == 0:
            if grid[i+1][j] == 1:
                alive_neighbors += 1
            if grid[i][j+1] == 1:
                alive_neighbors += 1
            if grid[i+1][j+1] == 1:
                alive_neighbors += 1
            row.append(alive_neighbors)
        count_alive_neighbors.append(row)

        # in case of the cell in the last row and first column
        if i == rows-1 and j == 0 :
            if grid[i-1][j] == 1:
                alive_neighbors += 1
            if grid[i][j+1] == 1:
                alive_neighbors += 1
            if grid[i-1][j+1] == 1:
                alive_neighbors += 1
            row.append(alive_neighbors)
        count_alive_neighbors.append(row)

        # in case of the cell in the first row and last column
        if i == 0 and j == columns-1:
            if grid[i+1][j] == 1:
                alive_neighbors += 1
            if grid[i][j-1] == 1:
                alive_neighbors += 1
            if grid[i+1][j-1] == 1:
                alive_neighbors += 1
            row.append(alive_neighbors)
        count_alive_neighbors.append(row)

        # in case of the cell in the last row and last column
        if i == rows-1 and j == columns-1:
            if grid[i-1][j] == 1:
                alive_neighbors += 1
            if grid[i][j-1] == 1:
                alive_neighbors += 1
            if grid[i-1][j-1] == 1:
                alive_neighbors += 1
            row.append(alive_neighbors)
        count_alive_neighbors.append(row)

        # in case of the cell in the first row and not in the corner
        if i == 0 and j != 0 and j != columns-1:
            if grid[i][j-1] == 1:
                alive_neighbors += 1
            if grid[i][j+1] == 1:
                alive_neighbors += 1
            if grid[i+1][j-1] == 1:
                alive_neighbors += 1
            if grid[i+1][j] == 1:
                alive_neighbors += 1
            if grid[i+1][j+1] == 1:
                alive_neighbors += 1
            row.append(alive_neighbors)
        count_alive_neighbors.append(row)

        # in case of the cell in the last row and not in the corner
        if i == rows-1 and j != 0 and j != columns-1:
            if grid[i-1][j-1] == 1:
                alive_neighbors += 1
            if grid[i-1][j] == 1:
                alive_neighbors += 1
            if grid[i-1][j+1] == 1:
                alive_neighbors += 1
            if grid[i][j-1] == 1:
                alive_neighbors += 1
            if grid[i][j+1] == 1:
                alive_neighbors += 1
            row.append(alive_neighbors)
        count_alive_neighbors.append(row)

        # in case of the cell in the last row and not in the corner
        if j == 0 and i != rows-1 and  i != 0:
            if grid[i-1][j] == 1:
                alive_neighbors += 1
            if grid[i+1][j] == 1:
                alive_neighbors += 1
            if grid[i-1][j+1] == 1:
                alive_neighbors += 1
            if grid[i][j+1] == 1:
                alive_neighbors += 1
            if grid[i+1][j+1] == 1:
                alive_neighbors += 1
            row.append(alive_neighbors)
        count_alive_neighbors.append(row)
        # in case of the cell in the last column and not in the corner
        if j == columns-1 and i != rows-1 and  i != 0:
            if grid[i-1][j] == 1:
                alive_neighbors += 1
            if grid[i+1][j] == 1:
                alive_neighbors += 1
            if grid[i-1][j-1] == 1:
                alive_neighbors += 1
            if grid[i][j-1] == 1:
                alive_neighbors += 1
            if grid[i+1][j-1] == 1:
                alive_neighbors += 1
            row.append(alive_neighbors)
        count_alive_neighbors.append(row)
        # in case of the cell in the not in the first row and not in the la
        for i in range(rows-1, rows+1):
            for j in range(columns-1, columns+1):
                if i >= 0 and i < rows and j >= 0 and j < columns:
                    if grid[i][j] == 1:
                        alive_neighbors += 1
                    row.append(alive_neighbors)
                count_alive_neighbors.append(row)
    return count_alive_neighbors

count_alive_neighbors_grid = count_alive_neighbors(g, 3, 4)
print(count_alive_neighbors_grid)

def new_state(count_alive_neighbors_grid, grid, rows, columns):
    new_state = []
    for _ in range(rows):
        for _ in range(columns):
            if grid[rows][columns] == 0:
                if count_alive_neighbors_grid[rows][columns] < 2:
                    new_state.append("dead")
                elif count_alive_neighbors_grid[rows][columns] > 3:
                    new_state.append("dead")
                else:
                    new_state.append("alive")
            else:
                if count_alive_neighbors_grid[rows][columns] == 3:
                    new_state.append("alive")
    grid=new_state
    return grid
