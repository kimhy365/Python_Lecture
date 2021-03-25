##################################################################
# 웹스크레이핑
##################################################################
"""
import requests
from bs4 import BeautifulSoup
from pprint import pprint

res = requests.get('http://www.naver.com')
print(res)  # 200
html = res.text         # 페이지 소스 보기

soup = BeautifulSoup(html, 'html.parser')
# soup = BeautifulSoup(html, 'lxml')

type(html)      # <class 'str'>
type(soup)      # <class 'bs4.BeautifulSoup'>

soup.a          # Tag a의 첫번째 태그를 반환
soup.div
soup.head
soup.body
soup.select('div')
soup.select('div:nth-of-type(1)')
print(soup.div.prettify())


soup.find('div')                            # Tag로 찾기
soup.find_all('div')
soup.find('a')
soup.find('a', href='#newsstand')           # Tag와 Attributes로 찾기
soup.find('a', {'href': '#newsstand'})
soup.find(href='#newsstand')                # Attributes로 찾기
soup.find(id='wrap')

##################################################################
# 웹스크레이핑 - 네이버 날씨 정보 가져오기
##################################################################
import requests
import re           # 정규식(regular expression) : 패턴을 이용한 검색
from bs4 import BeautifulSoup
from pprint import pprint

res = requests.get('https://search.naver.com/search.naver?query=날씨')
html = res.text         # 페이지 소스 보기

soup = BeautifulSoup(html, 'html.parser')
data = soup.find_all('div', {'class': 'info_data'})
pprint(data)
temp = data[0].find('span', {'class': 'todaytemp'}).text
# temp = soup.find_all('div', {'class': 'info_data'})[0].find('span', {'class': 'todaytemp'}).text

# temp = data[0].find('span', {'class': 'todaytemp'})
# print(temp)
# print(temp.text)
# temp = soup.find('p', {'class':'todaytemp'})


##################################################################
# 웹스크레이핑 - 네이버 날씨 정보 가져오기
##################################################################
import requests
from bs4 import BeautifulSoup
from pprint import pprint

res = requests.get('https://search.naver.com/search.naver?query=날씨')
html = res.text         # 페이지 소스 보기

soup = BeautifulSoup(html, 'html.parser')

soup.select("head > title")         # head 태그 하위의 title 태그를 선택  리스트로 반환
soup.select('.todaytemp')           # class명(.)으로 검색
soup.select_one('.todaytemp')
# 개발자 도구에서 Copy Selector
# "#main_pack > section.sc_new.cs_weather._weather > div > div.api_cs_wrap > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.main_info > div > p > span.todaytemp"
soup.select('div.main_info > div > p > span.todaytemp')
soup.select_one("a")
anchors = soup.select("a")
anchors[2]
soup.select_one("a.link")       # anchor 태그에서 클래스명이 link인 것
soup.select("a#link")           # anchor 태그에서 id가 link인 것
soup.select('a[href^="http://example.com/"]')
# anchor 태그에서 href 속성이 http://example.com/으로 시작되는 것, 정규식 ^는 시작
soup.select('a[href$="abc"]')
# anchor 태그에서 href 속성이 abc로 끝나는 것, 정규식 $는 끝을 의미

##################################################################
# 웹스크레이핑 - 네이버 날씨 정보 가져오기
##################################################################
import re

m = re.match('hello','hello world hello')     # 정규식과 문자열이 매칭되는지 조사
if m:
    print('Match found: ', m.group())       # group() 함수로 실제 매칭된 문자열 반환
else:
    print('No match')

data_list = re.findall('[-]?\d+', '<span class="todaytemp">-9.5</span>')
data_str = "".join(data_list)   # "".join(리스트): 리스트의 문자열을 합침
data_num = int(data_str) / 10
print(data_num)

data_list = re.findall('[+-]?[0-9]+[.0-9]*', '<span class="todaytemp">-9.5</span>')
float(data_list[0])     # data_list = ['-9.5']
"""
##################################################################
# 웹스크레이핑 - 기상청 날씨 정보 가져오기
##################################################################
import requests
from bs4 import BeautifulSoup

# 웹페이지를 가져온 뒤 BeautifulSoup 객체로 만듦
URL = 'https://www.weather.go.kr/weather/observation/currentweather.jsp'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

# <table class="table_develop3">을 찾음
table = soup.find('table',{'class':'table_develop3'})
data = []                               # 데이터를 저장할 리스트 생성
for tr in table.find_all('tr'):         # 모든 <tr> 태그를 찾아서 반복
    # 각 지점의 데이터를 가져옴 : tr(행), td(열)
    tds = tr.find_all('td')

    for td in tds:
        if td.find('a'):                # 행에 <a> 태그가 없으면 None 반환
            point = td.find('a').text   # 지역
            temp = tds[5].text          # 온도
            humi = tds[10].text         # 습도
            data.append([point, temp, humi])    # [지역, 온도, 습도] 리스트 추가
        # else:
        #     print(td.find('a'))

for row in data:
    print('{} \t {}C\t {}%'.format(*row))       # unpacking
