from configparser import ConfigParser
from xml.dom import minidom

import re

class ApplicationConfigManager(object):
    conf_parser     = None

    working_path    = None
    meshlist_path   = None

    def __init__(self):
        super().__init__()

    def Initialize(self) -> None:
        self.conf_parser = ConfigParser()
        self.conf_parser.read("config.ini")
        self.working_path = self.conf_parser.get('PATHS', 'working_path')
        self.meshlist_path = self.conf_parser.get('PATHS', 'meshlist_path')

    def getWorkPath(self):
        return self.working_path
    
    def getMeshlistPath(self):
        return self.meshlist_path

class DAE_Parser(object):
    dae         = None
    matlist     = None

    parselist   = []

    def __init__(self, dae):
        self.load(dae)
        super().__init__()
    
    def load(self, dae):
        self.dae = dae

    def parse(self):
        try:
            self.xmldae = minidom.parse(self.dae)
            self.matlist = self.xmldae.getElementsByTagName('init_from')
            for i in self.matlist:
                if re.match(r'.[A-z0-9]+$', i.firstChild.nodeValue):
                    pass
            else:
                regex_tmp = re.search('(?=static_objects)\S+', str(i.firstChild.nodeValue))
                try:
                    self.parselist.append(regex_tmp.group(0))
                except AttributeError:
                    err = open('out/errorlog.txt', 'a')
                    err.writelines('[INVALID ATTRIBUTE CONTENT]: ' + i.firstChild.nodeValue + '\n')
                    err.close()
        except PermissionError:
            err = open('out/errorlog.txt', 'a')
            err.writelines('[INVALID PATH]: ' + self.dae + '\n')
            err.close()
                
    
    def log(self):
        with open('out/' + 'matlist.txt', 'a') as self.file:
            for line in self.parselist:
                self.file.write(line + '\n')

    


    