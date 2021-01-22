import pyautogui
import keyboard
from time import sleep
import win32api, win32con
import sys

x, y = [1280, 735]

while True:
    print("watching")
    if not keyboard.is_pressed("`"):
        if keyboard.is_pressed(";"):
            print("Program exiting")
            sys.exit(0)

    else:
        initial_pixel_value = pyautogui.pixel(x,y)
        while keyboard.is_pressed("`"):
            for index, value in enumerate(initial_pixel_value):
                if abs(value - pyautogui.pixel(x, y)[index]) > 25:
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                    sleep(0.15)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
                    print("I shot. Cooldown = 2s")
                    sleep(2)
                    break




