# DemoFile.py 

#파일쓰기(유니코드 utf-8)
f = open("demo.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close() 

#파일읽기 
f = open("demo.txt", "rt", encoding="utf-8")
result = f.read()
print(result)
print("---readline()메서드---")
f.seek(0)
print( f.readline(), end="" )
print( f.readline(), end="" )
print("---readlines()메서드---")
f.seek(0)
result = f.readlines()
print(result)

f.close() 