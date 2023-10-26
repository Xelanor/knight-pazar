import pyautogui
import win32api, win32con
import time
import keyboard
import pydirectinput
import logging

coordinates = [
    (778, 490, 795, 260),
    (840, 490, 860, 260),
    (902, 490, 925, 260),
    (955, 490, 990, 260),
    (1014, 490, 1055, 260),
    (1071, 490, 1120, 260),
    (1128, 490, 794, 330),
    (780, 550, 859, 330),
    (842, 550, 924, 330),
    (898, 550, 989, 330),
    (956, 550, 1054, 330),
    (1016, 550, 1119, 330),
]

logging.basicConfig(level=logging.INFO)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)  # This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def drag_drop(from_x, from_y, to_x, to_y):
    win32api.SetCursorPos((from_x, from_y))
    time.sleep(0.01)  # This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.25)
    win32api.SetCursorPos((to_x, to_y))
    time.sleep(0.25)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while 1:
    logging.info("Uygulamayı çalıştırmak için q tuşuna basınız.")
    keyboard.wait("q")
    # price = input("Satmak istediğiniz ürünün fiyatı nedir?: ")
    price = "799999"
    # time.sleep(1)
    for from_x, from_y, to_x, to_y in coordinates:
        drag_drop(from_x, from_y, to_x, to_y)
        time.sleep(0.1)
        pyautogui.typewrite(price)
        pydirectinput.press("right")
        time.sleep(0.1)
        pydirectinput.press("enter")
        time.sleep(0.1)
        pydirectinput.press("enter")
        time.sleep(0.1)
