# gui_manager.py
from typing import Type
from typing import Tuple
import tkinter as tk
from typing import Tuple

from pages.editor_page import EditorPage
from pages.engine_selection_page import EngineSelectionPage
from pages.simulation_page import SimulationPage

Grid = Tuple[Tuple[int, ...], ...]
EngineName = str

class GUIManager:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.current_page = None
        self.root.title("Conway's Game of Life")
        self.switch_to_engine_selection()

    def clear_current(self):
        if self.current_page:
            self.current_page.destroy()
            self.current_page = None

    def switch_to_engine_selection(self):
        self.clear_current()
        page = EngineSelectionPage(self)
        page.frame.pack(fill="both", expand=True)
        self.current_page = page

    def switch_to_editor(self, engine: EngineName, grid_size: int):
        self.clear_current()
        page = EditorPage(self, engine, grid_size)
        page.frame.pack(fill="both", expand=True)
        self.current_page = page

    def switch_to_simulation(self, engine: EngineName, initial_grid: Grid):
        self.clear_current()
        page = SimulationPage(self, engine, initial_grid)
        page.frame.pack(fill="both", expand=True)
        self.current_page = page