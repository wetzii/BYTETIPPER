import pyautogui
import time
import random

def givRandTime() -> int:
    return random.randint(1,3)

pyautogui.press('s')
pyautogui.press('y')
pyautogui.press('s')
pyautogui.press('o')
pyautogui.press('enter')
time.sleep(1)

