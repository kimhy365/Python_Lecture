# -*- coding: utf-8 -*-
##################################################################
# Step1. Structure of Qt5 GUIs
##################################################################

# 모듈 불러오기
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton   # Recommended
# from PyQt5.QtWidgets import *  # 해당 모듈의 모든 변수, 함수, 클래스

# 응용프로그램 객체 생성
app = QApplication(sys.argv)        # sys.argv : 입력인자
# app = QApplication([])

# Top-level 윈도우(QMainWindow,QWidget,QDialog) 만들기
win = QWidget()                     # QWidget 객체 생성
win.setWindowTitle('윈도우 만들기')   # 속성 변경 : 윈도우 제목 지정
win.setGeometry(400, 300, 300, 200) # 속성 변경 : 위치 및 크기 지정

# 위젯 추가 : QLabel, QPushButton 등
btn = QPushButton('버턴', win)        # QPushButton 객체 생성
btn.move(100, 50)                    # 속성 변경 : 위치 지정

# 윈도우 표시하기
win.show()

# 프로그램 실행
app.exec_()                      # 무한 Event 처리루프
# sys.exit(app.exec_())          # 종료시 반환값 출력


##################################################################
# Step2. Layouts
##################################################################
from PyQt5.QtWidgets import *

app = QApplication([])

win = QWidget()                         # simple container widget
vbox = QVBoxLayout()                    # layout 생성
vbox.addStretch(1)                      # 신축성 있는 빈 공간 제공
vbox.addWidget(QPushButton("Top"))      # 위젯 추가
vbox.addWidget(QPushButton("Bottom"))
vbox.addStretch(5)
win.setLayout(vbox)
win.show()

app.exec_()

#################################################################
# Step3. Signals and Slots
##################################################################
from PyQt5.QtWidgets import *

app = QApplication([])
win = QWidget()

btn = QPushButton("버턴", win)


def on_button_clicked():                # slot(callback) 함수 정의
    alert = QMessageBox()
    alert.setText("버턴을 클릭하였습니다!")
    alert.exec_()


btn.clicked.connect(on_button_clicked)   # click signal(event) 발생시 호출함수 연결

win.show()
app.exec_()


##################################################################
# Step4. 클래스로 프로그램 구조화하기
##################################################################

from PyQt5.QtWidgets import *


class MyWindow(QWidget):        # QWidget에서 상속
    def __init__(self):
        super().__init__()      # Super Class 생성자 호출
        self.alert = None       # 모든 정의는 한 곳에서 하도록 권장
        self.setWindowTitle("PyQt5")
        self.setGeometry(400, 300, 300, 200)
        self.btn = QPushButton("클릭", self)
        self.btn.move(100, 50)
        self.btn.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        self.alert = QMessageBox()
        self.alert.setText("버턴을 클릭하였습니다!")
        self.alert.exec_()


if __name__ == "__main__":
    app = QApplication([])
    win = MyWindow()
    win.show()
    app.exec_()


##################################################################
# Step5. 전형적인 윈도우 만들기
##################################################################
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()      # Super Class 생성자 호출
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("윈도우 만들기")          # 타이틀
        self.setGeometry(300,300,400,300)           # 사이즈
        self.setWindowIcon(QIcon("icon_win.png"))   # 아이콘
        self.statusBar().showMessage('상태바')       # 상태바

        exitAction = QAction(QIcon('icon_exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+X')
        exitAction.triggered.connect(qApp.quit)
        menubar = self.menuBar()                    # 메뉴바
        filemenu = menubar.addMenu("&File")
        filemenu.addAction(exitAction)

        self.btn = QPushButton("메시지", self)
        self.btn.move(80, 50)
        self.btn.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        QMessageBox.about(self,"메시지","버턴이 클릭되었습니다.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


##################################################################
# Step6. Qt Designer로 GUI 만들기(1) - 변환
##################################################################
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from Lec_Window import *        # Qt Designer에서 만든 파일명(모듈)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()      # Super Class 생성자 호출
        self.ui = Ui_MyWindow()
        self.ui.setupUi(self)
        self.ui.btn.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        QMessageBox.about(self,"메시지","버턴이 클릭되었습니다.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()

    # win = QMainWindow()     # 부모 클래스 객체 생성
    # ui = Ui_MyWindow()      # Qt designer UI 객체 생성
    # ui.setupUi(win)         # 결합
    # win.show()

    sys.exit(app.exec_())


##################################################################
# Step6. Qt Designer로 GUI 만들기(2) - 연동
##################################################################
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()      # Super Class 생성자 호출
        self.ui = uic.loadUi('Lec_Window.ui', self)
        self.ui.btn.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        QMessageBox.about(self,"메시지","버턴이 클릭되었습니다.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

