import numpy as np
import time
import mss
import cv2
import pyautogui
import random
import keyboard


colors = {
    "Coal ore": np.array([53, 52, 35], dtype=np.uint8),
    "Iron ore": np.array([97, 64, 50], dtype=np.uint8),
    "Mithril ore": np.array([93, 93, 128], dtype=np.uint8),
    "Mithril bar": np.array([68, 68, 105], dtype=np.uint8),
    "Mithril pl8": np.array([58, 59, 88], dtype=np.uint8)
}

def is_inv_found(inv_number, target_color):
    box_left = 569 + ((inv_number - 1) % 4) * 41
    box_top = 242 + ((inv_number - 1) // 4) * 35
    box_right = box_left + 31
    box_bottom = box_top + 29
    
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    if np.any(matches):
        return "O"
    else:
        return "X"


def drop_inv(inv_number):
    rndmt = random.uniform(0.13, 0.18)

    box_left = 569 + ((inv_number - 1) % 4) * 41
    box_top = 242 + ((inv_number - 1) // 4) * 35
    box_right = box_left + 31
    box_bottom = box_top + 29

    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    offset_x = random.randint(-6, 6)
    offset_y = random.randint(-6, 6)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    pyautogui.moveTo(click_x, click_y, rndmt)
    pyautogui.keyDown('shift')
    time.sleep(rndmt/3)
    pyautogui.click()
    time.sleep(rndmt/3)
    pyautogui.keyUp('shift')


def click_on_purple():
    start_time = time.time()
    target_color = np.array([255, 0, 170], dtype=np.uint8) # BGR
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
            pyautogui.moveTo(cX, cY, random_float)
            pyautogui.click()
            break
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(click_on_purple): {execution_time} seconds")

def click_on_red():
    start_time = time.time()
    target_color = np.array([0, 0, 255], dtype=np.uint8) # BGR
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
            pyautogui.moveTo(cX+3, cY+3, random_float)
            pyautogui.click()
            break
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(click_on_red): {execution_time} seconds")

def click_on_cyan():
    start_time = time.time()
    target_color = np.array([255, 255, 0], dtype=np.uint8) # BGR
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
            pyautogui.moveTo(cX, cY, random_float)
            pyautogui.click()
            break
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(click_on_cyan): {execution_time} seconds")

def click_to_walk_on_cyan():
    start_time = time.time()
    target_color = np.array([255, 255, 0], dtype=np.uint8) # BGR
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
            pyautogui.moveTo(cX, cY, random_float)
            pyautogui.click(button='right')
            pyautogui.moveTo(cX, cY +38, random_float)
            pyautogui.click()
            break
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(click_to_walk_on_cyan): {execution_time} seconds")

def click_on_dark_red():
    start_time = time.time()
    target_color = np.array([2, 2, 100], dtype=np.uint8) # BGR
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
            pyautogui.moveTo(cX, cY, random_float)
            pyautogui.click()
            break
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(click_on_dark_red): {execution_time} seconds")

def click_on_dark_blue():
    start_time = time.time()
    target_color = np.array([99, 66, 33], dtype=np.uint8) # BGR
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
            pyautogui.moveTo(cX, cY, random_float)
            pyautogui.click()
            break
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(click_on_dark_blue): {execution_time} seconds")

def click_on_cream_blue():
    start_time = time.time()
    target_color = np.array([194, 106, 21], dtype=np.uint8) # BGR
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
            pyautogui.moveTo(cX, cY, random_float)
            pyautogui.click()
            break
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(click_on_cream_blue): {execution_time} seconds")

def click_on_dark_green():
    start_time = time.time()
    target_color = np.array([0, 55, 0], dtype=np.uint8) # BGR
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
            pyautogui.moveTo(cX, cY, random_float)
            pyautogui.click()
            break
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(click_on_dark_green): {execution_time} seconds")

def isLastInv_Found():
    box_left = 697
    box_top = 437
    box_right = 700
    box_bottom = 440
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([75, 66, 58], dtype=np.uint8)

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

def is_inside_anvil():

    start_time = time.time()

    box_left = 142
    box_top = 198
    box_right = 391
    box_bottom = 217
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([0, 255, 255], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_100_coal_found_on_shop): {execution_time} seconds")
    time.sleep(0.6)
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def mith_bars_inv():
    box_left = 698
    box_top = 428
    box_right = 721
    box_bottom = 444
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([93, 93, 128], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])
    time.sleep(0.6)
    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def is_shop_open():

    start_time = time.time()

    box_left = 303
    box_top = 306
    box_right = 323
    box_bottom = 321
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([73, 64, 52], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_shop_open): {execution_time} seconds")

    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def is_100_coal_found_on_shop():

    start_time = time.time()

    box_left = 377
    box_top = 90
    box_right = 379
    box_bottom = 95
    box = { 'left': box_left,
            'top': box_top,
            'width': box_right - box_left,
            'height': box_bottom - box_top}

    target_color = np.array([255, 255, 0], dtype=np.uint8)

    with mss.mss() as sct:
        screenshot = sct.grab(box)
        screenshot_np = np.array(screenshot, dtype=np.uint8)

    matches = (screenshot_np[:, :, 0] == target_color[2]) & \
              (screenshot_np[:, :, 1] == target_color[1]) & \
              (screenshot_np[:, :, 2] == target_color[0])

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time(is_100_coal_found_on_shop): {execution_time} seconds")

    if np.any(matches):
        return "Found"
    else:
        return "Not Found"

def click_iron_ore():
    rndmt = random.uniform(0.18, 0.24)

    box_left = 180
    box_top = 97
    box_right = 198
    box_bottom = 114

    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    offset_x = random.randint(-6, 6)
    offset_y = random.randint(-6, 6)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    pyautogui.moveTo(click_x, click_y, rndmt)
    pyautogui.click()

def click_mithril_ore():
    rndmt = random.uniform(0.18, 0.24)

    box_left = 227
    box_top = 94
    box_right = 246
    box_bottom = 116

    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    offset_x = random.randint(-6, 6)
    offset_y = random.randint(-6, 6)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    pyautogui.moveTo(click_x, click_y, rndmt)
    pyautogui.click()

def click_coal_ore():
    rndmt = random.uniform(0.18, 0.24)

    box_left = 369
    box_top = 99
    box_right = 387
    box_bottom = 114

    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    offset_x = random.randint(-6, 6)
    offset_y = random.randint(-6, 6)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    pyautogui.moveTo(click_x, click_y, rndmt)
    pyautogui.click()

def click_spellbook():
    rndmt = random.uniform(0.18, 0.24)

    box_left = 736
    box_top = 204
    box_right = 754
    box_bottom = 220

    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    offset_x = random.randint(-6, 6)
    offset_y = random.randint(-6, 6)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    pyautogui.moveTo(click_x, click_y, rndmt)
    pyautogui.click()

def click_high_alch():
    rndmt = random.uniform(0.18, 0.24)

    box_left = 717
    box_top = 333
    box_right = 732
    box_bottom = 348

    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    offset_x = random.randint(-6, 6)
    offset_y = random.randint(-6, 6)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    pyautogui.moveTo(click_x, click_y, rndmt)
    pyautogui.click()

def click_8_inv_slot():
    rndmt = random.uniform(0.18, 0.24)

    box_left = 702
    box_top = 283
    box_right = 721
    box_bottom = 299

    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    offset_x = random.randint(-6, 6)
    offset_y = random.randint(-6, 6)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    pyautogui.moveTo(click_x, click_y, rndmt)
    pyautogui.click()
    
def click_4_inv_slot():
    rndmt = random.uniform(0.18, 0.24)

    box_left = 696
    box_top = 249
    box_right = 717
    box_bottom = 264

    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    offset_x = random.randint(-6, 6)
    offset_y = random.randint(-6, 6)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    pyautogui.moveTo(click_x, click_y, rndmt)
    pyautogui.click()

def click_inv():
    rndmt = random.uniform(0.18, 0.24)

    box_left = 640
    box_top = 202
    box_right = 653
    box_bottom = 222

    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    offset_x = random.randint(-6, 6)
    offset_y = random.randint(-6, 6)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    pyautogui.moveTo(click_x, click_y, rndmt)
    pyautogui.click()

def move_mouse_to_player():
    rndmt = random.uniform(0.18, 0.24)

    box_left = 262
    box_top = 199
    box_right = 266
    box_bottom = 201

    box_center_x = (box_left + box_right) // 2
    box_center_y = (box_top + box_bottom) // 2

    offset_x = random.randint(-6, 6)
    offset_y = random.randint(-6, 6)
    click_x = box_center_x + offset_x
    click_y = box_center_y + offset_y

    pyautogui.moveTo(click_x, click_y, rndmt)
    #pyautogui.click()


running = False
hop_world_counter = 0
inventory_size = 24
inventory_results = {}
excluded_numbers = {17, 18, 21, 22}

for ore, color in colors.items():
    results = [is_inv_found(i, color) for i in range(1, inventory_size + 1) if i not in excluded_numbers]
    result_string = ' '.join(results)
    inventory_results[ore] = results
final_results = ['O' if 'O' in items else 'X' for items in zip(*inventory_results.values())]
final_result_string = ' '.join(final_results)
#print(final_result_string)

def put_money_on_coffer():
    click_on_cream_blue()
    time.sleep(6)
    pyautogui.press('1')
    time.sleep(0.8)
    pyautogui.typewrite('600\n')
    time.sleep(0.3)

def buy_ores_into_furnace():
    click_on_dark_blue()
    time.sleep(3.6)
    click_coal_ore()
    time.sleep(0.3)
    pyautogui.press('esc')
    time.sleep(0.3)
    click_on_purple()
    time.sleep(3.2)
    click_on_dark_blue()
    time.sleep(2.2)
    click_coal_ore()
    time.sleep(0.3)
    pyautogui.press('esc')
    time.sleep(0.3)
    click_on_purple()
    time.sleep(3.2)
    click_on_dark_blue()
    time.sleep(2.2)
    click_mithril_ore()
    time.sleep(0.3)
    pyautogui.press('esc')
    time.sleep(0.3)
    click_on_purple()
    time.sleep(3.2)

def bars_out_furnace():
    click_on_dark_green()
    time.sleep(4.4)
    click_on_red()
    time.sleep(3.2)
    pyautogui.press('space')
    time.sleep(0.6)
    while mith_bars_inv() == "Not Found":
        click_on_red()
        time.sleep(3.2)
        pyautogui.press('space')
        time.sleep(0.6)

def enter_anvil():
    click_to_walk_on_cyan()
    time.sleep(3.6)
    click_on_cyan()
    time.sleep(1.2)
    move_mouse_to_player()
    time.sleep(2)
    while is_inside_anvil() == "Not Found":
        click_on_cyan()
        time.sleep(1.2)
        move_mouse_to_player()
        time.sleep(2)

def and_smith():
    click_on_dark_red()
    time.sleep(2.4)
    pyautogui.press('space')
    time.sleep(12)

def high_alch():
    click_spellbook()
    time.sleep(0.2)
    for x in range(4):
        click_high_alch()
        time.sleep(1)
        click_4_inv_slot()
        time.sleep(1)

def out_of_anvil():
    click_inv()
    time.sleep(0.2)
    click_on_cyan()
    time.sleep(3.6)

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
        
        click_on_dark_green()
        time.sleep(0.9)
        for _ in range (0,5):
            pyautogui.press('backspace')
        if final_result_string == "X X X X X X X X X X X X X X X X X X X X":
            pyautogui.press('f2')
            time.sleep(0.3)
            click_on_dark_blue()
            time.sleep(2.2)
            if is_100_coal_found_on_shop() == "Found":
                pyautogui.press('esc')
                time.sleep(0.3)
                for x in range(2):
                    put_money_on_coffer()
                    buy_ores_into_furnace()
                    bars_out_furnace()
                    enter_anvil()
                    and_smith()
                    high_alch()
                    out_of_anvil()
            else:
                world_numbers = [356, 515, 516, 466, 494, 495, 496, 352, 355, 424, 357, 358, 386, 387, 395]
                pyautogui.press('esc')
                time.sleep(1.2)
                move_mouse_to_player()
                if hop_world_counter == 0:
                    pyautogui.typewrite(f'::hop {world_numbers[0]}\n')
                    hop_world_counter += 1
                elif hop_world_counter <= 4:
                    pyautogui.typewrite(f'::hop {world_numbers[hop_world_counter]}\n')
                    hop_world_counter += 1
                elif hop_world_counter == 5:
                    pyautogui.typewrite(f'::hop {world_numbers[hop_world_counter]}\n')
                    hop_world_counter += 1
                elif hop_world_counter <= 6:
                    pyautogui.typewrite(f'::hop {world_numbers[hop_world_counter]}\n')
                    hop_world_counter += 1
                elif hop_world_counter == 7:
                    pyautogui.typewrite(f'::hop {world_numbers[hop_world_counter]}\n')
                    hop_world_counter += 1
                elif hop_world_counter <= 8:
                    pyautogui.typewrite(f'::hop {world_numbers[hop_world_counter]}\n')
                    hop_world_counter += 1
                else:
                    pyautogui.typewrite(f'::hop {world_numbers[hop_world_counter]}\n')
                    hop_world_counter = 0
                time.sleep(10.6)
        else:
            for inv_number in range (1,25):
                if inv_number not in excluded_numbers:
                    drop_inv(inv_number)

