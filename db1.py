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

#검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)

    