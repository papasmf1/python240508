import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

def search_naver_blog(search_keyword):
    # 엑셀 워크북 생성
    wb = Workbook()
    ws = wb.active
    ws.append(["페이지", "블로그명", "블로그글 제목", "날짜"])  # 헤더 추가

    for page in range(1, 101):  # 1페이지부터 100페이지까지 순회합니다.
        url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}&start={page * 10 - 9}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }  # User-Agent를 설정하여 봇으로 인식되지 않도록 합니다.

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # 블로그 정보를 담고 있는 태그를 찾습니다.
        blog_items = soup.find_all('li', class_='bx')

        for item in blog_items:
            # 블로그명 추출
            blog_name = item.find('a', class_='sub_txt').text.strip()
            # 블로그글의 제목 추출
            blog_title = item.find('a', class_='api_txt_lines total_tit').text.strip()
            # 날짜 추출
            date = item.find('span', class_='sub_time sub_txt').text.strip()

            # 엑셀에 데이터 추가
            ws.append([page, blog_name, blog_title, date])

    # 엑셀 파일 저장
    wb.save("c:/work3/result.xlsx")

search_keyword = input("검색할 키워드를 입력하세요: ")
search_naver_blog(search_keyword)
