import winreg

path = winreg.HKEY_CURRENT_USER
ex = "Explorer"
pol_exporor = winreg.OpenKeyEx(path, r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\")
def remove_around_tray(enabled=True):
    if enabled==True:

        # HIDECLOCK
        CREATE_HIDECLOCK_KEY = winreg.CreateKey(pol_exporor, ex)
        winreg.SetValueEx(CREATE_HIDECLOCK_KEY, "HideClock", 0, winreg.REG_DWORD, 1)
        
        # HideSCAPower
        CREATE_HIDESCAPOWER_KEY = winreg.CreateKey(pol_exporor, ex)
        winreg.SetValueEx(CREATE_HIDESCAPOWER_KEY, "HideSCAPower", 0, winreg.REG_DWORD, 1)

        # HideSCAVolume
        CREATE_HIDESCAVOLUME_KEY = winreg.CreateKey(pol_exporor, ex)
        winreg.SetValueEx(CREATE_HIDESCAVOLUME_KEY, "HideSCAVolume", 0, winreg.REG_DWORD, 1)

        if CREATE_HIDECLOCK_KEY and CREATE_HIDESCAPOWER_KEY and CREATE_HIDESCAVOLUME_KEY:
            winreg.CloseKey(CREATE_HIDECLOCK_KEY)
            winreg.CloseKey(CREATE_HIDESCAPOWER_KEY)
            winreg.CloseKey(CREATE_HIDESCAVOLUME_KEY)
        # winreg.SetValueEx(Create_Hide_Clock_Key, )

def show_all_icons(enable=True):
    """`Show all icons`"""
    if enable:
        try:
            # HIDECLOCK
            HC = winreg.OpenKey(pol_exporor, ex)
            winreg.SetValueEx(HC, "HideClock", 0, winreg.REG_DWORD, 0)
            if HC:
                HC.Close()
        except Exception as e:
            print(e)
                
if __name__ == "__main__":
    # show_all_icons()
    remove_around_tray()

# import time
# import win32api
# import win32con
# import win32gui
# time.sleep(5)
# def hide_taskbar_icons():
#     # Hide Volume icon
#     win32api.SendMessage(win32gui.FindWindow("Shell_TrayWnd", None), win32con.WM_COMMAND, 419, 0)

#     # Hide Battery icon
#     win32api.SendMessage(win32gui.FindWindow("Shell_TrayWnd", None), win32con.WM_COMMAND, 436, 0)

#     # Hide Notification area icons
#     win32api.SendMessage(win32gui.FindWindow("Shell_TrayWnd", None), win32con.WM_COMMAND, 48043, 0)

#     # Hide Time label
#     win32api.SendMessage(win32gui.FindWindow("Shell_TrayWnd", None), win32con.WM_COMMAND, 410, 0)

# hide_taskbar_icons()

# import pystray
# from PIL import Image

# def remove_taskbar_icons(icon):
#     pass  # Placeholder function, as removing icons is not straightforward

# # Create an empty image for the system tray icon
# image = Image.new("RGB", (1, 1))

# # Create the system tray icon
# menu = (
#     pystray.MenuItem("Remove Taskbar Icons", remove_taskbar_icons),
#     pystray.MenuItem("Exit", lambda: exit())
# )
# icon = pystray.Icon("Taskbar Icons", image, "Taskbar Icons", menu)

# # Run the system tray icon application
# icon.run()

# import ctypes

# # Constants for Windows API
# HWND_BROADCAST = 0xFFFF
# WM_SYSCOMMAND = 0x0112
# SC_TASKLIST = 0xF130
# SPI_SETWORKAREA = 0x002F
# SPIF_SENDCHANGE = 0x02

# user32 = ctypes.windll.user32
# shell32 = ctypes.windll.shell32
# SPI_SETICONS = 0x0058
# SPI_GETICONS = 0x005F

# # Remove the volume icon
# user32.PostMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_TASKLIST, 0)

# # Remove the battery icon
# shell32.Shell_NotifyIconW(SPI_SETICONS, None)

# # Remove the notification icon
# # Replace "Notification Area" with the appropriate name for your Windows version (e.g., "System Icons")
# user32.SendMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SPI_SETICONS, "Notification Area")

# # Remove the time label
# user32.SystemParametersInfoW(SPI_SETWORKAREA, 0, None, SPIF_SENDCHANGE)
import ctypes, win32con, win32gui
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import cv2, os
from pyautogui import size
width = size().width
height = size().height

def getWallpaper():
    ubuf = ctypes.create_unicode_buffer(512)
    ctypes.windll.user32.SystemParametersInfoW(win32con.SPI_GETDESKWALLPAPER,len(ubuf),ubuf,0)
    
    return ubuf.value


working_dir = os.path.abspath(os.getcwd())
image = cv2.imread(getWallpaper())
CroppedImage2 = image[1150:1200, 1720:1920]
cv2.imwrite(f"{working_dir}\\wallpaper.png", CroppedImage2)


class Taskbar(QMainWindow):
    def __init__(self):
        super().__init__()
        # get the taskbar window handle
        taskbar_hwnd = win32gui.FindWindow("Shell_TrayWnd", "")
        # get the taskbar dimensions
        self.taskbar_rect = win32gui.GetWindowRect(taskbar_hwnd)
        print(self.taskbar_rect)

        self.pic_lab = QLabel(self)
        self.setCentralWidget(self.pic_lab)
        self.pic = QPixmap(f"{working_dir}\\wallpaper.png")
        self.pic_lab.setPixmap(self.pic)
        self.setGeometry(width-200, self.taskbar_rect[1], 200, 40)

        # set the window properties
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
        self.setWindowFlag(Qt.WindowType.Tool, True)
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool | Qt.CustomizeWindowHint)
        # self.setWindowFlag(Qt.FramelessWindowHint
        # self.setWindowFlag(Qt.WindowStaysOnTopHint)
        # self.setWindowFlag(Qt.Tool)
        # self.setWindowFlag(Qt.CustomizeWindowHint)
        # self.setFixedSize(self.toolbar.sizeHint())

if __name__ == "__main__":
    app = QApplication([])
    taskbar = Taskbar()
    taskbar.show()
    app.exec()
        # self.geometry().setY(self.taskbar_rect[1])
        # self.geometry().setX(self.taskbar_rect[0])
        # self.geometry().setY(860)
