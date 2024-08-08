#CAMERA ZOOM 714/896

import numpy as np
import time
import mss
import cv2
import pyautogui
import random
import keyboard
import sys

rndmt = random.uniform(0.069768, 0.084969)

def click_on_druids():
    start_time = time.time()
    target_color = np.array([155, 255, 0], dtype=np.uint8)  # BGR
    capture_box = {'top': 30, 'left': 8, 'width': 513, 'height': 336}
    with mss.mss() as sct:
        screenshot = sct.grab(capture_box)
        screenshot_np = np.array(screenshot)[:,:,:3]
    mask_purple = cv2.inRange(screenshot_np, target_color, target_color)
    contours, _ = cv2.findContours(mask_purple, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        rect = cv2.minAreaRect(contour)
        rect_box = cv2.boxPoints(rect)
        rect_box = rect_box.astype(int)
        center_x = int(np.mean(rect_box[:, 0])) + capture_box['left']
        center_y = int(np.mean(rect_box[:, 1])) + capture_box['top']
        screen_width, screen_height = pyautogui.size()
        if 0 <= center_x < screen_width and 0 <= center_y < screen_height:
            pyautogui.moveTo(center_x, center_y, 0.06+rndmt)
            pyautogui.click(button='left')
        else:
            print("Las coordenadas están fuera de la pantalla.")
        break  
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Tiempo de ejecución (click_on_druids): {execution_time} segundos")

def click_on_grimy_herb():
    start_time = time.time()
    target_color = np.array([180, 24, 200], dtype=np.uint8)  # BGR
    random_float = random.uniform(0.092343, 0.1301982)
    capture_box = {'top': 30, 'left': 8, 'width': 513, 'height': 336}
    with mss.mss() as sct:
        screenshot = sct.grab(capture_box)
        screenshot_np = np.array(screenshot)[:,:,:3]
    mask_purple = cv2.inRange(screenshot_np, target_color, target_color)
    contours, _ = cv2.findContours(mask_purple, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        rect = cv2.minAreaRect(contour)
        rect_box = cv2.boxPoints(rect)
        rect_box = rect_box.astype(int)
        center_x = int(np.mean(rect_box[:, 0])) + capture_box['left']
        center_y = int(np.mean(rect_box[:, 1])) + capture_box['top']
        screen_width, screen_height = pyautogui.size()
        if 0 <= center_x < screen_width and 0 <= center_y < screen_height:
            pyautogui.moveTo(center_x, center_y, random_float)
            pyautogui.click(button='left')
        else:
            print("Las coordenadas están fuera de la pantalla.")
        break  
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Tiempo de ejecución (click_on_grimy_herb): {execution_time} segundos")


def click_on_green_center():
    start_time = time.time()
    target_color = np.array([0, 255, 0], dtype=np.uint8)  # BGR
    random_float = random.uniform(0.13, 0.17)
    capture_box = {'top': 30, 'left': 8, 'width': 513, 'height': 336}
    with mss.mss() as sct:
        screenshot = sct.grab(capture_box)
        screenshot_np = np.array(screenshot)[:,:,:3]
    mask_purple = cv2.inRange(screenshot_np, target_color, target_color)
    contours, _ = cv2.findContours(mask_purple, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        rect = cv2.minAreaRect(contour)
        rect_box = cv2.boxPoints(rect)
        rect_box = rect_box.astype(int)
        center_x = int(np.mean(rect_box[:, 0])) + capture_box['left']
        center_y = int(np.mean(rect_box[:, 1])) + capture_box['top']
        screen_width, screen_height = pyautogui.size()
        if 0 <= center_x < screen_width and 0 <= center_y < screen_height:
            pyautogui.moveTo(center_x, center_y, random_float)
            pyautogui.click(button='left')
        else:
            print("Las coordenadas están fuera de la pantalla.")
        break  
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Tiempo de ejecución (click_on_green_center): {execution_time} segundos")

def is_green_found_east():
    start_time = time.time()
    box_left = 265
    box_top = 163
    box_right = 302
    box_bottom = 239
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
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_green_found_east): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def click_on_purple_center():
    start_time = time.time()
    target_color = np.array([255, 0, 170], dtype=np.uint8)  # BGR
    random_float = random.uniform(0.18, 0.29)
    capture_box = {'top': 30, 'left': 8, 'width': 513, 'height': 336}
    with mss.mss() as sct:
        screenshot = sct.grab(capture_box)
        screenshot_np = np.array(screenshot)[:,:,:3]
    mask_purple = cv2.inRange(screenshot_np, target_color, target_color)
    contours, _ = cv2.findContours(mask_purple, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        rect = cv2.minAreaRect(contour)
        rect_box = cv2.boxPoints(rect)
        rect_box = rect_box.astype(int)
        center_x = int(np.mean(rect_box[:, 0])) + capture_box['left']
        center_y = int(np.mean(rect_box[:, 1])) + capture_box['top']
        screen_width, screen_height = pyautogui.size()
        if 0 <= center_x < screen_width and 0 <= center_y < screen_height:
            pyautogui.moveTo(center_x, center_y, random_float)
            pyautogui.click(button='left')
        else:
            print("Las coordenadas están fuera de la pantalla.")
        break  
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(click_on_purple_center): {execution_time} seconds")

def is_purple_color_found():
    start_time = time.time()
    box_left = 7
    box_top = 33
    box_right = 522
    box_bottom = 365
    box = {
        'left': box_left,
        'top': box_top,
        'width': box_right - box_left,
        'height': box_bottom - box_top
    }
    target_color = np.array([170, 0, 255], dtype=np.uint8) #lime
    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)
    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_purple_color_found): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def is_light_purple_color_found():
    start_time = time.time()
    box_left = 7
    box_top = 33
    box_right = 522
    box_bottom = 365
    box = {
        'left': box_left,
        'top': box_top,
        'width': box_right - box_left,
        'height': box_bottom - box_top
    }
    target_color = np.array([200, 24, 180], dtype=np.uint8)
    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)
    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_purple_color_found): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"


def exp_drop():
    box_left = 501
    box_top = 73
    box_right = 521
    box_bottom = 201
    box = {
        'left': box_left,
        'top': box_top,
        'width': box_right - box_left,
        'height': box_bottom - box_top
    }
    target_color = np.array([100, 255, 100], dtype=np.uint8)  # lime

    while True:
        start_time = time.time()
        found = False

        while time.time() - start_time < 0.6333:
            with mss.mss() as sct:
                screenshot = sct.grab(box)
                screenshot_np = np.array(screenshot, dtype=np.uint8)

            matches = (screenshot_np[:, :, 0] == target_color[2]) & \
                      (screenshot_np[:, :, 1] == target_color[1]) & \
                      (screenshot_np[:, :, 2] == target_color[0])

            if np.any(matches):
                found = True
                break

        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time(exp_drop): {execution_time} seconds")

        if found:
            return "Found"
        else:
            return "Not Found"
        time.sleep(0.6222)


def is_blue_splat():
    start_time = time.time()
    box_left = 215
    box_top = 148
    box_right = 312
    box_bottom = 243
    box = {
        'left': box_left,
        'top': box_top,
        'width': box_right - box_left,
        'height': box_bottom - box_top
    }
    target_color = np.array([0, 0, 255], dtype=np.uint8) #blue
    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)
    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_blue_splat): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def is_red_splat():
    start_time = time.time()
    box_left = 215
    box_top = 148
    box_right = 312
    box_bottom = 243
    box = {
        'left': box_left,
        'top': box_top,
        'width': box_right - box_left,
        'height': box_bottom - box_top
    }
    target_color = np.array([255, 0, 0], dtype=np.uint8) #blue
    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)
    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_red_splat): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def is_inv_26_empty():
    start_time = time.time()
    box_left = 620
    box_top = 468
    box_right = 630
    box_bottom = 478
    box = {
        'left': box_left,
        'top': box_top,
        'width': box_right - box_left,
        'height': box_bottom - box_top
    }
    target_color = np.array([69, 60, 51], dtype=np.uint8) #lime
    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)
    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_inv_26_occupied): {execution_time} seconds")
    if np.any(matches):
        return "Yes"
    else:
        return "No"



def is_pale_pink():
    start_time = time.time()
    box_left = 565
    box_top = 29
    box_right = 757
    box_bottom = 191
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

def click_minimap_on_pale_rose():
    start_time = time.time()
    target_color = np.array([203, 192, 255], dtype=np.uint8) # BGR
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
    print(f"Execution time(click_minimap_on_pale_rose): {execution_time} seconds")


def is_lime_green():
    start_time = time.time()
    box_left = 565
    box_top = 29
    box_right = 757
    box_bottom = 191
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

def click_minimap_on_lime_green():
    start_time = time.time()
    target_color = np.array([0, 255, 204], dtype=np.uint8) # BGR
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
    print(f"Execution time(click_minimap_on_lime_green): {execution_time} seconds")


def is_turquoise():
    start_time = time.time()
    box_left = 565
    box_top = 29
    box_right = 757
    box_bottom = 191
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
    print(f"Execution time(is_lime_green): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def click_minimap_on_turquoise():
    start_time = time.time()
    target_color = np.array([208, 224, 64], dtype=np.uint8) # BGR
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
    print(f"Execution time(click_minimap_on_lime_green): {execution_time} seconds")


def is_coral():
    start_time = time.time()
    box_left = 565
    box_top = 29
    box_right = 757
    box_bottom = 191
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

def click_minimap_on_coral():
    start_time = time.time()
    target_color = np.array([80, 127, 255], dtype=np.uint8) # BGR
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
    print(f"Execution time(click_minimap_on_coral): {execution_time} seconds")

def is_aquamarine():
    start_time = time.time()
    box_left = 565
    box_top = 29
    box_right = 757
    box_bottom = 191
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

def click_minimap_on_aquamarine():
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
    print(f"Execution time(click_minimap_on_aquamarine): {execution_time} seconds")

def is_mustard_yellow():
    start_time = time.time()
    box_left = 565
    box_top = 29
    box_right = 757
    box_bottom = 191
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

def click_minimap_on_mustard_yellow():
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
    print(f"Execution time(click_minimap_on_mustard_yellow): {execution_time} seconds")

def is_dark_purple():
    start_time = time.time()
    box_left = 565
    box_top = 29
    box_right = 757
    box_bottom = 191
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}
    target_color = np.array([55, 0, 55], dtype=np.uint8)
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

def click_minimap_on_dark_purple():
    start_time = time.time()
    target_color = np.array([55, 0, 55], dtype=np.uint8) # BGR
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
    print(f"Execution time(click_minimap_on_dark_purple): {execution_time} seconds")

def is_oponent_bar_red_end():
    start_time = time.time()
    box_left = 13
    box_top = 69
    box_right = 22
    box_bottom = 92
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}
    target_color = np.array([98, 18, 19], dtype=np.uint8)
    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)
    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_oponent_bar_red_end): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def is_oponent_bar_green_or_red():
    start_time = time.time()
    box_left = 10
    box_top = 69
    box_right = 148
    box_bottom = 95
    box = {'left': box_left,
           'top': box_top,
           'width': box_right - box_left,
           'height': box_bottom - box_top}
    
    colors = [
        {'name': 'green', 'color': np.array([6, 136, 54], dtype=np.uint8), 'threshold': 3},
        {'name': 'red', 'color': np.array([97, 18, 17], dtype=np.uint8), 'threshold': 3}
    ]
    
    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    for color_info in colors:
        target_color = color_info['color']
        threshold = color_info['threshold']
        lower_bound = target_color - threshold
        upper_bound = target_color + threshold
        
        matches = ((screenshot_np[:, :, 0] >= lower_bound[2]) & (screenshot_np[:, :, 0] <= upper_bound[2]) &
                   (screenshot_np[:, :, 1] >= lower_bound[1]) & (screenshot_np[:, :, 1] <= upper_bound[1]) &
                   (screenshot_np[:, :, 2] >= lower_bound[0]) & (screenshot_np[:, :, 2] <= upper_bound[0]))
        
        if np.any(matches):
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"Execution time(is_oponent_bar_{color_info['name']}): {execution_time} seconds")
            return f"Found {color_info['name']}"

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_oponent_bar_green_or_red): {execution_time} seconds")
    return "Not Found"

def click_inv_slot_25():
    box_left = 577
    box_top = 464
    box_right = 591
    box_bottom = 480

    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    offset_x = random.randint(-9, 9)
    offset_y = random.randint(-9, 9)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    randomt = random.uniform(0.08, 0.14)
    pyautogui.moveTo(click_x, click_y, randomt)

    pyautogui.click()

def is_light_blue_color_found():
    start_time = time.time()
    box_left = 7
    box_top = 33
    box_right = 522
    box_bottom = 365
    box = {
        'left': box_left,
        'top': box_top,
        'width': box_right - box_left,
        'height': box_bottom - box_top
    }
    target_color = np.array([115, 153, 178], dtype=np.uint8)
    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)
    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_purple_color_found): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def is_light_orange_color_found():
    start_time = time.time()
    box_left = 7
    box_top = 33
    box_right = 522
    box_bottom = 365
    box = {
        'left': box_left,
        'top': box_top,
        'width': box_right - box_left,
        'height': box_bottom - box_top
    }
    target_color = np.array([223, 136, 100], dtype=np.uint8)
    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)
    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_purple_color_found): {execution_time} seconds")
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def click_on_ladder():
    start_time = time.time()
    target_color = np.array([216, 130, 0], dtype=np.uint8)  # BGR
    random_float = random.uniform(0.092343, 0.1301982)
    capture_box = {'top': 30, 'left': 8, 'width': 513, 'height': 336}
    with mss.mss() as sct:
        screenshot = sct.grab(capture_box)
        screenshot_np = np.array(screenshot)[:,:,:3]
    mask_purple = cv2.inRange(screenshot_np, target_color, target_color)
    contours, _ = cv2.findContours(mask_purple, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        rect = cv2.minAreaRect(contour)
        rect_box = cv2.boxPoints(rect)
        rect_box = rect_box.astype(int)
        center_x = int(np.mean(rect_box[:, 0])) + capture_box['left']
        center_y = int(np.mean(rect_box[:, 1])) + capture_box['top']
        screen_width, screen_height = pyautogui.size()
        if 0 <= center_x < screen_width and 0 <= center_y < screen_height:
            pyautogui.moveTo(center_x, center_y, 0.03+rndmt)
            pyautogui.click(button='left')
        else:
            print("Las coordenadas están fuera de la pantalla.")
        break  
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Tiempo de ejecución (click_on_grimy_herb): {execution_time} segundos")



# Rosa pálido: 255, 192, 203
# Verde lima: 204, 255, 0
# Turquesa: 64, 224, 208
# Coral: 255, 127, 80
# Aguamarina: 127, 255, 212
# Amarillo mostaza: 255, 255, 102
# Purpura oscuro: 55, 0, 55


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
        
        while is_inv_26_empty() == "Yes":
            
            if is_light_blue_color_found() == "Found":
                click_on_ladder()
                time.sleep(3.2+rndmt)

            if is_light_orange_color_found() == "Found":
                click_on_ladder()
                time.sleep(3.2+rndmt)

            while exp_drop() == "Found":
                time.sleep(0.5 + rndmt)
            else:
                
                while is_oponent_bar_green_or_red() == "Found green":
                    time.sleep(0.5 + rndmt)
                else:
                    while is_light_purple_color_found() == "Found":
                        time.sleep(0.6 + rndmt)
                        click_on_grimy_herb()
                        time.sleep(1.8 + rndmt)
                    else:
                        click_on_druids()
                        time.sleep(2.7 + rndmt)
                        break
                break
        else:
            click_inv_slot_25()
            time.sleep(1)
            if is_inv_26_empty() == "No":
                sys.exit()
