from PyQt4.QtGui import QComboBox, QListView
from Ui.Colors import COLOR_WIDGET_11, COLOR_OUTLINE_6, COLOR_FONT_4

class ComboboxStandard(QComboBox):
    
    def __init__(self):
        QComboBox.__init__(self)
        self.__InitUi()
        
    def __InitUi(self):
        self.setFixedHeight(30)
        self.setStyleSheet("QComboBox {"
                               "background: rgb("+str(COLOR_WIDGET_11[0])+","+str(COLOR_WIDGET_11[1])+","+str(COLOR_WIDGET_11[2])+");"
                               "border: 2px solid rgb("+str(COLOR_OUTLINE_6[0])+","+str(COLOR_OUTLINE_6[1])+","+str(COLOR_OUTLINE_6[2])+");"
                               "color: rgb("+str(COLOR_FONT_4[0])+","+str(COLOR_FONT_4[1])+","+str(COLOR_FONT_4[2])+");"
                               "font-size: 20px;"
                               "font-weight: bold;"
                               "border-radius: 3px"
                           "}"
                           "QComboBox::drop-down {"
                               "border-top: none;"
                               "border-bottom: none;"
                               "border-right: none;"
                               "color: green;"
                               "margin: 5px;"
                               "image: url(Ui/Controls/Combobox/Arrow-Down.png);"
                           "}"
                           "QAbstractItemView {"
                                "background: rgb("+str(COLOR_WIDGET_11[0])+","+str(COLOR_WIDGET_11[1])+","+str(COLOR_WIDGET_11[2])+");"
                               "border-top: none;"
                               "border-left: 2px solid rgb("+str(COLOR_OUTLINE_6[0])+","+str(COLOR_OUTLINE_6[1])+","+str(COLOR_OUTLINE_6[2])+");"
                               "border-right: 2px solid rgb("+str(COLOR_OUTLINE_6[0])+","+str(COLOR_OUTLINE_6[1])+","+str(COLOR_OUTLINE_6[2])+");"
                               "border-bottom: 2px solid rgb("+str(COLOR_OUTLINE_6[0])+","+str(COLOR_OUTLINE_6[1])+","+str(COLOR_OUTLINE_6[2])+");"
                               "color: rgb("+str(COLOR_FONT_4[0])+","+str(COLOR_FONT_4[1])+","+str(COLOR_FONT_4[2])+");"
                               "min-height: 30px;"
                               "font-size: 20px;"
                               "font-weight: bold;"
                               "outline: none;"
                               "}"
                            "QAbstractItemView::item {"
                               "border-top: none;"
                               "border-left: none;"
                               "border-right: none;"
                               "border-bottom: 2px solid rgb("+str(COLOR_OUTLINE_6[0])+","+str(COLOR_OUTLINE_6[1])+","+str(COLOR_OUTLINE_6[2])+");"
                               "min-height: 30px;"
                               "font-size: 20px;"
                               "font-weight: bold;"
                               "}")
        self.setView(QListView())