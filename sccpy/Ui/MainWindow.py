from PyQt4.QtGui import QMainWindow, QGridLayout, QWidget
from Controls.Master import Master
from Ui.Views.Login.Login import Login
from Helper import SetWidgetBackgroundColor
from Ui.Views.Home.ViewHome import ViewHome
from Ui.OpenChatsBar import OpenChatsBar

class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.__InitUi()
        
    def __InitUi(self):
        self.__Master = Master()
        self.__Login = Login()
        self.__wdgViewHome = ViewHome()
        
        self.__CentralWidget = QWidget()
        self.__CentralWidget.setContentsMargins(0, 0, 0, 0)
        SetWidgetBackgroundColor((28,28,28), self.__CentralWidget)
        
        self.__Layout = QGridLayout()
        self.__Layout.setContentsMargins(0,0,0,0)
        self.__Layout.setVerticalSpacing(0)
        self.__Layout.setHorizontalSpacing(0)
        
        self.__Layout.addWidget(self.__wdgViewHome, 0, 0,1,1)
        #self.__Layout.addWidget(self.__Login, 0, 0)
        self.__wdgOpenChatsBar = OpenChatsBar()
        self.__Layout.addWidget(self.__wdgOpenChatsBar, 1, 0,1,1)
        self.__Layout.addWidget(self.__Master, 0, 1, 2, 1)
        self.__CentralWidget.setLayout(self.__Layout)
        self.setCentralWidget(self.__CentralWidget)