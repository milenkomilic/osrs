import pyautogui
import random
import mss
import cv2
import numpy as np
import keyboard
import time

def click_on_blue():
    start_time = time.time()
    target_color = np.array([255, 0, 0], dtype=np.uint8) # BGR = RGB INVERSO
    random_float = random.uniform(0.15, 0.22)
    box = {'top': 30, 'left': 8, 'width': 513, 'height': 336}
    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot)[:,:,:3]
    mask_blue = cv2.inRange(screenshot_np, target_color, target_color)
    contours, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"]) + box['left']
            cY = int(M["m01"] / M["m00"]) + box['top']
            screen_width, screen_height = pyautogui.size()
            if 0 <= cX < screen_width and 0 <= cY < screen_height:
                pyautogui.moveTo(cX, cY, random_float)
                pyautogui.click()
            else:
                print("Las coordenadas están fuera de la pantalla.")
            break
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(click_on_blue): {execution_time} seconds")


def is_woodcutting():

    start_time = time.time()

    box_left = 29
    box_top = 59
    box_right = 126
    box_bottom = 71
    box = {
        'left': box_left,
        'top': box_top,
        'width': box_right - box_left,
        'height': box_bottom - box_top
    }

    target_color = np.array([0, 255, 0], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])
    time.sleep(0.7)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_woodcutting): {execution_time} seconds")

    if np.any(matches):
        return "Found"
    else:
        return "Not Found"


def is_inv_full_maple_log():

    start_time = time.time()

    box_left = 701
    box_top = 394
    box_right = 719
    box_bottom = 412
    box = {
        'left': box_left,
        'top': box_top,
        'width': box_right - box_left,
        'height': box_bottom - box_top
    }

    target_color = np.array([108, 72, 12], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_inv_full): {execution_time} seconds")

    if np.any(matches):
        return "Found"
    else:
        return "Not Found"


def is_inv_full_maple_long():

    start_time = time.time()

    box_left = 707
    box_top = 392
    box_right = 715
    box_bottom = 402
    box = {
        'left': box_left,
        'top': box_top,
        'width': box_right - box_left,
        'height': box_bottom - box_top
    }

    target_color = np.array([126, 106, 99], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_inv_full): {execution_time} seconds")

    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def click_knife_1():
    box_left = 577
    box_top = 252
    box_right = 590
    box_bottom = 263

    # Calculate the center coordinates of the box
    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    # Add random offset to the box center coordinates
    offset_x = random.randint(-2, 2)
    offset_y = random.randint(-2, 2)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    random018024 = random.uniform(0.18, 0.24)
    # Move the mouse to the random position within the box
    pyautogui.moveTo(click_x, click_y, random018024)

    # Perform the click
    pyautogui.click()

def click_maple_log_2():
    box_left = 617
    box_top = 250
    box_right = 632
    box_bottom = 266

    # Calculate the center coordinates of the box
    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    # Add random offset to the box center coordinates
    offset_x = random.randint(-2, 2)
    offset_y = random.randint(-2, 2)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    random018024 = random.uniform(0.18, 0.24)
    # Move the mouse to the random position within the box
    pyautogui.moveTo(click_x, click_y, random018024)

    # Perform the click
    pyautogui.click()

def click_maple_log_21():
    box_left = 701
    box_top = 394
    box_right = 719
    box_bottom = 412

    # Calculate the center coordinates of the box
    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    # Add random offset to the box center coordinates
    offset_x = random.randint(-2, 2)
    offset_y = random.randint(-2, 2)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    random018024 = random.uniform(0.18, 0.24)
    # Move the mouse to the random position within the box
    pyautogui.moveTo(click_x, click_y, random018024)

    # Perform the click
    pyautogui.click()

def click_chat_fletch():
    box_left = 250
    box_top = 433
    box_right = 281
    box_bottom = 470

    # Calculate the center coordinates of the box
    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    # Add random offset to the box center coordinates
    offset_x = random.randint(-4, 4)
    offset_y = random.randint(-4, 4)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    random018024 = random.uniform(0.18, 0.24)
    # Move the mouse to the random position within the box
    pyautogui.moveTo(click_x, click_y, random018024)

    # Perform the click
    pyautogui.click()


def drop_inv():

    for inv_number in range(20, 1, -1):
        box_left = 569 + ((inv_number - 1) % 4) * 41
        box_top = 242 + ((inv_number - 1) // 4) * 35
        box_right = box_left + 31
        box_bottom = box_top + 29

        # Calculate the center coordinates of the box
        box_center_x = (box_left + box_right) // 2
        box_center_y = (box_top + box_bottom) // 2

        # Add random offset to the box center coordinates
        offset_x = random.randint(-10, 10)
        offset_y = random.randint(-10, 10)
        click_x = box_center_x + offset_x
        click_y = box_center_y + offset_y

        # Move the mouse to the random position within the box
        random013016 = random.uniform(0.13, 0.16)
        pyautogui.moveTo(click_x, click_y, random013016)

        # Perform the click
        pyautogui.click()

running = False


def start_script():
    global running
    print("Script started")
    running = True


def stop_script():
    global running
    print("Script stopped")
    running = False


keyboard.add_hotkey("F6", start_script)
keyboard.add_hotkey("F7", stop_script)

while True:
    if running:

        if keyboard.is_pressed("F7"):
            break

        wc_status = is_woodcutting()
        if wc_status == "Found":
            pass
        else:
            inv_status = is_inv_full_maple_log()
            randomt = random.uniform(0.05, 0.08)
            if inv_status == "Found":
                click_knife_1()
                time.sleep(randomt)
                click_maple_log_2()
                time.sleep(randomt+0.6)
                click_chat_fletch()
                time.sleep(35)
                inv_status = is_inv_full_maple_long()
                if inv_status == "Found":
                    drop_inv()
                else:
                    click_knife_1()
                    time.sleep(randomt)
                    click_maple_log_21()
                    time.sleep(randomt+0.6)
                    click_chat_fletch()
                    time.sleep(35)
                    drop_inv()
            else:
                click_on_blue()
                time.sleep(randomt+1.9)