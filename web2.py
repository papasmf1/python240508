# web2.py 
#당근마켓 크롤링
#웹서버에 요청
import requests
from bs4 import BeautifulSoup

url = "https://www.daangn.com/fleamarket/" 
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

#파일에 저장
f = open("danggn.txt", "wt", encoding="utf-8")
posts = soup.find_all("div", attrs={"class":"card-desc"})
for post in posts:
    titleElem = post.find("h2", attrs={"class":"card-title"})
    priceElem = post.find("div", attrs={"class":"card-price"})
    addrElem = post.find("div", attrs={"class":"card-region-name"})
    title = titleElem.text.strip() 
    price = priceElem.text.strip()
    addr = addrElem.text.strip()
    #파이썬 3.6부터는 f-string사용 가능 
    print(f"{title}, {price}, {addr}")
    f.write(f"{title}, {price}, {addr}\n")

f.close() 

#  <div class="card-desc">
#       <h2 class="card-title">에어팟 프로1 팔.아요</h2>
#       <div class="card-price ">
#         110,000원
#       </div>
#       <div class="card-region-name">
#         경남 김