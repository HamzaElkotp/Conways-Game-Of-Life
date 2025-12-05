"""
Docstring for rendering.grid_renderer
GridRenderer handles pixels.

- converting each cell to a rectangle on the screen
- scaling its size by a variable zoom
- shifting its screen position using offset_x, offset_y

"""
from typing import Tuple

Grid = Tuple[Tuple[int, ...], ...]

class GridRenderer:
    def __init__(self) -> None:
        ...
    
    def draw_grid(self, grid: Grid, zoom: float, offset_x: int, offset_y: int) -> None:
        ...
