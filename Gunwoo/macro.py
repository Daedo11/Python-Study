import time
import pyautogui
import pyperclip

time.sleep(3)

position = pyautogui.position()
print(position)

pyautogui.click(1132, 111)

time.sleep(0.2)

a = "my "*1000
pyperclip.copy(a)
#pyautogui.write(a)
pyautogui.hotkey("command", "v")
