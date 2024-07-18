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



















#RuneLite configuration
#Thu Jul 18 00:09:09 CLT 2024
objectindicators.region_12700=[{"id"\:39648,"name"\:"Opening","regionId"\:12700,"regionX"\:27,"regionY"\:59,"z"\:0,"color"\:"\#FF00FFFF"}]
statusbars.rightBarMode=PRAYER
groundMarker.region_10547=[{"regionId"\:10547,"regionX"\:31,"regionY"\:22,"z"\:0,"color"\:"\#FF0000FF"},{"regionId"\:10547,"regionX"\:38,"regionY"\:34,"z"\:0,"color"\:"\#FFFF00FF"},{"regionId"\:10547,"regionX"\:45,"regionY"\:46,"z"\:0,"color"\:"\#FF00FFFF"}]
groundMarker.region_10546=[{"regionId"\:10546,"regionX"\:9,"regionY"\:23,"z"\:0,"color"\:"\#FF00FFFF"}]
thegauntlet.resourceOrb=true
chatfilter.filterGameChat=false
tobqol.nyloRoleSelectedMelee=false
groundMarker.markerColor=-65536
thegauntlet.resourceOre=9
grandexchange.quickLookup=true
chatcommands.bh=true
emote-clue-items.FilterInStash=true
BetterNpcHighlight.swTrueTileColor=-16711681
runelite.hiscoreplugin=true
idlenotifier.specNotification={"enabled"\:false,"initialized"\:false,"override"\:false,"tray"\:false,"volume"\:0,"timeout"\:0,"gameMessage"\:false,"sendWhenFocused"\:false}
BetterNpcHighlight.respawnFillColor=335609855
statusbars.hideAfterCombatDelay=0
tobqol.sotetsegHideUnderworldRocks=true
grandexchange.enableNotifications=true
actionprogress.magic.plank-make=true
agility.markHighlight=-65536
xpglobes.showXpHour=true
grounditems.deprioritizeHiddenItems=true
timers.showTzhaarTimers=true
fpscontrol.limitFpsUnfocused=false
runewatch.useHotkey=false
party.sounds=true
wintertodt.notifyCold=INTERRUPT
MahoganyHomes.highlightHotspotColor=838926080
groundMarker.region_11416=[{"regionId"\:11416,"regionX"\:40,"regionY"\:41,"z"\:0,"color"\:"\#FF00FFFF"},{"regionId"\:11416,"regionX"\:41,"regionY"\:40,"z"\:0,"color"\:"\#FF00FFFF"}]
raids.layoutMessage=false
driftnet.showNetStatus=true
nightmareZone.absorptionnotification=true
gearswitchalert.tagSortMethod=ALL_FIRST
corp.leftClickCore=true
screenshot.ccKick=false
xpdrop.meleePrayerColor=-15368019
BetterNpcHighlight.swTrueTileHighlight=false
tobqol.sotetsegSoundClipVolume=65
idlenotifier.highEnergyNotification={"enabled"\:false,"initialized"\:false,"override"\:false,"tray"\:false,"volume"\:0,"timeout"\:0,"gameMessage"\:false,"sendWhenFocused"\:false}
tobqol.roomTimeValidation=false
itemCharge.showBraceletOfSlaughterCharges=true
screenshot.includeFrame=true
runelite.opponentinfoplugin=true
music.granularSliders=true
kingdomofmiscellania.cofferThreshold=7500000
groundMarker.region_10571=[{"regionId"\:10571,"regionX"\:33,"regionY"\:39,"z"\:0,"color"\:"\#FF00C800"}]
BetterNpcHighlight.swTileHighlight=false
banktags.item_1275=cox
teamCapes.minimumCapeCount=1
party.memberColor=-3342592
implings.magpieColor=-7434733
runecraft.showNature=true
menuentryswapper.swapQuick=true
actionprogress.crafting.headsAndTips=true
runecraft.hightlightDarkMage=true
tearsofguthix.blueTearsColor=1677787135
banktags.item_19634=bursting,slayer
tileindicators.destinationTileBorderWidth=2.0
grounditems.defaultColor=-1
worldmap.fairyRingTooltips=true
banktags.item_7409=herbrun
menuentryswapper.npc_5832=-1
prayer.prayerBarHideIfNotPraying=true
banktags.item_952=herbrun,wildy clue
thegauntlet.hunllefPrayerOutlineColor=OFF
runelite.marker1720318034283_preferredSize=20x131
nyloer.fontsSize=12
entityhider.hidePlayers=true
bankedexperience.grabFromInventory=false
timers.showSpellbookSwap=true
motherlode.showOresFound=true
textrecolor.opaquePrivateMessageReceivedHighlight=-16767101
xpTracker.progressBarTooltipLabel=TIME_TO_LEVEL
emote-clue-items.TrackGroupStorage=false
chatcommands.gc=true
woodcutting.showRedwoods=true
coxscouterexternal.displayFloorBreak=false
vanguards.showHps=true
herblorerecipes.showTooltipOnComplex=true
kittenConfig.catOverlay=true
deathIndicator.timeOfDeath=2023-08-31T23\:47\:29.063767Z
tobqol.instanceTimerOffset=0
grounditems.menuHighlightMode=OPTION
tileindicators.highlightCurrentColor=-10266369
gearswitchalert.tagUnderline=true
inventorytags.tag_13073={"color"\:"\#FFE7FF00"}
pyramidplunder.highlightUrnsFloor=9
screenshot.valuableDrop=false
banktags.item_946=wintertodt
statusbars.barWidth=20
inventorytags.tag_13072={"color"\:"\#FFE7FF00"}
itemstat.absolute=true
coxscouterexternal.screenshotHotkey=0\:0
tobqol.showSotetsegChosenText=true
menuentryswapper.swapGEItemCollect=DEFAULT
zoom.rightClickMovesCamera=false
menuentryswapper.swapBait=false
banktags.tagtabs=tob,cox,hydra,bandos solo melee,herbrun,wildy clue,wintertodt,bursting,spindel,artio,calvarion,revenant,slayer
banktags.item_3024=bandos solo melee,spindel,artio,calvarion,revenant,cox,tob
attackIndicator.warnForStrength=false
banktags.item_13072=tob
banktags.item_13073=tob
npcindicators.fillColor=335609855
npcid.hoverOnly=false
runecraft.showLaw=true
herbiboar.showClickboxes=false
tobqol.displayTimeSplits=true
menuentryswapper.object_37978=1
runelite.cameraplugin=true
banktags.icon_artio=27649
attackIndicator.warnForDefensive=false
chatnotification.notifyOnPM=false
itemidentification.showPlanks=false
menuentryswapper.item_1985=-1
defencetracker.highDefColor=-1
attackIndicator.warnForMagic=false
BetterNpcHighlight.swTrueTileLines=REG
tobqol.trackDowns=true
nyloer.rangeNylocasSymbol=T
fishing.flyingFishNotification=true
BetterNpcHighlight.clickboxRaveSpeed=6000
radiusmarkers.includeInteractionRange=true
xpTracker.wiseOldManOpenOption=true
party.recolorNames=true
agility.highlightPortals=true
gpu.expandedMapLoadingChunks=3
tobqol.sotetsegHideWhiteScreen=true
groundMarker.fillOpacity=100
timers.showFarmersAffinity=true
BetterNpcHighlight.tileFillColor=335609855
worldmap.miscellaneousTeleportIcon=true
prayer.prayer_order_book_0=0,1,2,18,19,3,4,5,6,7,8,20,21,9,10,11,12,13,14,24,23,15,16,17,28,25,26,22,27
banktags.item_20657=bandos solo melee
menuentryswapper.swapJewelleryBox=true
npcUnaggroArea.npcUnaggroAreaColor=-256
prayer.prayerFlickColor=-16711681
dpscounter.showDamage=false
BetterNpcHighlight.respawnTimerColor=-1
gpu.fpsTarget=60
banktags.item_6585=bandos solo melee,cox,hydra,tob,slayer
groundMarker.region_12338=[{"regionId"\:12338,"regionX"\:31,"regionY"\:61,"z"\:0,"color"\:"\#FF00FFFF"},{"regionId"\:12338,"regionX"\:8,"regionY"\:50,"z"\:0,"color"\:"\#FF00C800"}]
idlenotifier.spec=0
BetterNpcHighlight.tagLegend=\#\#\# Valid Style Format\:\n\nTile \= "t", "tile" \nTrue Tile \= "tt", "truetile" \nSW Tile \= "sw", "swt", "swtile", "southwesttile", "southwest", "southwestt" \nSW True Tile \= "swtt", "swtruetile", "southwesttruetile", "southwesttt" \nHull \= "h", "hull" \nArea \= "a", "area" \nOutline \= "o", "outline" \nClickbox \= "c", "clickbox", "box" \nTurbo \= "tu", "turbo" \n
defencetracker.cappedDefColor=-16711936
inventorytags.tag_4101={"color"\:"\#FF0000FF"}
timers.showCannon=true
runelite.bankedexperienceplugin=false
prayer.showPrayerDoseIndicator=true
bank.blockJagexAccountAd=false
nyloer.meleeHighlightMageTiles=false
grounditems.notifyTier=OFF
banktags.item_6570=bandos solo melee,cox,hydra,tob,slayer
xpglobes.Orb\ size=40
emote-clue-items.NotifyUnopenedInterfaces=true
grounditems.recolorMenuHiddenItems=false
thegauntlet.resourceGrym=2
kittenConfig.lastAttentionType=SINGLE_STROKE
groundMarker.region_9625=[{"regionId"\:9625,"regionX"\:54,"regionY"\:12,"z"\:0,"color"\:"\#FFFFFF00"}]
actionprogress.progress-done-color=1677786932
motherlode.showMiningStats=true
nightmareZone.moveoverlay=true
dailytaskindicators.showStaves=true
emote-clue-items.HighlightElite=true
linemarkers.hideNavButton=false
implings.crystalColor=-10634030
music.muteOtherAreaSounds=false
inventorytags.fillOpacity=50
runelite.ammoplugin=false
runelite.menuentryswapperplugin=true
screenshot.displayDate=true
textrecolor.transparentPublicChatHighlight=-1
banktags.item_10828=wildy clue,spindel,calvarion
thegauntlet.resourceRemoveOutlineOnceAcquired=true
objectindicators.region_10571=[{"id"\:34763,"name"\:"Altar","regionId"\:10571,"regionX"\:34,"regionY"\:41,"z"\:0,"color"\:"\#FF640202"}]
groundMarker.region_13204=[{"regionId"\:13204,"regionX"\:16,"regionY"\:28,"z"\:0,"color"\:"\#FF00FFFF"}]
roofremoval.overridePOH=false
grounditems.dontHideUntradeables=true
hunterplugin.hexColorOpenTrap=-256
raids.blacklistedRooms=vanguards, vespula, vasa
questhelper.showOverlayPanel=true
maxhit.showNextMaxHit=true
itemCharge.showBellowCharges=true
poh.showSpellbook=true
inventoryViewer.toggleKeybind=0\:0
loottracker.npcKillChatMessage=false
interacthighlight.npcAttackHoverHighlightColor=-1862271232
gearswitchalert.tagFill=true
stretchedmode.integerScaling=false
gpu.brightTextures=true
emote-clue-items.HighlightDepositBox=false
BetterNpcHighlight.outlineRave=false
mining.statTimeout=5
chatcommands.price=true
specialcounter.bulwarkThreshold=0
tobqol.nyloInstanceTimer=false
banktags.item_563=wintertodt
keyremapping.f10=48\:0
banktags.item_560=bursting,bandos solo melee,cox,tob
banktags.item_561=slayer
textrecolor.transparentPrivateMessageReceivedHighlight=-1
keyremapping.f12=61\:0
keyremapping.f11=45\:0
grounditems.showLootbeamForHighlighted=false
objectindicators.markerColor=-6619136
wintertodt-notifications.overlayColor=-2130771968
tobqol.verzikTornadoes=true
banktags.item_557=wintertodt,tob,cox
banktags.item_555=bursting,cox
banktags.item_556=bursting,wintertodt
banktags.item_554=bursting,slayer
tileindicators.destinationTileFillColor=838860800
banktaglayouts.layout_artio=10374\:0,1712\:1,2503\:2,2497\:3,3105\:4,9243\:5,10499\:8,9185\:9,23203\:10,7462\:11,13128\:12,3024\:16,6685\:17,2444\:18,2434\:19,12625\:20,3144\:21,3144\:22,3144\:23,6685\:24,6685\:25,2444\:26,2434\:27,13441\:28,13441\:29,13441\:30,13441\:31,3144\:32,3144\:33,3144\:34,3144\:35,3144\:36,3144\:37,13441\:40,13441\:41,13441\:42,13441\:43,13441\:44,19564\:45
inventorytags.tag_4151={"color"\:"\#FFFF0000"}
worldmap.arceuusSpellbookIcon=true
fishing.overlayColor=-16711681
specialcounter.infobox=true
objectindicators.region_10551=[{"id"\:10832,"name"\:"Maple tree","regionId"\:10551,"regionX"\:54,"regionY"\:16,"z"\:0,"color"\:"\#FF0000FF"},{"id"\:10832,"name"\:"Maple tree","regionId"\:10551,"regionX"\:53,"regionY"\:14,"z"\:0,"color"\:"\#FF0000FF"},{"id"\:10832,"name"\:"Maple tree","regionId"\:10551,"regionX"\:51,"regionY"\:16,"z"\:0,"color"\:"\#FF0000FF"}]
banktags.item_5296=herbrun
playerindicators.nonClanMemberColor=-65536
actionprogress.crafting.molten-glass=true
screenshot.rewards=true
thegauntlet.resourceTileOutlineWidth=1
xpTracker.skillTabOverlayMenuOptions=true
MahoganyHomes.-7419237899471359219.currentTier=0
motherlode.showBrokenStruts=true
motherlode.showMiningState=true
bankxpvalue.itemXpTooltips=true
inventorytags.tagUnderline=false
blastmine.hexTimerColor=-2542080
menuentryswapper.npcShiftClickWalkHere=false
banktags.item_19693=wintertodt
banktags.item_7462=bandos solo melee,wildy clue,spindel,artio,calvarion,cox
banktags.item_19695=wintertodt
woodcutting.highlightGlowingRoots=true
npcindicators.ignorePets=true
attackIndicator.alwaysShowStyle=true
nyloer.fontsType=ARIAL
runelite.mahoganyhomesplugin=false
groundMarker.region_11053=[{"regionId"\:11053,"regionX"\:47,"regionY"\:63,"z"\:0,"color"\:"\#FF00FFFF"},{"regionId"\:11053,"regionX"\:46,"regionY"\:63,"z"\:0,"color"\:"\#FF00FFFF"}]
objectindicators.region_10547=[{"id"\:10355,"name"\:"Bank booth","regionId"\:10547,"regionX"\:32,"regionY"\:22,"z"\:0,"color"\:"\#FFFF0000"},{"id"\:11730,"name"\:"Baker\\u0027s stall","regionId"\:10547,"regionX"\:44,"regionY"\:47,"z"\:0,"color"\:"\#FFFF0000"}]
fpscontrol.maxFpsUnfocused=50
cooking.fermentTimer=true
customitemhovers.hoverDefaultColor=-1118482
averagetime.Boss\ Goals\ Bottom=TTG
woodcutting.forestryFriendlyEntNotification=true
tileindicators.highlightDestinationColor=-8355712
dailytaskindicators.showRunes=false
kourendLibrary.showTutorialOverlay=true
mining.showMiningStats=true
textrecolor.opaqueClanGuestInfoHighlight=-65536
runelite.interfaceFontType=REGULAR
itemstat.colorWorse=-1166541
implings.youngColor=-5266296
interfaceStyles.rsCrossSprites=false
runelite.infoboxFontType=REGULAR
playerindicators.highlightFriends=ENABLED
worldmap.standardSpellbookIcon=true
grandexchange.highlightSearchMatch=true
thegauntlet.overlayGrymRoot=true
BetterNpcHighlight.areaRave=false
menuentryswapper.item_9064=-1
playerindicators.highlightFriendsChat=ENABLED
BetterNpcHighlight.debugNPC=false
slayer.targetColor=-65536
groundMarker.region_13138=[{"regionId"\:13138,"regionX"\:13,"regionY"\:14,"z"\:3,"color"\:"\#FFFFFF00"},{"regionId"\:13138,"regionX"\:46,"regionY"\:40,"z"\:3,"color"\:"\#FF8D2B79"},{"regionId"\:13138,"regionX"\:13,"regionY"\:44,"z"\:2,"color"\:"\#FF8D2B79"},{"regionId"\:13138,"regionX"\:13,"regionY"\:44,"z"\:3,"color"\:"\#FF8D2B79"},{"regionId"\:13138,"regionX"\:46,"regionY"\:40,"z"\:2,"color"\:"\#FF8D2B79"},{"regionId"\:13138,"regionX"\:54,"regionY"\:22,"z"\:3,"color"\:"\#FF8D2B79"}]
chatfilter.filterClanChat=false
defencetracker.lowDefColor=-256
banktags.item_12631=bandos solo melee,revenant,cox,tob
banktags.icon_wildy\ clue=2722
timers.showHealGroup=true
roofremoval.removeBetween=true
keyremapping.left=65\:0
worldhopper.favorite_349=true
banktags.item_12625=wildy clue,spindel,artio,calvarion,revenant,cox,tob
party.pings=true
xpupdater.runetracker=false
banktags.item_11773=cox,hydra,tob
thegauntlet.utilitiesFishCheck=true
chathistory.pmTargetCycling=true
poh.showMythicalCape=true
banktags.tab=
implings.showbaby=NONE
grandexchange.enableGELimitReset=true
menuentryswapper.object_16105=3
runelite.npcindicatorsplugin=true
party.statusOverlayStamina=false
worldhopper.favorite_318=true
radiusmarkers.defaultRadiusInteraction=1
runelite.XpInfoBoxOverlayWoodcutting_preferredPosition=BOTTOM_RIGHT
lifesaver.hitpoints=10
questhelper.stewBoostsPanel=false
motherlode.showVeins=true
banktags.item_20232=bandos solo melee
banktags.item_1725=spindel
BetterNpcHighlight.highlightMenuNames=false
driftnet.highlightUntaggedFish=true
timers.showDivine=true
MahoganyHomes.highlightHotspots=true
pyramidplunder.highlightSpeartrapColor=-14336
grounditems.highValuePrice=1000000
prayer.prayerIndicatorOverheads=false
banktags.item_9676=bursting,hydra
tileindicators.highlightHoveredTile=true
banktags.item_9674=bursting,hydra
npcindicators.highlightcolor_2923=-15373630
nightmareZone.recurrentdamagenotification=false
npcindicators.borderWidth=2.0
questhelper.boostColour=-14336
chatcommands.clue=true
worldhopper.favorite_319=true
banktags.item_22400=tob
npcindicators.highlightcolor_520=-16711781
tileindicators.hoveredTileBorderWidth=2.0
banktags.item_1712=wildy clue,artio
MahoganyHomes.highlightTeleports=true
worldmap.questStartTooltips=true
nightmareZone.overloadearlywarningseconds=10
runelite.specialcounterplugin=true
radiusmarkers.defaultColourHunt=-33024
screenshot.valuableDropThreshold=0
menuentryswapper.npc_500=-1
objectindicators.region_12342=[{"id"\:16469,"name"\:"Furnace","regionId"\:12342,"regionX"\:38,"regionY"\:43,"z"\:0,"color"\:"\#FF0000FF"},{"id"\:10355,"name"\:"Bank booth","regionId"\:12342,"regionX"\:26,"regionY"\:37,"z"\:0,"color"\:"\#FFFF00FF"}]
brushMarkers.brushBorderWidth=2.0
worldhopper.favorite_373=true
banktags.item_10499=artio,revenant
groundMarker.region_6966=[{"regionId"\:6966,"regionX"\:45,"regionY"\:5,"z"\:0,"color"\:"\#FF00FFFF"},{"regionId"\:6966,"regionX"\:48,"regionY"\:12,"z"\:0,"color"\:"\#FF00FFFF"},{"regionId"\:6966,"regionX"\:10,"regionY"\:12,"z"\:0,"color"\:"\#FFFF7300"},{"regionId"\:6966,"regionX"\:6,"regionY"\:14,"z"\:0,"color"\:"\#FF214263"}]
runewatch.notifyOnJoin=true
gearswitchalert.defaultColourMelee=-65536
attackIndicator.warnForAttack=false
objectindicators.region_12341=[{"id"\:43475,"name"\:"Fire","regionId"\:12341,"regionX"\:34,"regionY"\:40,"z"\:0,"color"\:"\#FFFF7300"}]
mta.alchemy=true
NyloerConfig.meleeNylocasColor=-1
objectindicators.region_12338=[{"id"\:10819,"name"\:"Willow tree","regionId"\:12338,"regionX"\:17,"regionY"\:35,"z"\:0,"color"\:"\#FF0000FF"},{"id"\:47482,"name"\:"Tree roots","regionId"\:12338,"regionX"\:16,"regionY"\:37,"z"\:0,"color"\:"\#FF00FFFF"},{"id"\:10529,"name"\:"Bank Deposit Box","regionId"\:12338,"regionX"\:22,"regionY"\:40,"z"\:0,"color"\:"\#FFFF00FF"},{"id"\:10829,"name"\:"Willow tree","regionId"\:12338,"regionX"\:14,"regionY"\:36,"z"\:0,"color"\:"\#FF0000FF"}]
boosts.boostThreshold=0
barrows.deadBrotherLocColor=-65536
randomevents.notifyBob=false
playerindicators.colorPlayerMenu=true
grandexchange.geSearchMode=DEFAULT
xpglobes.Progress\ orb\ outline\ color=-16777216
timetracking.defaultTimerMinutes=5
specialcounter.specDropColor=-1
textrecolor.opaqueGameMessageHighlight=-1109984
runelite.automaticResizeType=KEEP_GAME_SIZE
itemprices.hideInventory=true
banktags.item_9242=cox
banktags.item_9243=artio
itemstat.showStatsInBank=true
banktaglayouts.layout_herbrun=13579\:0,7409\:1,13585\:2,13589\:3,13581\:8,13583\:9,13587\:10,5325\:16,5343\:17,13128\:18,4251\:19,21269\:20,5296\:21,5341\:24,952\:25,13123\:26,13393\:27,22997\:28
itemCharge.showExpeditiousBraceletCharges=true
interacthighlight.borderWidth=4
thegauntlet.resourceTirinum=9
objectindicators.region_7513=[{"id"\:13523,"name"\:"Amulet of Glory","regionId"\:7513,"regionX"\:40,"regionY"\:54,"z"\:0,"color"\:"\#FF630F8B"},{"id"\:4525,"name"\:"Portal","regionId"\:7513,"regionX"\:3,"regionY"\:12,"z"\:2,"color"\:"\#FF7FEF00"},{"id"\:15270,"name"\:"Altar space","regionId"\:7513,"regionX"\:20,"regionY"\:45,"z"\:2,"color"\:"\#FF007DFF"},{"id"\:13523,"name"\:"Amulet of Glory","regionId"\:7513,"regionX"\:40,"regionY"\:54,"z"\:2,"color"\:"\#FFCC00FF"},{"id"\:13181,"name"\:"Altar","regionId"\:7513,"regionX"\:20,"regionY"\:45,"z"\:2,"color"\:"\#FF630F8B"}]
NyloerConfig.meleeNylocasSymbol=I
herblorerecipes.showHerbloreLvlInTooltip=true
linemarkers.showWorldMap=true
hunterplugin.maniacalMonkeyNotify=false
banktaglayouts.autoLayoutStyle=ZIGZAG
worldhopper.favorite_366=true
gpu.anisotropicFilteringLevel=0
mta.telekinetic=true
worldhopper.favorite_361=true
runelite.screenshotplugin=false
worldhopper.favorite_363=true
worldhopper.favorite_365=true
BetterNpcHighlight.entityHiderCommands=true
itemCharge.showExplorerRingCharges=true
nyloer.customHighlightMageTiles=false
tileindicators.hoveredTileFillColor=838860800
NyloerConfig.fontsSize=12
specialcounter.dragonWarhammerThreshold=0
zoom.rightClickMenuBlocksCamera=true
averagetime.Fastest\ Kill=true
itemCharge.ringOfForgingNotification=true
thegauntlet.utilitiesOutlineWidth=1
banktags.item_13576=bandos solo melee,cox,hydra,tob
runelite.tooltipFontType=SMALL
npcindicators.ignoreDeadNpcs=true
coxtimers.showOlmPhaseTimers=true
banktaglayouts.updateMessages=true
actionprogress.magic.enchant-jewellery=true
cannon.showInfobox=false
herblorerecipes.showTooltipOnPlaceholder=true
actionprogress.crafting.shields=true
bankedexperience.grabFromFossilChest=true
runelite.AttackStylesOverlay_preferredPosition=BOTTOM_LEFT
worldhopper.showMessage=true
itemstat.showWeight=true
banktaglayouts.autoLayoutDuplicatesEnabled=true
BetterNpcHighlight.displayName=
coxscouterexternal.showRecommendedItems=false
BetterNpcHighlight.fontBackground=SHADOW
textrecolor.transparentGameMessageHighlight=-1109984
grounditems.groundItemTimers=TICKS
kittenConfig.secondsNeglected=57
tobqol.nyloRoleSelectedMage=false
BetterNpcHighlight.clickboxColor=-16711681
questhelper.outlineThickness=4
actionprogress.fletching.crossbows=true
bank.rightClickBankLoot=false
runelite.attackstylesplugin=false
implings.babyColor=-5140557
npcindicators.highlightHull=false
chatcommands.killcount=true
implings.showyoung=NONE
banktaglayouts.layout_revenant=6326\:0,12018\:1,2503\:2,21816\:3,2558\:4,9144\:5,21817\:6,12631\:7,10499\:8,861\:9,2497\:10,6328\:11,892\:12,6685\:13,3024\:14,22587\:15,2444\:16,2434\:17,13441\:18,13441\:19,13441\:20,13441\:21,13441\:22,13441\:23,12625\:24,2434\:25,3144\:26,3144\:27,3144\:28,3144\:29,3144\:30,3144\:31,13441\:32,13441\:33,13441\:34,13441\:35,13441\:36,19564\:37,3144\:40,3144\:41,3144\:42,3144\:43,3144\:44,11941\:45
raids.scoutOverlayAtBank=true
questhelper.debugColor=-65281
actionprogress.herblore.cleaning=true
actionprogress.fletching.shields=true
actionprogress.crafting.glassblowing=true
fpscontrol.maxFps=50
runelite.tooltipPosition=UNDER_CURSOR
inventoryViewer.hiddenDefault=false
itemstat.alwaysShowBaseStats=false
brushMarkers.brushpaintMode=false
npcindicators.highlightMenuNames=false
banktags.item_21166=wildy clue
questhelper.showSymbolOverlay=true
grounditems.hiddenItems=Vial,Ashes,Bones,Bucket,Jug,Seaweed,Raw salmon,Salmon,Trout,Raw trout,Burnt fish,Iron ore,Willow longbow (u),Willow logs,Maple longbow (u),Gold ring,Green dragonhide,Lime,Pineapple,Strawberry,Banana,Jangerberries,Cooking apple,Redberries,Raw beef,Cowhide, Mind rune,Mithril bolts,Air rune,Nature rune,bronze longsword, unholy mould, snape grass, vial of water,body rune, earth rune,uncut sapphire, uncut emerald, uncut ruby, chaos talisman, nature talisman, uncut diamond, loop half of key, tooth half of key, rune javelin, rune spear, shield left half, dragon spear,Nature rune,ensouled chaos druid head, Law rune, coins,
menuentryswapper.object_11723=1
runelite.linemarkerplugin=false
fishing.onlyCurrent=true
gpu.vsyncMode=ADAPTIVE
hiscore.autocomplete=true
banktags.item_12695=bandos solo melee,wildy clue,spindel,calvarion,hydra,cox,tob,slayer
runelite.actionprogressplugin=true
objectindicators.region_14133=[{"id"\:9341,"name"\:"Young tree","regionId"\:14133,"regionX"\:33,"regionY"\:58,"z"\:0,"color"\:"\#FF00FFFF"},{"id"\:9341,"name"\:"Young tree","regionId"\:14133,"regionX"\:30,"regionY"\:57,"z"\:0,"color"\:"\#FF00FFFF"},{"id"\:9341,"name"\:"Young tree","regionId"\:14133,"regionX"\:33,"regionY"\:61,"z"\:0,"color"\:"\#FF00FFFF"}]
nyloer.customHighlightMeleeTiles=false
randomevents.notifyPillory=false
randomevents.notifyFrog=false
groundMarker.region_11833=[{"regionId"\:11833,"regionX"\:10,"regionY"\:30,"z"\:0,"color"\:"\#FF00FFFF"}]
inventorygrid.highlightColor=755040000
chathistory.retainChatHistory=true
nyloer.mageRoleShiftSwaps=/walk here,*\n/attack,nylocas hagios*162*
textrecolor.transparentExamineHighlight=-16711936
MahoganyHomes.textOverlay=true
timetracking.timerWarningThreshold=10
banktags.item_13128=bursting,herbrun,wildy clue,spindel,artio,calvarion
tileindicators.highlightCurrentTile=true
cooking.statTimeout=5
menuentryswapper.swapAdmire=true
woodcutting.highlightPheasantNest=true
thegauntlet.grymRootOutlineColor=-256
cannon.showCannonSpots=true
menuentryswapper.swapHomePortal=HOME
tobqol.instanceTimerSize=16
maxhit.showMagic=false
agility.agilityArenaTimer=true
entityhider.hideClanChatMembers=false
partypanel.previousPartyId=kenko
thegauntlet.fishingSpotFillColor=838926335
randomevents.notifyMaze=false
barrows.brotherLocColor=-16711681
playerindicators.teamMemberColor=-15503625
BetterNpcHighlight.taskFillColor=350239793
agility.highlightSepulchreSkilling=true
groundMarker.region_11828=[{"regionId"\:11828,"regionX"\:54,"regionY"\:34,"z"\:0,"color"\:"\#FF000000"},{"regionId"\:11828,"regionX"\:54,"regionY"\:33,"z"\:0,"color"\:"\#FF000000"}]
worldmap.kourendTaskTooltips=true
party.statusOverlaySpec=false
textrecolor.opaqueClanChatGuestMessageHighlight=-16777216
keyremapping.f1=49\:0
runelite.QuestHelperOverlay_preferredLocation=4\:139
timetracking.stopwatches=[]
keyremapping.f3=51\:0
entityhider.hidePets=true
keyremapping.f2=50\:0
woodcutting.highlightMulch=true
BetterNpcHighlight.outlineRaveSpeed=6000
itemidentification.showComposts=false
agility.sepulchreHighlightColor=-16711936
smelting.statTimeout=5
runelite.roguesdenplugin=true
statusbars.enableCounter=false
chathistory.copyToClipboard=true
banktags.item_13123=herbrun,wildy clue
playerindicators.highlightOthers=PVP
chatcommands.bhRogue=true
emote-clue-items.HighlightShop=false
banktaglayouts.showAutoLayoutButton=true
specialcounter.defenceDrainInfobox=true
worldhopper.regionFilter=[]
BetterNpcHighlight.outlineNames=Knight of Ardougne
coxscouterexternal.highlightedShowThreshold=0
menuentryswapper.ui_shift_19726336_1069=3
worldmap.fishingSpotTooltips=true
banktags.item_13589=herbrun
zoom.outerLimit=0
banktags.item_3546=wildy clue
banktags.item_13111=wildy clue
banktags.item_13110=wildy clue
itemCharge.showBloodEssenceCharges=true
inventorygrid.showHighlight=true
motherlode.showLootIcons=false
questhelper.orderListBy=A_TO_Z
idlenotifier.animationidle=true
banktags.item_4874=cox
thegauntlet.utilitiesOutlineColor=-65281
herblorerecipes.showTooltipSeedVault=true
animationSmoothing.smoothObjectAnimations=true
runelite.playerindicatorsplugin=true
menuentryswapper.ui_shift_19726336_1070=2
banktaglayouts.layout_wildytask=DISABLED
BetterNpcHighlight.trueTileHighlight=false
nyloer.customFontConfig=0\:mage\:\#00FFFF
banktags.item_13579=herbrun
runewatch.useRW=true
banktags.item_13587=herbrun
banktags.item_4868=cox
coxscouterexternal.highlightColor=-65281
banktags.item_13585=herbrun
banktags.item_13583=herbrun
runelite.flashNotification=DISABLED
banktags.item_13581=herbrun
agility.trapOverlay=true
banktaglayouts.tutorialMessage=true
thegauntlet.overlayResources=true
runelite.inventoryviewerplugin=false
nightmareZone.absorptioncolorbelowthreshold=-65536
timers.showLiquidAdrenaline=true
optimal-quest-guide.requirementMetColor=-9510546
chatcommands.pets=true
radiusmarkers.includeAttackRange=true
timestamp.format=[HH\:mm]
kittenConfig.kittenOverlay=true
menuentryswapper.shopBuy=BUY_50
menuentryswapper.swapDepositItems=false
bank.rightClickPlaceholders=false
notes.notesData=
BetterNpcHighlight.drawBeneathLimit=10
coxscouterexternal.scoutOverlay=true
radiusmarkers.includeHuntRange=false
discord.showDungeonActivity=true
groundMarker.region_12853=[{"regionId"\:12853,"regionX"\:53,"regionY"\:28,"z"\:0,"color"\:"\#FF68FF69"},{"regionId"\:12853,"regionX"\:54,"regionY"\:29,"z"\:0,"color"\:"\#FF68FF69"},{"regionId"\:12853,"regionX"\:54,"regionY"\:28,"z"\:0,"color"\:"\#FF68FF69"},{"regionId"\:12853,"regionX"\:53,"regionY"\:29,"z"\:0,"color"\:"\#FF68FF69"},{"regionId"\:12853,"regionX"\:38,"regionY"\:38,"z"\:0,"color"\:"\#FFAA00FF"},{"regionId"\:12853,"regionX"\:37,"regionY"\:38,"z"\:0,"color"\:"\#FFAA00FF"},{"regionId"\:12853,"regionX"\:37,"regionY"\:37,"z"\:0,"color"\:"\#FFAA00FF"},{"regionId"\:12853,"regionX"\:38,"regionY"\:37,"z"\:0,"color"\:"\#FFAA00FF"}]
groundMarker.region_12850=[{"regionId"\:12850,"regionX"\:9,"regionY"\:24,"z"\:2,"color"\:"\#FFFF7300"}]
itemCharge.showWateringCanCharges=true
entityhider.hideNPCs=false
music.muteAmbientSounds=false
itemCharge.amuletOfChemistryNotification=true
zoom.compassLookPreservePitch=false
grounditems.insaneValuePrice=10000000
grandexchange.showTotal=true
actionprogress.herblore.tar=true
bank.rightClickBankEquip=false
menuentryswapper.swapArdougneCloak=WEAR
banktags.item_2497=wildy clue,spindel,artio,calvarion,revenant
slayer.superiornotification=true
grounditems.highlightedItems=Grimy tarromin, Grimy harralander, Grimy ranarr weed, Grimy irit leaf, Grimy avantoe, Grimy kwuarm, Grimy cadantine, Grimy lantadyme, Grimy dwarf weed, Grimy guam leaf, Grimy marrentill,
questhelper.showTextHighlight=true
motherlode.statTimeout=5
animationSmoothing.smoothPlayerAnimations=true
runepouch.fontcolor=-256
banktags.item_4675=bursting,bandos solo melee
stretchedmode.keepAspectRatio=false
itemCharge.showBasketCharges=true
banktaglayouts.layout_barrows=DISABLED
implings.spawnColor=-1
entityhider.hideLocalPlayer2D=false
radiusmarkers.defaultColourRetreatInteraction=-16776961
gearswitchalert.hidePlugin=false
banktags.item_24271=bandos solo melee,cox,tob
npcUnaggroArea.npcUnaggroAlwaysActive=true
averagetime.Display\ relative\ kills=true
tileindicators.currentTileFillColor=838860800
banktaglayouts.shiftModifierForExtraBankItemOptions=false
driftnet.annetteTagColor=-65536
herblorerecipes.showTooltipOnPrimaries=true
interacthighlight.npcInteractHighlightColor=-1862336512
vanguards.mageColor=-16711681
menuentryswapper.item_10149=4
clanchat.chatsData=Thievinghost,loool,dakota,da dakota,d dakota,the dakota,Dakotas,iron kenko,Looolo,Team AMBU
menuentryswapper.npc_2038=-1
idlenotifier.prayerNotification={"enabled"\:false,"initialized"\:false,"override"\:false,"tray"\:false,"volume"\:0,"timeout"\:0,"gameMessage"\:false,"sendWhenFocused"\:false}
nyloer.meleeNylocasColor=-1
groundMarker.region_12889=[{"regionId"\:12889,"regionX"\:37,"regionY"\:38,"z"\:0,"color"\:"\#FF8D2B79"},{"regionId"\:12889,"regionX"\:34,"regionY"\:38,"z"\:0,"color"\:"\#FF8D2B79"},{"regionId"\:12889,"regionX"\:28,"regionY"\:38,"z"\:0,"color"\:"\#FF8D2B79"},{"regionId"\:12889,"regionX"\:28,"regionY"\:43,"z"\:0,"color"\:"\#FF8D2B79"},{"regionId"\:12889,"regionX"\:31,"regionY"\:43,"z"\:0,"color"\:"\#FF8D2B79"},{"regionId"\:12889,"regionX"\:34,"regionY"\:43,"z"\:0,"color"\:"\#FF8D2B79"},{"regionId"\:12889,"regionX"\:37,"regionY"\:43,"z"\:0,"color"\:"\#FF8D2B79"},{"regionId"\:12889,"regionX"\:37,"regionY"\:41,"z"\:0,"color"\:"\#FF8D2B79"},{"regionId"\:12889,"regionX"\:37,"regionY"\:45,"z"\:0,"color"\:"\#FF8D2B79"},{"regionId"\:12889,"regionX"\:34,"regionY"\:45,"z"\:0,"color"\:"\#FF8D2B79"},{"regionId"\:12889,"regionX"\:31,"regionY"\:45,"z"\:0,"color"\:"\#FF8D2B79"},{"regionId"\:12889,"regionX"\:28,"regionY"\:45,"z"\:0,"color"\:"\#FF8D2B79"},{"regionId"\:12889,"regionX"\:28,"regionY"\:47,"z"\:0,"color"\:"\#FF8D2B79"},{"regionId"\:12889,"regionX"\:28,"regionY"\:50,"z"\:0,"color"\:"\#FF8D2B79"},{"regionId"\:12889,"regionX"\:31,"regionY"\:50,"z"\:0,"color"\:"\#FF8D2B79"},{"regionId"\:12889,"regionX"\:34,"regionY"\:50,"z"\:0,"color"\:"\#FF8D2B79"},{"regionId"\:12889,"regionX"\:37,"regionY"\:50,"z"\:0,"color"\:"\#FF8D2B79"},{"regionId"\:12889,"regionX"\:31,"regionY"\:38,"z"\:0,"color"\:"\#FF8D2B79"}]
runelite.clientBounds=0\:0\:765\:503\:g
actionprogress.cooking.mix-wine=true
banktags.item_4251=herbrun
screenshot.friendDeath=false
thegauntlet.weakNpcOutline=true
runelite.notificationTray=true
BetterNpcHighlight.tileHighlight=false
entityhider.hideThralls=false
loginscreen.pasteenabled=true
dpscounter.autopause=false
discord.showRegionsActivity=true
menuentryswapper.swapTan=false
specialcounter.specDrops=true
boosts.displayBoosts=COMBAT
banktaglayouts.layout_revenants=DISABLED
thegauntlet.timerChatMessage=false
nightmareZone.zappernotification=false
timers.showStamina=true
grounditems.highValueColor=-27136
implings.showearth=NONE
runelite.LapCounterOverlay_preferredPosition=BOTTOM_RIGHT
maxhit.inventoryWeapons=false
worldmap.ancientSpellbookIcon=true
BetterNpcHighlight.trueTileColor=-16711681
thegauntlet.overlayOreDeposit=true
tobqol.displayTimeSplitDifferences=false
MahoganyHomes.-7419237899471359219.currentHome=Tau
xpdrop.rangePrayerColor=-15368019
banktags.item_20727=calvarion,spindel
radiusmarkers.defaultColourAttack=-8454144
banktags.item_20724=bursting,cox,tob
emote-clue-items.HighlightEasy=true
grounditems.lowValueColor=-10046721
worldmap.agilityShortcutTooltips=true
averagetime.Side\ Panel=true
runecraft.showBody=true
clanchat.joinLeaveTimeout=20
antiDrag.disableOnCtrl=false
banktags.item_20720=wintertodt
runelite.XpInfoBoxOverlayFishing_preferredLocation=4\:241
menuentryswapper.swapStairsShiftClick=CLIMB
randomevents.notifyTwin=false
BetterNpcHighlight.trueTileLines=REG
radiusmarkers.defaultRadiusMax=7
agility.lapsPerHour=true
runelite.GWD_KC_preferredLocation=2\:94
idlenotifier.lowEnergy=100
agility.highlightStick=true
woodcutting.highlightBeeHive=true
kourendLibrary.hideDuplicateBook=true
playerindicators.clanchatMenuIcons=true
actionprogress.guardianOfTheRift.crafting=true
implings.eclecticColor=-7234747
questhelper.showFullRequirements=false
woodcutting.forestryRisingRootsNotification=true
blastfurnace.showBarDispenser=false
banktags.item_20712=wintertodt
menuentryswapper.swapTrade=true
zoom.ignoreExamine=false
idlenotifier.prayer=0
thegauntlet.tornadoOutlineColor=-26557
clanchat.clanChatShowJoinLeave=false
xpTracker.pauseSkillAfter=0
grounditems.mediumValuePrice=100000
slayer.statTimeout=5
runelite.kphplugin=true
woodcutting.forestryLeprechaunNotification=true
banktags.item_20704=wintertodt
itemCharge.bindingNotification=true
screenshot.pets=true
BetterNpcHighlight.npcMinimapMode=OFF
slayer.taskCommand=true
interfaceStyles.menuAlpha=255
actionprogress.magic.string-jewellery=true
pyramidplunder.highlightSpeartraps=true
prayer.prayerDoseOrbStartColor=-16711681
hunterplugin.hexColorFullTrap=-16711936
nyloer.makeDarkerHotkey=0\:0
actionprogress.cooking.mix-pastry=true
textrecolor.opaquePrivateMessageSentHighlight=-16767101
actionprogress.fletching.javelins=true
barrows.showChestValue=true
minimap.hideMinimap=false
BetterNpcHighlight.hullRaveSpeed=6000
menuentryswapper.item_11866=2
banktags.item_22954=bursting
NyloerConfig.fontsType=ARIAL
interfaceStyles.alwaysStack=false
woodcutting.showRespawnTimers=true
loginscreen.loginScreen=OFF
emote-clue-items.HighlightEquipment=false
npcid.showId=true
banktags.item_22947=bursting,wildy clue,spindel,calvarion,hydra,tob,slayer
pyramidplunder.highlightDoorsColor=-16711936
customitemhovers.enableObsoleteMessage=false
idlenotifier.highEnergy=0
opponentinfo.showOpponentsInMenu=true
zoom.invertPitch=false
timers.showStaffOfTheDead=true
runelite.blockExtraMouseButtons=true
linemarkers.defaultWidth=3.0
tobqol.xarpusSoundClip=true
timers.showAbyssalSireStun=true
playerindicators.highlightPartyMembers=ENABLED
slayer.highlightTile=false
attackIndicator.removeWarnedStyles=false
tileindicators.highlightDestinationTile=true
fishing.showTiles=true
worldhopper.favorite_391=true
banktags.icon_revenant=21816
worldhopper.favorite_396=true
clanchat.showIgnoresColor=-65536
chatcommands.clearSingleWord=8\:128
runewatch.notifyOnNearby=true
BetterNpcHighlight.clickboxRave=false
idlenotifier.timeout=5000
menuentryswapper.swapBoxTrap=true
BetterNpcHighlight.respawnTileWidth=2
itemstat.consumableStats=true
itemCharge.recoilNotification=false
optimal-quest-guide.inProgressColor=-995461
inventorytags.tag_12006={"color"\:"\#FFFF0000"}
tobqol.verzikSoundClip=false
inventorytags.tag_12002={"color"\:"\#FF0000FF"}
BetterNpcHighlight.areaHighlight=false
groundMarker.region_10291=[{"regionId"\:10291,"regionX"\:1,"regionY"\:17,"z"\:0,"color"\:"\#FFFF7F50"},{"regionId"\:10291,"regionX"\:5,"regionY"\:49,"z"\:0,"color"\:"\#FF7FFFD4"}]
itemprices.showHAValue=true
groundMarker.region_10290=[{"regionId"\:10290,"regionX"\:20,"regionY"\:21,"z"\:0,"color"\:"\#FFCCFF00"},{"regionId"\:10290,"regionX"\:2,"regionY"\:49,"z"\:0,"color"\:"\#FF40E0D0"}]
groundMarker.region_10293=[{"regionId"\:10293,"regionX"\:40,"regionY"\:30,"z"\:0,"color"\:"\#FFFF7300"}]
groundMarker.region_10292=[{"regionId"\:10292,"regionX"\:27,"regionY"\:8,"z"\:0,"color"\:"\#FFFFFF66"},{"regionId"\:10292,"regionX"\:5,"regionY"\:28,"z"\:0,"color"\:"\#FF370037"},{"regionId"\:10292,"regionX"\:0,"regionY"\:29,"z"\:1,"color"\:"\#FFDF8864"}]
virtuallevels.virtualTotalLevel=true
kittenConfig.kittenAttentionOverlay=true
bank.seedVaultValue=true
BetterNpcHighlight.outlineFeather=2
motherlode.showGemsFound=true
runelite.uiWindowOpacity=100
raids.scoutOverlay=true
actionprogress.magic.charge-orbs=true
runelite.entityhiderplugin=false
hunterplugin.hexColorTransTrap=-14336
discord.elapsedTime=ACTIVITY
radiusmarkers.borderWidth=3
attackIndicator.hideAutoRetaliate=false
menuentryswapper.swapPay=true
banktags.item_22997=herbrun
runelite.notificationTimeout=10000
infoboxoverlay.orient_InfoBoxOverlay=HORIZONTAL
BetterNpcHighlight.swTrueTileFillColor=335609855
tobqol.muteXarpusHMEntry=false
emote-clue-items.HighlightGroupStorage=false
pyramidplunder.hideTimer=true
banktags.item_12701=cox,tob
grounditems.mediumValueColor=-6684775
actionprogress.farming.ultracompost=true
barbarianAssault.waveTimes=true
runelite.inventorytagsplugin=false
herblorerecipes.showTooltipOnSeeds=true
banktaglayouts.layout_calvarion=10828\:0,10588\:1,2503\:2,2497\:3,3105\:4,22947\:5,22114\:8,20727\:9,12954\:10,7462\:11,13128\:12,3024\:16,6685\:17,12695\:18,2434\:19,12625\:20,3144\:21,3144\:22,3144\:23,6685\:24,6685\:25,12695\:26,2434\:27,13441\:28,13441\:29,13441\:30,13441\:31,3144\:32,3144\:33,3144\:34,3144\:35,3144\:36,3144\:37,13441\:40,13441\:41,13441\:42,13441\:43,13441\:44,19564\:45
banktags.icon_tob=22325
vanguards.showDmgToReset=true
thegauntlet.weakNpcOutlineWidth=1
thieving.gumdropFactor=0
screenshot.baHighGamble=false
banktags.item_22981=hydra,tob,slayer
grounditems.showMenuItemQuantities=true
banktags.icon_slayer=4141
runecraft.showRifts=true
chatcommands.clearEntireChatBox=0\:0
playerindicators.drawPlayerTiles=false
thegauntlet.phrenRootsOutlineColor=-16711936
tobqol.nyloWavesBigsSWTile=true
radiusmarkers.includeWanderRange=false
screenshot.duels=false
runelite.InfoBoxOverlay_preferredSize=223x35
runewatch.screenshotToClipboard=false
questhelper.showWorldLines=true
BetterNpcHighlight.slayerRaveSpeed=6000
discord.showMinigameActivity=true
gpu.hideUnrelatedMaps=true
itemstat.colorBetterSomecapped=-6492621
idlenotifier.movementidle=false
woodcutting.forestryFloweringTreeNotification=true
BetterNpcHighlight.swTrueTileRaveSpeed=6000
chatfilter.stripAccents=false
menuentryswapper.ui_19660816_882=5
teamCapes.friendsChatMemberCounter=false
runelite.gameSize=765x503
questhelper.showRuneliteObjects=true
discord.showBossActivity=true
friendlist.showWorldOnLogin=false
hiscore.bountylookup=false
raids.scoutOverlayInRaid=true
worldmap.farmingpatchTooltips=true
kourendLibrary.alwaysShowVarlamoreEnvoy=false
actionprogress.herblore.potions=true
randomevents.notifyDunce=false
fishing.showFishingStats=true
worldhopper.displayPing=true
menuentryswapper.ui_19660816_1781=4
inventorytags.tag_11665={"color"\:"\#FFFF0000"}
brushMarkers.brushPolyAlpha=64
inventorytags.tag_11664={"color"\:"\#FF00FF00"}
wintertodt-notifications.notificationFlash=true
menuentryswapper.ui_19660816_1783=4
banktaglayouts.showCoreRuneliteLayoutOptions=false
inventorytags.tag_11663={"color"\:"\#FF0000FF"}
actionprogress.progress-left-color=1694446644
BetterNpcHighlight.trueTileAA=true
worldhopper.favorite_450=true
agility.highlightShortcuts=true
objectindicators.region_13110=[{"id"\:34816,"name"\:"Mysterious ruins","regionId"\:13110,"regionX"\:42,"regionY"\:18,"z"\:0,"color"\:"\#FF7D3700"}]
inventorytags.tag_22328={"color"\:"\#FFFF0000"}
bank.showExact=false
banktaglayouts.warnForAccidentalBankReorder=true
itemidentification.showOres=false
woodcutting.highlightFlowers=true
worldhopper.favorite_467=true
npcindicators.highlightSouthWestTile=false
tobqol.verzikReds=true
objectindicators.region_13106=[{"id"\:34817,"name"\:"Mysterious ruins","regionId"\:13106,"regionX"\:49,"regionY"\:55,"z"\:0,"color"\:"\#FF0000FF"}]
runelite.woodcuttingplugin=true
banktags.item_590=wintertodt
BetterNpcHighlight.trueTileWidth=2.0
xpTracker.onScreenDisplayMode=XP_GAINED
pyramidplunder.highlightedChestFloor=9
nyloer.previousRole=
implings.showgourmet=NONE
gearswitchalert.defaultColourRanged=-16711936
itemCharge.showBraceletOfClayCharges=true
kittenConfig.kittenHungryOverlay=true
runelite.miningplugin=true
actionprogress.fletching.ammunition=true
brushMarkers.brushdrawOnMinimap=false
questhelper.highlightStyleObjects=OUTLINE
BetterNpcHighlight.areaNames=Knight of Ardougne
defaultworld.lastWorld=478
banktags.item_11889=cox,hydra,slayer
timers.showArceuus=true
xpTracker.logoutPausing=true
loottracker.syncPanel=true
tobqol.sotetsegChosenTextOffset=0
raids.enableLayoutWhitelist=false
runewatch.useWDR=true
zoom.middleClickMenu=false
agility.showClickboxes=true
worldhopper.menuOption=true
BetterNpcHighlight.drawBeneath=false
chatnotification.notifyOnHighlight=false
timers.showAntipoison=true
runelite.uiEnableCustomChrome=true
worldhopper.favorite_448=true
antiDrag.dragDelay=30
questhelper.targetOverlayColor=-16711681
worldhopper.favorite_449=true
minimap.zoom=true
herblorerecipes.showPotionRecipes=true
banktags.item_10551=cox,tob
banktags.icon_cox=20997
banktags.item_566=bursting,bandos solo melee
banktags.item_565=bursting,bandos solo melee,cox
nightmareZone.ultimateforcenotification=false
averagetime.Display\ Boss\ Goals\ Panel=true
clanchat.guestClanChatShowJoinLeave=false
textrecolor.transparentClanInfoHighlight=-65536
nyloer.mageHighlightRangeTiles=false
npcindicators.drawNames=false
randomevents.notifySandwich=false
banktags.item_9144=revenant
inventorytags.tag_10372={"color"\:"\#FF00FF00"}
playerindicators.partyMemberNameColor=-1410213
statusbars.enableRestorationBars=true
runelite.rememberScreenBounds=true
implings.gourmetColor=-5667998
chatnotification.notifyOnDuel=false
kittenConfig.kittenDisplaySeconds=true
radiusmarkers.includeAggressionRange=false
xpTracker.progressBarLabel=PERCENTAGE
banktags.item_3840=bursting
banktags.item_21268=herbrun,bursting,hydra,slayer
banktags.item_22114=spindel,calvarion
itemprices.showAlchProfit=false
inventorytags.tag_10370={"color"\:"\#FF00FF00"}
blastfurnace.showCofferTime=true
menuentryswapper.ui_shift_19726336_560=3
prayer.prayerBarHideIfNonCombat=false
customitemhovers.hoverEnableHotReload=false
nyloer.rangeHighlightMeleeTiles=false
optimal-quest-guide.completedColor=-9510546
textrecolor.opaqueClanChatInfoHighlight=-65536
coxscouterexternal.hideBlacklist=false
actionprogress.wintertodt.fletching=true
banktags.icon_wintertodt=20693
banktags.item_12791=bursting,bandos solo melee,wintertodt,cox,hydra,tob,slayer
keyremapping.cameraRemap=true
wintertodt-notifications.disableOverlayText=true
fpscontrol.drawFps=true
banktags.item_22586=revenant
banktags.item_22109=bursting,cox,tob
banktags.item_2503=bursting,wildy clue,spindel,artio,calvarion,revenant
randomevents.notifyAll=false
runelite.panelToggleKey=123\:128
coxscouterexternal.hideRopeless=false
worldhopper.favorite_474=true
agility.highlightMarks=false
chatnotification.highlightOwnName=true
runelite.warningOnExit=LOGGED_IN
thegauntlet.hunllefTileOutlineWidth=1
wiki.leftClickSearch=false
grounditems.insaneValueColor=-39246
actionprogress.crafting.string=true
grandexchange.enableGeLimits=true
hiscore.menuOption=true
worldmap.scrollIcon=true
itemidentification.showEnchantedJewellery=false
maxhit.maxhit=true
pyramidplunder.highlightContainersColor=-256
randomevents.notifyJekyll=false
nyloer.meleeNylocasOutlineColor=-16777216
NyloerConfig.rangeNylocasSymbol=T
fishing.showNames=false
menuentryswapper.swapBones=true
banktags.item_10588=calvarion,tob
nyloer.rangeRoleShiftSwaps=/walk here,*\n/attack,nylocas toxobolos*162*
MahoganyHomes.highlightTeleportsColor=838926335
BetterNpcHighlight.swTileFillColor=335609855
textrecolor.transparentClanGuestInfoHighlight=-65536
screenshot.kingdom=true
emote-clue-items.HighlightBank=true
actionprogress.smooth-progress-bar=true
metronome.tockVolume=0
banktags.item_9185=artio,cox
itemidentification.identificationType=SHORT
entityhider.hidePlayers2D=true
objectindicators.highlightClickbox=true
inventorytags.tag_19547={"color"\:"\#FF00FF00"}
radiusmarkers.markers=[{"id"\:1712192151668,"name"\:"Corrupt Hun Mage","visible"\:true,"collapsed"\:true,"z"\:1,"spawnX"\:0,"spawnY"\:0,"spawnColour"\:"\#FF00FFFF","spawnVisible"\:false,"wanderRadius"\:5,"wanderColour"\:"\#FFFFFF00","wanderVisible"\:true,"maxRadius"\:7,"maxColour"\:"\#FFFF00FF","maxVisible"\:true,"aggressionColour"\:"\#FFFF0000","aggressionVisible"\:true,"retreatInteractionColour"\:"\#FF0000FF","retreatInteractionVisible"\:false,"npcId"\:9037,"attackRadius"\:0,"attackColour"\:"\#FF00C800","attackType"\:"MAGIC","attackVisible"\:true,"huntRadius"\:1,"huntColour"\:"\#FFFF7F00","huntVisible"\:false,"interactionRadius"\:0,"interactionColour"\:"\#FF00C800","interactionVisible"\:false},{"id"\:1712192194235,"name"\:"Corrupt Hun Melee","visible"\:true,"collapsed"\:true,"z"\:1,"spawnX"\:0,"spawnY"\:0,"spawnColour"\:"\#FF00FFFF","spawnVisible"\:false,"wanderRadius"\:5,"wanderColour"\:"\#FFFFFF00","wanderVisible"\:true,"maxRadius"\:7,"maxColour"\:"\#FFFF00FF","maxVisible"\:true,"aggressionColour"\:"\#FFFF0000","aggressionVisible"\:true,"retreatInteractionColour"\:"\#FF0000FF","retreatInteractionVisible"\:false,"npcId"\:9035,"attackRadius"\:0,"attackColour"\:"\#FF7F0000","attackType"\:"MELEE","attackVisible"\:true,"huntRadius"\:1,"huntColour"\:"\#FFFF7F00","huntVisible"\:false,"interactionRadius"\:0,"interactionColour"\:"\#FF7F0000","interactionVisible"\:false},{"id"\:1712191690116,"name"\:"Corrupt bear","visible"\:true,"collapsed"\:true,"z"\:1,"spawnX"\:0,"spawnY"\:0,"spawnColour"\:"\#FF00FFFF","spawnVisible"\:false,"wanderRadius"\:5,"wanderColour"\:"\#FFFFFF00","wanderVisible"\:true,"maxRadius"\:7,"maxColour"\:"\#FFFF00FF","maxVisible"\:true,"aggressionColour"\:"\#FFFF0000","aggressionVisible"\:true,"retreatInteractionColour"\:"\#FF0000FF","retreatInteractionVisible"\:false,"npcId"\:9046,"attackRadius"\:16,"attackColour"\:"\#FF7F0000","attackType"\:"MELEE","attackVisible"\:true,"huntRadius"\:1,"huntColour"\:"\#FFFF7F00","huntVisible"\:false,"interactionRadius"\:0,"interactionColour"\:"\#FF7F0000","interactionVisible"\:true},{"id"\:1712191917708,"name"\:"Corrupt dark beast","visible"\:true,"collapsed"\:true,"z"\:1,"spawnX"\:0,"spawnY"\:0,"spawnColour"\:"\#FF00FFFF","spawnVisible"\:false,"wanderRadius"\:5,"wanderColour"\:"\#FFFFFF00","wanderVisible"\:true,"maxRadius"\:7,"maxColour"\:"\#FFFF00FF","maxVisible"\:true,"aggressionColour"\:"\#FFFF0000","aggressionVisible"\:true,"retreatInteractionColour"\:"\#FF0000FF","retreatInteractionVisible"\:false,"npcId"\:9048,"attackRadius"\:16,"attackColour"\:"\#FF00C800","attackType"\:"RANGED","attackVisible"\:true,"huntRadius"\:1,"huntColour"\:"\#FFFF7F00","huntVisible"\:false,"interactionRadius"\:0,"interactionColour"\:"\#FF00C800","interactionVisible"\:true},{"id"\:1712191955805,"name"\:"Corrupt dragon","visible"\:true,"collapsed"\:true,"z"\:1,"spawnX"\:0,"spawnY"\:0,"spawnColour"\:"\#FF00FFFF","spawnVisible"\:false,"wanderRadius"\:5,"wanderColour"\:"\#FFFFFF00","wanderVisible"\:true,"maxRadius"\:7,"maxColour"\:"\#FFFF00FF","maxVisible"\:true,"aggressionColour"\:"\#FFFF0000","aggressionVisible"\:true,"retreatInteractionColour"\:"\#FF0000FF","retreatInteractionVisible"\:false,"npcId"\:9047,"attackRadius"\:16,"attackColour"\:"\#FF0000FF","attackType"\:"MAGIC","attackVisible"\:true,"huntRadius"\:1,"huntColour"\:"\#FFFF7F00","huntVisible"\:false,"interactionRadius"\:0,"interactionColour"\:"\#FF0000FF","interactionVisible"\:true},{"id"\:1712192255533,"name"\:"Corrupt Hun Range","visible"\:true,"collapsed"\:true,"z"\:1,"spawnX"\:0,"spawnY"\:0,"spawnColour"\:"\#FF00FFFF","spawnVisible"\:false,"wanderRadius"\:5,"wanderColour"\:"\#FFFFFF00","wanderVisible"\:true,"maxRadius"\:7,"maxColour"\:"\#FFFF00FF","maxVisible"\:true,"aggressionColour"\:"\#FFFF0000","aggressionVisible"\:true,"retreatInteractionColour"\:"\#FF0000FF","retreatInteractionVisible"\:false,"npcId"\:9036,"attackRadius"\:0,"attackColour"\:"\#FF0000FF","attackType"\:"RANGED","attackVisible"\:true,"huntRadius"\:1,"huntColour"\:"\#FFFF7F00","huntVisible"\:false,"interactionRadius"\:0,"interactionColour"\:"\#FF0000FF","interactionVisible"\:false}]
randomevents.notifyMime=false
banktags.item_2556=spindel,revenant
banktags.item_2554=revenant
averagetime.Boss\ Goals\ Top=KPH
banktags.item_2552=revenant
herbiboar.showObject=true
BetterNpcHighlight.tileNames=
grounditems.highlight_207=-3663692
boosts.displayNextBuffChange=BOOSTED
radiusmarkers.defaultRadiusHunt=1
grounditems.highlight_209=-3663692
inventorytags.tag_19544={"color"\:"\#FF0000FF"}
grounditems.highlight_203=-3663692
runepouch.runePouchOverlayMode=BOTH
grounditems.highlight_205=-3663692
idlenotifier.interactionidle=true
banktags.item_2558=revenant
grounditems.highlight_201=-3663692
runewatch.menuOption=true
nyloer.mageHighlightMageTiles=false
thegauntlet.hunllefOutlineColor=-1
emote-clue-items.HighlightKeptOnDeath=false
lowmemory.hideLowerPlanes=false
menuentryswapper.npc_1561=-1
implings.showlucky=HIGHLIGHT
grounditems.highlight_217=-3663692
pyramidplunder.highlightedSarcophagusFloor=9
fishing.trawlerTimer=true
menuentryswapper.groundItemShiftClickWalkHere=false
grounditems.highlight_213=-3663692
BetterNpcHighlight.hullColor=-65281
xpTracker.prioritizeRecentXpSkills=false
clanchat.recentChats=true
grounditems.highlight_215=-3663692
grounditems.itemHighlightMode=NONE
grounditems.highlight_211=-3663692
randomevents.notifyFlippa=false
tobqol.debugSotetsegChosenText=false
screenshot.clanDeath=false
tobqol.maidenCrabHPDisplayType=OFF
teamCapes.teamCapesOverlay=false
BetterNpcHighlight.ignoreDeadNpcs=false
banktags.item_185=cox
nyloer.splitPrefix=s
thegauntlet.oreDepositFillColor=855572480
npcindicators.highlightcolor_1560=-14597533
itemCharge.showImpCharges=true
npcindicators.drawMinimapNames=false
statusbars.leftBarMode=HITPOINTS
npcindicators.tagstyle_0=tile
dpscounter.bossDamage=false
itemidentification.showTeleportScrolls=false
fightcavewaves.waveDisplay=BOTH
NyloerConfig.mageNylocasColor=-16711681
inventorytags.tag_12926={"color"\:"\#FF00FF00"}
herblorerecipes.showTooltipOnGrimy=true
idlenotifier.hitpoints=0
banktags.item_173=cox,tob
BetterNpcHighlight.hullIds=
objectindicators.outlineFeather=0
poh.showAltar=true
runelite.objectindicatorsplugin=true
runelite.dragHotkey=0\:512
bank.searchKeybind=70\:128
npcUnaggroArea.npcAggroAreaColor=1694498560
runelite.RESIZABLE_VIEWPORT_CHATBOX_PARENT_preferredLocation=0\:852
randomevents.notifyGenie=false
runewatch.screenshotTrades=true
nyloer.meleeRoleShiftSwaps=/walk here,*\n/attack,nylocas ischyros*162*
thegauntlet.resourceTrackingMode=DECREMENT
worldhopper.favorite_415=true
worldhopper.favorite_416=true
runelite.npcaggroareaplugin=false
fightcavewaves.commonNames=false
MahoganyHomes.displayHintArrows=true
runelite.itemstatplugin=true
NyloerConfig.showNylocasWave=true
banktaglayouts.layout_new\ tob=DISABLED
inventorytags.tag_12954={"color"\:"\#FFFF0000"}
itemidentification.showFruitTreeSeeds=false
nightmareZone.powersurgenotification=false
timers.showCharge=true
tileindicators.currentTileBorderWidth=2.0
radiusmarkers.defaultRadiusWander=5
menuentryswapper.npc_1511=2
runelite.containInScreen2=ALWAYS
thegauntlet.overlayLinumTirinum=true
textrecolor.opaquePublicChatHighlight=-16777216
averagetime.Side\ Panel\ Position=6
interacthighlight.objectShowHover=true
actionprogress.cooking.cooking=true
gearswitchalert.showTagOutline=true
grandexchange.showExact=false
worldhopper.favorite_428=true
BetterNpcHighlight.swTrueTileWidth=2.0
BetterNpcHighlight.hullWidth=2.0
keyremapping.fkeyRemap=false
grounditems.lowValuePrice=20000
xpTracker.resetSkillRateAfter=0
banktags.item_13239=bandos solo melee,cox,hydra,tob,slayer
worldhopper.favorite_420=true
tobqol.bankAllMES=true
grandexchange.showActivelyTradedPrice=true
customcursor.cursorStyle=RS3_GOLD
worldhopper.ping=false
questhelper.outlineFeathering=4
BetterNpcHighlight.taskColor=-2081743
randomevents.notifyPrison=false
questhelper.autoOpenSidebar=true
actionprogress.tempoross.firing=true
puzzlesolver.displayRemainingMoves=true
playerindicators.clanMenuIcons=true
BetterNpcHighlight.turboHighlight=false
optimal-quest-guide.filterMetRequirements=false
nyloer.meleeHighlightMeleeTiles=false
agility.portalsHighlight=-65281
bank.showHA=false
poh.showJewelleryBox=true
banktags.item_13226=bursting
runelite.AttackStylesOverlay_preferredSize=53x32
optimal-quest-guide.searchCompletedQuests=false
barbarianAssault.showHealerBars=true
banktags.icon_spindel=13177
wintertodt.notifyEmptyInv=true
textrecolor.transparentClanChatMessageHighlight=-1
tobqol.salveReminderColor=-16711681
bank.showGE=true
clanchat.confirmKicks=false
BetterNpcHighlight.highlightPets=false
thegauntlet.resourceTracker=true
NyloerConfig.splitsAsNextWave=false
tobqol.displayRoomTimes=OFF
tearsofguthix.greenTearsColor=1677786880
party.pingHotkey=0\:0
menuentryswapper.swapEssenceMineTeleport=false
banktaglayouts.layout_spindel=10828\:0,1725\:1,2503\:2,2497\:3,3105\:4,22947\:5,22114\:8,20727\:9,12954\:10,7462\:11,13128\:12,6685\:16,3024\:17,6685\:18,6685\:19,2434\:20,12625\:21,2556\:22,13441\:23,6685\:24,3024\:25,6685\:26,3024\:27,12695\:28,2448\:29,3144\:30,3144\:31,806\:32,13441\:33,13441\:34,13441\:35,13441\:36,13441\:37,3144\:40,3144\:41,3144\:42,3144\:43,3144\:44,19564\:45
brushMarkers.brushColor10=-256
playerindicators.clanChatMemberColor=-14413909
banktags.item_2564=revenant
banktags.item_1231=slayer
vanguards.rangeColor=-16711936
nyloer.rangeNylocasOutlineColor=-16777216
itemidentification.showImplingJars=false
timers.showFreezes=true
brushMarkers.brushColor12=-65281
brushMarkers.brushColor11=-16711681
pyramidplunder.timerLowWarning=30
groundMarker.region_10307=[{"regionId"\:10307,"regionX"\:31,"regionY"\:7,"z"\:0,"color"\:"\#FF214263"}]
thegauntlet.utilitiesOutline=true
worldhopper.worldTypeFilter=["NORMAL"]
runelite.CookingOverlay_preferredLocation=4\:102
actionprogress.show-product-icons=true
linemarkers.showMinimap=true
runelite.partyplugin2=true
grounditems.textOutline=false
partypanel.alwaysShowIcon=true
implings.showmagpie=NONE
fishing.statTimeout=5
interacthighlight.objectHoverHighlightColor=-1878982657
worldmap.minigameTooltip=true
banktags.useTabs=true
worldhopper.subscriptionFilter=MEMBERS
itemCharge.showWaterskinCharges=true
averagetime.Output\ Info=false
music.musicVolume=-3
runelite.trayIcon=true
boosts.compactDisplay=false
BetterNpcHighlight.presetColorAmount=ZERO
hunterplugin.hexColorEmptyTrap=-65536
thegauntlet.overlayFishingSpot=true
tobqol.muteVerzikSounds=false
questhelpervars.herbSeeds=GUAM
banktaglayouts.useWithInventorySetups=true
thegauntlet.strongNpcOutlineWidth=1
screenshot.notifyWhenTaken=true
groundMarker.drawOnMinimap=true
runecraft.showFire=true
poh.showRepairStand=true
BetterNpcHighlight.clickboxFillColor=335609855
xpglobes.Progress\ arc\ width=2
MahoganyHomes.worldMapIcon=true
runecraft.showAir=true
questhelper.showFan=false
banktaglayouts.version=1.4.29
raids.uploadScreenshot=CLIPBOARD
itemCharge.showAmuletOfChemistryCharges=true
banktags.item_23075=bursting,hydra,slayer
objectindicators.rememberObjectColors=true
defencetracker.lowDef=10
defencetracker.vulnerability=true
music.soundEffectVolume=-18
grounditems.notifyHighlightedDrops=false
banktags.item_6739=wintertodt
Shooting\ Stars\ Tracking.timeTillRemove=85
screenshot.playerDeath=false
entityhider.hideProjectiles=false
gearswitchalert.secondsBeforeTagging=0
runelite.itempricesplugin=true
chatfilter.collapseGameChat=false
randomevents.notifyMoM=false
banktags.icon_hydra=22978
tobqol.lootReminderColor=-926656167
thegauntlet.tornadoFillColor=855637760
herblorerecipes.showTooltipOnUnfinished=true
runelite.notificationRequestFocus=OFF
screenshot.combatAchievements=true
idlenotifier.oxygen=0
boosts.notifyOnBoost=true
tobqol.xarpusInstanceTimer=false
objectindicators.highlightTile=false
party.statusOverlayPrayer=false
NyloerConfig.fontsBold=true
banktaglayouts.layout_bursting=23075\:0,12002\:1,9674\:2,9676\:3,22954\:4,22947\:5,8013\:6,21793\:8,4675\:9,3840\:10,19544\:11,13128\:12,22109\:16,2434\:17,806\:18,566\:19,9763\:20,1540\:21,25781\:22,21268\:23,2503\:24,2434\:25,2434\:26,554\:27,20724\:28,556\:29,19634\:30,12791\:31,555\:32,565\:33,560\:34
entityhider.hideClanMates=false
grounditems.highlight_199=-3663692
runelite.zomleftclickdropper=true
discord.showMainMenu=true
playerindicators.highlightClanMembers=ENABLED
menuentryswapper.shiftClickCustomization=true
groundMarker.region_11673=[{"regionId"\:11673,"regionX"\:20,"regionY"\:17,"z"\:0,"color"\:"\#FF00FFFF"}]
chatcommands.lms=true
menuentryswapper.swapTemporossLeave=false
groundMarker.region_11672=[{"regionId"\:11672,"regionX"\:38,"regionY"\:53,"z"\:0,"color"\:"\#FF00FFFF"}]
questhelper.haveMinimapArrowFlash=true
questhelper.showCompletedQuests=false
screenshot.uploadScreenshot=NEITHER
idlenotifier.hitpointsNotification={"enabled"\:false,"initialized"\:false,"override"\:false,"tray"\:false,"volume"\:0,"timeout"\:0,"gameMessage"\:false,"sendWhenFocused"\:false}
metronome.tickVolume=96
worldmap.runecraftingAltarIcon=true
tobqol.themedDeathBall=true
customitemhovers.openDirChatCommand=openhoverdir
runecraft.showSoul=true
banktags.icon_bandos\ solo\ melee=11834
clanchat.privateMessageIcons=false
chatfilter.filterClan=false
gpu.uiScalingMode=LINEAR
grounditems.hotkey=0\:512
tobqol.verzikSoundClipVolume=65
bankedexperience.grabFromLootingBag=false
runelite.grounditemsplugin=true
entityhider.hideLocalPlayer=false
menuentryswapper.teleportSubmenus=false
entityhider.hideNPCs2D=false
tobqol.fontType=REGULAR
BetterNpcHighlight.hullNames=Knight of Ardougne
questhelper.lastversionchecked=Quest Helper has been updated to 4.3.0\! This adds Defender of Varrock.
cannon.showEmptyCannonNotification=true
itemidentification.showAllotmentSeeds=false
runelite.banktaglayoutsplugin=true
timers.showBlessedCrystalScarab=true
zoom.invertYaw=false
discord.showSkillActivity=true
npcid.textColour=-1
Shooting\ Stars\ Tracking.notifyTime=0
worldmap.miningSiteTooltips=true
actionprogress.magic.enchant-bolts=true
averagetime.Display\ Idle\ Time=false
herblorerecipes.showTooltipInBank=true
menuentryswapper.swapHerbs=true
itemstat.colorBetterUncapped=-13373901
idlenotifier.lowEnergyNotification={"enabled"\:false,"initialized"\:false,"override"\:false,"tray"\:false,"volume"\:0,"timeout"\:0,"gameMessage"\:false,"sendWhenFocused"\:false}
screenshot.collectionLogEntries=true
groundMarker.region_13878=[{"regionId"\:13878,"regionX"\:38,"regionY"\:33,"z"\:0,"color"\:"\#FFFF00FF"},{"regionId"\:13878,"regionX"\:25,"regionY"\:43,"z"\:0,"color"\:"\#FF00FFFF"},{"regionId"\:13878,"regionX"\:54,"regionY"\:29,"z"\:0,"color"\:"\#FF0000FF"}]
screenshot.kills=false
thegauntlet.linumTirinumFillColor=855638015
menuentryswapper.bankDepositShiftClick=EXTRA_OP
implings.earthColor=-12691904
textrecolor.transparentClanMessageHighlight=-1
party.statusOverlayVeng=true
xpglobes.Orb\ duration=10
partypanel.showPartyPassphrase=true
nyloer.splitFontsSize=12
groundMarker.showImportExport=true
BetterNpcHighlight.outlineWidth=2
itemidentification.showBerrySeeds=false
itemCharge.veryLowWarningColor=-65536
optimal-quest-guide.requirementUnmetColor=-1696226
questhelper.failColour=-65536
itemCharge.braceletOfClayNotification=true
timers.showAntiFire=true
nyloer.meleeNylocasSymbol=I
defaultworld.useLastWorld=false
BetterNpcHighlight.slayerAA=true
inventorytags.tag_11907={"color"\:"\#FF0000FF"}
woodcutting.showNestNotification=true
slayer.weaknessPrompt=true
implings.showname=true
actionprogress.cooking.slicing=true
menuentryswapper.npc_1260=-1
mousehighlight.uiTooltip=true
runelite.InventoryViewerOverlay_preferredLocation=573\:738
banktags.item_4587=wildy clue
music.muteOwnAreaSounds=false
chathistory.clearHistory=true
textrecolor.transparentClanChatGuestMessageHighlight=-1
menuentryswapper.objectLeftClickCustomization=true
attackIndicator.warnForRanged=false
grounditems.showHighlightedOnly=true
nyloer.splitsAsNextWave=false
BetterNpcHighlight.swTileLines=REG
itemidentification.showPyreLogs=false
banktags.item_11941=revenant
herblorerecipes.showTooltipInInventory=true
roofremoval.removePosition=true
thegauntlet.phrenRootsFillColor=838926080
radiusmarkers.defaultColourMax=-65281
driftnet.untaggedFishColor=-16711681
menuentryswapper.object_28822=2
combatlevel.wildernessAttackLevelRange=true
blastmine.hexWarningColor=-2542080
screenshot.hotkey=0\:0
poh.showXericsTalisman=true
thegauntlet.strongNpcOutline=true
worldhopper.showSidebar=false
nyloer.rangeHighlightMageTiles=false
wintertodt.showOverlay=true
blastfurnace.showConveyorBelt=false
groundMarker.region_10392=[{"regionId"\:10392,"regionX"\:3,"regionY"\:28,"z"\:0,"color"\:"\#FF7399B2"}]
actionprogress.fletching.bows=true
herbiboar.showTrail=true
menuentryswapper.bankWithdrawShiftClick=WITHDRAW_ALL
timers.showPickpocketStun=true
tobqol.spellbookReminderColor=-256
herblorerecipes.showImpRepellentIngs=false
timetracking.activeTab=HERB
groundMarker.region_12109=[{"regionId"\:12109,"regionX"\:48,"regionY"\:60,"z"\:1,"color"\:"\#FFFF7300"}]
itemstat.colorNoChange=-1118482
menuentryswapper.swapMorytaniaLegs=WEAR
actionprogress.crafting.leather=true
wintertodt.notifyBrazierOut=true
blastmine.showTimerOverlay=true
banktags.item_4151=barrows * tob
music.muteOtherAreaEnvironmentSounds=false
emote-clue-items.TrackInventory=true
runelite.groundmarkerplugin=true
npcindicators.highlightOutline=true
interfaceStyles.hdMenu=false
gpu.smoothBanding=false
xpglobes.showVirtualLevel=false
grounditems.highlightValueCalculation=HIGHEST
runelite.npcidplugin=false
questhelper.autostartQuests=true
interfaceStyles.hdHealthBars=false
runelite.runewatchplugin=true
chatcommands.duels=true
groundMarker.region_12598=[{"regionId"\:12598,"regionX"\:29,"regionY"\:31,"z"\:0,"color"\:"\#FFFFFF00"}]
randomevents.notifyQuiz=false
xpglobes.enableTooltips=true
coxscouterexternal.showTutorialOverlay=true
partypanel.autoExpandMembers=false
runelite.notificationFocused=false
thegauntlet.tornadoTileOutlineWidth=1
actionprogress.misc.campfire=true
itemCharge.showBindingNecklaceCharges=true
menuentryswapper.swapHarpoon=false
banktags.item_6326=revenant
banktags.item_6328=revenant
woodcutting.forestryEnchantmentRitualNotification=true
runelite.fontType=SMALL
banktags.item_21793=bursting,cox
kourendLibrary.showTargetHintArrow=true
thegauntlet.linumTirinumOutlineColor=-1
objectindicators.region_7224=[{"id"\:28823,"name"\:"Fruit Stall","regionId"\:7224,"regionX"\:3,"regionY"\:24,"z"\:0,"color"\:"\#FF00FFFF"},{"id"\:28823,"name"\:"Fruit Stall","regionId"\:7224,"regionX"\:9,"regionY"\:24,"z"\:0,"color"\:"\#FF00FFFF"}]
emote-clue-items.HighlightHard=true
thegauntlet.demibossOutline=true
menuentryswapper.swapBanker=true
banktaglayouts.layout_clues=DISABLED
worldhopper.quickhopOutOfDanger=true
inventorytags.tag_6570={"color"\:"\#FFFF0000"}
chatcommands.lvl=true
banktags.item_21304=tob
timers.showVengeance=true
timers.showMenaphiteRemedy=true
corp.showDamage=true
averagetime.Display\ Session\ Time=true
boosts.relativeBoost=false
inventorytags.tag_13239={"color"\:"\#FFFF0000"}
BetterNpcHighlight.hideInstructions=\#\#\# Format\:\n\n\!hide [npc name]\n\!hide [npc id]\n\!unhide [npc name]\n\!unhide [npc id]\n---------------------\n\#\#\# Example\:\n\n"\!hide cow" -> This would add "cow" to the Entity Hider names list\n\n"\!unhide 1234" -> This would remove "1234" from the Entity Hider IDs list\n
objectindicators.region_10315=[{"id"\:34764,"name"\:"Altar","regionId"\:10315,"regionX"\:25,"regionY"\:38,"z"\:0,"color"\:"\#FF0000FF"}]
blastmine.showRockIconOverlay=true
radiusmarkers.defaultColourAggression=-65536
worldmap.agilityShortcutIcon=true
party.previousPartyId=kenko
grounditems.collapseEntries=false
vanguards.highlight=true
poh.showPortals=true
objectindicators.region_7227=[{"id"\:10529,"name"\:"Bank Deposit Box","regionId"\:7227,"regionX"\:14,"regionY"\:9,"z"\:0,"color"\:"\#FFDD00FF"}]
thegauntlet.weakNpcOutlineColor=-14336
raids.screenshotHotkey=0\:0
worldmap.hunterAreaTooltips=true
actionprogress.smithing.cannonballs=true
banktaglayouts.layout_hydra=23075\:0,6585\:1,9674\:2,9676\:3,22981\:4,22947\:5,6570\:8,11889\:9,12954\:10,13239\:11,11773\:12,13576\:16,12695\:17,2434\:18,2434\:19,12791\:20,21268\:21,12905\:24,2434\:25,2434\:26,13441\:27,3144\:28
MahoganyHomes.highlightStairs=true
xpglobes.enableCustomArcColor=false
radiusmarkers.defaultColourWander=-256
dailytaskindicators.showEssence=false
emote-clue-items.HighlightMaster=true
runelite.marker1720318034283_preferredLocation=496\:45
itemidentification.showGems=false
playerindicators.highlightSelf=DISABLED
runenergy.ringOfEnduranceChargeMessage=true
npcindicators.highlightSouthWestTrueTile=false
wintertodt.notifySnowfall=INTERRUPT
timetracking.sortOrder=NONE
menuentryswapper.npc_8725=-1
bankxpvalue.resetToCenter=false
runelite.InfoBoxOverlay_preferredPosition=BOTTOM_RIGHT
linemarkers.markers=[{"id"\:1711503283942,"name"\:"Marker 1","visible"\:true,"collapsed"\:false,"lines"\:[{"colour"\:"\#FFFFFF00","edge"\:"WEST","width"\:3.0,"location"\:{"x"\:1733,"y"\:3477,"plane"\:0}}]},{"id"\:1711830308466,"name"\:"Marker 2","visible"\:true,"collapsed"\:false,"lines"\:[{"colour"\:"\#FFFFFF00","edge"\:"WEST","width"\:3.0,"location"\:{"x"\:1972,"y"\:5688,"plane"\:1}}]},{"id"\:1711844552096,"name"\:"Marker 3","visible"\:true,"collapsed"\:false,"lines"\:[{"colour"\:"\#FFFFFF00","edge"\:"WEST","width"\:3.0,"location"\:{"x"\:1972,"y"\:5688,"plane"\:1}}]},{"id"\:1712192325929,"name"\:"Marker 4","visible"\:true,"collapsed"\:false,"lines"\:[{"colour"\:"\#FFFFFF00","edge"\:"WEST","width"\:3.0,"location"\:{"x"\:1972,"y"\:5688,"plane"\:1}},{"colour"\:"\#FFFFFF00","edge"\:"WEST","width"\:3.0,"location"\:{"x"\:1972,"y"\:5688,"plane"\:1}}]},{"id"\:1712192340009,"name"\:"Marker 5","visible"\:true,"collapsed"\:false,"lines"\:[{"colour"\:"\#FFFFFF00","edge"\:"WEST","width"\:3.0,"location"\:{"x"\:1971,"y"\:5688,"plane"\:1}}]},{"id"\:1712192342049,"name"\:"Marker 6","visible"\:true,"collapsed"\:false,"lines"\:[{"colour"\:"\#FFFFFF00","edge"\:"WEST","width"\:3.0,"location"\:{"x"\:1972,"y"\:5688,"plane"\:1}},{"colour"\:"\#FFFFFF00","edge"\:"WEST","width"\:3.0,"location"\:{"x"\:1973,"y"\:5688,"plane"\:1}}]},{"id"\:1712192368268,"name"\:"Marker 7","visible"\:true,"collapsed"\:false,"lines"\:[{"colour"\:"\#FFFFFF00","edge"\:"WEST","width"\:3.0,"location"\:{"x"\:1973,"y"\:5688,"plane"\:1}},{"colour"\:"\#FFFFFF00","edge"\:"WEST","width"\:3.0,"location"\:{"x"\:1972,"y"\:5688,"plane"\:1}},{"colour"\:"\#FFFFFF00","edge"\:"WEST","width"\:3.0,"location"\:{"x"\:1971,"y"\:5688,"plane"\:1}},{"colour"\:"\#FFFFFF00","edge"\:"WEST","width"\:3.0,"location"\:{"x"\:1971,"y"\:5688,"plane"\:1}},{"colour"\:"\#FFFFFF00","edge"\:"WEST","width"\:3.0,"location"\:{"x"\:1971,"y"\:5688,"plane"\:1}}]}]
BetterNpcHighlight.swTileColor=-5497071
fishing.harpoonfishOverlayColor=-16711936
brushMarkers.brushFillPoly=false
randomevents.notifyTurpentine=false
vanguards.showDatabox=false
herblorerecipes.showTooltipGroupStorage=true
menuentryswapper.swapDesertAmulet=WEAR
chatfilter.collapsePlayerChat=false
tobqol.fontSize=16
questhelper.solvePuzzles=true
menuentryswapper.ui_19726336_4542=5
thegauntlet.resourceIconSize=14
banktaglayouts.layout_bandos\ solo\ melee=24271\:0,6585\:1,10370\:2,4994\:3,13239\:4,20232\:5,6570\:8,14006\:9,12954\:10,7462\:11,20657\:12,4675\:16,13441\:17,23991\:18,13441\:19,13576\:20,13441\:21,6685\:22,6685\:23,12002\:24,12631\:25,19544\:26,13441\:27,13441\:28,13441\:29,6685\:30,6685\:31,6685\:32,12695\:33,12695\:34,3024\:35,3024\:36,8013\:37,6685\:40,12695\:41,3024\:42,3024\:43,3024\:44,12791\:45,560\:48,565\:49,566\:50
optimal-quest-guide.notStartedColor=-3750202
inventorytags.tag_6585={"color"\:"\#FFFF0000"}
interacthighlight.npcShowInteract=true
xpdrop.fakeXpDropDelay=0
pyramidplunder.highlightDoors=true
questhelper.textHighlightColor=-16776961
timers.showImbuedHeart=true
maxhit.applyCharge=false
itemprices.showGEPrice=true
gpu.fogDepth=2
averagetime.Display\ Boss\ Goals\ Overlay=true
runelite.RESIZABLE_VIEWPORT_INVENTORY_PARENT_preferredLocation=1679\:682
menuentryswapper.ui_19660816_453=5
pyramidplunder.showExactTimer=true
objectindicators.region_6454=[{"id"\:28851,"name"\:"Gate","regionId"\:6454,"regionX"\:57,"regionY"\:49,"z"\:0,"color"\:"\#FFFF7300"},{"id"\:28852,"name"\:"Gate","regionId"\:6454,"regionX"\:57,"regionY"\:48,"z"\:0,"color"\:"\#FFFF7300"}]
gearswitchalert.fillOpacity=50
clanchat.showJoinLeave=false
nyloer.showNylocasSymbol=true
tobqol.hideCeilingChains=true
agility.highlightSepulchreNpcs=true
regenmeter.showSpecial=true
itemCharge.showDodgyCount=true
mousehighlight.chatboxTooltip=true
optimal-quest-guide.requirementBoostableColor=-13459206
menuentryswapper.ui_19660816_447=5
worldmap.fairyRingIcon=true
inventorytags.tag_7462={"color"\:"\#FFFF7300"}
keyremapping.esc=27\:0
BetterNpcHighlight.hullRave=false
brushMarkers.brushColor4=-256
brushMarkers.brushColor5=-16711681
brushMarkers.brushColor6=-65281
brushMarkers.brushColor7=-65536
questhelper.highlightItemsBackground=false
brushMarkers.brushColor1=-65536
brushMarkers.brushColor2=-16711936
brushMarkers.brushColor3=-16776961
emote-clue-items.HighlightGuidePrices=false
randomevents.notifyDemon=false
bank.rightClickBankInventory=false
barrows.showPrayerDrainTimer=true
banktaglayouts.layout_wintertodt=4502\:0,556\:32,20720\:1,557\:33,19693\:2,563\:34,19695\:3,20712\:8,20704\:9,14250\:10,2347\:16,590\:17,1993\:18,1993\:19,12791\:20,946\:24,6739\:25,1993\:26,1993\:27
MahoganyHomes.showSessionStats=true
itemCharge.showAmuletOfBountyCharges=true
grounditems.hideUnderValue=0
BetterNpcHighlight.clickboxAA=true
BetterNpcHighlight.clickboxHighlight=false
reportButton.time=LOGIN_TIME
menuentryswapper.swapPick=false
thieving.grubRate=225
banktags.item_23991=bandos solo melee
chatnotification.notifyOnOwnName=false
timers.showDfsSpecial=true
thegauntlet.overlayPhrenRoots=true
hiscore.virtualLevels=true
inventorytags.tag_12899={"color"\:"\#FF0000FF"}
groundMarker.region_13395=[{"regionId"\:13395,"regionX"\:22,"regionY"\:12,"z"\:3,"color"\:"\#FF00FF7D"},{"regionId"\:13395,"regionX"\:6,"regionY"\:11,"z"\:3,"color"\:"\#FF00FF7D"},{"regionId"\:13395,"regionX"\:14,"regionY"\:24,"z"\:3,"color"\:"\#FF00FF7D"}]
runecraft.showDeath=true
xpglobes.showXpLeft=true
dailytaskindicators.showHerbBoxes=true
banktags.item_23987=tob
poh.showPools=true
runelite.betternpchighlightplugin=false
itemprices.showEA=true
runecraft.degradingNotification=true
implings.showninja=NONE
tobqol.lootReminder=false
woodcutting.forestryPheasantControlNotification=true
BetterNpcHighlight.hullAA=true
runelite.gameAlwaysOnTop=false
nyloer.mageRoleSwaps=attack,nylocas ischyros*260*\nattack,nylocas ischyros*162*\nattack,nylocas toxobolos*260*\nattack,nylocas toxobolos*162*\nattack,nylocas hagios*260*\nattack,nylocas hagios*162*
menuentryswapper.ui_19660816_440=5
fishing.trawlerContribution=true
prayer.prayerFlickAlwaysOn=false
textrecolor.opaqueClanMessageHighlight=-16777216
radiusmarkers.defaultRadiusAttack=1
thegauntlet.darkBeastOutlineColor=-16711936
slayer.itemoverlay=true
kingdomofmiscellania.sendNotifications=false
woodcutting.forestryStrugglingSaplingNotification=true
roofremoval.removeHovered=true
worldmap.jewelleryIcon=true
fightcavewaves.showMonsterLevel=true
BetterNpcHighlight.tileAA=true
herblorerecipes.showPrimaryIngredientsInTooltip=true
feed.includeTweets=true
dailytaskindicators.showDynamite=false
objectindicators.region_12105=[{"id"\:10851,"name"\:"Climbing rocks","regionId"\:12105,"regionX"\:35,"regionY"\:26,"z"\:3,"color"\:"\#FFCC00FF"},{"id"\:10851,"name"\:"Climbing rocks","regionId"\:12105,"regionX"\:35,"regionY"\:25,"z"\:3,"color"\:"\#FFCC00FF"}]
BetterNpcHighlight.slayerRave=false
banktags.icon_herbrun=9774
dailytaskindicators.showBonemeal=false
itemCharge.dodgyNotification=true
tithefarmplugin.hexColorGrown=-16721664
objectindicators.region_12109=[{"id"\:7256,"name"\:"Doorway","regionId"\:12109,"regionX"\:48,"regionY"\:63,"z"\:1,"color"\:"\#FF00FFFF"}]
runelite.lockWindowSize=false
groundMarker.region_12084=[{"regionId"\:12084,"regionX"\:4,"regionY"\:26,"z"\:0,"color"\:"\#FF0000FF"},{"regionId"\:12084,"regionX"\:17,"regionY"\:34,"z"\:0,"color"\:"\#FF00FFFF"},{"regionId"\:12084,"regionX"\:17,"regionY"\:33,"z"\:0,"color"\:"\#FFFF7300"}]
banktags.item_1540=bursting
boosts.displayNextDebuffChange=NEVER
fairyrings.autoOpen=true
runelite.tileindicatorsplugin=false
BetterNpcHighlight.tileRave=false
averagetime.Session\ Timeout=0
runelite.notificationVolume=100
thegauntlet.resourceShard=540
partypanel.showPartyControls=true
BetterNpcHighlight.swTileRave=false
banktaglayouts.layout_cox=24271\:0,6585\:1,10551\:2,10372\:3,13239\:4,9242\:5,19352\:6,555\:7,6570\:8,11889\:9,12954\:10,7462\:11,11773\:12,13393\:13,565\:14,2444\:15,12899\:16,21793\:17,4868\:18,10370\:19,22109\:20,13576\:21,1275\:22,9185\:23,12002\:24,4874\:25,19544\:26,19547\:27,12926\:28,20724\:29,12018\:30,12911\:31,173\:32,12701\:33,6685\:34,6685\:35,3024\:36,3024\:37,12625\:38,12695\:39,12631\:40,13441\:41,6685\:42,6685\:43,3024\:44,12791\:45,12905\:46,557\:48,9075\:49,560\:50
thegauntlet.resourceSpike=false
actionprogress.notify-when-finished=true
BetterNpcHighlight.swTileRaveSpeed=6000
menuentryswapper.shopSell=SELL_50
grounditems.hiddenColor=-8355712
xpglobes.showActionsLeft=true
bankedexperience.limitToCurrentLevel=true
interacthighlight.objectInteractHighlightColor=-1862336512
actionprogress.crafting.battlestaves=true
screenmarkers.markers=[{"id"\:1720318034283,"name"\:"Marker 2","borderThickness"\:0,"color"\:"\#FF00FF00","fill"\:"\#0000FF00","visible"\:false,"labelled"\:false}]
objectindicators.region_10392=[{"id"\:17385,"name"\:"Ladder","regionId"\:10392,"regionX"\:2,"regionY"\:28,"z"\:0,"color"\:"\#FF0082D8","fillColor"\:"\#FF0082D8"}]
agility.lapsToLevel=true
animationSmoothing.smoothNpcAnimations=true
tobqol.getSotetsegProjectileTheme=INFERNO
grounditems.highlight_2485=-3663692
banktags.item_12899=cox,tob
logouttimer.idleTimeout=5
groundMarker.region_6710=[{"regionId"\:6710,"regionX"\:29,"regionY"\:55,"z"\:0,"color"\:"\#FFFF00FF"},{"regionId"\:6710,"regionX"\:30,"regionY"\:55,"z"\:0,"color"\:"\#FFFF00FF"},{"regionId"\:6710,"regionX"\:30,"regionY"\:56,"z"\:0,"color"\:"\#FFFF00FF"},{"regionId"\:6710,"regionX"\:29,"regionY"\:56,"z"\:0,"color"\:"\#FFFF00FF"},{"regionId"\:6710,"regionX"\:13,"regionY"\:56,"z"\:0,"color"\:"\#FF0000FF"},{"regionId"\:6710,"regionX"\:14,"regionY"\:56,"z"\:0,"color"\:"\#FF0000FF"},{"regionId"\:6710,"regionX"\:14,"regionY"\:55,"z"\:0,"color"\:"\#FF0000FF"},{"regionId"\:6710,"regionX"\:13,"regionY"\:55,"z"\:0,"color"\:"\#FF0000FF"}]
runelite.FishingOverlay_preferredLocation=1\:23
lowmemory.lowDetail=true
opponentinfo.hitpointsDisplayStyle=HITPOINTS
xpdrop.hideSkillIcons=false
objectindicators.region_7757=[{"id"\:9141,"name"\:"Gate","regionId"\:7757,"regionX"\:17,"regionY"\:41,"z"\:0,"color"\:"\#FF00FFFF","fillColor"\:"\#15FF00FF"},{"id"\:9100,"name"\:"Conveyor belt","regionId"\:7757,"regionX"\:23,"regionY"\:39,"z"\:0,"color"\:"\#FFAA00FF"},{"id"\:9092,"name"\:"Bar dispenser","regionId"\:7757,"regionX"\:21,"regionY"\:35,"z"\:0,"color"\:"\#FFFF0000","fillColor"\:"\#15FF00FF"},{"id"\:29330,"name"\:"Coffer","regionId"\:7757,"regionX"\:26,"regionY"\:29,"z"\:0,"color"\:"\#FF156AC2"},{"id"\:6150,"name"\:"Anvil","regionId"\:7757,"regionX"\:18,"regionY"\:43,"z"\:0,"color"\:"\#FF640202"}]
thegauntlet.resourceHullOutlineWidth=1
thegauntlet.minimapDemibossOverlay=true
brushMarkers.brushColor8=-16711936
randomevents.removeMenuOptions=true
brushMarkers.brushColor9=-16776961
herbiboar.colorTunnel=-16711936
nyloer.customRoleSwaps=attack,nylocas toxobolos*260*\nattack,nylocas toxobolos*162*\nattack,nylocas hagios*260*\nattack,nylocas hagios*162*\nattack,nylocas ischyros*260*\nattack,nylocas ischyros*162*
slayer.highlightOutline=false
coxtimers.showMuttadileTreeCutTime=true
menuentryswapper.npc_8693=-1
cannon.showDoubleHitSpot=false
banktaglayouts.layout_tob=24271\:0,6585\:1,10551\:2,21304\:3,13239\:4,22947\:5,22400\:7,6570\:8,13576\:9,12954\:10,22981\:11,11773\:12,11664\:16,8842\:17,12926\:18,13073\:19,12006\:20,23987\:21,173\:22,12631\:23,22109\:24,13072\:25,19547\:26,12899\:27,10588\:28,13441\:29,12701\:30,20724\:31,6685\:32,6685\:33,3024\:34,3024\:35,2444\:36,12625\:37,6685\:40,6685\:41,3024\:42,12695\:43,12695\:44,12791\:45,557\:48,9075\:49,560\:50
banktags.rememberTab=true
objectindicators.region_7770=[{"id"\:33417,"name"\:"Digsite Pendant","regionId"\:7770,"regionX"\:30,"regionY"\:0,"z"\:2,"color"\:"\#FFFF0000"},{"id"\:33415,"name"\:"Xeric\\u0027s Talisman","regionId"\:7770,"regionX"\:25,"regionY"\:0,"z"\:2,"color"\:"\#FF00FF00"},{"id"\:29155,"name"\:"Fancy Jewellery Box","regionId"\:7770,"regionX"\:14,"regionY"\:1,"z"\:1,"color"\:"\#FF003700","clickbox"\:true}]
runelite.InstanceMapOverlay_preferredLocation=347\:245
NyloerConfig.splitFontsType=ARIAL
music.muteOtherAreaNPCSounds=false
interfaceStyles.condensePlayerOptions=false
actionprogress.magic.tablets=true
banktags.item_1993=wintertodt
objectindicators.region_7769=[{"id"\:13523,"name"\:"Amulet of Glory","regionId"\:7769,"regionX"\:40,"regionY"\:54,"z"\:2,"color"\:"\#FFDD00FF"},{"id"\:13523,"name"\:"Amulet of Glory","regionId"\:7769,"regionX"\:40,"regionY"\:54,"z"\:1,"color"\:"\#FFDD00FF","hull"\:true}]
objectindicators.region_7768=[{"id"\:35965,"name"\:"Teleport Platform","regionId"\:7768,"regionX"\:61,"regionY"\:45,"z"\:1,"color"\:"\#FFCA0000"}]
loottracker.priceType=GRAND_EXCHANGE
runelite.sidebarToggleKey=122\:128
MahoganyHomes.showRequiredMaterials=true
gearswitchalert.allowTaggingUnequipables=false
grounditems.lootbeamStyle=MODERN
objectindicators.region_10806=[{"id"\:10832,"name"\:"Maple tree","regionId"\:10806,"regionX"\:43,"regionY"\:46,"z"\:0,"color"\:"\#FF00FFFF"},{"id"\:10832,"name"\:"Maple tree","regionId"\:10806,"regionX"\:45,"regionY"\:44,"z"\:0,"color"\:"\#FF00FFFF"}]
BetterNpcHighlight.tileRaveSpeed=6000
objectindicators.region_10804=[{"id"\:11365,"name"\:"Iron rocks","regionId"\:10804,"regionX"\:3,"regionY"\:1,"z"\:0,"color"\:"\#FFDD00FF"},{"id"\:11364,"name"\:"Iron rocks","regionId"\:10804,"regionX"\:5,"regionY"\:1,"z"\:0,"color"\:"\#FFDD00FF"},{"id"\:11364,"name"\:"Iron rocks","regionId"\:10804,"regionX"\:4,"regionY"\:0,"z"\:0,"color"\:"\#FFDD00FF"}]
runelite.roofremovalplugin=false
banktags.item_2434=bursting,wildy clue,spindel,artio,calvarion,revenant,hydra
xpTracker.onScreenDisplayModeBottom=XP_HOUR
banktags.item_12002=bursting,bandos solo melee,cox
npcindicators.tagstyle_520=hull
chatfilter.filterFriends=false
gpu.colorBlindMode=NONE
kourendLibrary.hideDarkManuscript=false
specialcounter.specDropMisses=false
poh.showGlory=true
motherlode.showRocks=true
banktags.item_25781=bursting,slayer
textrecolor.opaqueClanInfoHighlight=-65536
BetterNpcHighlight.outlineColor=-65281
implings.natureColor=-10712481
playerindicators.drawMinimapNames=true
banktags.item_11140=slayer
mta.graveyard=true
interfaceStyles.gameframe=AROUND_2010
randomevents.notifyForester=false
gpu.removeVertexSnapping=true
thegauntlet.hunllefFillColor=16777215
runelite.overlayBackgroundColor=-1673118414
itemidentification.showHerbSeeds=true
specialcounter.darklightThreshold=0
poison.changeHealthIcon=true
banktags.item_3749=revenant
xpTracker.xpPanelLabel2=XP_LEFT
xpTracker.xpPanelLabel3=XP_HOUR
zoom.rightClickObjects=true
xpTracker.xpPanelLabel4=ACTIONS_LEFT
poison.showInfoboxes=false
menuentryswapper.swapHelp=true
runelite.infoBoxVertical=false
xpTracker.xpPanelLabel1=XP_GAINED
clanchat.publicChatIcons=false
loottracker.showPriceType=false
banktags.icon_bursting=20724
defencetracker.disableIBColor=false
itemidentification.showHerbs=false
timers.showOverload=true
coxtimers.preciseTimers=RESPECT_INGAME_SETTING
screenshot.untradeableDrop=false
NyloerConfig.showNylocasSymbol=false
radiusmarkers.showWorldMap=true
kourendLibrary.hideButton=true
menuentryswapper.item_9780=2
fishing.showIcons=false
objectindicators.borderWidth=2.0
bankedexperience.cascadeBankedXp=true
agility.overlayColor=-16711936
worldhopper.favorite_533=true
menuentryswapper.swapAbyssTeleport=true
BetterNpcHighlight.clickboxNames=Knight of Ardougne
nyloer.splitFontsType=ARIAL
menuentryswapper.object_35965=1
corp.markDarkCore=true
opponentinfo.showOpponentHealthOverlay=true
maxhit.showSpec=true
colorpicker.recentColors=-3342592,-12525360,-32944,-8388652,-154,-6923152,-13172681,-16181,-13158401,-13158601,-15179990,-3663692,-9201230,-2127772,-16711781,-16743720
banktaglayouts.showLayoutPlaceholders=true
runelite.discordplugin=false
gearswitchalert.tagBox=true
inventorytags.tag_21793={"color"\:"\#FF0000FF"}
friendNotes.showIcons=true
worldhopper.favorite_528=true
objectindicators.region_12185=[{"id"\:11365,"name"\:"Iron rocks","regionId"\:12185,"regionX"\:24,"regionY"\:34,"z"\:0,"color"\:"\#FFDD00FF"},{"id"\:11365,"name"\:"Iron rocks","regionId"\:12185,"regionX"\:25,"regionY"\:33,"z"\:0,"color"\:"\#FFDD00FF"}]
regenmeter.showWhenNoChange=false
questhelper.highlightNeededMiniquestItems=true
music.mutePrayerSounds=false
playerindicators.clanMemberColor=-5635841
npcindicators.highlightTile=false
NyloerConfig.splitFontsSize=12
questhelper.filterListBy=SHOW_ALL
brushMarkers.brushdDoubleColors=false
BetterNpcHighlight.trueTileRaveSpeed=6000
deathIndicator.deathLocationPlane=0
itemCharge.showInfoboxes=false
banktaglayouts.preventVanillaPlaceholderMenuBug=true
woodcutting.showWoodcuttingStats=true
prayer.showPrayerBar=false
itemstat.colorBetterCapped=-1118669
loginscreen.username=milenko.milic@inacapmail.cl
nightmareZone.absorptionthreshold=50
banktaglayouts.autoLayoutIncludeRunePouchRunes=true
itemstat.relative=true
keyremapping.control=0\:128
nyloer.customHighlightRangeTiles=false
NyloerConfig.rangeNylocasOutlineColor=-16777216
playerindicators.ownNameColor=-16729900
questhelper.highlightStyleNpcs=OUTLINE
BetterNpcHighlight.presetInstructions=\#\#\# Preset Tag Format\:\n\n\!tag[style] [npc name]\:[preset \#]\n\!tag[style] [npc id]\:[preset \#]\n\!untag[style] [npc name]\:[preset \#]\n\!untag[style] [npc id]\:[preset \#]\n---------------------\n\#\#\# Example\:\n\n"\!tagswt cow\:2" -> This would add "cow" to the SW True Tile names list with preset color 2\n\# Tagging an NPC that already has a preset changes the preset to the new one\n\nUntagging is the same, regardless of preset\n
timers.showVengeanceActive=true
runelite.gpuplugin=false
runelite.infoBoxSize=35
banktags.item_12018=revenant,cox
itemCharge.showGuthixRestDoses=true
bank.bankPinKeyboard=true
interacthighlight.npcAttackHighlightColor=-1862336512
tobqol.xarpusSoundClipVolume=65
feed.includeBlogPosts=true
banktags.item_24478=slayer
BetterNpcHighlight.renderDistance=NONE
questhelper.showMiniMapArrow=true
kittenConfig.secondsAlive=8894
timetracking.timerNotification=false
runewatch.notifyWhenScreenshotTaken=true
groundMarker.region_12957=[{"regionId"\:12957,"regionX"\:16,"regionY"\:43,"z"\:0,"color"\:"\#FF0000FF"},{"regionId"\:12957,"regionX"\:15,"regionY"\:43,"z"\:0,"color"\:"\#FF0000FF"}]
banktags.item_9075=tob,cox
herbiboar.showStart=true
BetterNpcHighlight.outlineHighlight=true
worldhopper.favorite_527=true
linemarkers.defaultEdge=WEST
worldhopper.favorite_526=true
raids.whitelistedRooms=shamans, guardians, mystics
emote-clue-items.TrackBank=true
timers.showTeleblock=true
randomevents.notifyCerters=false
tobqol.nyloPillarHP=true
itemCharge.lowWarningColor=-256
MahoganyHomes.sessionTimeout=5
banktags.item_12006=bandos solo melee,tob
npcid.hideRandomEvents=false
raids.copyToClipboard=true
barrows.showBrotherLoc=true
interacthighlight.npcShowHover=true
banktags.item_2444=artio,revenant,cox,tob
boosts.displayIndicators=true
inventorytags.tag_21304={"color"\:"\#FFFF0000"}
npcid.showName=false
BetterNpcHighlight.ignoreDeadExclusion=
banktags.item_2448=spindel
brushMarkers.brushdrawOnworldmap=false
groundMarker.region_12601=[{"regionId"\:12601,"regionX"\:18,"regionY"\:41,"z"\:0,"color"\:"\#FF00FFFF"}]
inventorytags.tag_4868={"color"\:"\#FF0000FF"}
BetterNpcHighlight.trueTileNames=
nyloer.rangeRoleSwaps=attack,nylocas ischyros*260*\nattack,nylocas ischyros*162*\nattack,nylocas hagios*260*\nattack,nylocas hagios*162*\nattack,nylocas toxobolos*260*\nattack,nylocas toxobolos*162*
thegauntlet.dragonOutlineColor=-16776961
npcUnaggroArea.notifyExpire=false
objectindicators.highlightOutline=false
Shooting\ Stars\ Tracking.notifyType=BOTH
menuentryswapper.swapAssignment=true
inventorytags.tag_4874={"color"\:"\#FF0000FF"}
implings.dragonColor=-2992821
menuentryswapper.objectShiftClickWalkHere=false
menuentryswapper.npc_277=-1
gpu.unlockFps=true
zoom.cameraSpeed=1.0
tobqol.supplyChestMES=OFF
npcUnaggroArea.hideIfOutOfCombat=false
driftnet.tagAnnette=true
playerindicators.playerNamePosition=ABOVE_HEAD
groundMarker.region_12612=[{"regionId"\:12612,"regionX"\:34,"regionY"\:35,"z"\:1,"color"\:"\#FFFFFF00"},{"regionId"\:12612,"regionX"\:35,"regionY"\:32,"z"\:1,"color"\:"\#FFFFFF00"},{"regionId"\:12612,"regionX"\:33,"regionY"\:32,"z"\:1,"color"\:"\#FFFFFF00"},{"regionId"\:12612,"regionX"\:31,"regionY"\:34,"z"\:1,"color"\:"\#FFFFFF00"},{"regionId"\:12612,"regionX"\:31,"regionY"\:36,"z"\:1,"color"\:"\#FFFFFF00"},{"regionId"\:12612,"regionX"\:33,"regionY"\:38,"z"\:1,"color"\:"\#FFFFFF00"},{"regionId"\:12612,"regionX"\:35,"regionY"\:38,"z"\:1,"color"\:"\#FFFFFF00"},{"regionId"\:12612,"regionX"\:37,"regionY"\:36,"z"\:1,"color"\:"\#FFFFFF00"},{"regionId"\:12612,"regionX"\:37,"regionY"\:34,"z"\:1,"color"\:"\#FFFFFF00"},{"regionId"\:12612,"regionX"\:38,"regionY"\:30,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:39,"regionY"\:31,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:30,"regionY"\:30,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:29,"regionY"\:31,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:30,"regionY"\:40,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:38,"regionY"\:40,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:39,"regionY"\:39,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:39,"regionY"\:38,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:39,"regionY"\:37,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:39,"regionY"\:32,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:39,"regionY"\:33,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:37,"regionY"\:30,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:36,"regionY"\:30,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:31,"regionY"\:30,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:32,"regionY"\:30,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:29,"regionY"\:32,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:29,"regionY"\:33,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:30,"regionY"\:31,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:38,"regionY"\:31,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:38,"regionY"\:39,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:29,"regionY"\:38,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:29,"regionY"\:37,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:30,"regionY"\:39,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:31,"regionY"\:40,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:32,"regionY"\:40,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:37,"regionY"\:40,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:36,"regionY"\:40,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:35,"regionY"\:40,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:34,"regionY"\:40,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:33,"regionY"\:40,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:29,"regionY"\:36,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:29,"regionY"\:35,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:29,"regionY"\:34,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:33,"regionY"\:30,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:34,"regionY"\:30,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:35,"regionY"\:30,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:39,"regionY"\:35,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:39,"regionY"\:36,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:39,"regionY"\:34,"z"\:1,"color"\:"\#83686868"},{"regionId"\:12612,"regionX"\:29,"regionY"\:39,"z"\:1,"color"\:"\#83686868"}]
groundMarker.region_12613=[{"regionId"\:12613,"regionX"\:34,"regionY"\:29,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12613,"regionX"\:35,"regionY"\:29,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12613,"regionX"\:34,"regionY"\:28,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12613,"regionX"\:35,"regionY"\:28,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12613,"regionX"\:38,"regionY"\:20,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12613,"regionX"\:42,"regionY"\:20,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12613,"regionX"\:46,"regionY"\:20,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12613,"regionX"\:42,"regionY"\:41,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12613,"regionX"\:38,"regionY"\:41,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12613,"regionX"\:46,"regionY"\:41,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12613,"regionX"\:50,"regionY"\:20,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12613,"regionX"\:50,"regionY"\:41,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12613,"regionX"\:50,"regionY"\:22,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12613,"regionX"\:50,"regionY"\:39,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12613,"regionX"\:41,"regionY"\:29,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12613,"regionX"\:41,"regionY"\:30,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12613,"regionX"\:41,"regionY"\:31,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12613,"regionX"\:41,"regionY"\:32,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12613,"regionX"\:50,"regionY"\:16,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12613,"regionX"\:50,"regionY"\:15,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12613,"regionX"\:50,"regionY"\:14,"z"\:0,"color"\:"\#83686868"}]
groundMarker.region_12611=[{"regionId"\:12611,"regionX"\:26,"regionY"\:30,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:26,"regionY"\:29,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:38,"regionY"\:30,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:38,"regionY"\:29,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:40,"regionY"\:25,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:24,"regionY"\:25,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:40,"regionY"\:22,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:24,"regionY"\:22,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:25,"regionY"\:28,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:39,"regionY"\:28,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:29,"regionY"\:26,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:29,"regionY"\:27,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:29,"regionY"\:25,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:29,"regionY"\:24,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:30,"regionY"\:23,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:31,"regionY"\:23,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:32,"regionY"\:23,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:33,"regionY"\:23,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:34,"regionY"\:23,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:35,"regionY"\:24,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:35,"regionY"\:25,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:35,"regionY"\:26,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:35,"regionY"\:27,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:35,"regionY"\:28,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:34,"regionY"\:29,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:33,"regionY"\:29,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:32,"regionY"\:29,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:31,"regionY"\:29,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:30,"regionY"\:29,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:29,"regionY"\:28,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:40,"regionY"\:18,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:38,"regionY"\:17,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:26,"regionY"\:17,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:24,"regionY"\:18,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:32,"regionY"\:20,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:36,"regionY"\:24,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:28,"regionY"\:24,"z"\:0,"color"\:"\#83686868"},{"regionId"\:12611,"regionX"\:32,"regionY"\:28,"z"\:0,"color"\:"\#83686868"}]
bankxpvalue.includeSeedVault=true
bankedexperience.grabFromSeedVault=true
itemCharge.expeditiousNotification=true
loottracker.showRaidsLootValue=true
agility.lapTimeout=5
grounditems.highlightTiles=true
menuentryswapper.npc_3101=2
worldmap.dungeonTooltips=true
npcindicators.highlightcolor_5730=-16711681
menuentryswapper.npc_3108=2
kittenConfig.secondsHungry=81
regenmeter.notifyBeforeHpRegenDuration=0
inventorygrid.showItem=true
NyloerConfig.mageNylocasSymbol=H
timers.showHomeMinigameTeleports=true
keyremapping.f9=57\:0
keyremapping.f8=56\:0
banktags.item_3105=wildy clue,spindel,artio,calvarion
reportButton.switchTimeFormat=TIME_12H
keyremapping.f5=53\:0
menuentryswapper.swapFairyRing=LAST_DESTINATION
keyremapping.f4=52\:0
keyremapping.f7=55\:0
banktags.item_13393=herbrun,cox
runelite.chathistoryplugin=false
keyremapping.f6=54\:0
npcindicators.highlightcolor_3101=-65411
runenergy.replaceOrbText=false
loottracker.pvpKillChatMessage=false
mousehighlight.disableSpellbooktooltip=false
dpscounter.autoreset=false
chatfilter.maxRepeatedPublicChats=0
wintertodt.notifyFullInv=true
thegauntlet.timerOverlay=false
zoom.controlFunction=NONE
xpdrop.magePrayerColor=-15368019
blastmine.showWarningOverlay=true
wiki.showWikiMinimapButton=true
implings.shownature=NONE
idlenotifier.logoutidle=true
actionprogress.tempoross.cooking=true
tobqol.nyloLowDetail=true
banktags.item_5341=herbrun
npcindicators.showRespawnTimer=false
xpglobes.showTimeTilGoal=true
BetterNpcHighlight.trueTileFillColor=335609855
itemCharge.veryLowWarning=1
banktags.icon_calvarion=13179
tobqol.nyloRoleSelectedRange=false
zoom.preserveYaw=false
hiscore.playerOption=true
NyloerConfig.splitPrefix=s
inventorygrid.showGrid=true
thegauntlet.fishingSpotOutlineColor=-16711681
banktags.item_5343=herbrun
herblorerecipes.modifierKeybind=0\:0
npcindicators.npcColor=-16711681
itemidentification.showTablets=false
clanchat.clanChatShowOnlineMemberCount=false
itemidentification.showSpecialSeeds=false
driftnet.timeoutDelay=60
actionprogress.wintertodt.burning=true
discord.actionTimeout=5
itemCharge.showRingOfForgingCount=true
woodcutting.forestryPoachersNotification=true
barbarianAssault.showTimer=true
specialcounter.bandosGodswordThreshold=0
banktags.item_21816=revenant
herblorerecipes.showTooltipOnSecondaries=true
BetterNpcHighlight.swTileAA=true
worldmap.transportationTooltips=true
screenshot.boss=false
banktags.item_21817=revenant
banktags.item_8842=tob
gpu.antiAliasingMode=DISABLED
dailytaskindicators.showSand=false
specialcounter.thresholdNotification=false
implings.showessence=NONE
BetterNpcHighlight.turboNames=
partypanel.displayVirtualLevels=true
BetterNpcHighlight.tileLines=REG
runewatch.playerOption=true
itemstat.theoretical=false
prayer.prayerIndicator=false
npcid.hidePets=false
banktags.item_3144=wildy clue,spindel,artio,calvarion,revenant,hydra
runelite.XpInfoBoxOverlayFletching_preferredPosition=BOTTOM_RIGHT
NyloerConfig.meleeNylocasOutlineColor=-16777216
gpu.drawDistance=70
leftclickdrop.itemList=Raw salmon, Raw trout,Burnt fish, Clue scroll (beginner), Soda ash, Bucket of sand, Iron ore, Willow longbow (u), Maple longbow (u),Maple Logs, Uncut sapphire, Uncut, emerald, Uncut ruby, Uncut diamond, Oak shortbow (u), Cooking apple, Strawberry, Jangerberries, Banana, Pineapple, Lime, Redberries, Strange fruit, Lemon, Golovanova fruit top,Trout,Salmon
combatlevel.showPreciseCombatLevel=true
fishing.aerialOverlayColor=-16711936
banktags.item_5325=herbrun
teamCapes.clanChatMemberCounter=false
itemidentification.textColor=-16711936
woodcutting.statTimeout=5
grounditems.highlightedColor=-5635841
groundMarker.region_11347=[{"regionId"\:11347,"regionX"\:56,"regionY"\:40,"z"\:2,"color"\:"\#FF0000FF"}]
runelite.usernameInTitle=true
runelite.pinnedPlugins=Action Progress,Custom Left Click Drop,Entity Hider,GPU,Ground Items,Ground Markers,Inventory Tags,Inventory Viewer,Line Markers,Menu Entry Swapper,NPC Aggression Timer,NPC Indicators,Object Markers,RuneLite,Tile Indicators
chatnotification.notifyOnTrade=false
timetracking.farmingContractInfoBox=true
prayer.replaceOrbText=false
poh.showExitPortal=true
runelite.skyboxplugin=true
implings.showeclectic=HIGHLIGHT
deathIndicator.deathOnWorldMap=true
itemidentification.showSacks=false
fishing.showMinnowOverlay=true
menuentryswapper.leftClickCustomization=true
menuentryswapper.swapTravel=true
clanchat.clanChatIcons=true
inventorygrid.gridColor=771751935
banktags.item_806=bursting,spindel
worldmap.lunarSpellbookIcon=true
npcUnaggroArea.npcUnaggroShowTimer=true
bankedexperience.showSecondaries=false
banktags.item_12911=cox
worldmap.agilityCourseRooftopIcon=true
BetterNpcHighlight.tileWidth=2.0
itemidentification.showTreeSeeds=false
inventorytags.tagFill=false
thegauntlet.hunllefTileOutline=false
actionprogress.smithing.smelting=true
xpupdater.wiseoldman=false
worldmap.rareTreeTooltips=true
runewatch.uploadTradeScreenshot=NEITHER
thegauntlet.minimapResourceOverlay=true
BetterNpcHighlight.hullFillColor=335609855
objectindicators.region_11571=[{"id"\:14886,"name"\:"Bank chest","regionId"\:11571,"regionX"\:56,"regionY"\:16,"z"\:0,"color"\:"\#FFFF00FF"}]
itemidentification.showHopSeeds=false
actionprogress.cooking.top-pizza=true
itemCharge.showFungicideCharges=true
xpglobes.Progress\ arc\ color=-14336
banktags.item_12905=hydra,cox
nyloer.fontsBold=true
averagetime.Display\ Kill\ Duration=true
banktags.item_19544=bursting,bandos solo melee,cox
banktags.item_19547=cox,tob
poh.showMagicTravel=true
nyloer.mageNylocasSymbol=H
discord.showCityActivity=true
implings.essenceColor=-14657190
actionprogress.wintertodt.woodcutting=true
timers.showArceuusCooldown=false
itemidentification.showBars=false
banktags.item_861=revenant
emote-clue-items.ShowNavigation=true
xpglobes.hideMaxed=false
thegauntlet.grymRootFillColor=855637760
tobqol.maidenCrabProcDisplay=false
thegauntlet.strongNpcOutlineColor=-14336
banktaglayouts.autoLayoutDuplicateLimit=4
BetterNpcHighlight.respawnTimer=OFF
xpupdater.cml=false
zoom.ctrlZoomValue=512
emote-clue-items.AutoSyncWatsonBoard=false
runecraft.showClickBox=true
inventoryViewer.hideIfInventoryActive=false
tobqol.displayNyloRoleSelector=false
timers.showSilkDressing=true
thegauntlet.bearOutlineColor=-65536
tobqol.lightUp=true
kittenConfig.kittenNotifications=true
itemstat.geStats=true
NyloerConfig.splitFontsBold=true
nyloer.customRoleShiftSwaps=/walk here,*\n/attack,nylocas hagios*162*
itemstat.equipmentStats=true
screenshot.levels=true
mta.enchantment=true
tobqol.nyloWavesRecolorBigsMenuDarker=false
nightmareZone.overloadnotification=true
inventorytags.tag_13576={"color"\:"\#FFFF0000"}
actionprogress.ignore-single-actions=true
BetterNpcHighlight.tagInstructions=\#\#\# Format\:\n\n\!tag[style] [npc name]\n\!tag[style] [npc id]\n\!untag[style] [npc name]\n\!untag[style] [npc id]\n---------------------\n\#\#\# Example\:\n\n"\!tagswt cow" -> This would add "cow" to the SW True Tile names list\n\n"\!untago 1234" -> This would remove "1234" from the Outline IDs list\n
runelite.notificationFlashColor=1191116800
BetterNpcHighlight.swTileWidth=2.0
actionprogress.misc.grinding=true
inventorytags.tag_8842={"color"\:"\#FFE7FF00"}
runelite.nyloerplugin=false
gearswitchalert.gear_tag_10370={"isMeleeGear"\:false,"isRangeGear"\:true,"isMagicGear"\:false}
actionprogress.guardianOfTheRift.reward-pool=true
banktags.item_6685=bandos solo melee,spindel,artio,calvarion,revenant,cox,tob
herbiboar.colorTrail=-1
screenshot.wildernessLootChest=true
NyloerConfig.mageNylocasOutlineColor=-16777216
averagetime.Loot\ Display=SESSION
raids.ccDisplay=false
thegauntlet.resourceRemoveAcquired=true
tearsofguthix.showGreenTearsTimer=true
banktags.item_12954=bandos solo melee,wildy clue,spindel,calvarion,cox,hydra,tob,slayer
groundMarker.region_6454=[{"regionId"\:6454,"regionX"\:25,"regionY"\:44,"z"\:0,"color"\:"\#FF214263"},{"regionId"\:6454,"regionX"\:25,"regionY"\:45,"z"\:0,"color"\:"\#FF214263"},{"regionId"\:6454,"regionX"\:26,"regionY"\:45,"z"\:0,"color"\:"\#FF214263"},{"regionId"\:6454,"regionX"\:26,"regionY"\:44,"z"\:0,"color"\:"\#FF214263"}]
party.statusOverlayRenderSelf=true
runewatch.playerTextColor=-45824
runecraft.showEarth=true
tobqol.nyloHideObjects=OFF
thegauntlet.tornadoTileOutline=ON
npcid.showIndex=false
woodcutting.highlightRitualCircle=true
statusbars.enableSkillIcon=true
entityhider.hideAttackers=false
BetterNpcHighlight.hullHighlight=false
banktags.item_9787=wintertodt
roofremoval.removeDestination=true
textrecolor.opaqueClanChatMessageHighlight=-16777216
objectindicators.region_12853=[{"id"\:10583,"name"\:"Bank booth","regionId"\:12853,"regionX"\:53,"regionY"\:27,"z"\:0,"color"\:"\#FF0000FF"}]
actionprogress.misc.collect-sand=true
groundMarker.region_13109=[{"regionId"\:13109,"regionX"\:20,"regionY"\:43,"z"\:0,"color"\:"\#FF6464FF"},{"regionId"\:13109,"regionX"\:21,"regionY"\:43,"z"\:0,"color"\:"\#FF6464FF"},{"regionId"\:13109,"regionX"\:21,"regionY"\:42,"z"\:0,"color"\:"\#FF6464FF"},{"regionId"\:13109,"regionX"\:20,"regionY"\:42,"z"\:0,"color"\:"\#FF6464FF"}]
opponentinfo.lookupOnInteraction=false
objectindicators.region_9778=[{"id"\:8986,"name"\:"Net trap","regionId"\:9778,"regionX"\:15,"regionY"\:26,"z"\:0,"color"\:"\#FF0000FF"},{"id"\:8990,"name"\:"Young tree","regionId"\:9778,"regionX"\:17,"regionY"\:28,"z"\:0,"color"\:"\#FF0000FF"},{"id"\:8986,"name"\:"Net trap","regionId"\:9778,"regionX"\:19,"regionY"\:25,"z"\:0,"color"\:"\#FF0000FF"},{"id"\:8986,"name"\:"Net trap","regionId"\:9778,"regionX"\:21,"regionY"\:20,"z"\:0,"color"\:"\#FF0000FF"}]
groundMarker.region_13106=[{"regionId"\:13106,"regionX"\:47,"regionY"\:53,"z"\:0,"color"\:"\#FFFF0000"},{"regionId"\:13106,"regionX"\:47,"regionY"\:52,"z"\:0,"color"\:"\#FFFF0000"},{"regionId"\:13106,"regionX"\:48,"regionY"\:52,"z"\:0,"color"\:"\#FFFF0000"},{"regionId"\:13106,"regionX"\:47,"regionY"\:51,"z"\:0,"color"\:"\#FFFF0000"},{"regionId"\:13106,"regionX"\:46,"regionY"\:52,"z"\:0,"color"\:"\#FFFF0000"}]
woodcutting.highlightFoxTrap=true
actionprogress.crafting.waeving=true
grounditems.onlyShowLoot=true
inventorytags.tag_24271={"color"\:"\#FFFF0000"}
loginscreen.showLoginFire=true
groundMarker.region_7768=[{"regionId"\:7768,"regionX"\:59,"regionY"\:55,"z"\:1,"color"\:"\#FF214263"},{"regionId"\:7768,"regionX"\:59,"regionY"\:56,"z"\:1,"color"\:"\#FF214263"},{"regionId"\:7768,"regionX"\:56,"regionY"\:52,"z"\:1,"color"\:"\#FF214263"},{"regionId"\:7768,"regionX"\:55,"regionY"\:52,"z"\:1,"color"\:"\#FF214263"},{"regionId"\:7768,"regionX"\:52,"regionY"\:55,"z"\:1,"color"\:"\#FF214263"},{"regionId"\:7768,"regionX"\:52,"regionY"\:56,"z"\:1,"color"\:"\#FF214263"},{"regionId"\:7768,"regionX"\:55,"regionY"\:59,"z"\:1,"color"\:"\#FF214263"},{"regionId"\:7768,"regionX"\:56,"regionY"\:59,"z"\:1,"color"\:"\#FF214263"}]
zoom.inner=false
averagetime.Infobox=true
dailytaskindicators.showFlax=false
prayer.showPrayerTooltip=true
chatnotification.notifyOnBroadcast=false
menuentryswapper.swapExchange=true
screenshot.copyToClipboard=false
nyloer.rangeNylocasColor=-16711936
thegauntlet.demibossOutlineWidth=1
thegauntlet.resourceFrame=2
banktags.item_9763=bursting
averagetime.Kills\ This\ Session=true
worldhopper.previousKey=37\:192
BetterNpcHighlight.trueTileRave=false
specialcounter.elderMaulThreshold=0
deathIndicator.deathInfoBox=true
menuentryswapper.swapKaramjaGloves=WEAR
feed.includeOsrsNews=true
worldhopper.nextKey=39\:192
motherlode.showDepositsLeft=true
grounditems.priceDisplayMode=OFF
groundMarker.region_13110=[{"regionId"\:13110,"regionX"\:31,"regionY"\:10,"z"\:0,"color"\:"\#FF9B9BFF"},{"regionId"\:13110,"regionX"\:32,"regionY"\:10,"z"\:0,"color"\:"\#FF9B9BFF"},{"regionId"\:13110,"regionX"\:31,"regionY"\:9,"z"\:0,"color"\:"\#FF9B9BFF"},{"regionId"\:13110,"regionX"\:32,"regionY"\:9,"z"\:0,"color"\:"\#FF9B9BFF"}]
tobqol.sotetsegInstanceTimer=OFF
BetterNpcHighlight.slayerHighlight=false
thegauntlet.oreDepositOutlineColor=-65536
groundMarker.region_7757=[{"regionId"\:7757,"regionX"\:16,"regionY"\:39,"z"\:0,"color"\:"\#FF003700"}]
inventorytags.showTagOutline=true
clanchat.showIgnores=true
menuentryswapper.swapRadasBlessing=EQUIP
zoom.rightClickExamine=false
runelite.WintertodtOverlay_preferredPosition=TOP_RIGHT
bankxpvalue.tutorial=true
menuentryswapper.swapGEAbort=false
nyloer.showNylocasWave=false
banktags.item_12926=cox,tob
npcindicators.outlineFeather=0
runelite.banktagsplugin=true
runelite.minimapplugin=true
implings.showCrystal=NONE
wintertodt.notifyBrazierDamage=INTERRUPT
banktags.item_892=revenant
banktags.item_19564=spindel,artio,calvarion,revenant
coxtimers.showIcePopTime=true
tithefarmplugin.hexColorUnwatered=-17664
groundMarker.region_13125=[{"regionId"\:13125,"regionX"\:21,"regionY"\:32,"z"\:0,"color"\:"\#83686868"},{"regionId"\:13125,"regionX"\:21,"regionY"\:31,"z"\:0,"color"\:"\#83686868"},{"regionId"\:13125,"regionX"\:20,"regionY"\:32,"z"\:0,"color"\:"\#83686868"},{"regionId"\:13125,"regionX"\:20,"regionY"\:31,"z"\:0,"color"\:"\#83686868"},{"regionId"\:13125,"regionX"\:19,"regionY"\:31,"z"\:0,"color"\:"\#83686868"},{"regionId"\:13125,"regionX"\:19,"regionY"\:32,"z"\:0,"color"\:"\#83686868"},{"regionId"\:13125,"regionX"\:18,"regionY"\:31,"z"\:0,"color"\:"\#83686868"},{"regionId"\:13125,"regionX"\:18,"regionY"\:32,"z"\:0,"color"\:"\#83686868"},{"regionId"\:13125,"regionX"\:16,"regionY"\:32,"z"\:0,"color"\:"\#83686868"},{"regionId"\:13125,"regionX"\:16,"regionY"\:31,"z"\:0,"color"\:"\#83686868"},{"regionId"\:13125,"regionX"\:17,"regionY"\:31,"z"\:0,"color"\:"\#83686868"},{"regionId"\:13125,"regionX"\:17,"regionY"\:30,"z"\:0,"color"\:"\#83686868"},{"regionId"\:13125,"regionX"\:17,"regionY"\:32,"z"\:0,"color"\:"\#83686868"},{"regionId"\:13125,"regionX"\:17,"regionY"\:33,"z"\:0,"color"\:"\#83686868"},{"regionId"\:13125,"regionX"\:18,"regionY"\:30,"z"\:0,"color"\:"\#83686868"},{"regionId"\:13125,"regionX"\:18,"regionY"\:29,"z"\:0,"color"\:"\#83686868"},{"regionId"\:13125,"regionX"\:18,"regionY"\:33,"z"\:0,"color"\:"\#83686868"},{"regionId"\:13125,"regionX"\:18,"regionY"\:34,"z"\:0,"color"\:"\#83686868"}]
banktags.removeTabSeparators=false
defaultworld.defaultWorld=487
randomevents.notifyArnav=false
groundMarker.region_13123=[{"regionId"\:13123,"regionX"\:17,"regionY"\:37,"z"\:0,"color"\:"\#FFFFFF00"},{"regionId"\:13123,"regionX"\:18,"regionY"\:42,"z"\:0,"color"\:"\#FFFFFF00"},{"regionId"\:13123,"regionX"\:12,"regionY"\:38,"z"\:0,"color"\:"\#FF0000FF"},{"regionId"\:13123,"regionX"\:13,"regionY"\:43,"z"\:0,"color"\:"\#FF0000FF"},{"regionId"\:13123,"regionX"\:15,"regionY"\:37,"z"\:0,"color"\:"\#FFFF0000"},{"regionId"\:13123,"regionX"\:11,"regionY"\:24,"z"\:0,"color"\:"\#FF686868"},{"regionId"\:13123,"regionX"\:14,"regionY"\:24,"z"\:0,"color"\:"\#FF686868"},{"regionId"\:13123,"regionX"\:17,"regionY"\:24,"z"\:0,"color"\:"\#FF686868"},{"regionId"\:13123,"regionX"\:20,"regionY"\:24,"z"\:0,"color"\:"\#FF686868"},{"regionId"\:13123,"regionX"\:20,"regionY"\:27,"z"\:0,"color"\:"\#FF686868"},{"regionId"\:13123,"regionX"\:17,"regionY"\:27,"z"\:0,"color"\:"\#FF686868"},{"regionId"\:13123,"regionX"\:14,"regionY"\:27,"z"\:0,"color"\:"\#FF686868"},{"regionId"\:13123,"regionX"\:11,"regionY"\:27,"z"\:0,"color"\:"\#FF686868"},{"regionId"\:13123,"regionX"\:11,"regionY"\:31,"z"\:0,"color"\:"\#FF686868"},{"regionId"\:13123,"regionX"\:14,"regionY"\:31,"z"\:0,"color"\:"\#FF686868"},{"regionId"\:13123,"regionX"\:17,"regionY"\:31,"z"\:0,"color"\:"\#FF686868"},{"regionId"\:13123,"regionX"\:20,"regionY"\:34,"z"\:0,"color"\:"\#FF686868"},{"regionId"\:13123,"regionX"\:17,"regionY"\:34,"z"\:0,"color"\:"\#FF686868"},{"regionId"\:13123,"regionX"\:14,"regionY"\:34,"z"\:0,"color"\:"\#FF686868"},{"regionId"\:13123,"regionX"\:11,"regionY"\:34,"z"\:0,"color"\:"\#FF686868"},{"regionId"\:13123,"regionX"\:20,"regionY"\:31,"z"\:0,"color"\:"\#FF686868"}]
BetterNpcHighlight.taskHighlightStyle=[]
averagetime.Average\ Kill\ Time=true
textrecolor.transparentClanChatInfoHighlight=-65536
BetterNpcHighlight.entityHiderToggle=false
questhelper.highlightStyleInventoryItems=FILLED_OUTLINE
actionprogress.tempoross.reward-pool=true
slayer.highlightHull=false
blastmine.showOreOverlay=true
banktags.item_8013=bursting,bandos solo melee,wildy clue
herblorerecipes.showSecondaryIngredientsInTooltip=true
poh.showBurner=true
banktags.item_11664=tob
questhelper.passColour=-16711936
thegauntlet.resourcePaddlefish=20
banktaglayouts.layout_wildy\ clue=10828\:0,1712\:1,2503\:2,2497\:3,3105\:4,22947\:5,8013\:7,13123\:8,4587\:9,12954\:10,7462\:11,13128\:12,13110\:16,12625\:17,3546\:18,13441\:19,3144\:20,3144\:21,3144\:22,3144\:23,12695\:24,2434\:25,952\:26,3144\:27,13441\:28,13441\:29,13441\:30,13441\:31,3144\:32,3144\:33,3144\:34,3144\:35,3144\:36,13441\:37,13441\:40,13441\:41,13441\:42,13441\:43,13441\:44,21166\:45
idlenotifier.oxygenNotification={"enabled"\:false,"initialized"\:false,"override"\:false,"tray"\:false,"volume"\:0,"timeout"\:0,"gameMessage"\:false,"sendWhenFocused"\:false}
playerindicators.friendNameColor=-16725933
brushMarkers.brushreplaceMode=false
interacthighlight.objectShowInteract=true
runewatch.notificationCooldown=60
dailytaskindicators.showArrows=false
BetterNpcHighlight.areaRaveSpeed=6000
actionprogress.smithing.smithing=true
vanguards.meleeColor=-65536
timetracking.preferSoonest=false
runelite.guideplugin=false
optimal-quest-guide.showCompletedQuests=false
agility.showLapCount=true
zoom.zoomIncrement=25
deathIndicator.deathLocationX=3215
nyloer.meleeRoleSwaps=attack,nylocas hagios*269*\nattack,nylocas hagios*162*\nattack,nylocas toxobolos*260*\nattack,nylocas toxobolos*162*\nattack,nylocas ischyros*260*\nattack,nylocas ischyros*162*
deathIndicator.deathLocationY=10091
itemCharge.lowWarning=2
averagetime.KPH\ Calc\ Method=PRECISE
customitemhovers.enableTutorialMessage=true
BetterNpcHighlight.tagCommands=true
nyloer.tileHighlightWidth=2.0
runelite.XpInfoBoxOverlayCooking_preferredLocation=4\:289
itemidentification.showLogs=false
runelite.agilityplugin=true
nyloer.mageHighlightMeleeTiles=false
chatcommands.sw=true
fishing.minnowsOverlayColor=-65536
tobqol.maidenLeaks=false
menuentryswapper.object_29780=1
runelite.gearswitchalertplugin=false
motherlode.showSack=true
questhelper.highlightNeededAchievementDiaryItems=true
menuentryswapper.object_29779=1
groundMarker.region_5536=[{"regionId"\:5536,"regionX"\:25,"regionY"\:38,"z"\:0,"color"\:"\#FF214263"},{"regionId"\:5536,"regionX"\:28,"regionY"\:38,"z"\:0,"color"\:"\#FF214263"},{"regionId"\:5536,"regionX"\:14,"regionY"\:38,"z"\:0,"color"\:"\#FF214263"},{"regionId"\:5536,"regionX"\:12,"regionY"\:33,"z"\:0,"color"\:"\#FF214263"},{"regionId"\:5536,"regionX"\:12,"regionY"\:29,"z"\:0,"color"\:"\#FF214263"},{"regionId"\:5536,"regionX"\:20,"regionY"\:31,"z"\:0,"color"\:"\#FF214263"},{"regionId"\:5536,"regionX"\:19,"regionY"\:30,"z"\:0,"color"\:"\#FF214263"},{"regionId"\:5536,"regionX"\:33,"regionY"\:22,"z"\:0,"color"\:"\#FF00C800"},{"regionId"\:5536,"regionX"\:15,"regionY"\:33,"z"\:0,"color"\:"\#FF214263"}]
groundMarker.region_12181=[{"regionId"\:12181,"regionX"\:49,"regionY"\:23,"z"\:0,"color"\:"\#FFFFFF00"}]
maxhit.spellChoice=ICE_BARRAGE
worldmap.agilityCourseTooltips=true
raids.enableRotationWhitelist=false
keyremapping.up=87\:0
nyloer.rangeHighlightRangeTiles=false
coxscouterexternal.hideMissingHighlighted=false
menuentryswapper.object_29770=1
gearswitchalert.defaultColourMagic=-16776961
gpu.useComputeShaders=true
attackIndicator.showChatWarnings=true
specialcounter.arclightThreshold=0
itemprices.showWhileAlching=true
wintertodt.roundNotification=5
regenmeter.showHitpoints=true
brushMarkers.brushSize=ONE
menuentryswapper.swapPortalNexus=true
menuentryswapper.swapPrivate=false
textrecolor.transparentPrivateMessageSentHighlight=-1
runecraft.showMind=true
grounditems.showLootbeamTier=MEDIUM
questhelper.highlightStyleGroundItems=OUTLINE
banktags.position=0
nyloer.meleeHighlightRangeTiles=false
menuentryswapper.item_702=-1
itemidentification.showFlowerSeeds=false
objectindicators.region_10292=[{"id"\:16685,"name"\:"Ladder","regionId"\:10292,"regionX"\:0,"regionY"\:28,"z"\:1,"color"\:"\#FF0082D8","fillColor"\:"\#FF0082D8"},{"id"\:11723,"name"\:"Door","regionId"\:10292,"regionX"\:5,"regionY"\:28,"z"\:0,"color"\:"\#FF00FF00"}]
averagetime.Kph\ In\ Chat\ Box=false
xpTracker.intermediateLevelMarkers=false
objectindicators.region_10293=[{"id"\:10529,"name"\:"Bank Deposit Box","regionId"\:10293,"regionX"\:28,"regionY"\:24,"z"\:0,"color"\:"\#FFFF00FF"}]
driftnet.countColor=-1
randomevents.notifyCountCheck=false
stretchedmode.scalingFactor=50
interacthighlight.npcHoverHighlightColor=-1862271232
runelite.infoBoxTextOutline=false
coxscouterexternal.hideMissingLayout=false
agility.agilityArenaNotifier=true
BetterNpcHighlight.areaColor=-65281
runelite.externalPlugins=zom-leftclick-dropper,herblorerecipes,shooting-stars-tracking,fight-cave-waves,line-markers,mahogany-homes,npc-id,party-panel,party-defence-tracker,lance-enhance,kitten-tracker,quest-helper,maxhitplugin,tobqol,action-progress,bank-tag-layouts,the-gauntlet,wintertodt-notifications,life-saver,optimal-quest-guide,better-npc-highlight,banked-experience,nyloer,rogues-den,deathindicator,profit-calculator,runewatch,kph-tracker,emote-clue-items,bank-xp-value,radius-markers
npcindicators.npcToHighlight=Rod fishing spot,Trader Crewmember,Captain Bentley,Hellhound,Bat,Pestilent Bloat,Pyramid block,Xarpus,Ordan,Wizard Akutha,Sawmill operator,Tekton,Ice demon,The Maiden of Sugadinti,Alchemical Hydra,Master Farmer,Abyssal leech,Chaos druid
itemCharge.showAbyssalBraceletCharges=true
barrows.showPuzzleAnswer=true
radiusmarkers.includeMaxRange=false
banktags.item_23203=artio
raids.raidsTimer=true
puzzlesolver.displaySolution=true
groundMarker.borderWidth=2.0
radiusmarkers.defaultColourInteraction=-16726016
questhelper.highlightNeededQuestItems=true
averagetime.Overlay=false
BetterNpcHighlight.tileColor=-16711681
deathIndicator.deathWorld=353
banktags.item_10372=cox
banktags.item_10374=artio
npcid.stripTags=true
banktags.item_10370=bandos solo melee,cox
fpscontrol.limitFps=false
keyremapping.space=32\:0
BetterNpcHighlight.presetColor5=-16738616
zoom.relaxCameraPitch=true
prayer.prayerFlickLocation=NONE
grounditems.doubleTapDelay=250
emote-clue-items.HighlightInventory=true
BetterNpcHighlight.presetColor2=-14301873
BetterNpcHighlight.presetColor1=-2081743
tobqol.verzikMarkedTornadoColor=-2655647
BetterNpcHighlight.presetColor4=-14221399
BetterNpcHighlight.presetColor3=-3175683
menuentryswapper.item_28136=1
implings.luckyColor=-10090651
itemCharge.showPotionDoseCount=false
runecraft.showBlood=true
runelite.profitcalcplugin=false
maxhit.inventorySelectiveSpecial=false
tobqol.sotetsegSoundClip=true
timers.showMagicImbue=true
playerindicators.highlightTeamMembers=ENABLED
radiusmarkers.defaultColourSpawn=-16711681
thegauntlet.resourceBark=9
deathIndicator.deathHintArrow=true
inventorytags.tag_22109={"color"\:"\#FF00FF00"}
tobqol.fontStyle=PLAIN
tobqol.nyloWavesRecolorMenu=false
clanchat.joinLeaveRank=UNRANKED
poh.showDigsitePendant=true
herbiboar.showTunnel=true
menuentryswapper.swapTeleToPoh=false
tileindicators.highlightHoveredColor=0
menuentryswapper.object_36084=1
itemidentification.showPotions=false
grandexchange.notifyOnOfferComplete=false
runelite.dpscounterplugin=false
emote-clue-items.HighlightMedium=true
nyloer.mageNylocasColor=-16711681
groundMarker.region_6813=[{"regionId"\:6813,"regionX"\:12,"regionY"\:42,"z"\:0,"color"\:"\#FFFFFF00"},{"regionId"\:6813,"regionX"\:12,"regionY"\:44,"z"\:0,"color"\:"\#FFFFFF00"},{"regionId"\:6813,"regionX"\:9,"regionY"\:42,"z"\:0,"color"\:"\#FFFFFF00"},{"regionId"\:6813,"regionX"\:9,"regionY"\:44,"z"\:0,"color"\:"\#FFFFFF00"}]
agility.trapHighlight=-65536
groundMarker.region_6812=[{"regionId"\:6812,"regionX"\:2,"regionY"\:9,"z"\:0,"color"\:"\#FFFFFF00"},{"regionId"\:6812,"regionX"\:1,"regionY"\:8,"z"\:0,"color"\:"\#FFFFFF00"},{"regionId"\:6812,"regionX"\:53,"regionY"\:30,"z"\:0,"color"\:"\#FFFF0000"},{"regionId"\:6812,"regionX"\:52,"regionY"\:29,"z"\:0,"color"\:"\#FFFF0000"}]
implings.ninjaColor=-12106165
clanchat.guestClanChatShowOnlineMemberCount=false
poh.showPortalNexus=true
xpupdater.templeosrs=false
Shooting\ Stars\ Tracking.displayAsTime=true
timers.showPrayerEnhance=true
runelite.notificationSound=NATIVE
menuentryswapper.npc_8337=-1
groundMarker.region_10806=[{"regionId"\:10806,"regionX"\:34,"regionY"\:13,"z"\:0,"color"\:"\#FF0000FF"},{"regionId"\:10806,"regionX"\:40,"regionY"\:25,"z"\:0,"color"\:"\#FF0000FF"},{"regionId"\:10806,"regionX"\:25,"regionY"\:38,"z"\:2,"color"\:"\#FF00FFFF"},{"regionId"\:10806,"regionX"\:41,"regionY"\:35,"z"\:3,"color"\:"\#FF00FFFF"},{"regionId"\:10806,"regionX"\:22,"regionY"\:24,"z"\:2,"color"\:"\#FF00FFFF"},{"regionId"\:10806,"regionX"\:22,"regionY"\:16,"z"\:3,"color"\:"\#FF00FFFF"}]
slayer.infobox=true
tithefarmplugin.hexColorWatered=-16737793
timetracking.timers=[{"duration"\:1200,"remaining"\:1200,"loop"\:false,"name"\:"IDLE AFK MAGE","lastUpdate"\:1691380721,"active"\:false}]
banktags.item_12598=bursting
metronome.tickCount=1
worldmap.rareTreeIcon=true
defencetracker.redKeris=true
music.areaSoundEffectVolume=-81
combatlevel.showLevelsUntil=true
menuentryswapper.swapBirdhouseEmpty=true
entityhider.hideDeadNpcs=false
wintertodt.damageNotificationColor=-16711681
cluescroll.displayHintArrows=true
implings.showdragon=HIGHLIGHT
antiDrag.onShiftOnly=true
menuentryswapper.ui_shift_19660816_9075=5
woodcutting.forestryBeeHiveNotification=true
kittenConfig.felineId=5594
itemCharge.showTeleportCharges=true
partypanel.displayPlayerWorlds=true
nyloer.splitFontsBold=true
questhelper.questDifficulty=ALL
radiusmarkers.showMinimap=true
BetterNpcHighlight.respawnOutlineColor=-16711681
banktags.item_13441=bandos solo melee,wildy clue,spindel,artio,calvarion,revenant,cox,hydra,tob,slayer
emote-clue-items.TrackEquipment=true
runecraft.showCosmic=true
menuentryswapper.swapChase=false
bankxpvalue.levelUps=true
maxhit.inventoryWeaponsSpecial=false
implings.showspawn=true
nightmareZone.absorptioncoloroverthreshold=-256
entityhider.hideRandomEvents=false
keyremapping.down=83\:0
itemCharge.showSackCharges=true
menuentryswapper.swapStairsLeftClick=CLIMB
timers.showGodWarsAltar=true
entityhider.hideIgnores=false
runecraft.showChaos=true
loginscreen.syncusername=true
emote-clue-items.HighlightBeginner=true
radiusmarkers.hideNavButton=false
npcUnaggroArea.npcUnaggroShowAreaLines=true
runelite.radiusmarkerplugin=true
runelite.useWikiItemPrices=true
runecraft.showWater=true
party.statusOverlayHealth=false
MahoganyHomes.highlightStairsColor=335609600
chatcommands.lp=true
BetterNpcHighlight.tagStyleMode=TILE
BetterNpcHighlight.presetFillColor4=338100137
BetterNpcHighlight.presetFillColor5=335582920
BetterNpcHighlight.presetFillColor2=338019663
BetterNpcHighlight.presetFillColor3=349145853
BetterNpcHighlight.presetFillColor1=350239793
interacthighlight.outlineFeather=4
randomevents.notifyGravedigger=false
cannon.highlightDoubleHitColor=-65536
menuentryswapper.swapTeleportItem=false
timetracking.timeFormatMode=ABSOLUTE_24H
agility.stickHighlightColor=-65536
banktags.item_4946=slayer
woodcutting.clueNestNotifyTier=DISABLED
xpglobes.Progress\ orb\ background\ color=2139127936
thegauntlet.resourceBowstring=true
BetterNpcHighlight.swTrueTileRave=false
thieving.highlightBats=true
discord.showRaidingActivity=true
npcUnaggroArea.showOnSlayerTask=false
banktags.item_4940=slayer
tobqol.salveReminder=true
linemarkers.defaultColour=-256
xpglobes.alignOrbsVertically=false
averagetime.Dagannoth\ Selector=Kings
actionprogress.herblore.chemistry=true
itemCharge.slaughterNotification=true
NyloerConfig.rangeNylocasColor=-16711936
menuentryswapper.npcLeftClickCustomization=true
xpTracker.hideMaxed=false
tobqol.spellbookReminder=true
runelite.notificationGameMessage=false
raids.pointsMessage=true
actionprogress.use-ticks=false
randomevents.notifyBeekeeper=false
questhelper.showWidgetHints=true
stretchedmode.increasedPerformance=false
agility.highlightSepulchreObstacles=true
keyremapping.right=68\:0
banktags.item_2347=wintertodt
tobqol.shrunkLiveTimerDesign=false
puzzlesolver.drawDots=false
banktaglayouts.layout_slayer=23075\:0,554\:32,6585\:1,561\:33,4940\:2,4946\:3,13239\:4,6570\:8,11889\:9,12954\:10,22981\:11,22947\:12,12695\:16,13441\:17,24478\:18,25781\:19,12791\:20,1231\:24,11140\:25,19634\:26,21268\:27
npcindicators.highlightTrueTile=false
randomevents.notifyDwarf=false
chatfilter.filterType=CENSOR_WORDS
radiusmarkers.includeRetreatInteractionRange=false
herbiboar.colorGameObject=-16711681
inventorytags.tag_10551={"color"\:"\#FFFF0000"}
inventorytags.tag_11889={"color"\:"\#FFFF0000"}
chatcommands.pb=true
cannon.lowWarningThreshold=0
entityhider.hideFriends=false
boosts.displayPanel=false
banktaglayouts.layoutEnabledByDefault=false
herbiboar.colorStart=-16711681
textrecolor.opaqueExamineHighlight=-16776961
banktags.preventTagTabDrags=false
itemidentification.showSaplings=true
inventorytags.tag_22981={"color"\:"\#FFFF0000"}
npcindicators.highlightcolor_0=-6619136
banktags.item_4994=bandos solo melee
menuentryswapper.removeDeadNpcMenus=false
banktags.item_4995=bandos solo melee
objectindicators.highlightHull=false
chatcommands.qp=true
actionprogress.crafting.cast-gold-and-silver=true
kingdomofmiscellania.approvalThreshold=100
nyloer.mageNylocasOutlineColor=-16777216
BetterNpcHighlight.swTrueTileAA=true
actionprogress.crafting.gems=true
objectindicators.region_6710=[{"id"\:10820,"name"\:"Oak tree","regionId"\:6710,"regionX"\:61,"regionY"\:48,"z"\:0,"color"\:"\#FF5858FF"}]
herblorerecipes.useKeybind=false
itemidentification.showJewellery=false
groundMarker.rememberTileColors=true
banktags.item_4502=wintertodt