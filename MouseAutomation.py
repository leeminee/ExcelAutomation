import pyautogui

# 좌표 객체 얻기
position = pyautogui.position()

# 화면 전체 크기 확인
print(pyautogui.size())

# x, y 좌표
print(position.x)
print(position.y)

# 마우스 이동 (x좌표, y좌표)
pyautogui.moveTo(500,500)

# 마우스 이동 (x좌표, y좌표, 2초간)
pyautogui.moveTo(100, 100, 2)




