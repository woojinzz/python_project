import pyautogui
import pyperclip

# 키보드 입력(문자)
# pyautogui.write('start', interval=0.25)

# 키도드 입력 (키)
# pyautogui.press('enter')
# pyautogui.press('up')

# 여러개 입력
# pyautogui.hotkey('ctrl', 'c')
# 복사단어
# 한글입력
pyperclip.copy('한글입력')
pyautogui.hotkey('ctrl', 'v')