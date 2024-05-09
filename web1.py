# web1.py 
#웹크롤링을 위한 선언 
from bs4 import BeautifulSoup

#페이지를 로딩:메서드체인 
page = open("Chap09_test.html", "rt", encoding="utf-8").read() 

#검색이 용이한 스프객체 생성(html, xml)
soup = BeautifulSoup(page, "html.parser")
#print(soup.prettify())
#<p>전체 검색
# print(soup.find_all("p"))
#<p>하나 검색 
# print(soup.find("p"))
#필터링: <p class='outer-text'>
#파이썬 class키워드를 사용할 수 없다! 
#print(soup.find_all("p", class_="outer-text"))
#attrs는 속성을 지정(attributes) 
#print(soup.find_all("p", attrs={"class":"outer-text"}))
#<p id='first'>
# print(soup.find_all("p", id="first"))

#내부에 컨텐츠를 추출: .text속성 
for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n", "")
    print(title)

