from typing import Tuple
from functools import reduce

Grid = Tuple[Tuple[int, ...], ...]  # 0 = dead, 1 = alive


def get_cell(grid: Grid, row: int, col: int) -> int:
   if row<0 or row>= len(grid):
       return 0
   elif col<0 or col>=len(grid[0]):
       return 0
   else: return grid[row][col]


neighbors:Tuple[Tuple[int, int]] = [
    (-1, -1), (-1, 0), (-1, 1), 
    ( 0, -1),          ( 0, 1), 
    ( 1, -1), ( 1, 0), ( 1, 1)
]

"""
#### We have 5 implementations for counting neigbors
"""

"""
########## METHOD1: Not very functional (uses loops)
"""
def count_neighbors(grid: Grid, row: int, col: int) -> int:
    neighbors_values = [get_cell(grid, row + dx, col + dy) for (dx, dy) in neighbors]
    result = sum(neighbors_values)
    return result

"""
########## METHOD2: More functional (uses Recursive)
"""
def count_neighbors_recursive(grid: Grid, row: int, col: int, indx:int = 0) -> int:
    if indx >= 8:
        return 0
    
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    return (
        get_cell(grid, row + neighbors[indx][0], col + neighbors[indx][1])
        +
        count_neighbors_recursive(grid, row, col, indx+1)
    )

"""
########## METHOD3: More More functional (uses Tail Recursive)
"""
def count_neighbors_tail_recursive(grid: Grid, row: int, col: int, indx:int = 0, acc:int = 0) -> int:
    if indx >= 8:
        return acc
    
    new_acc = acc + get_cell(grid, row + neighbors[indx][0], col + neighbors[indx][1])

    return count_neighbors_tail_recursive(grid, row, col, indx+1, new_acc)

"""
########## METHOD4: More More More functional (uses Higher order function + Tail Recursive)
########## We implemented the array.reduce higher from scratch

“ Always Try To ReInvent The Wheel ”
- Hamza M. Elkotb, A CS Student @ FCAIH.
"""
def array_reduce(array, operation_func, accumulator:int, indx:int, *args, **kwargs):
    if(indx>=len(array)):
        return accumulator
    new_acc = operation_func(accumulator, array[indx], *args, **kwargs) # pass accumulator and current
    return array_reduce(array, operation_func, new_acc, indx+1, *args, **kwargs)

def count_neighbors_with_accumelator(accumulator:int, array, row:int, col:int, grid:Grid):
    return accumulator + get_cell(grid, row + array[0], col + array[1])

"""
# Example of usage
meow:Grid = [[1,2,3], [4,5,6], [7,8,9]]
res = array_reduce(neighbors, count_neighbors_with_accumelator, 0, 0, 1, 1, meow)
print(res)
"""

"""
########## METHOD5: Not better than ours (uses Built-in Higher order function + Tail Recursive)
##########
"""
def add(x, y):
    return x+y

def count_neighbors_with_reduce(grid:Grid, row:int, col:int):
    return reduce(
        lambda accumelator, 
        current: accumelator+get_cell(grid, row + current[0], col + current[1]), 
        neighbors,
        0
    )

"""
meow:Grid = [[1,2,3], [4,5,6], [7,8,9]]
res = count_neighbors_with_reduce(meow, 1, 1)
print(res)
"""


def next_state(current_state: int, neighbors: int):
    if current_state == 1 and neighbors < 2: # (underpopulation)
        return 0
    elif current_state == 1 and (neighbors == 2 or neighbors == 3):
        return 1
    elif current_state == 1 and neighbors > 3: # (overpopulation)
        return 0
    elif current_state == 0 and neighbors == 3: # (reproduction)
        return 1
    return 0


def next_generation(grid: Grid) -> Grid:
    rows = len(grid)
    cols = len(grid[0])

    return tuple(
        tuple(
            next_state(
                get_cell(grid, x, y),
                count_neighbors_tail_recursive(grid, x, y) 
                # count_neighbors will work too, but count_neighbors_tail_recursive is morefunctional programming
            )
            for y in range(cols)
        )
        for x in range(rows)
    )
