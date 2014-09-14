from PyQt4.QtGui import QWidget, QGridLayout
from Labels.LabelBigSize import LabelBigSize
from Ui.Colors import COLOR_FONT_1, COLOR_FONT_7, COLOR_WIDGET_3

class Header(QWidget):
    
    def __init__(self):
        QWidget.__init__(self)
        self.__InitUi()
        
    def __InitUi(self):
        self.setStyleSheet("background-color: rgb("+str(COLOR_WIDGET_3[0])+","+str(COLOR_WIDGET_3[1])+","+str(COLOR_WIDGET_3[2])+");")
        self.setFixedHeight(150)
        self.__Layout = QGridLayout()
        self.__Layout.setContentsMargins(30, 30, 30, 30)
        self.__Layout.setVerticalSpacing(0)
        self.__Layout.setHorizontalSpacing(0)
        self.__lblTitle = LabelBigSize("S.C.C.", COLOR_FONT_7, True)
        self.__lblSubtitle = LabelBigSize("Spin Chat Client", COLOR_FONT_1, False)
        self.__Layout.addWidget(self.__lblTitle)
        self.__Layout.addWidget(self.__lblSubtitle)
        self.setLayout(self.__Layout)
        
        '''
        chkExit = new CheckBox(this);
        QWidget *wdgSpace = new QWidget(this);
        wdgSpace->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Expanding);
        '''