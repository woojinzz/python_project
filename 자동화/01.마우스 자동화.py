import pyautogui
import time

# print(pyautogui.size()) # 화면 크기 출력

# time.sleep(2) #2초 뒤
# print(pyautogui.position()) # 마우스 위치 출력

#마우스 이동
#pyautogui.moveTo(51, 410)
# pyautogui.moveTo(51, 410, 2)

#마우스 클릭
# pyautogui.click()
# pyautogui.click(button='right')
# pyautogui.doubleClick()
# pyautogui.click(clicks=3, interval=1) # 3번클릭한건데 1초마다 하셈

#마우스 드래그
#923,85->629,86
pyautogui.moveTo(923, 85, 2)
pyautogui.dragTo(629, 86, 2)