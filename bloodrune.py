import numpy as np
import time
import mss
import cv2
import pyautogui
import random
import keyboard

def click_on_green_full_screen():
    start_time = time.time()
    target_color = np.array([0, 255, 0], dtype=np.uint8) # BGR
    random_float = random.uniform(0.15, 0.22)
    box = {'left': 4, 'top': 35, 'width': 517, 'height': 370}
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
    print(f"Execution time(click_on_green_full_screen): {execution_time} seconds")

def click_on_green_half_screen():
    start_time = time.time()
    target_color = np.array([0, 255, 0], dtype=np.uint8) # BGR
    random_float = random.uniform(0.15, 0.22)
    box = {'left': 4, 'top': 35, 'width': 326, 'height': 259}
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
            pyautogui.moveTo(cX+4, cY-2, random_float)
            pyautogui.click()
            break
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(click_on_green_half_screen): {execution_time} seconds")

def click_on_dark_altar():
    start_time = time.time()
    target_color = np.array([226, 43, 138], dtype=np.uint8) # BGR
    random_float = random.uniform(0.15, 0.22)
    box = {'top': 35, 'left': 4, 'width': 517, 'height': 370}
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
    print(f"Execution time(click_on_dark_altar): {execution_time} seconds")

def click_on_blue():
    start_time = time.time()
    target_color = np.array([255, 0, 0], dtype=np.uint8) # BGR
    random_float = random.uniform(0.15, 0.22)
    box = {'top': 35, 'left': 4, 'width': 517, 'height': 370}
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

def click_on_red():
    start_time = time.time()
    target_color = np.array([0, 0, 255], dtype=np.uint8) # BGR
    random_float = random.uniform(0.15, 0.22)
    box = {'top': 35, 'left': 4, 'width': 517, 'height': 370}
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
    print(f"Execution time(click_on_red): {execution_time} seconds")

def click_on_coral():
    start_time = time.time()
    target_color = np.array([80, 127, 255], dtype=np.uint8) # BGR
    random_float = random.uniform(0.15, 0.22)
    box = {'top': 35, 'left': 4, 'width': 517, 'height': 370}
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
    print(f"Execution time(click_on_coral): {execution_time} seconds")


def click_minimap_on_blue():
    start_time = time.time()
    target_color = np.array([255, 0, 0], dtype=np.uint8) # BGR
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
    print(f"Execution time(click_minimap_on_blue): {execution_time} seconds")

def click_minimap_on_aqua():
    start_time = time.time()
    target_color = np.array([212, 255, 127], dtype=np.uint8) # BGR
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
    print(f"Execution time(click_minimap_on_aqua): {execution_time} seconds")

def click_minimap_on_yellow():
    start_time = time.time()
    target_color = np.array([102, 255, 255], dtype=np.uint8) # BGR
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
    print(f"Execution time(click_minimap_on_yellow): {execution_time} seconds")

def click_minimap_on_rose():
    start_time = time.time()
    target_color = np.array([208, 127, 255], dtype=np.uint8) # BGR
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
    print(f"Execution time(click_minimap_on_rose): {execution_time} seconds")

def click_minimap_on_violet():
    start_time = time.time()
    target_color = np.array([255, 0, 255], dtype=np.uint8) # BGR
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
    print(f"Execution time(click_minimap_on_violet): {execution_time} seconds")

def is_standing_on_blue():
    start_time = time.time()

    box_left = 255
    box_top = 192
    box_right = 272
    box_bottom = 205
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
    print(f"Execution time(is_standing_on_blue): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"
    
def is_standing_on_red():
    start_time = time.time()

    box_left = 255
    box_top = 192
    box_right = 272
    box_bottom = 205
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([255, 0, 0], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_standing_on_red): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def is_standing_on_violet():
    start_time = time.time()

    box_left = 255
    box_top = 192
    box_right = 272
    box_bottom = 205
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
    print(f"Execution time(is_standing_on_violet): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def is_standing_on_rose():
    start_time = time.time()

    box_left = 255
    box_top = 192
    box_right = 272
    box_bottom = 205
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([255, 127, 208], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_standing_on_rose): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"


def is_standing_on_yellow():
    start_time = time.time()

    box_left = 255
    box_top = 192
    box_right = 272
    box_bottom = 205
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([255, 255, 102], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_standing_on_yellow): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"
    
def is_standing_on_aqua():
    start_time = time.time()

    box_left = 255
    box_top = 192
    box_right = 272
    box_bottom = 205
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([127, 255, 212], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_standing_on_aqua): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def is_purple_standing():
    start_time = time.time()

    box_left = 252
    box_top = 189
    box_right = 276
    box_bottom = 210
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([138, 43, 226], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_purple_standing): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def is_inv_1_DarkEssenceFragments():
    start_time = time.time()

    box_left = 573
    box_top = 250
    box_right = 592
    box_bottom = 266
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([82, 65, 82], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_inv_1_DarkEssenceFragments): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def is_inv_full_of_DenseEssenceBlocks():
    start_time = time.time()

    box_left = 616
    box_top = 464
    box_right = 636
    box_bottom = 482
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([133, 133, 135], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_inv_full_of_DenseEssenceBlocks): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"


def is_inv_full_of_DarkEssenceBlocks():
    start_time = time.time()

    box_left = 616
    box_top = 464
    box_right = 636
    box_bottom = 482
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([107, 105, 101], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_inv_full_of_DarkEssenceBlocks): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def is_mining():
    box_left = 42
    box_top = 57
    box_right = 110
    box_bottom = 72
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([0, 255, 0], dtype=np.uint8)

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

def is_inv_full_of_essence():
    box_left = 616
    box_top = 463
    box_right = 637
    box_bottom = 483
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([133, 133, 135], dtype=np.uint8)

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

def click_inv_slot_27():
    box_left = 660
    box_top = 465
    box_right = 673
    box_bottom = 481

    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    offset_x = random.randint(-9, 9)
    offset_y = random.randint(-9, 9)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    randomt = random.uniform(0.08, 0.14)
    pyautogui.moveTo(click_x, click_y, randomt)

    pyautogui.click()

def click_inv_slot_26():
    box_left = 615
    box_top = 464
    box_right = 635
    box_bottom = 481

    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    offset_x = random.randint(-9, 9)
    offset_y = random.randint(-9, 9)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    randomt = random.uniform(0.08, 0.14)
    pyautogui.moveTo(click_x, click_y, randomt)

    pyautogui.click()

running = False
randomt = random.uniform(0.01, 0.03)
randoml = random.uniform(0.001, 0.003)

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
        
        restart_flow = False
        while not restart_flow:

            while True:
                if is_mining() == "Not Found":
                    if is_inv_full_of_DenseEssenceBlocks() == "Not Found":
                        click_on_coral()
                        time.sleep(7+randomt)
                    else:
                        break
                else:
                    time.sleep(2+randomt)

            while True:
                if is_standing_on_blue() == "Not Found":
                    click_minimap_on_blue()
                    time.sleep(12+randomt)
                else:
                    print("Blue tile checkpoint")
                    break
            
            while True:
                if is_standing_on_violet() == "Not Found":
                    click_on_green_full_screen()
                    time.sleep(3.1+randomt)
                else:
                    print("Violet tile checkpoint")
                    break

            while True:
                if is_standing_on_rose() == "Not Found":
                    click_minimap_on_rose()
                    time.sleep(10.5+randomt)
                else:
                    print("Rose tile checkpoint")
                    break

            while True:
                if is_inv_full_of_DarkEssenceBlocks() == "Not Found":
                    click_on_dark_altar()
                    time.sleep(7.4+randomt)
                else:
                    print("Dark essence checkpoint")
                    break

            while True:
                if is_inv_1_DarkEssenceFragments() == "Not Found":
                    while True:
                        if is_standing_on_rose() == "Not Found":
                            click_minimap_on_rose()
                            time.sleep(7.2+randomt)
                        else:
                            print("Rose tile checkpoint")
                            break

                    while True:
                        if is_standing_on_violet() == "Not Found":
                            click_minimap_on_violet()
                            time.sleep(11+randomt)
                        else:
                            print("Violet tile checkpoint")
                            break                    

                    while True:
                        if is_standing_on_blue() == "Not Found":
                            click_on_green_full_screen()
                            time.sleep(3.6+randomt)
                        else:
                            print("Blue tile checkpoint")
                            click_on_coral()
                            time.sleep(90+randomt)
                            if is_inv_full_of_DarkEssenceBlocks() == "Found":
                                for _ in range(26):
                                    click_inv_slot_27()
                                    time.sleep(randoml)
                                    click_inv_slot_26()
                                    time.sleep(randoml)
                            if is_inv_1_DarkEssenceFragments() == "Found":
                                restart_flow = True
                                break
                if restart_flow:
                    break

                while True:
                    if is_standing_on_yellow() == "Not Found":
                        click_minimap_on_yellow()
                        time.sleep(40+randomt)
                    else:
                        print("Yellow tile checkpoint")
                        break

                while True:
                    if is_standing_on_red() == "Not Found":
                        click_on_red()
                        time.sleep(8+randomt)
                    else:
                        print("Red tile checkpoint")
                        break

                while True:
                    if is_standing_on_violet() == "Not Found":
                        click_minimap_on_violet()
                        time.sleep(13.3+randomt)
                    else:
                        print("Violet tile checkpoint")
                        break

                while True:
                    if is_inv_full_of_DarkEssenceBlocks() == "Not Found":
                        click_minimap_on_aqua()
                        time.sleep(14+randomt)
                        break
                    else:
                        click_on_blue()
                        time.sleep(2+randomt)
                        for _ in range(26):
                            click_inv_slot_27()
                            time.sleep(randoml)
                            click_inv_slot_26()
                            time.sleep(randoml)
                        click_on_blue()
                        time.sleep(2+randomt)

                while True:
                    if is_standing_on_aqua() == "Not Found":
                        click_minimap_on_aqua()
                        time.sleep(11+randomt)
                    else:
                        print("Aqua tile checkpoint")
                        break
                
                while True:
                    if is_purple_standing() == "Not Found":
                        click_on_green_half_screen()
                        time.sleep(6+randomt)
                    else:
                        print("Purple tile checkpoint")
                        break

                while True:
                    if is_mining() == "Not Found":
                        if is_inv_full_of_DenseEssenceBlocks() == "Not Found":
                            click_on_coral()
                            time.sleep(7+randomt)
                        else:
                            restart_flow = True
                            break
                    else:
                        time.sleep(2+randomt)

                if restart_flow:
                    break

