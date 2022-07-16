import datetime
from threading import Thread
import tkinter
import Functions as f
import GUI as w
    
class FileFinder(tkinter.Tk):
    def __init__(self, parent):
        super(FileFinder, self).__init__()
        global root
        self.parent = parent
        self.W,self.H = 665,280

        self.selItem = []

        self.fileType = ""
        self.startDir = ""
        
        self.load = tkinter.BooleanVar(self, False)

        if not f.path.exists(f.settings_dir):
            f.mkdir(f.settings_dir)
        else:
            if f.path.isfile(f.settings_dir + "Settings.ini"):
                f.getSettings(self)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width/2 - self.W / 2)
        center_y = int(screen_height/2 - self.H / 2)
        self.geometry(f'{self.W}x{self.H}+{center_x}+{center_y}')
        self.resizable(0, 0)
        self.attributes("-fullscreen",False)
        
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        self.date = date.strftime("%Y")
        
        w.Window(self)
        self.title(''.join(["DCM Deep Search Tool v", f.Version[4:f.Version.__len__()]]))

    def SearchFile(self):
        if not self.search.get().__len__() <= 0:
            self.tree.delete(*self.tree.get_children())
            t = Thread(None, target=f.SearchFile, args=(self, self.search.get()))
            t.daemon = True
            t.start()

    def selectItem(self, widget):
        curItem = self.tree.focus()
        self.selItem = self.tree.item(curItem)['values']

    def setLoad(self):
        if f.path.isfile(f.settings_dir + "Settings.ini"):
            self.parser = f.configparser.RawConfigParser(interpolation=f.ExtendedInterpolation(),
                                                         inline_comment_prefixes=('#', ';'),
                                                         comment_prefixes=('#', ';'))
            self.parser.read(f.settings_dir + "Settings.ini")
            self.parser.set('Config','AutoLoad',''.join(["'",str(self.load.get()),"'"]))
            with open(f.settings_dir + "Settings.ini", "w+") as w:
                self.parser.write(w)
        else:
            f.saveSettings(self)


if __name__ == '__main__':
    global root
    root = tkinter.Tk
    app = FileFinder(root)
    root.mainloop(app)
        