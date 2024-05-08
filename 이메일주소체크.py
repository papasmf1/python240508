import re

def check_email(email):
    # 정규표현식 패턴 설정
    pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
    # 주어진 이메일 주소가 패턴과 일치하는지 확인
    if re.match(pattern, email):
        return True
    else:
        return False

# 이메일 주소 검사할 샘플 생성
sample_emails = [
    "example@example.com",  # 유효한 이메일 주소
    "test.email@example.com",  # 유효한 이메일 주소
    "user@domain.com",  # 유효한 이메일 주소
    "user.name@domain.com",  # 유효한 이메일 주소
    "email123@example-domain.com",  # 유효한 이메일 주소
    "user@example.co.uk",  # 유효한 이메일 주소
    "email.address123@sub.domain.co.uk",  # 유효한 이메일 주소
    "name+tag@example.com",  # 유효한 이메일 주소
    "user@192.168.1.1",  # 유효한 이메일 주소
    "invalid_email@"  # 유효하지 않은 이메일 주소
]

# 생성한 샘플 이메일 주소 출력 및 체크
for email in sample_emails:
    # 각각의 이메일 주소를 검사하고 결과 출력
    if check_email(email):
        print(f"{email}: 유효한 이메일 주소")
    else:
        print(f"{email}: 유효하지 않은 이메일 주소")
