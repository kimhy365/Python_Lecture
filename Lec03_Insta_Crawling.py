import time
from urllib.parse import quote_plus     # 아스키 코드로 변환시켜준다.
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver

# 변수 url 에 저장될 url 형식은 아래와 같다.
# https://www.instagram.com/explore/tags/%EC%95%84%EC%9D%B4%EC%9C%A0/


base_url = 'https://www.instagram.com/explore/tags/'
# plus_url = input('검색할 태그를 입력하세요 : ')
plus_url = 'SonHeungMin'
url = base_url + quote_plus(plus_url)
print(url)

# 인스타그램의 페이지 소스를 보면 대부분 JavaScript다.
# 그래서 selenium 의 webdriver 가 필요하다.
# beautifulSoup로 JavaScript로 되어 있는 사이트는 크롤링할 수 없다.

driver = webdriver.Chrome()
driver.get(url)

# selenium 은 기본적으로 느리다.
# 만약 속도가 매우 느리다면 사진이 하나하나씩 뜨는 경우가 생길 수 있으므로 사진이 다 뜨기 전에
# 창이 닫히는 경우를 방지하기 위해 드라이버를 띄우고 나서 3초를 기다려 준다.
# 여기서 3초를 기다린 다음에 아래에서 페이지 소스(이미지)들을 불러오기 시작한다.
time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html,'lxml')

insta = soup.select('')     # select는 페이지에 있는 정보를 다 가져온다.
n = 1
for i in insta:
    # 인스타 주소에 i번 째의 a태그의 href 속성을 더하여 출력한다.
    print('https://www.instagram.com' + i.a['href'])
    # 인스타 페이지 소스에서 이미지에 해당하는 클래스의 이미지 태그의 src 속성을
    # imgUrl에 저장한다.
    img_url = i.select_one('.')
    with urlopen(img_url) as f:
        with open('./img/' + plus_url + str(n) + '.jpg', "wb") as h:
            # f를 읽고 img에 저장한다.
            img = f.read()
            # h에 위 내용을 쓴다.
            h.write(img)
        # 계속 programmer 1에 덮어쓰지 않도록 1을 증가시켜 준다
n += 1
print(img_url)
# 출력한 걸 보았을 때 구분하기 좋도록 빈 줄을 추가시킨다.
print()
# 마지막에 driver를 닫아준다. (열린 창을 닫는다.)
driver.close()


