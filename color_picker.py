import win32api, win32con
import pyautogui
import keyboard
import time

coordinates = [
    (795, 240),
    (859, 240),
    (923, 240),
    (987, 240),
    (1051, 240),
    (1115, 240),
    (795, 304),
    (859, 304),
    (923, 304),
    (987, 304),
    (1051, 304),
    (1115, 304),
]


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)  # This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while 1:
    print("Waiting for input")
    keyboard.wait("q")
    for x, y in coordinates:
        click(x, y)
        time.sleep(0.5)
        print(pyautogui.pixel(x, y))
        time.sleep(1)
