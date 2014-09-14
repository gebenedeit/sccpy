from PyQt4.QtGui import QWidget, QGridLayout, QSizePolicy
from Labels.LabelBigSize import LabelBigSize
from Ui.Colors import COLOR_FONT_1, COLOR_FONT_7, COLOR_WIDGET_3
from Ui.Helper import SetWidgetBackgroundColor
from Ui.Controls.Checkboxes.CheckboxBigSizeGreen import CheckboxBigSizeGreen

from Functions.ExitProgram import ExitProgram

class Header(QWidget):
    
    def __init__(self):
        QWidget.__init__(self)
        self.__InitUi()
        self.__ConnectUi()
        
    def __InitUi(self):
        SetWidgetBackgroundColor(COLOR_WIDGET_3, self)
        self.setFixedHeight(150)
        self.__Layout = QGridLayout()
        self.__Layout.setContentsMargins(30, 30, 30, 30)
        self.__Layout.setVerticalSpacing(30)
        self.__Layout.setHorizontalSpacing(30)
        self.__lblTitle = LabelBigSize("S.C.C.", COLOR_FONT_7, True)
        self.__lblSubtitle = LabelBigSize("Spin Chat Client", COLOR_FONT_1, False)
        self.__chkExit = CheckboxBigSizeGreen()
        self.__wdgSpace = QWidget()
        self.__wdgSpace.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.__Layout.addWidget(self.__lblTitle,0,1,1,1)
        self.__Layout.addWidget(self.__wdgSpace,0,2,1,1)
        self.__Layout.addWidget(self.__chkExit,0,3,1,1)
        self.__Layout.addWidget(self.__lblSubtitle,1,1,1,1)
        self.setLayout(self.__Layout)
        self.__chkExit.setChecked(True)
        
    def __ConnectUi(self):
        self.__chkExit.stateChanged.connect(self.__chkExit_CheckedChanged)
    
    def __chkExit_CheckedChanged(self):
        if not self.__chkExit.isChecked():
            ExitProgram()