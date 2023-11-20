import keyboard, pyautogui, time

def is_hotkey_pressed(key):
    # Check if Ctrl, Alt, and H keys are all pressed
    return keyboard.is_pressed(key)
def is_button_released(key):
    return not keyboard.is_pressed(key)
pressing = -1
while True:
    if is_hotkey_pressed('alt+c'):
        pressing = pressing * -1
        time.sleep(0.1)
    if pressing == 1:
        pyautogui.click(clicks=2)
    