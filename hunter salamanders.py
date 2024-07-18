import pyautogui
import random
import mss
import cv2
import numpy as np
import keyboard
import time


def click_on_cyan():
    start_time = time.time()
    target_color = np.array([255, 255, 0], dtype=np.uint8) # BGR = RGB INVERSO
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
    print(f"Execution time(click_on_cyan): {execution_time} seconds")

def click_on_purple():
    start_time = time.time()
    target_color = np.array([255, 0, 170], dtype=np.uint8)  # BGR = RGB INVERSO
    random_float = random.uniform(0.15, 0.22)
    capture_box = {'top': 30, 'left': 8, 'width': 513, 'height': 336}

    with mss.mss() as sct:
        screenshot = sct.grab(capture_box)
        screenshot_np = np.array(screenshot)[:,:,:3]

    mask_purple = cv2.inRange(screenshot_np, target_color, target_color)
    contours, _ = cv2.findContours(mask_purple, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        rect = cv2.minAreaRect(contour)  # Encuentra el rectángulo girado mínimo
        rect_box = cv2.boxPoints(rect)  # Encuentra los cuatro vértices del rectángulo
        rect_box = rect_box.astype(int)  # Redondea a valores enteros

        # Calcula el centro del rectángulo
        center_x = int(np.mean(rect_box[:, 0])) + capture_box['left']
        center_y = int(np.mean(rect_box[:, 1])) + capture_box['top']

        screen_width, screen_height = pyautogui.size()
        if 0 <= center_x < screen_width and 0 <= center_y < screen_height:
            pyautogui.moveTo(center_x, center_y, random_float)
            pyautogui.click()
        else:
            print("Las coordenadas están fuera de la pantalla.")
        break  # Quita este break si quieres procesar múltiples cuadrados

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Tiempo de ejecución (click_on_purple): {execution_time} segundos")

def click_on_green():
    start_time = time.time()
    target_color = np.array([15, 160, 45], dtype=np.uint8)  # BGR
    threshold=10
    lower_color = target_color - threshold
    upper_color = target_color + threshold

    random_float = random.uniform(0.15, 0.22)
    capture_area = {'top': 30, 'left': 8, 'width': 513, 'height': 336}

    with mss.mss() as sct:
        screenshot = sct.grab(capture_area)
        screenshot_np = np.array(screenshot)[:, :, :3]

    mask = cv2.inRange(screenshot_np, lower_color, upper_color)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        contour = contours[0]
        rect = cv2.minAreaRect(contour)
        box = cv2.boxPoints(rect)
        box = np.intp(box)  # Actualizado de np.int0 a np.intp

        center_x = int(np.mean(box[:, 0])) + capture_area['left']
        center_y = int(np.mean(box[:, 1])) + capture_area['top']

        screen_width, screen_height = pyautogui.size()
        if 0 <= center_x < screen_width and 0 <= center_y < screen_height:
            pyautogui.moveTo(center_x, center_y, random_float)
            pyautogui.click()
        else:
            print("Las coordenadas están fuera de la pantalla.")
    else:
        print("Not Found")

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Tiempo de ejecución (click_on_green): {execution_time} segundos")


def click_on_swamp_green():
    start_time = time.time()
    target_color = np.array([15, 45, 15], dtype=np.uint8)  # BGR color
    random_float = random.uniform(0.15, 0.22)
    
    screen_width, screen_height = pyautogui.size()
    
    box = {'top': 236, 'left': 556, 'width': 183, 'height': 255}
    
    if box['left'] + box['width'] > screen_width or box['top'] + box['height'] > screen_height:
        print("Fuera de los límites de la pantalla.")
        return

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot)[:,:,:3]

    mask = cv2.inRange(screenshot_np, target_color, target_color)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)
        cX = x + w // 2 + box['left']
        cY = y + h // 2 + box['top']

        if 0 <= cX < screen_width and 0 <= cY < screen_height:
            pyautogui.moveTo(cX, cY, random_float)
            pyautogui.click()
        else:
            print("Las coordenadas están fuera de la pantalla.")
    
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(click_on_swamp_green): {execution_time} seconds")


def is_swamp_green_found():

    start_time = time.time()

    box_left = 564
    box_top = 238
    box_right = 740
    box_bottom = 489
    box = {
        'left': box_left,
        'top': box_top,
        'width': box_right - box_left,
        'height': box_bottom - box_top
    }

    target_color = np.array([15, 45, 15], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_swamp_green_found): {execution_time} seconds")

    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def is_cyan_found():

    start_time = time.time()

    box_left = 32
    box_top = 7
    box_right = 513
    box_bottom = 336
    box = {
        'left': box_left,
        'top': box_top,
        'width': box_right - box_left,
        'height': box_bottom - box_top
    }

    target_color = np.array([0, 255, 255], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_cyan_found): {execution_time} seconds")

    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def is_green_found():

    start_time = time.time()

    box_left = 32
    box_top = 7
    box_right = 513
    box_bottom = 336
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
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_green_found): {execution_time} seconds")

    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def is_purple_found():

    start_time = time.time()

    box_left = 32
    box_top = 7
    box_right = 513
    box_bottom = 336
    box = {
        'left': box_left,
        'top': box_top,
        'width': box_right - box_left,
        'height': box_bottom - box_top
    }

    target_color = np.array([170, 0, 255], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_purple_found): {execution_time} seconds")

    if np.any(matches):
        return "Found"
    else:
        return "Not Found"



running = False
randomt = random.uniform(0.05, 0.08)

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
        if is_swamp_green_found() == "Not Found":
            if is_purple_found() == "Not Found":
                time.sleep(0.3+randomt)
            else:
                click_on_purple()
                time.sleep(4+randomt)
                click_on_purple()
                time.sleep(1+randomt)
            if is_cyan_found() == "Not Found":
                time.sleep(0.3+randomt)
            else:
                click_on_cyan()
                time.sleep(4.5+randomt)
            if is_green_found() == "Not Found":
                time.sleep(0.3+randomt)
            else:
                click_on_green()
                time.sleep(3+randomt)
        else:
            while is_swamp_green_found() == "Found":
                click_on_swamp_green()
                time.sleep(0.01+randomt)













