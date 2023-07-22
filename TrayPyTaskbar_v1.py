import os
from time import sleep
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qt_material
from PyTaskbar_v1 import PyTaskbar
from Remove_St import Remove_Start_Button
import subprocess


class Tray_Taskbar_v1(QSystemTrayIcon):
    def __init__(self, parent=None):
        super(Tray_Taskbar_v1, self).__init__()
        self.count_hidden_msg = 0
        # Set The Tray Icon
        self.setIcon(QIcon("Ticons\icon512.png"))
        # Set The Tray Icon Tooltip
        self.setToolTip("PyTaskbar Ver.1.0")
        # Make the tray icon menu
        self.menu = QMenu()

        # Add the tray icon menu button that show main window of application
        self.mainwindow = self.menu.addAction("PyTaskbar")
        self.mainwindow.setIcon(QIcon("window icon.png"))
        self.mwindow = PyTaskbar()
        self.mwindow.setHidden(True)
        self.mainwindow.triggered.connect(lambda: self.mwindow.show())

        self.hidemwindow = self.menu.addAction("Hide Window")
        self.hidemwindow.triggered.connect(self.hide_window)
        self.hidemwindow.setIcon(QIcon("👁"))
        self.menu.addSeparator()

        self.show_start_btn = self.menu.addAction("Show Start Button")
        self.show_start_btn.triggered.connect(self.restart_expolorer)
        self.show_start_btn.setIcon(QIcon("Start\\Windows 10X.ico"))

        self.remove_start_button = self.menu.addAction("Remove Start Button")
        self.remove_start_button.triggered.connect(
            lambda: Remove_Start_Button())
        self.remove_start_button.setIcon(QIcon("Start\\StartRemover.ico"))
        self.menu.addSeparator()

        self.rest_taskbar_ip = self.menu.addAction(
            "Default Taskbar Icons Position")
        self.rest_taskbar_ip.triggered.connect(self.quit_centertaskbarapp)
        self.rest_taskbar_ip.setIcon(QIcon("Start\\StartRemover.ico"))

        self.start_centertaskbar_qa = self.menu.addAction(
            "Center Taskbar Icons")
        self.start_centertaskbar_qa.triggered.connect(
            self.start_centertaskbarapp)
        self.start_centertaskbar_qa.setIcon(QIcon("Start\\StartRemover.ico"))
        self.menu.addSeparator()

        # Add the tray icon menu button that exit application
        self.exitapp = self.menu.addAction("Exit...")
        # When exit button is clicked exit application
        self.exitapp.triggered.connect(self.exit_trapp)
        self.exitapp.setIcon(QIcon("close-window.png"))

        # Set the tray icon context menu self.menu
        self.setContextMenu(self.menu)

        # Set style sheet for the tray icon menu
        # qt_material.apply_stylesheet(self.menu, qt_material.list_themes()[-18], save_as="windows_style.css")

        self.menu.setStyleSheet(open("windows_style.css", "r").read())
        # print(self.menu.styleSheet())

        # self.start_timer = QTimer(self)
        # self.start_timer.start(1)
        # self.start_timer.timeout.connect(self.remove_start_btn)

        # If parent is not none so set the parent to user argument
        if parent:
            self.setParent(parent)

    def quit_centertaskbarapp(self):
        os.system("""wmic process where "name='CenterTaskbar.exe'" delete""")
        self.restart_expolorer()
        Remove_Start_Button()

    def start_centertaskbarapp(self):
        os.startfile("Start\\CenterTaskbar.exe")

    def exit_trapp(self):
        self.showMessage("Position Of Taskbar Icon", "If you want to reset the position of the taskbar go to tray sys icon and right click on centertaskbar icon then exit".title(),
                         QIcon("Ticons\icon512.png"), 3000)
        sleep(4.0)
        self.restart_expolorer()
        os.system("""wmic process where "name='CenterTaskbar.exe'" delete""")
        sys.exit()

    def hide_window(self):
        if self.mwindow.isHidden():

            self.count_hidden_msg += 1
            if not self.count_hidden_msg > 2:
                self.showMessage("Pytaskbar", "Window is already hidden", QIcon(
                    "Ticons\icon512.png"), 3000)

        else:
            self.mwindow.setHidden(True)

    def restart_expolorer(self):
        # Restating The Explorer to Show Start Button
        subprocess.run(["taskkill", "/F", "/IM", "explorer.exe",
                       "&", "start", "explorer"], shell=True)


# If statement
if __name__ == "__main__":
    # Make an application
    app = QApplication(sys.argv)
    app.setApplicationDisplayName("PyTaskbar - Ver.1.0")
    app.setApplicationName("PyTaskbar V.1.0")
    app.setApplicationVersion("Version 1.0.0")
    app.setWindowIcon(QIcon("Ticons\icon128.png"))

    # Create the application object
    tray = Tray_Taskbar_v1(parent=app)
    # Show the tray
    tray.show()
    tray.showMessage("PyTaskbar Ver.1.0", "app is now on on the tray area.",
                     QIcon("Ticons\icon512.png"), 1000)
    tray.restart_expolorer()
    import time
    time.sleep(5)
    tray.remove_start_button.trigger()
    tray.start_centertaskbar_qa.trigger()

    # execute application
    sys.exit(app.exec_())
