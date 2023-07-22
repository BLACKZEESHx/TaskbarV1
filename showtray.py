from PyQt5.QtCore import *
from PyQt5.QtGui import *
import win32gui
from PyQt5.QtWidgets import QMainWindow, QApplication, QShortcut
from Ui.tray import Ui_MainWindow
from pyautogui import size
width = size().width
height = size().height

class MainWindow(QMainWindow):
        def __init__(self):
            super(MainWindow, self).__init__()
            self.ui = Ui_MainWindow()
            # get the taskbar window handle
            taskbar_hwnd = win32gui.FindWindow("Shell_TrayWnd", "")
            # get the taskbar dimensions
            self.taskbar_rect = win32gui.GetWindowRect(taskbar_hwnd)
            print(self.taskbar_rect)
            self.ui.setupUi(self)
            # self.setGeometry(535, 718, 300, 60)
            self.setGeometry(width-193, self.taskbar_rect[1]-10, 200, 60)
            self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
            self.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
            self.setWindowFlag(Qt.WindowType.Tool, True)
            self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
            self.ui.widget.setStyleSheet("*{\n"
"    border-radius: 10px;\n"
"    background-color: rgba(255, 255, 0, 0);\n"
"     border: 4px solid rgb(255, 255, 255);\n"
"}")

if __name__ == "__main__":
    app = QApplication([])
    borderT = MainWindow()
    borderT.show()
    app.exec()