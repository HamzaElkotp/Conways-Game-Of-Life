# pages/simulation_page.py
import tkinter as tk
from tkinter import ttk

from typing import Tuple

from rendering.grid_renderer import GridRenderer

Grid = Tuple[Tuple[int]]
EngineName = str

from engines.functional_engine import functional_next_generation
from engines.imperative_engine import imperative_next_generation


class SimulationPage:
    def __init__(self, manager, engine: EngineName, initial_grid: Grid):
        self.manager = manager
        self.engine = engine
        self.grid = initial_grid
        self.root = manager.root
        self.frame = ttk.Frame(self.root)
        # top controls
        top = ttk.Frame(self.frame)
        top.pack(side="top", fill="x")
        self.btn_pause = ttk.Button(top, text="Pause", command=self.toggle_pause)
        self.btn_pause.pack(side="left")
        self.btn_restart = ttk.Button(top, text="Restart (to Editor)", command=self.restart_to_editor)
        self.btn_restart.pack(side="left", padx=(8,0))
        ttk.Label(top, text=f"Engine: {engine}").pack(side="right")
        # canvas
        self.canvas = tk.Canvas(self.frame, background="#fff")
        self.canvas.pack(side="top", fill="both", expand=True)

        # renderer
        self.renderer = GridRenderer(self.canvas, cell_size=26.0)
        self.renderer.offset_x = 10.0
        self.renderer.offset_y = 10.0

        # event handling (disable left-click editing)
        self.canvas.bind("<ButtonPress-1>", lambda e: None)
        self.canvas.bind("<ButtonPress-3>", self.on_right_press)
        self.canvas.bind("<B3-Motion>", self.on_right_drag)
        self.canvas.bind("<MouseWheel>", self.on_mouse_wheel)
        self.canvas.bind("<Button-4>", self.on_mouse_wheel)
        self.canvas.bind("<Button-5>", self.on_mouse_wheel)
        self.canvas.bind("<Configure>", lambda e: self.redraw())

        self._pan_start = None
        self.running = True
        self.speed_ms = 500

        # start timer loop
        self._after_id = None
        self.schedule_next()

    def toggle_pause(self):
        self.running = not self.running
        self.btn_pause.config(text="Resume" if not self.running else "Pause")
        if self.running:
            self.schedule_next()
        else:
            if self._after_id:
                self.canvas.after_cancel(self._after_id)
                self._after_id = None

    def restart_to_editor(self):
        # convert current grid to editable by passing its size
        n = len(self.grid)
        self.manager.switch_to_editor(self.engine, n)

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
        if hasattr(event, "delta"):
            delta = event.delta
        else:
            delta = 120 if event.num == 4 else -120
        factor = 1.1 if delta > 0 else 0.9
        new_zoom = self.renderer.cell_size * factor
        self.renderer.set_zoom(new_zoom, center_x=event.x, center_y=event.y)
        self.redraw()

    def schedule_next(self):
        if self.running:
            self._after_id = self.canvas.after(self.speed_ms, self._tick)

    def _tick(self):
        # compute next generation using selected engine
        if self.engine == "functional":
            self.grid = functional_next_generation(self.grid)
        else:
            self.grid = imperative_next_generation(self.grid)
        self.redraw()
        self.schedule_next()

    def redraw(self):
        print("from simpage")
        print(self.grid)
        self.renderer.draw_grid(self.grid)

    def destroy(self):
        if self._after_id:
            self.canvas.after_cancel(self._after_id)
        self.frame.destroy()
