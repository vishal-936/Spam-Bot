import pyautogui
import time
import random

spam_text=["You are getting Spam","Nice work","You are web devoloper Now","this is whatsapp spam"]
NumberOfTimes=100

for _ in range(NumberOfTimes):
    pyautogui.typewrite(random.choice(spam_text))
    pyautogui.press('enter')
    time.sleep(0.1)
    
    


    
