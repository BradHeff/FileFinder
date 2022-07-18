from tkinter import *
from tkinter import ttk
from tkinter.filedialog import FileDialog

from numpy import pad
from Functions import Version, saveSettings
from variable import icon
import tkinter

def Window(self):
    
    photo = tkinter.PhotoImage(data=icon)
    self.wm_iconphoto(False, photo)

    menubar = Menu(self, activebackground='white', activeforeground='black')
    self.file = Menu(menubar, tearoff=0)
    self.file.add_checkbutton(label="Auto Load", variable=self.load, command=self.setLoad)
    self.file.add_command(label="Save", command=lambda: saveSettings(self))
    self.file.add_separator()
    self.file.add_command(label="Exit", command=self.quit)
    
    menubar.add_cascade(label="File", menu=self.file)
    self.config(menu=menubar)

    self.columnconfigure(1, weight=1)    
    self.rowconfigure(2, weight=1)
    
    lbl_title = Label(self, text="Deep File Search Tool")
    lbl_title.grid(sticky='new', columnspan=3, padx=10, pady=5)

    lbl_search = Label(self, text="File Search: ")
    lbl_search.grid(sticky='nw', column=0, row=1, padx=10, pady=5)
    self.search = Entry(self, border=1, borderwidth=2, width=40)
    self.search.grid(sticky='nsew', column=1, row=1, pady=5)
    self.search_btn = Button(self, text="Search", width=20, command=self.SearchFile)
    self.search_btn.grid(sticky='n', column=2, row=1, padx=10, pady=5)

    lbl_frame = LabelFrame(self, text="Search Results", font=self.font)
    lbl_frame.grid(sticky='nsew', columnspan=3, row=2, padx=10, pady=5)

    lbl_frame.columnconfigure(1, weight=1)
    lbl_frame.rowconfigure(0, weight=1)

    self.tree = ttk.Treeview(lbl_frame, column=("c1", "c2"), show='headings')    
    self.tree.column("# 1", anchor="w",width=20)
    self.tree.heading("# 1", text="FILENAME")
    self.tree.column("# 2", anchor="w")
    self.tree.heading("# 2", text="PATH")
    self.tree.bind('<ButtonRelease-1>', self.selectItem)
    self.tree.grid(sticky='nsew', columnspan=3, row=0, padx=20, pady=10)

    scrollbar = Scrollbar(lbl_frame)
    scrollbar.config(command=self.tree.yview)
    scrollbar.grid(sticky='nse', rowspan=3, column=2, row=0)

    self.tree.config(yscrollcommand=scrollbar.set)

    lbl_stat = Label(self, text="Searching :")
    lbl_stat.grid(sticky='we', column=0, row=3)
    
    self.lbl_status = Label(self, text="Idle...")
    self.lbl_status.grid(sticky='w', column=1, columnspan=2, row=3, padx=10)

    self.progressbar = ttk.Progressbar(self, maximum=100, orient=HORIZONTAL)    
    self.progressbar.grid(sticky='ews', columnspan=3, row=4)