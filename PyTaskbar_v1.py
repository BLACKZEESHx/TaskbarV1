import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qt_material
import win32gui
from pyautogui import size
from Ui import title_bar_c


class PyTaskbar(QMainWindow):
    def __init__(self):
        super(PyTaskbar, self).__init__()
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui = title_bar_c.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.title_bar.mouseMoveEvent = self.MoveWindow
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.btn_close.clicked.connect(lambda: self.setHidden(True))
        self.ui.btn_maximize.setCheckable(True)
        self.ui.btn_maximize.clicked.connect(self.maximizebutton_set)
        self.themeindex = 4
        self.theme = qt_material.list_themes()[self.themeindex]
        qt_material.apply_stylesheet(self, self.theme)

        qApp.setApplicationDisplayName("PyTaskbar - Ver.1.0")
        qApp.setApplicationName("PyTaskbar V.1.0")
        qApp.setApplicationVersion("Version 1.0.0")
        qApp.setWindowIcon(QIcon("Ticons\icon128.png"))

        # self.show()

    def maximizebutton_set(self):
        if self.ui.btn_maximize.isChecked():
            self.showMaximized()

        elif not self.ui.btn_maximize.isChecked():
            self.showNormal()

    def MoveWindow(self, event):
        if self.isMaximized() == False:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = PyTaskbar()
#     app.setApplicationDisplayName("PyTaskbar - Ver.1.0")
#     app.setApplicationName("PyTaskbar V.1.0")
#     app.setApplicationVersion(1.0)
#     sys.exit(app.exec_())
