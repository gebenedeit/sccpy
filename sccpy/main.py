from PyQt4.QtGui import QApplication, QFont
from PyQt4.Qt import Qt
from sys import exit, argv
from Ui.MainWindow import MainWindow

if __name__ == '__main__':
    __appSccpy = QApplication(argv) 
    __appSccpy.setAttribute(Qt.AA_DontShowIconsInMenus, False)
    __appSccpy.setFont(QFont("Abel", 8, QFont.Normal, False))
    __winMainWindow = MainWindow()
    __winMainWindow.showFullScreen()
    exit(__appSccpy.exec_())