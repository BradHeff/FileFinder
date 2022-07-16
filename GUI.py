from tkinter import *
from tkinter import ttk
from Functions import Version, saveSettings
import tkinter


def Window(self):
    
    # photo = tkinter.PhotoImage(data=icon)
    # self.wm_iconphoto(False, photo)

    menubar = Menu(self, activebackground='white', activeforeground='black')
    self.file = Menu(menubar, tearoff=0)
    self.file.add_checkbutton(label="Auto Load", variable=self.load, command=self.setLoad)
    self.file.add_command(label="Save", command=lambda: saveSettings(self))
    self.file.add_separator()
    self.file.add_command(label="Exit", command=self.quit)
    
    menubar.add_cascade(label="File", menu=self.file)
    self.config(menu=menubar)