# gui_manager.py
from typing import Type

class GUIManager:
    def __init__(self) -> None:
        ...
    
    def switch_page(self, page_class: Type) -> None:
        ...
