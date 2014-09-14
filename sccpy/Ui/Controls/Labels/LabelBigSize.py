from PyQt4.QtGui import QLabel

class LabelBigSize(QLabel):

    def __init__(self, strText="", tplColor=(0, 0, 0), bolBold=True):
        QLabel.__init__(self)
        self.__InitUi(strText, tplColor, bolBold)
        
    def __InitUi(self, strText="", tplColor=(0, 0, 0), bolBold=True):
        self.setFixedHeight(30)
        self.setText(strText)
        if bolBold:
            self.setStyleSheet("text-align: bottom;"
                               "font-weight: bold;"
                               "color: rgb("+str(tplColor[0])+", "+str(tplColor[1])+", "+str(tplColor[2])+");"
                               "font-size: 20px;")
        else:
            self.setStyleSheet("text-align: bottom;"
                               "color: rgb("+str(tplColor[0])+", "+str(tplColor[1])+", "+str(tplColor[2])+");"
                               "font-size: 20px;")