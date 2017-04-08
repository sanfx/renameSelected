import maya.OpenMayaUI as mu  
from PySide_loadUiType import loadUiType
import sip
from PySide import QtGui,QtCore
import maya.cmds as cmds
import maya.mel as mel
import shiboken
 
 
def wrapinstance(ptr, base=None):
		"""
		Utility to convert a pointer to a Qt class instance (PySide/PyQt compatible)
		:type base: QtGui.QWidget
		:return: QWidget or subclass instance
		:rtype: QtGui.QWidget
		"""
		if ptr is None:
				return None
		ptr = long(ptr) #Ensure type
		if globals().has_key('shiboken'):
				if base is None:
						qObj = shiboken.wrapInstance(long(ptr), QtCore.QObject)
						metaObj = qObj.metaObject()
						cls = metaObj.className()
						superCls = metaObj.superClass().className()
						if hasattr(QtGui, cls):
								base = getattr(QtGui, cls)
						elif hasattr(QtGui, superCls):
								base = getattr(QtGui, superCls)
						else:
								base = QtGui.QWidget
				return shiboken.wrapInstance(long(ptr), base)
		elif globals().has_key('sip'):
				base = QtCore.QObject
				return sip.wrapinstance(long(ptr), base)
		else:
				return None
		
def getMayaWindow():
		#'get the maya main window as QMainWindow instance'
		ptr =mui.MQtUtil.mainWindow()
		return wrapinstance(long(ptr))
 

form_class, base_class = loadUiType("renameSelNode.ui")  
 
class RenameSelNodeUI(form_class,base_class):
		
		def __init__(self, parent=getMayaWindow()):
 
				super(RenameSelNodeUI,self).__init__(parent)
				self.setupUi(self)
				#method
				self.connectSignals()
		
		def connectSignals(self):
				""" Connect all the UI signals
				"""
				self.connect(self.clear_btn,QtCore.SIGNAL('released()'),self.clearTextField)
				self.connect(self.rename_btn,QtCore.SIGNAL('released()'),self.renameNode)
		
		def clearTextField(self):
				"""	Clears the text field
				"""
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