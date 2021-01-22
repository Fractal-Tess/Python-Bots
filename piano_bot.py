from pyautogui import pixel
from time import sleep
from keyboard import is_pressed
import win32api, win32con


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while not is_pressed("q"):
    if pixel(1775, 640)[0] <= 20:     
        click(1775, 640)
    if pixel(1900, 640)[0] <= 20:
        click(1900, 640)
    if pixel(2010, 640)[0] <= 20:
        click(2010, 640)
    if pixel(2110, 640)[0] <= 20:
        click(2110, 640)
