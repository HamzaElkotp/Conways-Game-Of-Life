# pages/simulation_page.py
from typing import Tuple

Grid = Tuple[Tuple[int, ...], ...]

class SimulationPage:
    def __init__(self, gui_manager, initial_grid: Grid, engine: str) -> None:
        ...
    
    def draw(self) -> None:
        ...
    
    def handle_event(self, event) -> None:
        ...
    
    def update_simulation(self) -> None:
        ...
