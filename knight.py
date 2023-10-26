import pyautogui
from PIL import Image
import pytesseract
from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

print('Bitti')
custom_config = r'-l eng --psm 3'
print(pytesseract.image_to_string(Image.open('i1.jpg'), config=custom_config))
