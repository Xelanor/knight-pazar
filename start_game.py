import pyautogui
import win32api, win32con
from time import sleep
import pydirectinput
import logging
import os

def click(x, y, delay=0.10):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(delay)  # This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print(f"Clicked x:{x} y:{y}")

def exit_and_login():
    os.system("TASKKILL /F /IM knightonline.exe")
    sleep(1)
    os.startfile('C:\\NTTGame\\KnightOnlineEn\\Launcher.exe')
    sleep(2)
    click(979, 728, delay=0.5)
    click(979, 728, delay=0.5)
    click(979, 728, delay=0.5)
    sleep(17)
    click(979, 728)
    sleep(0.5)
    pydirectinput.press('enter')
    sleep(1)
    pyautogui.typewrite('xelanor101')
    sleep(0.25)
    pydirectinput.press('tab')
    pyautogui.typewrite('Xelanor01')
    sleep(0.25)
    pydirectinput.press('enter')

exit_and_login()