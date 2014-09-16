from PyQt4.QtGui import QWidget, QGridLayout
from Ui.Views.Home.Personal.Personal import Personal
from Ui.Views.Home.FavoriteRooms.FavoriteRooms import FavoriteRooms
from Ui.Views.Home.Friends.Friends import Friends
from Ui.Views.Home.News.News import News
from Ui.Helper import SetWidgetBackgroundColor
from Ui.Colors import COLOR_WIDGET_7

class ViewHome(QWidget):
    
    def __init__(self):
        QWidget.__init__(self)
        self.__InitUi()
        
    def __InitUi(self):
        SetWidgetBackgroundColor(COLOR_WIDGET_7, self)
        self.__grdLayout = QGridLayout()
        self.setLayout(self.__grdLayout)
        self.__grdLayout.setContentsMargins(30, 30, 30, 30)
        self.__grdLayout.setHorizontalSpacing(30)
        self.__grdLayout.setVerticalSpacing(30)
        
        self.__wdgPersonal = Personal()
        self.__grdLayout.addWidget(self.__wdgPersonal,0,0)
        
        self.__wdgFavoriteRooms = FavoriteRooms()
        self.__grdLayout.addWidget(self.__wdgFavoriteRooms,1,0)
        
        self.__wdgFriends = Friends()
        self.__grdLayout.addWidget(self.__wdgFriends,0,1)
        
        self.__wdgNews = News()
        self.__grdLayout.addWidget(self.__wdgNews,1,1)