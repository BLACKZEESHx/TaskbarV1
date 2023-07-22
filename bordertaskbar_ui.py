from showtray import MainWindow as traywindow
import sys
from Ui.borderTaskbar import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QShortcut
import ctypes, win32con, win32gui



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        taskbar_hwnd = win32gui.FindWindow("Shell_TrayWnd", "")
        # get the taskbar dimensions

        self.taskbar_rect = win32gui.GetWindowRect(taskbar_hwnd)
        print(self.taskbar_rect)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.setWindowOpacity(0.1)
        self.setGeometry(535, 718, 300, 60)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
        self.setWindowFlag(Qt.WindowType.Tool, True)
        # self.setWindowFlag(Qt.WindowType.WindowTransparentForInput, True)
        # self.setWindowFlags(Qt.WA_TranslucentBackground, True)
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnBottomHint | Qt.Tool | Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)

        self.closer = QShortcut("Ctrl+alt+O", self)
        self.closer.activated.connect(self.close)

        self.trayteller = QShortcut("Ctrl+alt+T", self)
        self.trayteller.activated.connect(self.showtray)
        
    def showtray(self):
        traywindow()
        

if __name__ == "__main__":
    app = QApplication([])
    borderT = MainWindow()
    borderT.show()
    app.exec()