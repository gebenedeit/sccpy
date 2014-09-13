from PyQt4.QtGui import QApplication
from PyQt4.Qt import Qt
from sys import exit, argv

if __name__ == '__main__':
    __appSccpy = QApplication(argv)
    __appSccpy.setAttribute(Qt.AA_DontShowIconsInMenus, False)
    exit(__appSccpy.exec_())