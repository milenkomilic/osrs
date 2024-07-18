import pyautogui
import numpy as np
import random
import time
import threading
import keyboard
import mouse


loop_running = False


def go_back_worlds():
    rand = random.randint(1,5)
    vrvznx = random.randint(100, 200)
    randms = vrvznx / 1000
    pyautogui.moveTo(647+rand, 510+rand, randms)    # 647 510/logout
    pyautogui.click(button='left')
    time.sleep(0.5)
    pyautogui.moveTo(639+rand, 275+rand, randms)    # 639 275/w302
    time.sleep(0.2)
    mouse.wheel(delta=20)
    time.sleep(0.2)
    pyautogui.click(button='left')
    time.sleep(10)


def shop_buy():
    rand = random.randint(1,5)
    vrvznx = random.randint(100, 200)
    randms = vrvznx / 1000
    pyautogui.moveTo(624+rand, 253+rand, randms)    # 624 253/second inv space
    pyautogui.click(button='left')
    time.sleep(0.5)
    pyautogui.moveTo(284+rand, 198+rand, randms)    # 284 198/buy buckets of sand on shop
    pyautogui.click(button='left')
    time.sleep(0.5)
    pyautogui.moveTo(375+rand, 197+rand, randms)    # 375 197/buy soda ash on shop
    pyautogui.click(button='left')
    time.sleep(0.5)
    pyautogui.moveTo(486+rand, 63+rand, randms)     # 486 63/exit shop
    pyautogui.click(button='left')
    time.sleep(0.5)
    pyautogui.moveTo(748+rand, 210+rand, randms)    # 748 210/magic spellbook
    pyautogui.click(button='left')
    time.sleep(0.5)
    pyautogui.moveTo(567+rand, 352+rand, randms)    # 567 352/glassmake spell
    pyautogui.click(button='left')
    time.sleep(0.5)
    pyautogui.moveTo(648+rand, 208+rand, randms)    # 585 255/inventory
    pyautogui.click(button='left')
    time.sleep(0.5)
    pyautogui.moveTo(585+rand, 255+rand, randms)    # 585 255/first inv space
    pyautogui.click(button='left')
    time.sleep(0.5)
    pyautogui.moveTo(624+rand, 253+rand, randms)    # 624 253/second inv space
    pyautogui.click(button='left')
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(25)
    pyautogui.keyDown('ctrl'); pyautogui.keyDown('shift'); pyautogui.keyDown('right')
    pyautogui.keyUp('right'); pyautogui.keyUp('shift'); pyautogui.keyUp('ctrl')
    time.sleep(8)


def find_charter_shop():
    # Define the coordinates of the top-left and bottom-right corners of the box
    box_left = 8
    box_top = 30
    box_right = 521
    box_bottom = 366

    # Example: searching for generic cyan color
    target_color = np.array([0, 255, 255])

    # Capture a screenshot and convert it to a NumPy array
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)

    # Extract the pixels within the box and check if they match the target color
    box_pixels = screenshot_np[box_top:box_bottom, box_left:box_right, :]
    target_found = False
    for y in range(box_bottom - box_top):
        if target_found:
            break
        for x in range(box_right - box_left):
            if target_found:
                break
            pixel_color = box_pixels[y, x, :]
            color_diff = np.abs(pixel_color - target_color)
            if np.all(color_diff <= 15):
                print(
                    f"Starting trade with npc XY: ({x + box_left}, {y + box_top})")
                click_x = x + box_left + 0  # Adjust the click location by a small offset
                click_y = y + box_top + 5  # Adjust the click location by a small offset
                pyautogui.moveTo(click_x, click_y, 0.3)
                time.sleep(0.2)
                pyautogui.click(button='left')
                time.sleep(1.3)
                target_found = True


def shop_open_check():
    # Define the coordinates of the top-left and bottom-right corners of the box
    box_left = 383
    box_top = 266
    box_right = 385
    box_bottom = 270

    # Define the target colors and box coordinates
    target_color_1 = np.array([73, 64, 52])

    # Capture a screenshot and convert it to a NumPy array
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)

    # Extract the pixels within the box and check if they match the target colors
    box_pixels = screenshot_np[box_top:box_bottom, box_left:box_right, :]
    target1_found = np.any(
        np.all(np.abs(box_pixels - target_color_1) <= 15, axis=2))

    # If either target color is found, return its name
    if target1_found:
        return "Found"
    else:
        return "No color found"


def loop_function():
    global loop_running
    next_time = time.time() + 550  # set the initial next execution time to 5 seconds from now
    while loop_running:
        if loop_running:  # Check if loop_running is still True
            find_charter_shop()
            time.sleep(0.5)
            checkshop = shop_open_check()
            if checkshop == "Found":
                checkshop = shop_open_check()
                shop_buy()

        # check if the current time is greater than or equal to the next execution time
        if time.time() >= next_time:
            time.sleep(5)
            print("Script hopping worlds")
            go_back_worlds()  # execute the function
            next_time = time.time() + 550  # set the next execution time to 5 seconds from now


def start_loop():
    global loop_running
    if not loop_running:
        loop_running = True
        print("Script running")
        threading.Thread(target=loop_function).start()
    else:
        print("Script already running")


def stop_loop():
    global loop_running
    if loop_running:
        loop_running = False
        print("Script stopping")
    else:
        print("Script not running")


while True:
    if keyboard.is_pressed('f1'):
        start_loop()
    elif keyboard.is_pressed('f2'):
        stop_loop()
    elif keyboard.is_pressed('esc'):
        break
    time.sleep(0.1)
