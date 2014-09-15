from PyQt4.QtGui import QLineEdit
from Ui.Colors import COLOR_WIDGET_11, COLOR_OUTLINE_6, COLOR_FONT_4

class LineEditStandard(QLineEdit):
    
    def __init__(self):
        QLineEdit.__init__(self)
        self.__InitUi()
        
    def __InitUi(self):
        self.setFixedHeight(30)
        self.setFixedWidth(300)
        self.setStyleSheet("QLineEdit {"
                           "background-color: rgb("+str(COLOR_WIDGET_11[0])+","+str(COLOR_WIDGET_11[1])+","+str(COLOR_WIDGET_11[2])+");"
                           "border: 2px solid rgb("+str(COLOR_OUTLINE_6[0])+","+str(COLOR_OUTLINE_6[0])+","+str(COLOR_OUTLINE_6[0])+");"
                           "border-radius: 3px;"
                           "color: rgb("+str(COLOR_FONT_4[0])+","+str(COLOR_FONT_4[0])+","+str(COLOR_FONT_4[0])+");"
                           "font-size: 20px;"
                           "font-weight: bold;"
                           "}")