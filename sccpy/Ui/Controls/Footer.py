from PyQt4.QtGui import QWidget
from Ui.Helper import SetWidgetBackgroundColor
from Ui.Colors import COLOR_WIDGET_2, COLOR_FONT_4
from PyQt4.Qt import QGridLayout
from Ui.Controls.Labels.LabelSmalSize import LabelSmalSize
from Ui.Controls.Progressbars.Progressbar import Progressbar

class Footer(QWidget):
    
    def __init__(self):
        QWidget.__init__(self)
        self.__InitUi()
        
    def __InitUi(self):
        self.setFixedHeight(160)
        SetWidgetBackgroundColor(COLOR_WIDGET_2, self)
        self.__Layout = QGridLayout()
        self.setLayout(self.__Layout)
        self.__Layout.setContentsMargins(30,30,30,30)
        self.__Layout.setHorizontalSpacing(30)
        self.__Layout.setVerticalSpacing(30)
        self.__lblProcess = LabelSmalSize("", COLOR_FONT_4, True)
        self.__Layout.addWidget(self.__lblProcess)        
        self.__pgbProgress = Progressbar()
        self.__Layout.addWidget(self.__pgbProgress)
        
    def ProcessStartet(self, strProcess):
        self.__lblProcess.setText(strProcess)
        self.__pgbProgress.setMaximum(0)
        
    def ProcessEnded(self):
        self.__lblProcess.setText("")
        self.__pgbProgress.setMaximum(100)