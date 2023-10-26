import multiprocessing
from multiprocessing import Pool
import time
import easyocr
import keyboard
import pyautogui
import numpy
import win32api, win32con
import time
from datetime import datetime
import logging
from openpyxl import Workbook, load_workbook

reader = easyocr.Reader(["en"])
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
wb_name = "knight.xlsx"
ws_name = "Pazar"

logging.basicConfig(level=logging.INFO)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)  # This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def get_item_picture(array):
    pic = pyautogui.screenshot(region=(650, 0, 800, 800))
    array.append(pic)


def append_worksheet(item, wb, ws):
    if not len(item) == 0:
        ws.append([item["seller"], item["name"], item["price"], item["date"]])
        wb.save(wb_name)


def analyze_picture(picture):
    picture = numpy.asarray(picture)
    result = reader.readtext(picture, detail=0)
    try:
        seller = result[0]
        item_name = result[1]
        price = int(result[result.index("Purchasing Price") + 1].replace(",", ""))

        logging.info(f"Seller: {seller} Item: {item_name} Price: {price}")
        item = {
            "seller": seller,
            "name": item_name,
            "price": price,
            "date": datetime.now(),
        }

        return item

    except Exception as ex:
        logging.debug("Cannot get item details, passing... ", ex)
        return {}


def getting_pictures(array):
    logging.info("Waiting for input")
    while 1:
        keyboard.wait("q")
        for x, y in coordinates:
            logging.debug("Processing an Item")
            click(x, y)
            # Eğer item yoksa geç renkten anla 34 33 17
            time.sleep(0.5)
            get_item_picture(array)


def analyzing_pictures(array):
    wb = load_workbook(wb_name)
    ws = wb[ws_name]
    while 1:
        logging.debug(len(array))
        if len(array) > 0:
            for pic in array[:]:
                logging.debug("Analyzing picture")
                item = analyze_picture(pic)
                logging.debug("Finished analyzing picture")
                append_worksheet(item, wb, ws)
                array.remove(pic)
                logging.info("Remaining items: %s" % len(array))
        time.sleep(3)


if __name__ == "__main__":
    mgr = multiprocessing.Manager()
    array = mgr.list()
    pool = Pool(processes=2)
    start = time.time()
    r1 = pool.apply_async(getting_pictures, args=[array])
    r2 = pool.apply_async(analyzing_pictures, args=[array])
    pool.close()
    pool.join()
    end = time.time()
    print("Time taken in seconds -", end - start)
    exit()