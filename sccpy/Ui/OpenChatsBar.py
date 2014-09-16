from PyQt4.QtGui import QWidget, QGridLayout
from Ui.Helper import SetWidgetBackgroundColor
from Ui.Colors import COLOR_WIDGET_3, COLOR_WIDGET_7
from Ui.Controls.Buttons.ButtonStandard import ButtonStandard
class OpenChatsBar(QWidget):
    
    def __init__(self):
        QWidget.__init__(self)
        self.__InitUi()
        
    def __InitUi(self):
        SetWidgetBackgroundColor(COLOR_WIDGET_7, self)
        self.setFixedHeight(120)
        
        self.__grdLayout = QGridLayout()
        self.setLayout(self.__grdLayout)
        self.__grdLayout.setContentsMargins(30,0,30,30)
        self.__grdLayout.setHorizontalSpacing(0)
        self.__grdLayout.setVerticalSpacing(0)
        
        self.__wdgBar = QWidget()
        self.__grdLayout.addWidget(self.__wdgBar)
        SetWidgetBackgroundColor(COLOR_WIDGET_3, self.__wdgBar)
        
        self.__grdBarLayout = QGridLayout()
        self.__wdgBar.setLayout(self.__grdBarLayout)
        self.__grdBarLayout.setContentsMargins(30,30,30,30)
        self.__grdBarLayout.setHorizontalSpacing(30)
        self.__grdBarLayout.setVerticalSpacing(0)
        
        self.__intOpenChats = 0
        
        self.__AddButton("Computerfreaks")
        self.__AddButton("Computerfreaks")
        self.__AddButton("Computerfreaks")
        self.__AddButton("Computerfreaks")
        self.__AddButton("Computerfreaks")
        self.__AddButton("Computerfreaks")
        
    def __AddButton(self, strName):
        btnTemp = ButtonStandard(strName)
        self.__grdBarLayout.addWidget(btnTemp, 0, self.__intOpenChats)
        self.__intOpenChats += 1