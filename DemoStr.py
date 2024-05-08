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


