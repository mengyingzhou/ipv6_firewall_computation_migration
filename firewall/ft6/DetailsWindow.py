from details import Ui_Dialog
from PyQt4.QtGui import QDialog
class DetailsWindow(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		
	def addDetail(self, item):
		
		self.ui.listWidget.addItem(item)

	def show(self):
		self.exec_()
