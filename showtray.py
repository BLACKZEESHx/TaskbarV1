import datetime as dt
from PyQt5.QtCore import *
import ctypes
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
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.timerbattime)
            self.timer.start(100)
            self.ui.widget.setStyleSheet("*{\n"
"    border-radius: 10px;\n"
"    background-color: rgba(255, 255, 0, 0);\n"
"    border: 4px solid rgb(255, 255, 255);\n"
"    color: white;\n"
"}")
        def timerbattime(self):
            class SYSTEM_POWER_STATUS(ctypes.Structure):
                _fields_ = [
                    ("ACLineStatus", ctypes.c_byte),
                    ("BatteryFlag", ctypes.c_byte),
                    ("BatteryLifePercent", ctypes.c_byte),
                    ("Reserved1", ctypes.c_byte),
                    ("BatteryLifeTime", ctypes.c_ulong),
                    ("BatteryFullLifeTime", ctypes.c_ulong),
                ]

            # create an instance of the SYSTEM_POWER_STATUS structure
            status = SYSTEM_POWER_STATUS()

            # call the GetSystemPowerStatus function to get the battery status
            ctypes.windll.kernel32.GetSystemPowerStatus(ctypes.byref(status))

            # extract the battery life percentage from the structure
            battery_percent = status.BatteryLifePercent
            # print the battery life percentage
            # print("Battery Life:", battery_percent, "%")
            self.ui.pushButton_3.setText(str(battery_percent)+"%")
            current_time = dt.datetime.now().strftime('%H:%M')
            self.ui.pushButton.setText(str(current_time))


if __name__ == "__main__":
    app = QApplication([])
    borderT = MainWindow()
    borderT.show()
    app.exec()