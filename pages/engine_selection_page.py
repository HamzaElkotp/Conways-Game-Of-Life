import tkinter as tk
from tkinter import ttk

class EngineSelectionPage:
    def __init__(self, manager):
        self.manager = manager
        self.root = manager.root
        self.frame = ttk.Frame(self.root, padding=12)

        # engine selection
        self.engine_var = tk.StringVar(value="functional")
        ttk.Label(self.frame, text="Choose engine:").pack(anchor="w")
        ttk.Radiobutton(self.frame, text="Functional", variable=self.engine_var, value="functional").pack(anchor="w")
        ttk.Radiobutton(self.frame, text="Imperative", variable=self.engine_var, value="imperative").pack(anchor="w")

        # grid size
        self.size_var = tk.IntVar(value=32)
        size_frame = ttk.Frame(self.frame)
        size_frame.pack(anchor="w", pady=(8, 8))
        ttk.Label(size_frame, text="Grid size (N × N):").pack(side="left")
        ttk.Spinbox(size_frame, from_=10, to=200, textvariable=self.size_var, width=6).pack(side="left")

        # continue button
        btn = ttk.Button(self.frame, text="Continue to Editor", command=self.on_continue)
        btn.pack(pady=(12, 0))

    def on_continue(self):
        engine = self.engine_var.get()
        grid_size = int(self.size_var.get())
        self.manager.switch_to_editor(engine, grid_size)

    def destroy(self):
        self.frame.destroy()