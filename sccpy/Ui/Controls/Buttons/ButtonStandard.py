from PyQt4.QtGui import QPushButton
from Ui.Colors import COLOR_WIDGET_10, COLOR_FONT_7, COLOR_OUTLINE_5

class ButtonStandard(QPushButton):
    
    def __init__(self, strText=""):
        QPushButton.__init__(self)
        self.__InitUi(strText)
        
    def __InitUi(self, strText):
        self.setText(strText)
        self.setFixedHeight(30)
        self.setStyleSheet(
            "QPushButton {"
            "background: rgb("+str(COLOR_WIDGET_10[0])+","+str(COLOR_WIDGET_10[1])+","+str(COLOR_WIDGET_10[2])+"); "
            "font-weight: bold; "
            "color: rgb("+str(COLOR_FONT_7[0])+","+str(COLOR_FONT_7[1])+","+str(COLOR_FONT_7[2])+"); "
            "font-size: 20px;"
            "outline: 0;"
            "border-radius: 3px;"
            "border: 2px solid rgb("+str(COLOR_OUTLINE_5[0])+","+str(COLOR_OUTLINE_5[1])+","+str(COLOR_OUTLINE_5[2])+");}"
            )