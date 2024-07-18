#CAMERA ZOOM 248/896

import numpy as np
import time
import mss
import cv2
import pyautogui
import random
import keyboard
import sys

def click_agi_pot():
    start_time = time.time()
    target_color = np.array([16, 149, 124], dtype=np.uint8) # BGR
    random_float = random.uniform(0.15, 0.22)
    box = {'top': 235, 'left': 554, 'width': 492, 'height': 739}
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


def click_on_green_full_screen():
    start_time = time.time()
    target_color = np.array([0, 255, 0], dtype=np.uint8) # BGR
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
    print(f"Execution time(click_on_green_full_screen): {execution_time} seconds")

def click_on_green_half_screen_down():
    start_time = time.time()
    target_color = np.array([0, 255, 0], dtype=np.uint8) # BGR
    random_float = random.uniform(0.15, 0.22)
    box = {'top': 6, 'left': 180, 'width': 522, 'height': 365}
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
    print(f"Execution time(click_on_green_half_screen_down): {execution_time} seconds")


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

def click_on_mark():
    start_time = time.time()
    target_color = np.array([19, 155, 177], dtype=np.uint8) # BGR
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
    print(f"Execution time(click_on_mark): {execution_time} seconds")

def is_mark_on_floor_1():
    start_time = time.time()

    box_left = 150
    box_top = 114
    box_right = 273
    box_bottom = 210
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([177, 155, 19], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_mark_on_floor_1): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"
    

def is_mark_on_floor_2():
    start_time = time.time()

    box_left = 132
    box_top = 161
    box_right = 239
    box_bottom = 242
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([177, 155, 19], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_mark_on_floor_2): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"
    

def is_mark_on_floor_3():
    start_time = time.time()

    box_left = 268
    box_top = 175
    box_right = 342
    box_bottom = 237
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([177, 155, 19], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_mark_on_floor_3): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"
    
def is_mark_on_floor_4():
    start_time = time.time()

    box_left = 104
    box_top = 143
    box_right = 193
    box_bottom = 209
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([177, 155, 19], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_mark_on_floor_4): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"
    
def is_mark_on_floor_5():
    start_time = time.time()

    box_left = 166
    box_top = 186
    box_right = 264
    box_bottom = 281
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([177, 155, 19], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_mark_on_floor_5): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def is_mustard_yellow():
    start_time = time.time()

    box_left = 252
    box_top = 189
    box_right = 276
    box_bottom = 210
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
    print(f"Execution time(is_mustard_yellow): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def is_aquamarine():
    start_time = time.time()

    box_left = 252
    box_top = 189
    box_right = 276
    box_bottom = 210
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
    print(f"Execution time(is_aquamarine): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def is_coral():
    start_time = time.time()

    box_left = 252
    box_top = 189
    box_right = 276
    box_bottom = 210
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([255, 127, 80], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_coral): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def is_turquoise():
    start_time = time.time()

    box_left = 252
    box_top = 189
    box_right = 276
    box_bottom = 210
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([64, 224, 208], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_turquoise): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def is_lime_green():
    start_time = time.time()

    box_left = 252
    box_top = 189
    box_right = 276
    box_bottom = 210
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([204, 255, 0], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_lime_green): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def is_pale_pink():
    start_time = time.time()

    box_left = 252
    box_top = 189
    box_right = 276
    box_bottom = 210
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([255, 192, 203], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_pale_pink): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def is_blue():
    start_time = time.time()

    box_left = 244
    box_top = 176
    box_right = 290
    box_bottom = 220
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
    print(f"Execution time(is_at_starting_tile): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def is_red():
    start_time = time.time()

    box_left = 244
    box_top = 176
    box_right = 290
    box_bottom = 220
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
    print(f"Execution time(is_at_starting_tile): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"
    
def is_ocean_blue():
    start_time = time.time()

    box_left = 252
    box_top = 189
    box_right = 276
    box_bottom = 210
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([77, 133, 222], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_ocean_blue): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def is_dark_purple():
    start_time = time.time()

    box_left = 252
    box_top = 189
    box_right = 276
    box_bottom = 210
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([88, 0, 177], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_dark_purple): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def is_hp_below_50_percent():
    start_time = time.time()

    box_left = 552
    box_top = 79
    box_right = 553
    box_bottom = 80
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([19, 19, 19], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_ocean_blue): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"


def click_on_wine_of_zamorak():
    start_time = time.time()
    target_color = np.array([56, 62, 162], dtype=np.uint8)  # BGR
    lower_bound = target_color - np.array([10, 10, 10])
    upper_bound = target_color + np.array([10, 10, 10])
    random_float = random.uniform(0.13, 0.17)
    box = {'top': 243, 'left': 571, 'width': 722-571, 'height': 449-243}
    #print(f"Capturing box: {box}")
    
    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot)[:,:,:3]
    
    #print("Screenshot captured.")
    
    mask_blue = cv2.inRange(screenshot_np, lower_bound, upper_bound)
    #print("Mask created.")
    
    contours, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #print(f"Number of contours found: {len(contours)}")
    
    for contour in contours:
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"]) + box['left']
            cY = int(M["m01"] / M["m00"]) + box['top']
            #print(f"Moving to position: ({cX}, {cY})")
            pyautogui.moveTo(cX, cY, random_float)
            pyautogui.click()
            break
    else:
        print("No valid contour found.")
    
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(click_on_food): {execution_time} seconds")

def is_wine_of_zamora_in_inv():
    start_time = time.time()

    box_left = 568
    box_top = 243
    box_right = 727
    box_bottom = 452
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([162, 62, 56], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_ocean_blue): {execution_time} seconds")
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
        
        restart_flow = False
        while not restart_flow:

            if is_wine_of_zamora_in_inv() == "Not Found":
                print("Out of wine")
                sys.exit()          

            while True:
                if is_pale_pink() == "Not Found":
                    click_on_green_full_screen()
                    time.sleep(6.6)
                else:
                    if is_mark_on_floor_1() == "Found":
                        click_on_mark()
                        print("Taking mark 1")
                        time.sleep(4)
                    print("Phase 1: Pale Pink found")
                    break

            while True:
                if is_dark_purple() == "Found":
                    time.sleep(1)
                    click_minimap_on_blue()
                    time.sleep(7)
                    print("Returning to rooftops...")
                    restart_flow = True
                    break
                if is_lime_green() == "Not Found":
                    click_on_green_full_screen()
                    time.sleep(7)
                else:
                    if is_mark_on_floor_2() == "Found":
                        click_on_mark()
                        print("Taking mark 2")
                        time.sleep(4.2)
                    print("Phase 2: Lime Green found")
                    break

            if restart_flow:
                break

            while True:
                if is_ocean_blue() == "Found":
                    click_minimap_on_blue()
                    time.sleep(8)
                    print("Returning to rooftops...")
                    restart_flow = True
                    break 
                if is_turquoise() == "Not Found":
                    click_on_green_half_screen_down()
                    time.sleep(10.5)
                else:
                    if is_mark_on_floor_3() == "Found":
                        click_on_mark()
                        print("Taking mark 3")
                        time.sleep(4.3)
                    print("Phase 3: Turquoise found")
                    break

            if restart_flow:
                break

            while True:
                if is_coral() == "Not Found":
                    click_on_green_full_screen()
                    time.sleep(5.5)
                else:
                    if is_mark_on_floor_4() == "Found":
                        click_on_mark()
                        print("Taking mark 4")
                        time.sleep(4)
                    print("Phase 4: Coral found")
                    break

            while True:
                if is_aquamarine() == "Not Found":
                    click_on_green_full_screen()
                    time.sleep(5.5)
                else:
                    if is_mark_on_floor_5() == "Found":
                        click_on_mark()
                        print("Taking mark 5")
                        time.sleep(4)
                    print("Phase 5: Aquamarine found")
                    break

            while True:
                if is_mustard_yellow() == "Not Found":
                    time.sleep(10)
                    click_on_green_full_screen()
                    time.sleep(4.5)
                else:
                    print("Phase 6: Mustard Yellow found")
                    break

            while True:
                if is_red() == "Not Found":
                    click_minimap_on_red()
                    time.sleep(2.5)
                    if is_hp_below_50_percent() == "Found":
                        click_on_wine_of_zamorak()
                    time.sleep(4.7)
                else:
                    print("Phase 7: Red found")
                    break

            while True:
                if is_blue() == "Not Found":
                    click_minimap_on_blue()
                    time.sleep(6.5)
                else:
                    print("Phase 8: Blue found")
                    break

            if restart_flow:
                break


    # Rosa pálido: 255, 192, 203
    # Verde lima: 204, 255, 0
    # Turquesa: 64, 224, 208
    # Coral: 255, 127, 80
    # Aguamarina: 127, 255, 212
    # Amarillo mostaza: 255, 255, 102

    # if is_at_starting_tile() == "Found":
    # else:
    #     sys.exit()
    

    

