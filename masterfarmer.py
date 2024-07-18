import pyautogui
import numpy as np
import random
import time
import threading
import keyboard
import random


def click_cyan():
    randomt = random.uniform(0.12, 0.15)
    target_color = np.array([0, 255, 255])
    box_left, box_top, box_right, box_bottom = 8, 30, 521, 366

    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)

    box_pixels = screenshot_np[box_top:box_bottom, box_left:box_right, :]

    color_diff = np.abs(box_pixels - target_color)

    mask = np.all(color_diff <= 0, axis=2)


    if np.any(mask):
        y, x = np.where(mask)
        click_x = x[0] + box_left + 3
        click_y = y[0] + box_top + 3

        print(f"X:({click_x} Y:{click_y})")

        pyautogui.moveTo(click_x, click_y, randomt)
        pyautogui.click()
        return click_x, click_y

    return None

while True:

    click_cyan()
    time.sleep(0.3)