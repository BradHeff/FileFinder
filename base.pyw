import tkinter
import Functions as f
import GUI
    
    
class FileFinder():
    def __init__(self, parent):
        super(FileFinder, self).__init__()
        
        GUI.Window(self)



if __name__ == '__main__':
    root = tkinter.Tk()
    app = FileFinder(root)
    root.mainloop()
        