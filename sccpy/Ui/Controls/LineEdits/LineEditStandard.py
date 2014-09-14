from PyQt4.QtGui import QLineEdit

class LineEditStandard(QLineEdit):
    
    def __init__(self):
        QLineEdit.__init__(self)
        self.__InitUi()
        
    def __InitUi(self):
        self.setFixedHeight(30)
        self.setFixedWidth(300)