from PyQt4.QtGui import QWidget, QGridLayout
from Header import Header
from Navigationbar import Navigationbar
from Footer import Footer

class Master(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.__InitUi()
        
    def __InitUi(self):
        self.setFixedWidth(300)
        self.__Header = Header()
        self.__Navigationbar = Navigationbar()
        self.__Footer = Footer()
        self.__Layout = QGridLayout()
        self.__Layout.addWidget(self.__Header)
        self.__Layout.addWidget(self.__Navigationbar)
        self.__Layout.addWidget(self.__Footer)
        self.setLayout(self.__Layout)