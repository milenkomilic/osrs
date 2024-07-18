import pyautogui
import random
import mss
import cv2
import numpy as np
import keyboard
import time

def click_on_dark_green():
    start_time = time.time()
    target_color = np.array([0, 55, 0], dtype=np.uint8) # BGR
    random_float = random.uniform(0.14, 0.18)
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
            pyautogui.moveTo(cX, cY, random_float)
            pyautogui.click()
            time.sleep(random_float)
            pyautogui.click()
            break
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(click_on_dark_green): {execution_time} seconds")

def click_on_smooth_purple():
    start_time = time.time()
    target_color = np.array([99, 0, 99], dtype=np.uint8) # BGR
    random_float = random.uniform(0.14, 0.18)
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
            pyautogui.moveTo(cX, cY, random_float)
            pyautogui.click()
            time.sleep(random_float)
            pyautogui.click()
            break
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(click_on_smooth_purple): {execution_time} seconds")

def click_on_pink():
    start_time = time.time()
    target_color = np.array([255, 0, 255], dtype=np.uint8) # BGR
    random_float = random.uniform(0.14, 0.18)
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
            pyautogui.moveTo(cX, cY, random_float)
            pyautogui.click()
            break
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(click_on_pink): {execution_time} seconds")

def click_minimap_soft_purple():
    start_time = time.time()
    target_color = np.array([255, 100, 100], dtype=np.uint8) # BGR
    random_float = random.uniform(0.14, 0.18)
    box = {'top': 29, 'left': 565, 'width': 757-565, 'height': 191-29}
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
            pyautogui.moveTo(cX, cY, random_float)
            pyautogui.click()
            break
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(click_minimap_soft_purple): {execution_time} seconds")

def is_any_pouch_broken():
    start_time = time.time()

    box_left = 561
    box_top = 237
    box_right = 690
    box_bottom = 267
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([50, 39, 39], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_in_fire_altar): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def run_energy():
    box_left = 564
    box_top = 137
    box_right = 571
    box_bottom = 143
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([141, 141, 137], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    if np.any(matches):
        return "Found"
    else:
        return "Not Found"


def is_bank_open():
    box_left = 414
    box_top = 43
    box_right = 433
    box_bottom = 59
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([72, 62, 51], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    if np.any(matches):
        return "Found"
    else:
        return "Not Found"


def click_bank_slot_1():
    box_left = 82
    box_top = 119
    box_right = 100
    box_bottom = 135

    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    offset_x = random.randint(-6, 6)
    offset_y = random.randint(-6, 6)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    randomt = random.uniform(0.12, 0.18)
    pyautogui.moveTo(click_x, click_y, randomt)
    pyautogui.click()

def click_pouch_inv_1():
    box_left = 573
    box_top = 252
    box_right = 588
    box_bottom = 266

    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    offset_x = random.randint(-4, 4)
    offset_y = random.randint(-4, 4)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    randomt = random.uniform(0.02, 0.04)
    pyautogui.moveTo(click_x, click_y, randomt)
    pyautogui.click()


def click_pouch_inv_2():
    box_left = 615
    box_top = 247
    box_right = 629
    box_bottom = 263

    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    offset_x = random.randint(-4, 4)
    offset_y = random.randint(-4, 4)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    randomt = random.uniform(0.02, 0.04)
    pyautogui.moveTo(click_x, click_y, randomt)
    pyautogui.click()


def click_pouch_inv_3():
    box_left = 655
    box_top = 249
    box_right = 669
    box_bottom = 261

    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    offset_x = random.randint(-4, 4)
    offset_y = random.randint(-4, 4)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    randomt = random.uniform(0.02, 0.04)
    pyautogui.moveTo(click_x, click_y, randomt)
    pyautogui.click()

def empty_pouch_inv_1():
    box_left = 573
    box_top = 252
    box_right = 588
    box_bottom = 266

    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    offset_x = random.randint(-4, 4)
    offset_y = random.randint(-4, 4)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    randomt = random.uniform(0.02, 0.04)
    pyautogui.moveTo(click_x, click_y, randomt)

    pyautogui.keyDown('shift')
    time.sleep(randomt)
    pyautogui.click()
    time.sleep(randomt)
    #pyautogui.keyUp('shift')

def empty_pouch_inv_2():
    box_left = 615
    box_top = 247
    box_right = 629
    box_bottom = 263

    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    offset_x = random.randint(-4, 4)
    offset_y = random.randint(-4, 4)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    randomt = random.uniform(0.02, 0.04)
    pyautogui.moveTo(click_x, click_y, randomt)

    #pyautogui.keyDown('shift')
    time.sleep(randomt)
    pyautogui.click()
    time.sleep(randomt)
    #pyautogui.keyUp('shift')


def empty_pouch_inv_3():
    box_left = 655
    box_top = 249
    box_right = 669
    box_bottom = 261

    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    offset_x = random.randint(-4, 4)
    offset_y = random.randint(-4, 4)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    randomt = random.uniform(0.02, 0.04)
    pyautogui.moveTo(click_x, click_y, randomt)

    #pyautogui.keyDown('shift')
    time.sleep(randomt)
    pyautogui.click()
    time.sleep(randomt)
    pyautogui.keyUp('shift')

def click_spellbook():
    box_left = 742
    box_top = 207
    box_right = 754
    box_bottom = 221

    # Calculate the center coordinates of the box
    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    # Add random offset to the box center coordinates
    offset_x = random.randint(-3, 3)
    offset_y = random.randint(-3, 3)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    random018024 = random.uniform(0.17, 0.23)
    # Move the mouse to the random position within the box
    pyautogui.moveTo(click_x, click_y, random018024)

    # Perform the click
    pyautogui.click()

def click_lunar_teleport():
    box_left = 679
    box_top = 263
    box_right = 690
    box_bottom = 276

    # Calculate the center coordinates of the box
    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    # Add random offset to the box center coordinates
    offset_x = random.randint(-3, 3)
    offset_y = random.randint(-3, 3)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    random018024 = random.uniform(0.17, 0.23)
    # Move the mouse to the random position within the box
    pyautogui.moveTo(click_x, click_y, random018024)

    # Perform the click
    pyautogui.click()

def click_npc_contact():
    box_left = 559
    box_top = 265
    box_right = 569
    box_bottom = 276

    # Calculate the center coordinates of the box
    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    # Add random offset to the box center coordinates
    offset_x = random.randint(-3, 3)
    offset_y = random.randint(-3, 3)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    random018024 = random.uniform(0.17, 0.23)
    # Move the mouse to the random position within the box
    pyautogui.moveTo(click_x, click_y, random018024)

    # Perform the click
    pyautogui.click()

def click_npc_contact_dark_mage():
    box_left = 238
    box_top = 112
    box_right = 272
    box_bottom = 159

    # Calculate the center coordinates of the box
    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    # Add random offset to the box center coordinates
    offset_x = random.randint(-3, 3)
    offset_y = random.randint(-3, 3)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    random018024 = random.uniform(0.17, 0.23)
    # Move the mouse to the random position within the box
    pyautogui.moveTo(click_x, click_y, random018024)

    # Perform the click
    pyautogui.click()

def click_inv_slot_28():
    box_left = 699
    box_top = 467
    box_right = 715
    box_bottom = 484

    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    offset_x = random.randint(-3, 3)
    offset_y = random.randint(-3, 3)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    randomt = random.uniform(0.14, 0.17)
    pyautogui.moveTo(click_x, click_y, randomt)

    pyautogui.click()

def click_walk_to_altar():
    box_left = 673
    box_top = 158
    box_right = 678
    box_bottom = 160

    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    offset_x = random.randint(-2, 2)
    offset_y = random.randint(-2, 2)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    randomt = random.uniform(0.14, 0.17)
    pyautogui.moveTo(click_x, click_y, randomt)

    pyautogui.click()


def click_run():
    box_left = 562
    box_top = 143
    box_right = 578
    box_bottom = 159

    # Calculate the center coordinates of the box
    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    # Add random offset to the box center coordinates
    offset_x = random.randint(-3, 3)
    offset_y = random.randint(-3, 3)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    random018024 = random.uniform(0.08, 0.04)
    # Move the mouse to the random position within the box
    pyautogui.moveTo(click_x, click_y, random018024)

    # Perform the click
    pyautogui.click()



running = False
randomt = random.uniform(0.01, 0.03)

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

        if run_energy() == "Found":
            click_run()

        counter = 0
        for x in range(0, 2):
            counter += 1
            print(counter)
            pyautogui.press('f2')
            time.sleep(0.1 + randomt)
            click_on_pink()
            time.sleep(7.5 + randomt)
            if is_any_pouch_broken() == "Found":
                pyautogui.press('f4')
                time.sleep(0.5)
                click_npc_contact()
                time.sleep(1.9)
                click_npc_contact_dark_mage()
                time.sleep(5.5)
                pyautogui.press('space')
                time.sleep(1)
                pyautogui.press('2')
                time.sleep(1)
                pyautogui.press('space')
                time.sleep(1)
            else:
                click_on_dark_green()
                time.sleep(1.6 + randomt)
                while is_bank_open() == "Not Found":
                    click_on_pink()
                    time.sleep(7.5 + randomt)
                    click_on_dark_green()
                    time.sleep(1.6 + randomt)
                else:
                    click_bank_slot_1()
                    time.sleep(0.6 + randomt)
                    pyautogui.press('esc')
                    click_pouch_inv_1()
                    time.sleep(0.2+randomt)
                    click_pouch_inv_2()
                    time.sleep(0.2+randomt)
                    click_pouch_inv_3()
                    time.sleep(0.2+randomt)
                    click_on_dark_green()
                    time.sleep(0.7 + randomt)
                    click_bank_slot_1()
                    time.sleep(0.6 + randomt)
                    pyautogui.press('esc')
                    click_walk_to_altar()
                    time.sleep(10.5 + randomt)
                    click_walk_to_altar()
                    time.sleep(8 + randomt)
                    click_minimap_soft_purple()
                    time.sleep(12 + randomt)
                    click_on_smooth_purple()
                    time.sleep(0.6 + randomt)
                    empty_pouch_inv_1()
                    time.sleep(0.2+randomt)
                    empty_pouch_inv_2()
                    time.sleep(0.2+randomt)
                    empty_pouch_inv_3()
                    time.sleep(0.2+randomt)
                    click_on_smooth_purple()
                    time.sleep(0.5 + randomt)
                    if counter == 2:
                        click_inv_slot_28()
                        time.sleep(6 + randomt)
                        click_on_smooth_purple()
                        time.sleep(3 + randomt)
                        pyautogui.press('f4')
                        time.sleep(0.5 + randomt)
                        click_lunar_teleport()
                        time.sleep(5 + randomt)
                    else:    
                        pyautogui.press('f4')
                        time.sleep(0.3 + randomt)
                        click_lunar_teleport()
                        time.sleep(5 + randomt)
