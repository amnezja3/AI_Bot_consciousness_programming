import pyautogui
import time, os

while True:
    os.system('cls')
    pyautogui.move(20,0)
    time.sleep(2)
    pyautogui.move(-20,0)
    time.sleep(2)
    pyautogui.move(0,-10)
    time.sleep(2)
    pyautogui.move(0,10)