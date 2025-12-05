# pages/editor_page.py
from typing import Tuple

Grid = Tuple[Tuple[int, ...], ...]

class EditorPage:
    def __init__(self, gui_manager, grid_size: int, engine: str) -> None:
        ...
    
    def draw(self) -> None:
        ...
    
    def handle_event(self, event) -> None:
        ...
    
    def get_configured_grid(self) -> Grid:
        ...
