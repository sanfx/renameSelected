import maya.OpenMayaUI as mui

import sip
from PySide import QtGui,QtCore,uic

import maya.cmds as cmds
import maya.mel as mel

def getMayaWindow():
    #'get the maya main window as QMainWindow instance'
    ptr =mui.MQtUtil.mainWindow()
    return sip.wrapinstance(long(ptr),QtCore.QObject)

#userProfile =mel.eval('getenv("USERPROFILE")')
#mayaVersion="2012-x64"
uifile=("/media/Archives&Backup/san_documents/Dropbox/Research_Study/cgcircuit/QtDesigner_RenameSelectedNode/renameSelNode.ui")
form_class, base_class= uic.loadUiType(uifile)

class RenameSelNodeUI(form_class,base_class):
    def __init__(self,parent=getMayaWindow()):
        super(RenameSelNodeUI,self).__init__(parent)
        self.setupUi(self)
        #method
        self.connectSignals()
    
    def connectSignals(self):
        """Connect all the UI signals"""
        self.connect(self.clear_btn,QtCore.SIGNAL('released()'),self.clearTextField)
        self.connect(self.rename_btn,QtCore.SIGNAL('released()'),self.renameNode)
    
    def clearTextField(self):
        """Clears the text field"""
        self.nodeName_txt.clear()
        
    def renameNode(self):
        """Renames the selected node using the content of the text field
        if multiple nodes are selected, only the first node will be renamed"""
        
        #--- get the text from the UI
        currentText = str(self.nodeName_txt.text())
        
        #---grab the selection in maya
        selection= cmds.ls(sl=1)
        
        #--- rename the maya node
        if selection is not None:
            if len(selection) > 0:
                if currentText != "":
                    cmds.rename(selection[0],currentText)
                    
        
        
        
def runUI():
    global app
    global win
    app=QtGui.qApp
    win = RenameSelNodeUI()
    win.show()
    
    "Connect all the UI signals"""
        self.connect(self.clear_btn,QtCore.SIGNAL('released()'),self.clearTextField)
        self.connect(self.rename_btn,QtCore.SIGNAL('released()'),self.renameNode)
    
    def clearTextField(self):
        """Clears the text field"""
        self.nodeName_txt.clear()
        
    def renameNode(self):
        """Renames the selected node using the content of the text field
        if multiple nodes are selected, only the first node will be renamed"""
        
        #--- get the text from the UI
        currentText = str(self.nodeName_txt.text())
        
        #---grab the selection in maya
        selection= cmds.ls(sl=1)
        
        #--- rename the maya node
        if selection is not None:
            if len(selection) > 0:
                if currentText != "":
                    cmds.rename(selection[0],currentText)
                    
      
def runUI():
    global app
    global win
    app=QtGui.qApp
    win = RenameSelNodeUI()
    win.show()
    
    