# pages/editor_page.py
from typing import List, Tuple
import tkinter as tk
from tkinter import ttk

from rendering.grid_renderer import GridRenderer

Grid = Tuple[Tuple[int, ...], ...]
EngineName = str

class EditorPage:
    def __init__(self, manager, engine: EngineName, grid_size: int):
        self.manager = manager
        self.engine = engine
        self.grid_size = grid_size
        self.root = manager.root
        self.frame = ttk.Frame(self.root)
        self.canvas = tk.Canvas(self.frame, background="#ffffff")
        self.canvas.pack(side="left", fill="both", expand=True)
        sidebar = ttk.Frame(self.frame, width=220)
        sidebar.pack(side="right", fill="y")
        ttk.Label(sidebar, text=f"Engine: {engine}").pack(anchor="nw", pady=(6,6))
        ttk.Label(sidebar, text=f"Grid size: {grid_size} × {grid_size}").pack(anchor="nw", pady=(0,6))
        ttk.Button(sidebar, text="Start Simulation", command=self.on_start).pack(anchor="nw", pady=(6,6))
        ttk.Button(sidebar, text="Back", command=self.on_back).pack(anchor="nw")

        # initialize mutable editor buffer as lists for editing ease
        self._rows = grid_size
        self._cols = grid_size
        self.buffer: List[List[int]] = [[0]*self._cols for _ in range(self._rows)]

        # renderer
        self.renderer = GridRenderer(self.canvas, cell_size=26.0)

        # event handling
        self.canvas.bind("<Button-1>", self.on_left_click)   # toggle
        self.canvas.bind("<ButtonPress-3>", self.on_right_press)
        self.canvas.bind("<B3-Motion>", self.on_right_drag)
        self.canvas.bind("<MouseWheel>", self.on_mouse_wheel)  # Windows
        self.canvas.bind("<Button-4>", self.on_mouse_wheel)    # Linux scroll up
        self.canvas.bind("<Button-5>", self.on_mouse_wheel)    # Linux scroll down
        # redraw when resized
        self.canvas.bind("<Configure>", lambda e: self.redraw())

        # pan tracking
        self._pan_start = None

        # initial draw
        self.redraw()

    def on_left_click(self, event):
        # toggle cell only in editor
        r, c = self.renderer.screen_to_grid(event.x, event.y)
        if 0 <= r < self._rows and 0 <= c < self._cols:
            self.buffer[r][c] = 1 - self.buffer[r][c]
            self.redraw()

    def on_right_press(self, event):
        self._pan_start = (event.x, event.y)

    def on_right_drag(self, event):
        if self._pan_start is None:
            return
        sx, sy = self._pan_start
        dx = event.x - sx
        dy = event.y - sy
        self.renderer.pan(dx, dy)
        self._pan_start = (event.x, event.y)
        self.redraw()

    def on_mouse_wheel(self, event):
        # zoom in/out; event.delta is platform dependent
        if hasattr(event, "delta"):
            delta = event.delta
        else:
            # linux Button-4/5
            delta = 120 if event.num == 4 else -120

        factor = 1.1 if delta > 0 else 0.9
        new_zoom = self.renderer.cell_size * factor
        self.renderer.set_zoom(new_zoom, center_x=event.x, center_y=event.y)
        self.redraw()

    def on_start(self):
        # convert buffer to immutable grid
        initial_grid: Grid = tuple(tuple(row) for row in self.buffer)
        self.manager.switch_to_simulation(self.engine, initial_grid)

    def on_back(self):
        self.manager.switch_to_engine_selection()

    def redraw(self):
        self.renderer.draw_grid(tuple(tuple(row) for row in self.buffer))

    def get_configured_grid(self) -> Grid:
        return tuple(tuple(row) for row in self.buffer)

    def destroy(self):
        self.frame.destroy()
