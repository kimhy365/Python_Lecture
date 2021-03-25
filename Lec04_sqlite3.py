##################################################################
# sqlite3 모듈을 이용한 Database 다루기
##################################################################

import sqlite3


# Database와의 연결(connection) 객체 생성
conn = sqlite3.connect('test_database')     # 인자로 URL, 파일명, 메모리 등

# Cursor 객체 생성
cur = conn.cursor()

# SQL 명령을 수행
conn.execute('SELECT * FROM item')
cur.execute('SELECT * FROM item')

# 데이터 가져오기 : fetchone/fetchmany/fetchall
cur.fetchone()
cur.fetchmany(2)
item = cur.fetchall()   # 변수에 할당하여 접근하기 --> 리스트
item[0][0]

# 데이터베이스 반영 및 연결 종료
conn.commit()   # 변경사항이 있으면 반드시 commit()을 실행해야 저장됨
conn.close()

##################################################################
# 테이블 삭제
##################################################################
import sqlite3


conn = sqlite3.connect('test_database')
# conn.execute('DROP TABLE IF EXISTS item')
conn.execute('DROP TABLE item')
conn.close()

##################################################################
# 테이블 생성
##################################################################
import sqlite3

query = '''CREATE TABLE item (
                item_code 		varchar(20)	NOT NULL,
                item_name		varchar(100),
                process			varchar(10),
                supplier		varchar(20),
                PRIMARY KEY (item_code)
            )'''

with sqlite3.connect('test_database') as conn:
    conn.execute(query)

##################################################################
# 테이블 변경
##################################################################
import sqlite3


query = 'ALTER TABLE item ADD price int CHECK (0<price)'
with sqlite3.connect('test_database') as conn:
    conn.execute(query)

##################################################################
# 데이터 추가 - 1개
##################################################################
import sqlite3


query = '''INSERT INTO item VALUES 
        ('SI0700', '설화수 자음수 125ml', '완제품', '승일산업', 500)'''
with sqlite3.connect('test_database') as conn:
    conn.execute(query)


##################################################################
# 데이터 추가 - 다중행 (executemany)
##################################################################
import sqlite3


query = 'INSERT INTO item VALUES (?, ?, ?, ?, ?)'

# ?에 대응하는 값을 갖는 튜플/리스트 자료형
data = \
[('7165847','리리코스 마린콜라겐V크림(50ml 캡)','완제품','승일산업',100),
 ('SV0150','리리코스 마린보톡신크림 50ML 스크류캡 중캡 증착(실버)','증착','우창산업',300),
 ('SI0390','리리코스 마린보톡신크림 50ML 스크류캡 중캡 사출','사출','(주)선일',200),
 ('SI0879','리리코스 마린콜라겐V크림(50ml 캡 외캡 사출','사출','(주)선일',200),
 ('SI0880','리리코스 마린콜라겐V크림(50ml 캡 내캡 사출','사출','(주)선일',150),
 ('C00551','리리코스 마린보톡신크림 50ML 캡바킹','부자재','우일산업',50)]

with sqlite3.connect('test_database') as conn:
    conn.executemany(query, data)


##################################################################
# 데이터 수정
##################################################################
import sqlite3

query = "UPDATE item SET supplier = '(주)선일' " \
        "WHERE item_code = 'SI0700'"
with sqlite3.connect('test_database') as conn:
    conn.execute(query)


##################################################################
# 데이터 삭제
##################################################################
import sqlite3

query = "DELETE FROM item WHERE item_code = 'SI0700'"
with sqlite3.connect('test_database') as conn:
    conn.execute(query)



##################################################################
# 데이터 조회 - SQL 실행결과를 Cursor 객체에 할당하고 fetch로 가져옴
# Cursor 객체 메서드 : execute, executemany, fetchone, fetchmany, fetchall 등
##################################################################
import sqlite3


query = "SELECT * FROM item"
with sqlite3.connect('test_database') as conn:
    cur = conn.execute(query)
    items = cur.fetchall()

for item in items:
    print(item)

##################################################################
# MS SQL Server 다루기
##################################################################
import pymssql


conn = pymssql.connect(
    server="192.168.15.49",
    port=1433,          # 디폴트값(1433)은 생략가능 (포트를 방화벽 해제해야 함)
    user="sa",
    password="smart",
    database="mydata")

cursor = conn.cursor()
cursor.execute("SELECT * FROM item")
print(cursor.fetchone())

cursor.execute("SELECT @@VERSION")
print(cursor.fetchone()[0])


