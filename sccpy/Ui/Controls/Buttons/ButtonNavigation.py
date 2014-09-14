from PyQt4.QtGui import QPushButton
from Ui.Colors import COLOR_FONT_3, COLOR_FONT_7, COLOR_WIDGET_5, COLOR_WIDGET_7

class ButtonNavigation(QPushButton):
    
    def __init__(self, strText=""):
        QPushButton.__init__(self)
        self.__InitUi(strText)
        
    def __InitUi(self, strText=""):
        self.setText(strText)
        self.setFixedHeight(90)
        self.setStyleSheet(
            "QPushButton {border: none; "
            "background: rgb("+str(COLOR_WIDGET_5[0])+","+str(COLOR_WIDGET_5[1])+","+str(COLOR_WIDGET_5[2])+"); "
            "text-align: left; "
            "padding-left: 30px; "
            "font-weight: bold; "
            "color: rgb("+str(COLOR_FONT_3[0])+","+str(COLOR_FONT_3[1])+","+str(COLOR_FONT_3[2])+"); "
            "font-size: 30px;"
            "outline: 0;} "
            "QPushButton:hover {border: none; "
            "background: rgb("+str(COLOR_WIDGET_7[0])+","+str(COLOR_WIDGET_7[1])+","+str(COLOR_WIDGET_7[2])+");"
            "text-align: left; "
            "padding-left: 30px;"
            "font-weight: bold; "
            "color: rgb("+str(COLOR_FONT_7[0])+","+str(COLOR_FONT_7[1])+","+str(COLOR_FONT_7[2])+"); "
            "font-size: 30px; "
            "outline: 0;}"
            );