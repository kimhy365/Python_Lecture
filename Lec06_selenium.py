##################################################################
# Selenium을 이용한 웹 브라우저 자동화
##################################################################
"""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.implicitly_wait(10)   # 암묵적으로 웹자원 로드를 위해 10초까지 기다려 준다.
driver.get('https://google.com')

copy_css_selector = 'div > div.a4bIc > input'
driver.find_element_by_css_selector(copy_css_selector).send_keys('파이썬')
driver.find_element_by_css_selector(copy_css_selector).send_keys(Keys.ENTER)

# driver.find_element_by_class_name("LC20lb").click()     # 첫번째 검색 결과
# driver.find_element_by_css_selector('.LC20lb').text     # 태그 검색 확인
driver.find_elements_by_class_name('LC20lb')[2].click() # 3번째 검색 결과

time.sleep(5)
driver.quit()

##################################################################
# Selenium을 이용한 웹 브라우저 자동화
##################################################################
import time
from selenium import webdriver
from myid import ID, PW
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait             # Implicitly wait
from selenium.webdriver.support import expected_conditions as EC    # Explicitly wait

driver = webdriver.Chrome()     # 인자로 경로지정 : './Users/chromedriver'
driver.implicitly_wait(time_to_wait=10)      # 암묵적 대기(초)

try:
    driver.get('https://login.ecounterp.com/ECERP')

    WebDriverWait(driver, 10).until(   # 'com_code' ID 태그를 찾을 때까지 10초를 기다림
        EC.presence_of_element_located((By.ID, 'com_code')))

    driver.find_element_by_id('com_code').send_keys('304822')
    driver.find_element_by_id('id').send_keys(ID['erp'])
    driver.find_element_by_id('passwd').send_keys(PW['erp'])
    # driver.find_element_by_xpath('//*[@id="com_code"]').send_keys('304822')
    # driver.find_element_by_xpath('//*[@id="id"]').send_keys(ID['erp'])
    # driver.find_element_by_xpath('//*[@id="passwd"]').send_keys(PW['erp'])
    driver.find_element_by_id('save').click()

except Exception as e:
    print(e)

finally:
    time.sleep(5)
    driver.quit()       # driver.close()
"""
##################################################################
# Selenium - 팝업창 닫기
##################################################################
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait             # Implicitly wait
from selenium.webdriver.support import expected_conditions as EC    # Explicitly wait
from selenium.webdriver.common.keys import Keys
from myid import ID, PW

opts = webdriver.ChromeOptions()
# opts.add_argument('headless')       # 백그라운드 실행 옵션
opts.add_argument('window-size=1300,760')
# opts.add_argument('window-size=1920,1080')
driver = webdriver.Chrome(options=opts)
# driver = webdriver.Chrome()
driver.implicitly_wait(time_to_wait=10)      # 암묵적 대기(초)
driver.get('https://appartner.amorepacific.com')

WebDriverWait(driver, 20).until(   # 'principal' ID 태그를 찾을 때까지 20초를 기다림
    EC.presence_of_element_located((By.ID, 'principal')))

base_page = driver.window_handles[0]
while len(driver.window_handles) > 1:       # 모든 팝업창을 닫음
    driver.switch_to.window(driver.window_handles[1])
    driver.close()

driver.switch_to.window(base_page)

driver.find_element_by_id('principal').clear()
driver.find_element_by_id('principal').send_keys(ID['partner'])
# driver.find_element_by_id('pstext').click()
# driver.find_element_by_id('pstext').send_keys(PW['partner'])
driver.find_element_by_xpath('//*[@id="pstext"]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="pstext"]').send_keys(PW['partner'])

# selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable
# ele = driver.find_element_by_xpath('//*[@id="pstext"]')
# driver.execute_script("arguments[0].send_keys('si2148571!')",ele)
driver.find_element_by_class_name('sploginBtn').click()

time.sleep(5)
driver.close()

"""
##################################################################
# Selenium - 웹 브라우저 숨기기
##################################################################
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_argument('headless')                   # 백그라운드 실행 옵션
# opts.add_argument('window-size=1920,1080')      # 화면구성이 변경되지 않도록 크기 지정
opts.add_argument('window-size=1300,760')
driver = webdriver.Chrome(options=opts)

try:
    driver.get('http://naver.com')
    print(driver.title)
except Exception as e:
    print(e)
finally:
    driver.quit()





##################################################################
# Selenium과 BeautifulSoup을 이용한 크롤링
##################################################################

from selenium import webdriver
from bs4 import BeautifulSoup

# setup Driver|Chrome : 크롬드라이버를 사용하는 driver 생성
driver = webdriver.Chrome('/Users/beomi/Downloads/chromedriver')
driver.implicitly_wait(3) # 암묵적으로 웹 자원을 (최대) 3초 기다리기
# Login
driver.get('https://nid.naver.com/nidlogin.login') # 네이버 로그인 URL로 이동하기
driver.find_element_by_name('id').send_keys('naver_id') # 값 입력
driver.find_element_by_name('pw').send_keys('mypassword1234')
driver.find_element_by_xpath(
    '//*[@id="frmNIDLogin"]/fieldset/input'
).click() # 버튼클릭하기
driver.get('https://order.pay.naver.com/home') # Naver 페이 들어가기
html = driver.page_source # 페이지의 elements모두 가져오기
soup = BeautifulSoup(html, 'html.parser') # BeautifulSoup사용하기
notices = soup.select('div.p_inr > div.p_info > a > span')

for n in notices:
    print(n.text.strip())

"""


##################################################################
# Selenium 실습 - https://sacko.tistory.com/14?category=643535
##################################################################
from selenium import webdriver

# selenium의 webdriver로 크롬 브라우저를 실행한다
driver = webdriver.Chrome()

# "Google"에 접속한다
driver.get("http://www.google.co.kr")

# 페이지의 제목을 체크하여 'Google'에 제대로 접속했는지 확인한다
assert "Google" in driver.title
# assert "Naver" in driver.title

# 검색 입력 부분에 커서를 올리고
# 검색 입력 부분에 다양한 명령을 내리기 위해 elem 변수에 할당한다
elem = driver.find_element_by_name("q")

# 입력 부분에 default로 값이 있을 수 있어 비운다
elem.clear()

# 검색어를 입력한다
elem.send_keys("Selenium")

# 검색을 실행한다
elem.submit()

# 검색이 제대로 됐는지 확인한다
assert "No results found." not in driver.page_source

# 브라우저를 종료한다
driver.close()