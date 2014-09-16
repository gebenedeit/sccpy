from PyQt4.QtGui import QWidget
from Ui.Colors import COLOR_WIDGET_3
from Ui.Helper import SetWidgetBackgroundColor

class Friends(QWidget):
    
    def __init__(self):
        QWidget.__init__(self)
        self.__InitUi()
        
    def __InitUi(self):
        SetWidgetBackgroundColor(COLOR_WIDGET_3, self)