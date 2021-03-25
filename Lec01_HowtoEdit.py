############################################################
# PyCharm 편집기 사용법
############################################################
# 모듈 불러오기 (3가지) : built-in(내장) 함수는 필요없음
import sys                  # core module (표준모듈)
import numpy as np          # third-party module / aliasing(별명)
from myid import ID, PW     # user-defined module


def py_version():     # 함수, 변수명은 lowercase_underscore 형식
    """
    함수 설명하는 Docstring
    다중 라인 주석처리, 이 때에도 들여쓰기(indentation)는 필수
    """
    print("파이썬 버전 : " + sys.version)


# 클래스, 함수 정의 앞뒤에는 2줄 띄움
class PyClass():    # 클래스명은 CapitalizedWord 형식
    """클래스에 대한 예시 (Docstring)"""
    def __init__(self, num=1):
        self.num = num
        print('클래스 객체 생성')

    def add(self):
        result = 0
        for n in range(1, self.num+1):
            result += n
        return result

    def multiply(self):
        result = 1
        for n in range(1, self.num+1):
            result *= n
        return result


if __name__ == "__main__":          # 실제 실행할 부분
    key = 'erp'
    print('id : ' + ID[key])        # 상수는 ALL_CAPS 형식
    print('password : ', PW[key])

    print(py_version.__doc__)       # Docstring 표시
    py_version()
    print(dir(sys))                 # 모듈의 멤버 변수와 함수 조회

    print(PyClass.__doc__)          # Docstring 표시
    print(dir(PyClass))
    a = PyClass(10)
    print('1에서 %d까지의 합 : %s' % (a.num, format(a.add(),",")))    # Python 2버전
    print('1에서 {}까지의 곱 : {:,}'.format(a.num, a.multiply()))     # Python 3버전