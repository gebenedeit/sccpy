from PyQt4.QtGui import QMainWindow, QGridLayout, QWidget
from Controls.Master import Master

class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.__InitUi()
        
    def __InitUi(self):
        self.__Master = Master()
        self.__CentralWidget = QWidget()
        self.__Layout = QGridLayout()
        self.__Layout.addWidget(self.__Master)
        self.__CentralWidget.setLayout(self.__Layout)
        self.setCentralWidget(self.__CentralWidget)