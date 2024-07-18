import time
import numpy as np
import mss
import cv2
import pyautogui
import random
import keyboard

def click_on_dark_cyan():
    start_time = time.time()
    target_color = np.array([255, 88, 88], dtype=np.uint8) # BGR
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
    print(f"Execution time(click_on_dark_cyan): {execution_time} seconds")


def click_on_purple():
    start_time = time.time()
    target_color = np.array([255, 0, 255], dtype=np.uint8)  # BGR
    random_float = random.uniform(0.15, 0.22)
    box = {'top': 49, 'left': 566, 'width': 731-566, 'height': 177-49}
    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot)[:,:,:3]
    mask_blue = cv2.inRange(screenshot_np, target_color, target_color)
    contours, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        contour = max(contours, key=cv2.contourArea)  # Utiliza el contorno más grande si hay varios
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
    else:
        print("No se encontró el contorno")
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(click_on_purple): {execution_time} seconds")

def click_on_blue():
    start_time = time.time()
    target_color = np.array([255, 0, 0], dtype=np.uint8)  # BGR
    random_float = random.uniform(0.15, 0.22)
    box = {'top': 49, 'left': 566, 'width': 731-566, 'height': 177-49}
    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot)[:,:,:3]
    mask_blue = cv2.inRange(screenshot_np, target_color, target_color)
    contours, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        contour = max(contours, key=cv2.contourArea)  # Utiliza el contorno más grande si hay varios
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
    else:
        print("No se encontró el contorno")
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(click_on_blue): {execution_time} seconds")

def click_on_purple2():
    start_time = time.time()
    target_color = np.array([255, 0, 170], dtype=np.uint8)  # BGR
    random_float = random.uniform(0.15, 0.22)
    box = {'top': 49, 'left': 566, 'width': 731-566, 'height': 177-49}
    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot)[:,:,:3]
    mask_blue = cv2.inRange(screenshot_np, target_color, target_color)
    contours, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        contour = max(contours, key=cv2.contourArea)  # Utiliza el contorno más grande si hay varios
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
    else:
        print("No se encontró el contorno")
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(click_on_purple2): {execution_time} seconds")

def click_on_orange():
    start_time = time.time()
    target_color = np.array([0, 115, 255], dtype=np.uint8)  # BGR
    random_float = random.uniform(0.15, 0.22)
    box = {'top': 30, 'left': 8, 'width': 513, 'height': 336}
    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot)[:,:,:3]
    mask_blue = cv2.inRange(screenshot_np, target_color, target_color)
    contours, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        contour = max(contours, key=cv2.contourArea)  # Utiliza el contorno más grande si hay varios
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
    else:
        print("No se encontró el contorno")
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(click_on_orange): {execution_time} seconds")


def click_on_light_pink():
    start_time = time.time()
    target_color = np.array([185, 135, 185], dtype=np.uint8)  # BGR
    random_float = random.uniform(0.15, 0.22)
    box = {'top': 49, 'left': 566, 'width': 731-566, 'height': 177-49}
    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot)[:,:,:3]
    mask_blue = cv2.inRange(screenshot_np, target_color, target_color)
    contours, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        contour = max(contours, key=cv2.contourArea)  # Utiliza el contorno más grande si hay varios
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
    else:
        print("No se encontró el contorno")
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(click_on_light_pink): {execution_time} seconds")


def click_on_deep_blue():
    start_time = time.time()
    target_color = np.array([99, 66, 33], dtype=np.uint8)  # BGR
    random_float = random.uniform(0.15, 0.22)
    box = {'top': 49, 'left': 566, 'width': 731-566, 'height': 177-49}
    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot)[:,:,:3]
    mask_blue = cv2.inRange(screenshot_np, target_color, target_color)
    contours, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        contour = max(contours, key=cv2.contourArea)  # Utiliza el contorno más grande si hay varios
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
    else:
        print("No se encontró el contorno")
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(click_on_deep_blue): {execution_time} seconds")


def click_on_redpink():
    start_time = time.time()
    target_color = np.array([125, 0, 255])  # BGR para OpenCV
    box = {'top': 30, 'left': 7, 'width': 519-7, 'height': 366-30}
    
    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot)[:,:,:3]

    hsv_img = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2HSV)
    target_hsv_color = cv2.cvtColor(np.uint8([[target_color]]), cv2.COLOR_BGR2HSV)[0][0]
    
    mask = cv2.inRange(hsv_img, target_hsv_color, target_hsv_color)
    coordinates = cv2.findNonZero(mask)
    
    if coordinates is not None:
        x_center = int(np.mean(coordinates[:,0,0])) + box['left']
        y_center = int(np.mean(coordinates[:,0,1])) + box['top']
        
        pyautogui.moveTo(x_center, y_center, 0.2)
        pyautogui.click()
    else:
        print("Color objetivo no encontrado.")

    end_time = time.time()
    print(f"Execution time(click_on_redpink): {end_time - start_time} seconds")


def click_chat_fletch():
    box_left = 177
    box_top = 435
    box_right = 223
    box_bottom = 473

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


def click_spellbook():
    box_left = 742
    box_top = 207
    box_right = 754
    box_bottom = 221

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

def click_teleport_to_house():
    box_left = 590
    box_top = 312
    box_right = 599
    box_bottom = 322

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


def click_on_light_blue():
    start_time = time.time()
    target_color = np.array([255, 125, 0], dtype=np.uint8) # BGR
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
    print(f"Execution time(click_on_light_blue): {execution_time} seconds")


def click_inventory():
    box_left = 643
    box_top = 206
    box_right = 653
    box_bottom = 219

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


def click_on_lime():
    start_time = time.time()
    target_color = np.array([0, 239, 127], dtype=np.uint8) # BGR
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
    print(f"Execution time(click_on_lime): {execution_time} seconds")


def is_lime_found():

    start_time = time.time()

    box_left = 7
    box_top = 30
    box_right = 521
    box_bottom = 366
    box = {
        'left': box_left,
        'top': box_top,
        'width': box_right - box_left,
        'height': box_bottom - box_top
    }

    target_color = np.array([127, 239, 0], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_lime_found): {execution_time} seconds")

    if np.any(matches):
        return "Found"
    else:
        return "Not Found"


def is_inv_full_log():

    start_time = time.time()

    box_left = 702
    box_top = 391
    box_right = 716
    box_bottom = 409
    box = {
        'left': box_left,
        'top': box_top,
        'width': box_right - box_left,
        'height': box_bottom - box_top
    }

    target_color = np.array([138, 106, 62], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_inv_full_log): {execution_time} seconds")

    if np.any(matches):
        return "Found"
    else:
        return "Not Found"


def is_inv_full_planks():

    start_time = time.time()

    box_left = 702
    box_top = 391
    box_right = 716
    box_bottom = 409
    box = {
        'left': box_left,
        'top': box_top,
        'width': box_right - box_left,
        'height': box_bottom - box_top
    }

    target_color = np.array([132, 105, 72], dtype=np.uint8)

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
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_woodcutting): {execution_time} seconds")

    if np.any(matches):
        return "Found"
    else:
        return "Not Found"


def is_run_below_50_percent():

    start_time = time.time()

    box_left = 560
    box_top = 150
    box_right = 562
    box_bottom = 153
    box = {
        'left': box_left,
        'top': box_top,
        'width': box_right - box_left,
        'height': box_bottom - box_top
    }

    target_color = np.array([19, 19, 19], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_woodcutting): {execution_time} seconds")

    if np.any(matches):
        return "Found"
    else:
        return "Not Found"



def is_construction_window_open():

    start_time = time.time()

    box_left = 303
    box_top = 306
    box_right = 323
    box_bottom = 321
    box = {
        'left': box_left,
        'top': box_top,
        'width': box_right - box_left,
        'height': box_bottom - box_top
    }

    target_color = np.array([73, 64, 52], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])
    time.sleep(0.3)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(construction_window_open): {execution_time} seconds")

    if np.any(matches):
        return "Found"
    else:
        return "Not Found"
    

def is_altar_removable():

    start_time = time.time()

    box_left = 6
    box_top = 30
    box_right = 520
    box_bottom = 366
    box = {
        'left': box_left,
        'top': box_top,
        'width': box_right - box_left,
        'height': box_bottom - box_top
    }

    target_color = np.array([99, 15, 139], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])
    time.sleep(0.3)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_altar_removable): {execution_time} seconds")

    if np.any(matches):
        return "Found"
    else:
        return "Not Found"




def build_altar_blue():
    start_time = time.time()
    target_color = np.array([255, 125, 0], dtype=np.uint8) # BGR
    random_float = random.uniform(0.22, 0.29)
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
                pyautogui.click(button='right')
                pyautogui.moveTo(
                cX + random.randint(-1, 1),
                cY + 55 + random.randint(-1, 1),
                random_float)
                time.sleep(0.2 + random_float)
                pyautogui.click()
                time.sleep(0.4 + random_float)
                pyautogui.press('1')
                time.sleep(1.2 + random_float)
            break
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(click_altar_blue()): {execution_time} seconds")

def remove_actions():
    start_time = time.time()
    target_color = np.array([139, 15, 99], dtype=np.uint8) # BGR
    random_float = random.uniform(0.2, 0.22)
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
                pyautogui.click(button='right')
                pyautogui.moveTo(
                cX + random.randint(-1, 1),
                cY + 66 + random.randint(-1, 1),
                random_float)
                time.sleep(0.2 + random_float)
                pyautogui.click()
                time.sleep(1)
                pyautogui.press('1')
                time.sleep(1.5)
            else:
                print("Las coordenadas están fuera de la pantalla.")
            break
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(click_altar_purple): {execution_time} seconds")

def click_near_altar():
    box_left = 260
    box_top = 121
    box_right = 278
    box_bottom = 126

    # Calculate the center coordinates of the box
    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    # Add random offset to the box center coordinates
    offset_x = random.randint(-8, 8)
    offset_y = random.randint(-8, 8)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y
    print(click_x,click_y) 

    randomsleep = random.uniform(0.12, 0.18)
    pyautogui.moveTo(click_x, click_y, randomsleep)
    pyautogui.click()


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
    

        while is_inv_full_planks() == "Found":
            if is_altar_removable() == "Found":
                remove_actions()
            else:
                if is_construction_window_open() == "Found":
                    pyautogui.press('1')
                    time.sleep(0.4)
                else:
                    build_altar_blue()
                
        else:
            if is_lime_found() == "Found":
                time.sleep(20)
                click_on_lime()
                time.sleep(6)
                click_on_dark_cyan()
                time.sleep(10)
            else:
                if is_inv_full_log() == "Found":
                    click_on_purple()
                    time.sleep(13)
                    click_on_blue()
                    time.sleep(8)
                    click_on_orange()
                    time.sleep(7)
                    click_on_deep_blue()
                    time.sleep(12)
                    click_on_redpink()
                    time.sleep(1.4)
                    click_chat_fletch()
                    time.sleep(0.4)
                    click_spellbook()
                    time.sleep(0.4)
                    click_teleport_to_house()
                    time.sleep(5.5)
                    click_near_altar()
                    time.sleep(0.5)
                    click_inventory()
                    time.sleep(3)
                else:
                    if is_woodcutting() == "Not Found":
                        click_on_dark_cyan()
                        time.sleep(4)
                    else:
                        time.sleep(4)