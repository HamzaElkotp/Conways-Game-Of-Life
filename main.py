import tkinter as tk
from tkinter import ttk

from gui_manager import GUIManager

def main():
    root = tk.Tk()
    root.geometry("900x650")
    manager = GUIManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()