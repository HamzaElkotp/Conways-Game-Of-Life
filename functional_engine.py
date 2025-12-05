from typing import Tuple

Grid = Tuple[Tuple[int, ...], ...]  # 0 = dead, 1 = alive

# def create_grid(rows: int, cols: int) -> Grid: # 
#     """Create a new immutable grid with all cells dead."""
#     ...

def get_cell(grid: Grid, row: int, col: int) -> int: # Nadeen
    """Returns the current state of the cell"""
    ...

def count_neighbors(grid: Grid, row: int, col: int) -> int: # Hend
    """Return the number of live neighbors around a given cell."""
    ...

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
