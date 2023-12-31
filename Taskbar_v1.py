import winshell
import winreg
import psgshortcut.gui
import os
import subprocess
import asyncio
import time
import shutil
import struct
from Remove_St import Remove_Start_Button

desktop = winshell.desktop()
path = winreg.HKEY_CURRENT_USER


def Make_Taskbar_Transparent(Enable=True):
    if Enable:
        color_key = winreg.OpenKeyEx(
            path, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize", 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(color_key, 'ColorPrevalence', 0, winreg.REG_DWORD, 0)
        blury = winreg.SetValueEx(
            color_key, "EnableTransparency", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(blury)
        winreg.CloseKey(color_key)
        ex_advance = winreg.OpenKeyEx(
            path, r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\")
        Create_Taskbar_transparent_key = winreg.CreateKey(
            ex_advance, "Advanced")
        winreg.SetValueEx(Create_Taskbar_transparent_key,
                          "TaskbarAcrylicOpacity", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(Create_Taskbar_transparent_key)


sysbit = struct.calcsize("P") * 8


def Start_shortcut_creator():
    if not (os.path.exists(desktop + "\\Start.lnk")):
        psgshortcut.gui.create_shortcut_exe_or_other(arguments=f"{os.path.abspath(os.getcwd())}\\Start\\start.vbs",
                                                     target="wscript",
                                                     icon=f"{os.path.abspath(os.getcwd())}\\Start\\Windows 10X.ico",
                                                     new_name="Start")
        time.sleep(5)
        shutil.move("Start.lnk",
                    f"{desktop}\\Start.lnk")


if __name__ == "__main__":
    Make_Taskbar_Transparent()
    # asyncio.run(Start_shortcut_creator())
    # End Windows Explorer task
    # subprocess.run(["taskkill", "/F", "/IM", "explorer.exe", "/f"], shell=True)
    os.startfile("Start\\CenterTaskbar.exe")
    # Start Windows Explorer task
    # subprocess.run(["explorer.exe"], shell=True)
    while True:
        # Check if the explorer process is running
        if "explorer.exe" in subprocess.check_output("tasklist /fi \"imagename eq explorer.exe\"", shell=True).decode("utf-8"):
            Remove_Start_Button()
        else:
            print("Explorer process is not running. Start button will be visible.")
