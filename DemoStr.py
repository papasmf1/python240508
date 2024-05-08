# DemoStr.py 

strA = "python is very powerful"
strB = "파이썬은단순해"

print(len(strA))
print(len(strB))
print(strA.capitalize())
print(strA.count("p"))
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isdecimal())
data = "<<<  spam and ham  >>>"
result = data.strip("<> ")
print(data)
print(result)
result2 = result.replace("spam", "spam egg")
print(result2)
print("---리스트로 변환---")
lst = result2.split()
print(lst)
print(":)".join(lst))

#정규표현식
import re 

result = re.search("[0-9]*th", "35th")
print(result)
print(result.group())
#연도
result = re.search("\d{4}", "올해는 2024년입니다.")
print(result.group())
#우편번호
#연도
result = re.search("\d{5}", "우리 동네는 52111")
print(result.group())
#단어
result = re.search("apple", "this is apple")
print(result.group())
