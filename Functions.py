import sys, json, configparser, pythoncom
from os import path, mkdir, walk
from pathlib import Path
from configparser import ExtendedInterpolation

DEBUG=True
Version="v1.0.0.1"

if not DEBUG:
    exe_dir = str(path.dirname(sys.executable))
else:
    exe_dir = str(Path(__file__).parents[0])

settings_dir = ''.join([exe_dir, '\Settings\\'])

def SearchFile(self, filename):
    pythoncom.CoInitialize()
    data = dict()
    count = 0
    self.progressbar['mode'] = 'indeterminate'
    print(path.abspath('.').split(path.sep)[0]+path.sep)
    for root,dirs,file in walk(path.abspath('.').split(path.sep)[0]+path.sep):
        if str(filename) in root:
            print(root)
            print(dirs)
            print(file)
            count += 1
            data[count] = {'filename': file, 'path':root}
    
    self.progressbar['mode'] = 'determinate'
    self.progressbar['maximum'] = count
    count = 0
    for i in data:
        count+=1
        self.progressbar['value'] = count
        self.tree.insert('', 'end', values=(data[count]['filename'], data[count]['path']))
    self.progressbar['value'] = 0
    

def getSettings(self):
    self.parser = configparser.RawConfigParser(interpolation=ExtendedInterpolation(),
                                               inline_comment_prefixes=('#', ';'),
                                               comment_prefixes=('#', ';'))
    self.parser.read(settings_dir + "Settings.ini")
    if self.parser.has_section('Settings'):
        self.fileType = self.parser.get('Settings', 'type').replace("\'", "").replace("\"","")
        self.startDir = self.parser.get('Settings', 'directory').replace("\'", "").replace("\"","")
    if self.parser.has_section('Config'):    
        self.load.set(eval(self.parser.get('Config', 'AutoLoad').replace("\'", "")))

def saveSettings(self):
    self.parser = configparser.RawConfigParser(interpolation=ExtendedInterpolation(),
                                               inline_comment_prefixes=('#', ';'),
                                               comment_prefixes=('#', ';'))
    self.parser.read(settings_dir + "Settings.ini")
    self.parser['Config'] = {}
    self.parser['Config']['AutoLoad'] = ''.join(["'",str(self.load.get()),"'"])

    self.parser['Settings'] = {}
    self.parser['Settings']['type'] = ''.join(["'",str(self.fileType),"'"])
    self.parser['Settings']['directory'] = ''.join(["'",str(self.startDir),"'"])

    with open(settings_dir + "Settings.ini", "w") as w:
        self.parser.write(w)

def updateSettings(data, title, option):
    parser = configparser.ConfigParser(interpolation=ExtendedInterpolation(),
                                          inline_comment_prefixes=('#', ';'),
                                          comment_prefixes=('#', ';'))
    parser.read(settings_dir + "Settings.ini")
    if not parser.has_section(title):
        parser.add_section(title)
    parser.set(title, option, ''.join(["\'",str(data),"\'"]))
    with open(settings_dir + "Settings.ini", "w+") as w:
        parser.write(w)