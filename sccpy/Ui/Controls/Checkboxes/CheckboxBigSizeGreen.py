from PyQt4.QtGui import QCheckBox

class CheckboxBigSizeGreen(QCheckBox):
	
	def __init__(self):
		QCheckBox.__init__(self)
		self.__InitUi()
		
	def __InitUi(self):
		self.setFixedSize(60,30)
		self.setStyleSheet("QCheckBox {outline: 0;}"
						"QCheckBox::indicator {width: 60px; height: 30px;}"
						"QCheckBox::indicator:checked {image: url(Ui/Controls/Checkboxes/On.png);}"
						"QCheckBox::indicator:unchecked {image: url(Ui/Controls/Checkboxes/Off.png);}")