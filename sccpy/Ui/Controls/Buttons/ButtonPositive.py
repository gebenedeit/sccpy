from PyQt4.QtGui import QPushButton
from Ui.Colors import COLOR_WIDGET_12, COLOR_FONT_8, COLOR_OUTLINE_7

class ButtonPositive(QPushButton):
    
    def __init__(self, strText=""):
        QPushButton.__init__(self)
        self.__InitUi(strText)
        
    def __InitUi(self, strText):
        self.setText(strText)
        self.setFixedHeight(30)
        self.setFixedWidth(120)
        self.setStyleSheet(
            "QPushButton {"
            "background: rgb("+str(COLOR_WIDGET_12[0])+","+str(COLOR_WIDGET_12[1])+","+str(COLOR_WIDGET_12[2])+"); "
            "font-weight: bold; "
            "color: rgb("+str(COLOR_FONT_8[0])+","+str(COLOR_FONT_8[1])+","+str(COLOR_FONT_8[2])+"); "
            "font-size: 20px;"
            "outline: 0;"
            "border-radius: 3px;"
            "border: 2px solid rgb("+str(COLOR_OUTLINE_7[0])+","+str(COLOR_OUTLINE_7[1])+","+str(COLOR_OUTLINE_7[2])+");}"
            )