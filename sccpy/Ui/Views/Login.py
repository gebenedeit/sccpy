from PyQt4.QtGui import QWidget, QSizePolicy
from Ui.Helper import SetWidgetBackgroundColor
from Ui.Colors import COLOR_WIDGET_7

class Login(QWidget):
    
    def __init__(self):
        QWidget.__init__(self)
        self.__InitUi()
    
    def __InitUi(self):
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        SetWidgetBackgroundColor(COLOR_WIDGET_7, self)