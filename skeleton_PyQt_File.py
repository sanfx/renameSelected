import maya.OpenMayaUI as mui

import sip
from PyQt4 import QtGui,QtCore,uic

import maya.cmds as cmds
import maya.mel as mel

def getMayaWindow():
    #'get the maya main window as QMainWindow instance'
    ptr =mui.MQtUtil.mainWindow()
    return sip.wrapinstance(long(ptr),QtCore.QObject)

userProfile =mel.eval('getenv("USERPROFILE")')
mayaVersion="2012-x64"
uifile=("/media/Archives&Backup/san_documents/Dropbox/Research_Study/cgcircuit/QtDesigner_RenameSelectedNode/renameSelNode.ui")
form_class, base_class= uic.loadUiType(uifile)

class MyUI(form_class,base_class):
    def __init__(self,parent=getMayaWindow()):
        super(MyUI,self).__init__(parent)
        self.setupUi(self)
        #method
        self.connectSignals()
    
    def connectSignals(self):
        """Connect all the UI signals"""
        print "Connect Signals"
        
        
def runUI():
    gloabl app
    global win
    app=QtGui.qApp
    win = MyUI()
    win.show()
    
    