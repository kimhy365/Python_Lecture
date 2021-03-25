"""
##################################################################
# Pyqutogui를 이용한 마우스 화면제어
##################################################################
import pyautogui
import time

# 화면 전체 크기 확인하기
screen_size = pyautogui.size()

type(screen_size)
screen_size[0]
screen_size.width
screen_size[1]
screen_size.height

screen_width, screen_height = pyautogui.size()

# 좌표 객체 얻기
mouse_x, mouse_y = pyautogui.position()
pyautogui.position()

# 마우스 이동 (x 좌표, y 좌표, 이동시간)
pyautogui.moveTo(100, 150)
pyautogui.moveTo(100, 150, 10)
pyautogui.moveRel(100, 150)

# 마우스 클릭
pyautogui.click()
pyautogui.click(x=1417, y=15)
pyautogui.click(x=1417, y=15, clicks=2, interval=2)     # 2번, 2초 간격
pyautogui.doubleClick()
pyautogui.click(button='right')                         # 우클릭

# 드래그하기
pyautogui.moveTo(x=1736, y=427)
pyautogui.dragRel(100, 40, 3, button='left')    # xoffset, yoffset, duration
pyautogui.dragTo(1900, 550, 10, button='left')

# 스크롤하기
pyautogui.moveTo(x=100, y=300)
pyautogui.scroll(100)                   # scroll up 1 "clicks"
pyautogui.scroll(50, x=100, y=250)       # (100, 200)으로 이동후 scroll down 5 "clicks"
pyautogui.hscroll(10)                   # scroll right 10 "clicks"


if __name__ == "__main__":
    pyautogui.click(x=85, y=418)
    for i in range(10):
        print(i)
        pyautogui.scroll(-50, x=85, y=418)
        time.sleep(1)

##################################################################
# Pyqutogui를 이용한 키보드 제어
##################################################################
import pyautogui
import pyperclip

# 문자 타이핑! (한글 미지원)
pyautogui.write('hello world!')
pyautogui.write('hello world!', interval=0.25)  # 각 문자를 0.25간젹으로 타이핑

# 한글 타이핑
pyperclip.copy("안녕하세요")                      # 클립보드에 텍스트를 복사
pyautogui.hotkey('ctrl', 'v')                   # 붙여넣기

# 문자가 아닌 <Shift>, <Ctrl> 키 입력
pyautogui.press('shift')                        # <shift> 키
pyautogui.press('esc')

# Press() = keyDown() + keyUp()
pyautogui.keyDown('ctrl')                       # <ctrl>키 누른 상태
pyautogui.press('c')                            # <c> key 입력
pyautogui.keyUp('ctrl')                         # <ctrl>키를 뗌

# 키를 여러번 입력하는 경우
pyautogui.press(['left', 'left', 'left'])       # 왼쪽 방향키 세번 입력
pyautogui.press('left', presses=3)
pyautogui.press('enter', presses=3, interval=3) # <enter>키, 3회, 3초간격

# 여러 키를 동시에 입력할 경우
pyautogui.hotkey('ctrl', 'c')                   # <ctrl> + <c>


##################################################################
# Pyqutogui를 이용한 메시지 박스 함수
##################################################################
import pyautogui

pyautogui.alert(text='경고창', title='제목', button='OK')
pyautogui.confirm('확인창', '제목', buttons=['OK', 'Cancel'])
pyautogui.prompt(text='What is your name')
pyautogui.password('Enter password', title='제목', default='abc', mask='*')

"""

##################################################################
# Pyqutogui를 이용한 파트너 접속
##################################################################
import subprocess
import pyautogui as pg
import time


# Chrome을 실행한 후 'Partner' 페이지로 이동
def open_site(dt):
    path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe";
    subprocess.Popen(path)
    time.sleep(dt)
    pg.write('https://appartner.amorepacific.com//splogin.jsp')
    pg.press('enter')


if __name__ == '__main__':
    open_site(5)

