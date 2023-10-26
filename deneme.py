import multiprocessing
from multiprocessing import Pool
import time
import keyboard
import pyautogui
import numpy
import win32api, win32con
import time
from datetime import datetime
import logging
import pydirectinput
from time import sleep


def take_screenshot(x=1280, y=1000):
    pic = pyautogui.screenshot(region=(0, 0, x, y))
    # pic.save('images/ss-repair-3.png')
    return pic

# def locate_all_tiles(ss, tile, grayscale=False, confidence=0.90):
#     pass

### GENIE BAŞLATMA ###
ss = take_screenshot()
genie_start_btn_x, genie_start_btn_y = pyautogui.locateCenterOnScreen("images/genie_start_btn.png")
pyautogui.click(genie_start_btn_x, genie_start_btn_y)
print(genie_start_btn_x, genie_start_btn_y)