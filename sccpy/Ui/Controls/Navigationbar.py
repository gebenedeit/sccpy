from PyQt4.QtGui import QWidget, QSizePolicy, QGridLayout
from Ui.Colors import COLOR_WIDGET_3
from Ui.Controls.Buttons.ButtonNavigation import ButtonNavigation
from Ui.Helper import SetWidgetBackgroundColor

class Navigationbar(QWidget):
    
    def __init__(self):
        QWidget.__init__(self)
        self.__InitUi()
        
    def __InitUi(self):
        self.setAutoFillBackground(True)
        SetWidgetBackgroundColor(COLOR_WIDGET_3, self)
        self.__Layout = QGridLayout()
        self.__Layout.setContentsMargins(0,0,0,0)
        self.__Layout.setHorizontalSpacing(0)
        self.__Layout.setVerticalSpacing(2)
        self.setLayout(self.__Layout)
        
        self.__btnHome = ButtonNavigation("Home")
        self.__Layout.addWidget(self.__btnHome)
        
        self.__btnChat = ButtonNavigation("Chat")
        self.__Layout.addWidget(self.__btnChat)
        
        self.__wdgSpace = QWidget()
        self.__wdgSpace.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.__Layout.addWidget(self.__wdgSpace)
        '''
        QPalette palCOL(this->palette());
        palCOL.setColor(QPalette::Background, QColor::fromRgb(28, 36, 51));
        this->setPalette(palCOL);
    
        btnOpenbooks = new NavigationButton("Open Books", this);
        btnHelp = new NavigationButton("Help", this);
        btnAbout = new NavigationButton("About", this);
    
        QGridLayout *grdLayout = new QGridLayout(this);
        grdLayout->setContentsMargins(0,0,0,0);
        grdLayout->setHorizontalSpacing(0);
        grdLayout->setVerticalSpacing(2);
    
        grdLayout->addWidget(btnOpenbooks);
        grdLayout->addWidget(btnHelp);
        grdLayout->addWidget(btnAbout);
        '''