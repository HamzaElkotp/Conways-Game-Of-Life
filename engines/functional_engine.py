from typing import Tuple

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

#### We have 5 implementations for counting neigbors

########## METHOD1: Not very functional (uses loops)
def count_neighbors(grid: Grid, row: int, col: int) -> int:
    neighbors_values = [get_cell(grid, row + dx, col + dy) for (dx, dy) in neighbors]
    result = sum(neighbors_values)
    return result


########## METHOD2: More functional (uses Recursive)
def count_neighbors_recursive(grid: Grid, row: int, col: int, indx:int = 0) -> int:
    if indx >= 8:
        return 0
    
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    return (
        get_cell(grid, row + neighbors[indx][0], col + neighbors[indx][1])
        +
        count_neighbors_recursive(grid, row, col, indx+1)
    )

########## METHOD3: More More functional (uses Tail Recursive)
def count_neighbors_tail_recursive(grid: Grid, row: int, col: int, indx:int = 0, acc:int = 0) -> int:
    if indx >= 8:
        return acc
    
    new_acc = acc + get_cell(grid, row + neighbors[indx][0], col + neighbors[indx][1])

    return count_neighbors_tail_recursive(grid, row, col, indx+1, new_acc)


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
