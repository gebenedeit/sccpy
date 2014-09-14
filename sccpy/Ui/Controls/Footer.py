from PyQt4.QtGui import QWidget

class Footer(QWidget):
    
    def __init__(self):
        QWidget.__init__(self)
        self.__InitUi()
        
    def __InitUi(self):
        self.setFixedHeight(150)