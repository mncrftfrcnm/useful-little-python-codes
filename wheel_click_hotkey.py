import keyboard, pyautogui

def is_hotkey_pressed(key):
    # Check if Ctrl, Alt, and H keys are all pressed
    return keyboard.is_pressed(key)
def is_button_released(key):
    return not keyboard.is_pressed(key)
while True:
    if is_hotkey_pressed('alt+c'):
        pyautogui.click(button='middle')
