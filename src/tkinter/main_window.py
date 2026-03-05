from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Todo List Manager")

mainframe = ttk.Frame(root, padding=(6,6,12,12))

mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

button = ttk.Button(mainframe)