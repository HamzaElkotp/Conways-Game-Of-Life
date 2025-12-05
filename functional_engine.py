from typing import Tuple

Grid = Tuple[Tuple[int, ...], ...]  # 0 = dead, 1 = alive

# def create_grid(rows: int, cols: int) -> Grid: # 
#     """Create a new immutable grid with all cells dead."""
#     ...

def get_cell(grid: Grid, row: int, col: int) -> int: # Nadeen
   if row<0 or row>= len(grid):
       return 0
   elif col<0 or col>=len(grid[0]):
       return 0
   else: return grid[row][col]


 #   ...

def count_neighbors(grid: Grid, row: int, col: int) -> int: # Hend
    """Return the number of live neighbors around a given cell."""
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    neighbors_values = [get_cell(grid, row + dx, col + dy) for (dx, dy) in neighbors]

    result = sum(neighbors_values)

    return result
    #...

def next_state(current_state: int, neighbors: int) -> int: # Abdo
    """Return the next state (0 or 1) for a single cell."""
    ...

def next_generation(Grid: Grid) -> Grid: # Mostafa, Yasmin
    """Return a new immutable grid representing the next generation."""
    rows = len(Grid)
    cols = len(Grid[0])

    return tuple(
            tuple(
                next_state(
                    get_cell(Grid, x, y),
                    count_neighbors(Grid, x, y)
                )
                for y in range(cols)
            )
            for x in range(rows)
        )
    ...
