# from pyautogui import write,press
# import time
# time.sleep(5)
# for i in range(1,5):
#     # pyautogui.write('hello')
#     time.sleep(2)
#     write('Hello world!', interval=0.25)
#     press('enter')
    

import pyautogui
import time
time.sleep(3)
for i in range(1,3):
    time.sleep(2)
    pyautogui.write("I love python!",interval=0.25)
    pyautogui.press('enter')

pyautogui.alert('This is an alert box.')
