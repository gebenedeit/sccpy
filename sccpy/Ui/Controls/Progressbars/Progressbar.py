from PyQt4.QtGui import QProgressBar
from Ui.Colors import COLOR_WIDGET_10, COLOR_OUTLINE_1, COLOR_FONT_7

class Progressbar(QProgressBar):

    def __init__(self):
        QProgressBar.__init__(self)
        self.__InitUi()
        
    def __InitUi(self):
        self.setFixedHeight(50)
        self.setMinimum(0)
        self.setMaximum(100)
        self.setTextVisible(False)
        self.setStyleSheet(
            "QProgressBar {border: 2px solid rgb("+str(COLOR_OUTLINE_1[0])+","+str(COLOR_OUTLINE_1[1])+","+str(COLOR_OUTLINE_1[2])+");"
            "border-radius: 5px; background-color: rgb("+str(COLOR_WIDGET_10[0])+","+str(COLOR_WIDGET_10[1])+","+str(COLOR_WIDGET_10[2])+");} "
            "QProgressBar::chunk{ background-color: rgb("+str(COLOR_FONT_7[0])+", "+str(COLOR_FONT_7[1])+","+str(COLOR_FONT_7[2])+"); width: 10px;}"
            );