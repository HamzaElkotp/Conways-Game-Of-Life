from typing import Tuple

Grid = Tuple[Tuple[int, ...], ...]  # 0 = dead, 1 = alive

def next_generation(grid: Grid) -> Grid:
    N = len(grid)
    newGrid = [[0] * N for i in range(N)] # create empty list with initial value for all = 0

    for r in range(N):
        for c in range(N):
            state = grid[r][c]
            total_alive = 0

            ## Count alive neighbors
            upper = r-1, lower = r+1, left = c-1, right = c+1
            if(upper >= 0):
                total_alive+=grid[upper][c] # get the upper cell 2
            if(lower < len(grid[0])):
                total_alive+=grid[lower][c] # get the lower cell 8
            if(left >= 0):
                total_alive+=grid[r][left] # get the left cell 4
                if(lower < len(grid[0])):
                    total_alive+=grid[lower][left] # get the lower left cell 7
                if(upper >= 0):
                    total_alive+=grid[upper][left] # get the upper left cell 1
            if(right < len(grid[0])):
                total_alive+=grid[r][right] # get the right cell
                if(lower < len(grid[0])):
                    total_alive+=grid[lower][right] # get the lower right cell
                if(upper >= 0):
                    total_alive+=grid[upper][right] # get the upper right cell

            # Decide new state
            if state:
                if total_alive < 2:
                    newGrid[r][c] = 0 # this line can be discareded
                elif total_alive == 2 or total_alive == 3:
                    newGrid[r][c] = 1
                elif total_alive > 3: # this line can be discareded
                    newGrid[r][c] = 0
            else:
                if total_alive == 3:
                    newGrid[r][c] = 1
    
    return tuple(tuple(row) for row in newGrid) # convert again to tuple 





"""
def determine_each_cell_state(grid, rows, columns):
    return grid[rows][columns]

def count_alive_neighbors(grid, rows, columns):
    upper = rows-1
    lower = rows+1
    left = columns-1
    right = columns+1

    sum = 0

    if(upper >= 0):
        print(grid[upper][columns])
        sum+=grid[upper][columns] # get the upper cell 2
    if(lower < len(grid[0])):
        print(grid[lower][columns])
        sum+=grid[lower][columns] # get the lower cell 8
    if(left >= 0):
        print(grid[rows][left])
        sum+=grid[rows][left] # get the left cell 4
        if(lower < len(grid[0])):
            print(grid[lower][left])
            sum+=grid[lower][left] # get the lower left cell 7
        if(upper >= 0):
            print(grid[upper][left])
            sum+=grid[upper][left] # get the upper left cell 1
    if(right < len(grid[0])):
        print(grid[rows][right])
        sum+=grid[rows][right] # get the right cell
        if(lower < len(grid[0])):
            print(grid[lower][right])
            sum+=grid[lower][right] # get the lower right cell
        if(upper >= 0):
            print(grid[upper][right])
            sum+=grid[upper][right] # get the upper right cell
    return sum
"""