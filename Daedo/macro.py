import time
import pyautogui

print(pyautogui.size())
print(pyautogui.position())
print(pyautogui.moveTo(531, 683, duration=0.5))
print(pyautogui.click())
print(pyautogui.moveTo(621, 690, duration=0.2))
print(pyautogui.click())
print(pyautogui.moveTo(1297, 293, duration=0.5))
print(pyautogui.click())

# \n는 줄바꿈
print(pyautogui.write('Hello World!! \n', interval=0.2))
print(pyautogui.write(["h", "e", "l", "l", "o", " "], interval=0.2))
print(pyautogui.scroll(-100))

time.sleep(0.5)

print(pyautogui.scroll(100))
