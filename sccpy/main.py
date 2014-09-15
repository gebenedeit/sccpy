from PyQt4.QtGui import QApplication, QFont
from sys import exit, argv
from Ui.MainWindow import MainWindow

if __name__ == '__main__':
    __appSccpy = QApplication(argv)
    __appSccpy.setFont(QFont("Abel", 8, QFont.Normal, False))
    __winMainWindow = MainWindow()
    __winMainWindow.showMaximized()
    exit(__appSccpy.exec_())