import pyautogui
import time
import random

def givRandTime() -> int:
    return random.randint(1,3)
while(True): 
    pyautogui.press('s')
    time.sleep(givRandTime())
    pyautogui.press('y')
    time.sleep(givRandTime())
    pyautogui.press('s')
    time.sleep(givRandTime())
    pyautogui.press('o')
    time.sleep(givRandTime())
    pyautogui.press('enter')

    for i in range(1,60):
        time.sleep(1)
        print(f"Wartezeit : {60-i} Sekunden")

