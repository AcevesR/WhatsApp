from winreg import HKEY_LOCAL_MACHINE
from pluggy import HookimplMarker
import pyautogui as spam
import time

i = 0

# Set the desired number of messages
qty = 260

# This is important to define; after this time, they auto typing will begin.
time.sleep(10)


while i < int(qty):

    # The desired message will be here.
    spam.typewrite("MESSAGE")
    
    #This is important since it's the enter to send each message.
    spam.press("Enter")
    
    i += 1
