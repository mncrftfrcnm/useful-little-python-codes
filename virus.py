import pyautogui, random, time
pyautogui.FAILSAFE = False
while True:
    tre = random.randint(-100,100)
    tre2 = random.randint(-100,100)
    x,y = pyautogui.position()
    pyautogui.moveTo(tre+x, y+tre2)
    pyautogui.click(clicks=2)
