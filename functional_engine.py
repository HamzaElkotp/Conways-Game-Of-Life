from typing import Tuple

Grid = Tuple[Tuple[int, ...], ...]  # 0 = dead, 1 = alive


def get_cell(grid: Grid, row: int, col: int) -> int: # Nadeen
   if row<0 or row>= len(grid):
       return 0
   elif col<0 or col>=len(grid[0]):
       return 0
   else: return grid[row][col]


def count_neighbors(grid: Grid, row: int, col: int) -> int: # Hend
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    neighbors_values = [get_cell(grid, row + dx, col + dy) for (dx, dy) in neighbors]

    result = sum(neighbors_values)

    return result


def count_neighbors_recursive(grid: Grid, row: int, col: int, indx:int = 0) -> int:
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    # Your logic here
    return 1


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


def next_generation(grid: Grid) -> Grid: # Mostafa, Yasmin
    rows = len(grid)
    cols = len(grid[0])

    return tuple(
        tuple(
            next_state(
                get_cell(grid, x, y),
                count_neighbors(grid, x, y)
            )
            for y in range(cols)
        )
        for x in range(rows)
    )
