import tkinter as tk

from gui_manager import GUIManager

def main():
    root = tk.Tk()
    root.geometry("1000x850")
    manager = GUIManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()