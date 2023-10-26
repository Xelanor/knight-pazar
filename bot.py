import pyautogui
import win32api, win32con
import time
import keyboard
import pydirectinput
import pyperclip
import logging
import datetime
import cv2 as cv
from utils import telegram_bot_sendtext
import numpy as np
from PIL import Image

logging.basicConfig(level=logging.INFO)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)  # This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def take_screenshot():
    pic = pyautogui.screenshot(region=(0, 0, 1920, 1080))
    # pic.save('images/ss-repair-3.png')
    return pic


def locate_all_tiles(ss, tile, grayscale=False, confidence=0.90):
    tiles = list(
        pyautogui.locateAll(tile, ss, grayscale=grayscale, confidence=confidence)
    )
    logging.debug(tiles)

    # img = np.array(ss)
    # img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    # for tile in tiles:
    #     top_left = (tile.left, tile.top)
    #     bottom_right = (tile.left + tile.width, tile.top + tile.height)
    #     cv.rectangle(img, top_left, bottom_right, (0,255,0), 1)

    # cv.imshow("rectangle", img)
    # cv.waitKey()
    return len(tiles)


def check_inventory(ss):
    close_button = locate_all_tiles(ss, "images/inv_close_button.png")
    if close_button < 1:
        logging.info(f"Close button bulunamadı")
        pydirectinput.press("i")
        time.sleep(1)
        ss = take_screenshot()
        pydirectinput.press("i")
    empty_tiles = locate_all_tiles(ss, "images/empty_item2.png")
    if empty_tiles < 2:
        logging.info(f"Üzerin dolmak üzere boş yer: {empty_tiles}")
        telegram_bot_sendtext("Üzerin dolmak üzere")
        time.sleep(60*5)
    else:
        logging.info(f"Üzerinde daha {empty_tiles} yer var")

    return empty_tiles


def check_repair(ss):
    repair_tiles = locate_all_tiles(ss, "images/repair_icon.png", True, 0.7)
    if repair_tiles > 0:
        logging.info("Repair yapman gerekiyor")
        telegram_bot_sendtext("Repair zamanı geldi")
        time.sleep(60*5)
    else:
        logging.info(f"Repair yapmana gerek yok")


def check_problem(start, empty_tiles):
    now = datetime.datetime.now()
    passed_minutes = int((now - start).seconds / 60)
    if passed_minutes > 20 and empty_tiles > 10:
        logging.info(f"{passed_minutes} dakika geçti fakat hala {empty_tiles} boş yer var")
        telegram_bot_sendtext(
            f"{passed_minutes} dakika geçti fakat hala {empty_tiles} boş yer var"
        )
        start = datetime.datetime.now()
    else:
        logging.info(f"Bir sıkıntı yok")


if __name__ == "__main__":
    start = datetime.datetime.now()
    print(f"Started at {start}")

    while 1:
        logging.info("Uygulamayı çalıştırmak için q tuşuna basınız.")
        # keyboard.wait("q")
        time.sleep(1)
        ss = take_screenshot()
        empty_tiles = check_inventory(ss)
        check_repair(ss)
        # check_problem(start, empty_tiles)
        time.sleep(60)