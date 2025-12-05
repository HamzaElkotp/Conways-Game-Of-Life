# controllers/simulation_controller.py
from typing import Tuple

Grid = Tuple[Tuple[int, ...], ...]

class SimulationController:
    def __init__(self, initial_grid: Grid, engine: str) -> None:
        ...
    
    def next_step(self) -> Grid:
        ...
    
    def set_speed(self, speed: float) -> None:
        ...
