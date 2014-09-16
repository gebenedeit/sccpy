from PyQt4.QtGui import QWidget, QSizePolicy, QGridLayout, QLineEdit
from PyQt4.Qt import Qt
from PyQt4.QtCore import QVariant
from Ui.Helper import SetWidgetBackgroundColor, SetWidgetBackgroundColorWithAlpha
from Ui.Colors import COLOR_WIDGET_7, COLOR_TRANSPARENT, COLOR_FONT_7, COLOR_FONT_4
from Ui.Controls.LineEdits.LineEditStandard import LineEditStandard
from Ui.Controls.Labels.LabelBigSize import LabelBigSize
from Ui.Controls.Labels.LabelSmalSize import LabelSmalSize
from Ui.Controls.Buttons.ButtonPositive import ButtonPositive
from Ui.Controls.Combobox.ComboboxStandard import ComboboxStandard

class Login(QWidget):
    
    def __init__(self):
        QWidget.__init__(self)
        self.__InitUi()
    
    def __InitUi(self):
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        SetWidgetBackgroundColorWithAlpha(COLOR_TRANSPARENT, self)
        self.__Layout = QGridLayout()
        self.setLayout(self.__Layout)
        
        self.__Credentials = QWidget()
        SetWidgetBackgroundColor(COLOR_WIDGET_7, self.__Credentials)
        self.__Credentials.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.__CredentialsLayout = QGridLayout()
        self.__Credentials.setLayout(self.__CredentialsLayout)
        self.__CredentialsLayout.setContentsMargins(30,30,30,30)
        self.__CredentialsLayout.setHorizontalSpacing(20)
        self.__CredentialsLayout.setVerticalSpacing(20)
        self.__lblLogin = LabelBigSize("Login", COLOR_FONT_7,True)
        self.__lblUsername = LabelSmalSize("Username",COLOR_FONT_4,True)
        self.__lblPassword = LabelSmalSize("Password",COLOR_FONT_4,True)
        self.__lblServer = LabelSmalSize("Server",COLOR_FONT_4,True)
        self.__txtUsername = LineEditStandard()
        self.__txtPassword = LineEditStandard()
        self.__txtPassword.setEchoMode(QLineEdit.Password)
        self.__cboServer = ComboboxStandard()
        self.__cboServer.addItem("Public", QVariant(3000))
        self.__cboServer.addItem("Public (No Chat)", QVariant(3001))
        self.__cboServer.addItem("Erotic", QVariant(3002))
        self.__cboServer.addItem("Erotic (No Chat)", QVariant(3003))
        
        self.__btnLogin = ButtonPositive("Login")
        
        self.__CredentialsLayout.addWidget(self.__lblLogin, 0, 0, 1, 2)
        self.__CredentialsLayout.addWidget(self.__lblUsername, 1, 0, 1, 1)
        self.__CredentialsLayout.addWidget(self.__lblPassword, 2, 0, 1, 1)
        self.__CredentialsLayout.addWidget(self.__lblServer, 3, 0, 1, 1)
        self.__CredentialsLayout.addWidget(self.__txtUsername, 1, 1, 1, 1)
        self.__CredentialsLayout.addWidget(self.__txtPassword, 2, 1, 1, 1)
        self.__CredentialsLayout.addWidget(self.__cboServer, 3, 1, 1, 1)
        self.__CredentialsLayout.addWidget(self.__btnLogin, 4, 1, 1, 1, Qt.AlignRight)
        
        self.__Layout.addWidget(self.__Credentials)