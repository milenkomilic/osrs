import numpy as np
import time
import mss
import cv2
import pyautogui
import random
import keyboard

def click_minimap_on_red():
    start_time = time.time()
    target_color = np.array([0, 0, 255], dtype=np.uint8) # BGR
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
    print(f"Execution time(click_minimap_on_red): {execution_time} seconds")


def click_on_blue():
    start_time = time.time()
    target_color = np.array([255, 0, 0], dtype=np.uint8) # BGR
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
    print(f"Execution time(click_on_blue): {execution_time} seconds")


def click_on_purple():
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
    print(f"Execution time(click_on_purple): {execution_time} seconds")

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
            break
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(click_on_smooth_purple): {execution_time} seconds")

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

def click_tp_to_house():
    box_left = 586
    box_top = 309
    box_right = 602
    box_bottom = 322

    # Calculate the center coordinates of the box
    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    # Add random offset to the box center coordinates
    offset_x = random.randint(-3, 3)
    offset_y = random.randint(-3, 3)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    random018024 = random.uniform(0.15, 0.20)
    # Move the mouse to the random position within the box
    pyautogui.moveTo(click_x, click_y, random018024)

    # Perform the click
    pyautogui.click()

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

def is_in_pvp_arena():

    start_time = time.time()

    box_left = 466
    box_top = 264
    box_right = 502
    box_bottom = 297
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([63, 46, 11], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_in_pvp_arena): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def is_in_fire_altar():

    start_time = time.time()

    box_left = 344
    box_top = 306
    box_right = 524
    box_bottom = 364
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([0, 0, 255], dtype=np.uint8)

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

def is_in_crafting_guild():

    start_time = time.time()

    box_left = 314
    box_top = 262
    box_right = 521
    box_bottom = 366
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([255, 0, 255], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_in_crafting_guild): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def is_inside_house():

    start_time = time.time()

    box_left = 10
    box_top = 36
    box_right = 503
    box_bottom = 350
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([0, 55, 0], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_inside_house): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

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

        counter = 0
        for x in range(0, 10):
            counter += 1
            print(counter)
            #Crafting guild start
            click_on_purple()
            time.sleep(3.5 + randomt)
            click_bank_slot_1()
            time.sleep(1.2 + randomt)
            pyautogui.press('esc')
            click_pouch_inv_1()
            time.sleep(0.3+randomt)
            click_pouch_inv_2()
            time.sleep(0.3+randomt)
            click_pouch_inv_3()
            time.sleep(0.3+randomt)
            click_on_purple()
            time.sleep(0.8 + randomt)
            click_bank_slot_1()
            time.sleep(1.2 + randomt)
            pyautogui.press('esc')
            click_spellbook()
            time.sleep(0.3 + randomt)
            click_tp_to_house()
            time.sleep(5 + randomt)
            while is_inside_house == "Not Found":
                click_spellbook()
                time.sleep(0.3 + randomt)
                click_tp_to_house()
                time.sleep(5 + randomt)
            else:
                if counter == 10:
                    click_on_smooth_purple()
                    time.sleep(2.8 + randomt)
                click_on_dark_green()
                time.sleep(6.5 + randomt)
                while is_in_pvp_arena() == "Not Found":
                    if counter == 10:
                        click_on_smooth_purple()
                        time.sleep(2.8 + randomt)
                    click_on_dark_green()
                    time.sleep(6.5 + randomt)
                else:
                    click_minimap_on_red()
                    time.sleep(5 + randomt)
                    pyautogui.press('f2')
                    time.sleep(3 + randomt)
                    click_on_blue()
                    time.sleep(3 + randomt)
                    while is_in_fire_altar() == "Not Found":
                        click_minimap_on_red()
                        time.sleep(5 + randomt)
                        pyautogui.press('f2')
                        time.sleep(3 + randomt)
                        click_on_blue()
                        time.sleep(3 + randomt)
                    else:
                        click_on_blue()
                        time.sleep(5 + randomt)
                        empty_pouch_inv_1()
                        time.sleep(0.3+randomt)
                        empty_pouch_inv_2()
                        time.sleep(0.3+randomt)
                        empty_pouch_inv_3()
                        time.sleep(0.3+randomt)
                        click_on_blue()
                        time.sleep(1.8 + randomt)
                        click_inv_slot_28()
                        time.sleep(5.5 + randomt)



