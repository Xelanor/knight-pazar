import pyautogui
import win32api, win32con
from time import sleep
import keyboard
import pydirectinput
import logging
import os

coordinates = [
    (1546, 514),
    (1607, 514),
    (1668, 514),
    (1729, 514),
    (1790, 514),
    (1851, 514),
    (1485, 570),
    (1546, 570),
    (1607, 570),
    (1668, 570),
    (1729, 570),
    (1790, 570),
    (1851, 570),
    (1485, 631),
    (1546, 631),
    (1607, 631),
    (1668, 631),
    (1729, 631),
    (1790, 631),
    (1851, 631),
    (1485, 691),
    (1546, 691),
    (1607, 691),
    (1668, 691),
    (1729, 691),
    (1790, 691),
    (1851, 691),
]

scroll = (1485, 514)

logging.basicConfig(level=logging.INFO)


def click(x, y, delay=0.05):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(delay)  # This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print(f"Clicked x:{x} y:{y}")

def r_click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    sleep(0.10)  # This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
    print(f"Right Clicked x:{x} y:{y}")

def upgrade(x_coor, y_coor):
    click(1025, 421, 0.01)
    sleep(0.06)
    r_click(1025, 421)
    sleep(0.06)
    click(966, 515)
    sleep(0.06)
    r_click(scroll[0], scroll[1])
    sleep(0.03)
    r_click(x_coor, y_coor)
    sleep(0.03)
    click(1583, 389)
    sleep(0.05)
    click(1573, 515)
    sleep(0.05)

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
    sleep(0.5)
    pyautogui.typewrite('xelanor101')
    sleep(0.10)
    pydirectinput.press('tab')
    pyautogui.typewrite('Xelanor01')
    sleep(0.10)
    pydirectinput.press('enter')

item_count = 0
slot_count = 26
remaining = 31
start = False

while remaining > 0:
    logging.info("Uygulamayı çalıştırmak için q tuşuna basınız.")
    if not start:
        slot_count = int(input("Slot kaç olsun?\n"))
        keyboard.wait("q")
        start = True

    for x_coor, y_coor in coordinates:
        if item_count >= slot_count:
            item_count = 0
            break

        if remaining <= 0:
            break

        upgrade(x_coor, y_coor)
        remaining -= 1
        item_count += 1
        print(item_count)

exit_and_login()