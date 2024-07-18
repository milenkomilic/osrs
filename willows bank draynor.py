import pyautogui
import random
import mss
import cv2
import numpy as np
import keyboard
import time

def click_on_pink():
    start_time = time.time()
    target_color = np.array([255, 0, 255], dtype=np.uint8) # BGR = RGB INVERSO
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
    print(f"Execution time(click_on_green): {execution_time} seconds")

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

def is_deposit_open():

    start_time = time.time()

    box_left = 367
    box_top = 74
    box_right = 377
    box_bottom = 85
    box = {
        'left': box_left,
        'top': box_top,
        'width': box_right - box_left,
        'height': box_bottom - box_top
    }

    target_color = np.array([255, 152, 31], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_deposit_open): {execution_time} seconds")

    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def is_inv_full():

    start_time = time.time()

    box_left = 700
    box_top = 468
    box_right = 720
    box_bottom = 477
    box = {
        'left': box_left,
        'top': box_top,
        'width': box_right - box_left,
        'height': box_bottom - box_top
    }

    target_color = np.array([80, 71, 26], dtype=np.uint8)

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

def click_deposit():
    box_left = 331
    box_top = 301
    box_right = 347
    box_bottom = 312

    # Calculate the center coordinates of the box
    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    # Add random offset to the box center coordinates
    offset_x = random.randint(-2, 2)
    offset_y = random.randint(-2, 2)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    # Move the mouse to the random position within the box
    pyautogui.moveTo(click_x, click_y, 0.2)

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

        wc_status = is_woodcutting()
        if wc_status == "Found":
            pass
        else:
            inv_status = is_inv_full()
            if inv_status == "Found":
                click_on_pink()
                time.sleep(9)
                bank_status = is_deposit_open()
                if bank_status == "Found":
                    click_deposit()
                    time.sleep(0.3)
                    pyautogui.press('esc')
                    time.sleep(0.3)
                else:
                    click_on_pink()
                    time.sleep(9)
                    click_deposit()
                    time.sleep(0.3)
                    pyautogui.press('esc')
                    time.sleep(0.3)
                click_on_blue()
                time.sleep(9)
            else:
                click_on_blue()
                time.sleep(2.5)

                
    if keyboard.is_pressed("F7"):
        break




