import openpyxl
import random

# 제품ID와 제품명 리스트
product_ids = [1001, 1002, 1003, 1004, 1005]
product_names = ["스마트폰", "노트북", "태블릿", "냉장고", "세탁기"]

# 엑셀 파일 경로
file_path = "c:\\work3\\products.xlsx"

# 빈 워크북 생성
wb = openpyxl.Workbook()

# 활성화된 시트 선택
sheet = wb.active

# 헤더 추가
sheet.append(["제품ID", "제품명", "수량", "가격"])

# 제품 데이터 생성 및 추가
for _ in range(100):
    product_id = random.choice(product_ids)
    product_name = random.choice(product_names)
    quantity = random.randint(1, 50)
    price = round(random.uniform(100, 1000), 2)
    sheet.append([product_id, product_name, quantity, price])

# 엑셀 파일 저장
wb.save(file_path)
