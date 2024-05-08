# db1.py 
import sqlite3
#전역함수:임시로 메모리에 작업 
#연결객체(인스턴스)
con = sqlite3.connect(":memory:")

#실제 구문을 실행할 커서 객체 
cur = con.cursor() 

#테이블구조(데이터 저장소)
cur.execute("create table PhoneBook (Name text, PhoneNum text);")

#입력 
cur.execute("insert into PhoneBook values ('전우치', '010-222');")
#입력 파라메터 처리
name = "홍길동"
phoneNumber = "010-123"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber))
#한번에 2개를 입력(다중 레코드):2차원 배열 
datalist = (("이순신","010-222"), ("박문수","010-567"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)

#검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row[0], row[1]) 

