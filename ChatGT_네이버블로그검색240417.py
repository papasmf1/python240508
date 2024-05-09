import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

search_keyword='맥북에어'

url = f'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}'

response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')

# create a new Excel workbook and select the active sheet\
wb = Workbook()
ws = wb.active

# write the column names to the first row of the sheet
ws.append(["블로그명", "블로그주소", "글 제목", "포스팅 날짜"])

for page in range(1, 100):
    url = f'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}&start={page * 10 - 9}'

   
# <div class="fds-ugc-block-mod-list swvwrquoALMoh11A2Inw"><div class="fds-ugc-block-mod swvwrquoALMoh11A2Inw"><div class="_keep_wrap fds-article-simple-box swvwrquoALMoh11A2Inw"><div 
#<a nocr="1" href="https://blog.naver.com/gywnstjswkd/223429700587" class="WA5NokotVTFlsTmcyqjA fds-comps-right-image-text-title" target="_blank" data-cb-target="'SYS-0000000035525141.90000003_00000000000000340572ABEB'" data-cb-trigger="true"><span class="yzABCkcX2xTtNICntyz1"><mark>맥북에어</mark> m2 실버 스펙 장점 감면 받는법</span></a>
    posts = soup.find_all('div', {'class':'fds-ugc-block-mod-list swvwrquoALMoh11A2Inw'})
    for post in posts:
        try:

            blog_address_elem = post.find("a", 
                attrs={"class":"WA5NokotVTFlsTmcyqjA fds-comps-right-image-text-title"}) 
            blog_address = blog_address_elem["href"]
            blog_address_title_elem = post.find("span", attrs={"class":"yzABCkcX2xTtNICntyz1"})
            blog_address_title = blog_address_title_elem.text 
        except TypeError:
            blog_address = "" 
            blog_address_title = ""
        
        #<span class="fds-info-sub-inner-text yzABCkcX2xTtNICntyz1">2주 전</span>
        post_date_elem = post.find('span', {'class':'fds-info-sub-inner-text yzABCkcX2xTtNICntyz1'})
        post_date = post_date_elem.text if post_date_elem else ""
        post_title_elem = post.find("a", attrs={"class":"WA5NokotVTFlsTmcyqjA fds-comps-right-image-text-title"})
        post_title = post_title_elem.text if post_title_elem else "" 

        print(blog_address)
        print(blog_address_title)
        print(post_title)
        print(post_date)

        ws.append([blog_address_title, blog_address, post_title, post_date])

#path = 'c:\\work\\'
#file_path = f'{path}{search_keyword}_blog_data.xlsx'
file_path = f'{search_keyword}_blog_data.xlsx'
wb.save(file_path)