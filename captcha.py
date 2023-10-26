import time
import cv2
import easyocr
import keyboard
import pyautogui
import numpy
import win32api, win32con
import time
from datetime import datetime
from PIL import Image
import text

reader = easyocr.Reader(["en"])

img  = Image.open("captchas/captcha5.png")
img = numpy.asarray(img)

image = cv2.imread('captchas/captcha4.png')
gray = text.get_grayscale(image)
thresh = text.thresholding(gray)
opening = text.opening(gray)
canny = text.canny(gray)

result = reader.readtext(canny, detail=0)
print (result)