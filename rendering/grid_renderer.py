"""
Docstring for rendering.grid_renderer
GridRenderer handles pixels.

- converting each cell to a rectangle on the screen
- scaling its size by a variable zoom
- shifting its screen position using offset_x, offset_y

"""
from typing import Tuple
import tkinter as tk

Grid = Tuple[Tuple[int]]

class GridRenderer:
    def __init__(self, canvas: tk.Canvas, cell_size: float = 12.0):
        self.canvas = canvas
        self.cell_size = cell_size
        self.offset_x = 0.0
        self.offset_y = 0.0
        self._cell_rects = []

    def world_to_screen(self, r: int, c: int) -> Tuple[float, float, float, float]:
        x = self.offset_x + c * self.cell_size
        y = self.offset_y + r * self.cell_size
        return (x, y, x + self.cell_size, y + self.cell_size)

    def screen_to_grid(self, sx: float, sy: float) -> Tuple[int, int]:
        c = int((sx - self.offset_x) // self.cell_size)
        r = int((sy - self.offset_y) // self.cell_size)
        return r, c

    def set_zoom(self, zoom: float, center_x: float = None, center_y: float = None):
        old_zoom = self.cell_size
        if center_x is not None and center_y is not None:
            world_c = (center_x - self.offset_x) / old_zoom
            world_r = (center_y - self.offset_y) / old_zoom
        else:
            world_c = world_r = 0.0

        self.cell_size = max(2.0, min(60.0, zoom))

        if center_x is not None and center_y is not None:
            self.offset_x = center_x - world_c * self.cell_size
            self.offset_y = center_y - world_r * self.cell_size

    def pan(self, dx: float, dy: float):
        self.offset_x += dx
        self.offset_y += dy

    def clear(self):
        self.canvas.delete("all")
        self._cell_rects = []

    def draw_grid(self, grid: Grid) -> None:
        self.clear()
        print(grid)
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0
        h = int(self.canvas.winfo_height())
        w = int(self.canvas.winfo_width())
        self.canvas.create_rectangle(0, 0, w, h, fill="#ffffff", outline="")

        for r in range(rows):
            for c in range(cols):
                x1, y1, x2, y2 = self.world_to_screen(r, c)
                if x2 < 0 or y2 < 0 or x1 > w or y1 > h:
                    continue
                color = "#000000" if grid[r][c] else "#ffffff"
                rect_id = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="#cccccc")
                self._cell_rects.append(rect_id)