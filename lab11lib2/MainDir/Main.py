import tkinter as tk
from lab11lib2.classes.DBInterface import DBInterface
from lab11lib2.classes.GUI import GUI

if __name__ == '__main__':
    DBInterface = DBInterface()
    root = tk.Tk()
    GUI = GUI(root)

    root.mainloop()
