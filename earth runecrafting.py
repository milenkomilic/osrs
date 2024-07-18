import pyautogui
import numpy as np
import random
import time
import threading
import keyboard

loop_running = False

def click_on_cyan():
    target_color = np.array([0, 255, 255])
    box_left, box_top, box_right, box_bottom = 8, 30, 521, 366

    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)

    box_pixels = screenshot_np[box_top:box_bottom, box_left:box_right, :]

    # Calculate the color difference in the entire box at once
    color_diff = np.abs(box_pixels - target_color)

    # Check if any pixel in the box is within the color difference threshold
    mask = np.all(color_diff <= 1, axis=2)


    if np.any(mask):
        y, x = np.where(mask)
        click_x = x[0] + box_left
        click_y = y[0] + box_top + 10

        pyautogui.moveTo(click_x, click_y, 0.3)
        pyautogui.click()
        return click_x, click_y

    return None

def click_on_cyan_minimap():
    target_color = np.array([0, 255, 255])
    box_left, box_top, box_right, box_bottom = 592, 58, 712, 164

    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)

    box_pixels = screenshot_np[box_top:box_bottom, box_left:box_right, :]

    # Calculate the color difference in the entire box at once
    color_diff = np.abs(box_pixels - target_color)

    # Check if any pixel in the box is within the color difference threshold
    mask = np.all(color_diff <= 1, axis=2)


    if np.any(mask):
        y, x = np.where(mask)
        click_x = x[0] + box_left
        click_y = y[0] + box_top + 10

        pyautogui.moveTo(click_x, click_y, 0.3)
        pyautogui.click()
        return click_x, click_y

    return None

def click_on_cyan_minimap2():
    target_color = np.array([0, 255, 255])
    box_left, box_top, box_right, box_bottom = 592, 58, 712, 164

    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)

    box_pixels = screenshot_np[box_top:box_bottom, box_left:box_right, :]

    # Calculate the color difference in the entire box at once
    color_diff = np.abs(box_pixels - target_color)

    # Check if any pixel in the box is within the color difference threshold
    mask = np.all(color_diff <= 1, axis=2)


    if np.any(mask):
        y, x = np.where(mask)
        click_x = x[0] + box_left
        click_y = y[0] + box_top

        pyautogui.moveTo(click_x, click_y, 0.3)
        pyautogui.click()
        return click_x, click_y

    return None


def click_altar():
    target_color = np.array([0, 255, 255])
    box_left, box_top, box_right, box_bottom = 8, 30, 521, 366

    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)

    box_pixels = screenshot_np[box_top:box_bottom, box_left:box_right, :]

    # Calculate the color difference in the entire box at once
    color_diff = np.abs(box_pixels - target_color)

    # Check if any pixel in the box is within the color difference threshold
    mask = np.all(color_diff <= 1, axis=2)


    if np.any(mask):
        y, x = np.where(mask)
        click_x = x[0] + box_left + 10
        click_y = y[0] + box_top + 10

        pyautogui.moveTo(click_x, click_y, 0.3)
        pyautogui.click()
        return click_x, click_y

    return None


def click_minimap_1():
    box_left = 712
    box_top = 79
    box_right = 717
    box_bottom = 85

    # Calculate the center coordinates of the box
    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    # Add random offset to the box center coordinates
    offset_x = random.randint(-3, 3)
    offset_y = random.randint(-3, 3)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    # Move the mouse to the random position within the box
    pyautogui.moveTo(click_x, click_y, 0.155)

    # Perform the click
    pyautogui.click()


def click_minimap_2():
    box_left = 645
    box_top = 37
    box_right = 650
    box_bottom = 43

    # Calculate the center coordinates of the box
    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    # Add random offset to the box center coordinates
    offset_x = random.randint(-3, 3)
    offset_y = random.randint(-3, 3)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    # Move the mouse to the random position within the box
    pyautogui.moveTo(click_x, click_y, 0.155)

    # Perform the click
    pyautogui.click()


def click_minimap_3():
    box_left = 685
    box_top = 49
    box_right = 690
    box_bottom = 57

    # Calculate the center coordinates of the box
    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    # Add random offset to the box center coordinates
    offset_x = random.randint(-3, 3)
    offset_y = random.randint(-3, 3)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    # Move the mouse to the random position within the box
    pyautogui.moveTo(click_x, click_y, 0.155)

    # Perform the click
    pyautogui.click()


def click_minimap_4():
    box_left = 647
    box_top = 88
    box_right = 651
    box_bottom = 94

    # Calculate the center coordinates of the box
    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    # Add random offset to the box center coordinates
    offset_x = random.randint(-3, 3)
    offset_y = random.randint(-3, 3)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    # Move the mouse to the random position within the box
    pyautogui.moveTo(click_x, click_y, 0.155)

    # Perform the click
    pyautogui.click()


def click_spellbook():
    box_left = 739
    box_top = 205
    box_right = 753
    box_bottom = 216

    # Calculate the center coordinates of the box
    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    # Add random offset to the box center coordinates
    offset_x = random.randint(-3, 3)
    offset_y = random.randint(-3, 3)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    # Move the mouse to the random position within the box
    pyautogui.moveTo(click_x, click_y, 0.155)

    # Perform the click
    pyautogui.click()


def click_varrock_tp():
    box_left = 587
    box_top = 286
    box_right = 598
    box_bottom = 296

    # Calculate the center coordinates of the box
    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    # Add random offset to the box center coordinates
    offset_x = random.randint(-3, 3)
    offset_y = random.randint(-3, 3)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    # Move the mouse to the random position within the box
    pyautogui.moveTo(click_x, click_y, 0.155)

    # Perform the click
    pyautogui.click()


def click_minimap_5():
    box_left = 702
    box_top = 84
    box_right = 707
    box_bottom = 90

    # Calculate the center coordinates of the box
    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    # Add random offset to the box center coordinates
    offset_x = random.randint(-3, 3)
    offset_y = random.randint(-3, 3)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    # Move the mouse to the random position within the box
    pyautogui.moveTo(click_x, click_y, 0.155)

    # Perform the click
    pyautogui.click()


def click_minimap_6():
    box_left = 683
    box_top = 146
    box_right = 687
    box_bottom = 149

    # Calculate the center coordinates of the box
    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    # Add random offset to the box center coordinates
    offset_x = random.randint(-3, 3)
    offset_y = random.randint(-3, 3)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    # Move the mouse to the random position within the box
    pyautogui.moveTo(click_x, click_y, 0.155)

    # Perform the click
    pyautogui.click()

def click_minimap_7():
    box_left = 712
    box_top = 111
    box_right = 716
    box_bottom = 116

    # Calculate the center coordinates of the box
    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    # Add random offset to the box center coordinates
    offset_x = random.randint(-3, 3)
    offset_y = random.randint(-3, 3)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    # Move the mouse to the random position within the box
    pyautogui.moveTo(click_x, click_y, 0.155)

    # Perform the click
    pyautogui.click()


def click_pure_ess():
    box_left = 418
    box_top = 114
    box_right = 440
    box_bottom = 131

    # Calculate the center coordinates of the box
    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    # Add random offset to the box center coordinates
    offset_x = random.randint(-3, 3)
    offset_y = random.randint(-3, 3)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    # Move the mouse to the random position within the box
    pyautogui.moveTo(click_x, click_y, 0.155)

    # Perform the click
    pyautogui.click()


def is_run_available():

    target_color = np.array([73, 73, 71])  #Run is full

    box_left = 567
    box_top = 161
    box_right = 571
    box_bottom = 162

    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    box_pixels = screenshot_np[box_top:box_bottom, box_left:box_right, :]

    target_found = np.any(np.all(np.abs(box_pixels - target_color) <= 0, axis=2))

    if target_found:
        return "Full"
    else:
        return "No color found"


def click_run():
    box_left = 562
    box_top = 142
    box_right = 577
    box_bottom = 158

    # Calculate the center coordinates of the box
    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    # Add random offset to the box center coordinates
    offset_x = random.randint(-3, 3)
    offset_y = random.randint(-3, 3)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    # Move the mouse to the random position within the box
    pyautogui.moveTo(click_x, click_y, 0.155)

    # Perform the click
    pyautogui.click()


def loop_function():
    global loop_running

    # Initialize a flag to control 
    runecrafting_mode = True

    while loop_running:

        if not loop_running:
            print("Loop stopped.")
            break

        if runecrafting_mode == True:
            while True :
                if is_run_available() == "Full":
                    click_run()
                    time.sleep(0.5)
                    click_on_cyan()     #Bank
                    time.sleep(3)
                    click_pure_ess()
                    time.sleep(1)
                    click_minimap_1()
                    time.sleep(9)
                    click_minimap_1()
                    time.sleep(8)
                    click_minimap_2()
                    time.sleep(8)
                    click_on_cyan_minimap2()
                    time.sleep(6)
                    click_minimap_5()
                    time.sleep(8)
                    click_altar()     #Enter altar
                    time.sleep(2)
                    click_minimap_4()
                    time.sleep(3)
                    click_altar()     #Click altar
                    time.sleep(3)
                    click_varrock_tp()
                    time.sleep(3)
                    click_minimap_1()
                    time.sleep(8)
                    click_minimap_7()
                    time.sleep(8)
                    click_on_cyan_minimap()
                    time.sleep(8)
                    click_run()
                else:
                    click_on_cyan()     #Bank
                    time.sleep(3)
                    click_pure_ess()
                    time.sleep(1)
                    click_minimap_1()
                    time.sleep(14)
                    click_minimap_1()
                    time.sleep(13)
                    click_minimap_2()
                    time.sleep(13)
                    click_on_cyan_minimap2()
                    time.sleep(9)
                    click_minimap_5()
                    time.sleep(11)
                    click_altar()     #Enter altar
                    time.sleep(2)
                    click_minimap_4()
                    time.sleep(5)
                    click_altar()     #Click altar
                    time.sleep(3)
                    click_varrock_tp()
                    time.sleep(3)
                    click_minimap_1()
                    time.sleep(12)
                    click_minimap_7()
                    time.sleep(12)
                    click_on_cyan_minimap()
                    time.sleep(9)


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
    if keyboard.is_pressed('f9'):
        start_loop()
    elif keyboard.is_pressed('f10'):
        stop_loop()
    elif keyboard.is_pressed('esc'):
        break
    time.sleep(0.1)