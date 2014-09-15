from PyQt4.QtGui import QPalette, QColor

def SetWidgetBackgroundColor(tplColor, wdgWidget):
    wdgWidget.setAutoFillBackground(True)
    palBackground = QPalette()
    palBackground.setColor(QPalette.Background, QColor.fromRgb(tplColor[0], tplColor[1], tplColor[2]))
    wdgWidget.setPalette(palBackground)

def SetWidgetBackgroundColorWithAlpha(tplColor, wdgWidget):
    wdgWidget.setAutoFillBackground(True)
    palBackground = QPalette()
    palBackground.setColor(QPalette.Background, QColor.fromRgb(tplColor[0], tplColor[1], tplColor[2], tplColor[3]))
    wdgWidget.setPalette(palBackground)