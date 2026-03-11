from tkinter import *
from tkinter import ttk

class MainWindow():
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List Manager")
        self.root.geometry("860x860")
        self.mainframe = ttk.Frame(root, padding=(6,6,12,12))
        self.icon = PhotoImage(file='') # for window icon
        #self.window.iconphoto(True,icon)
        self.root.config(background="#5b6961")
    
    def widgets(self):
        self.testlabel = Label(root, text="Silksong")
        self.testlabel.pack()
        self.button = ttk.Button(self.mainframe)
