# function1.py

#함수 이름 해석 규칙(LGB)
#전역변수가 있는 경우 
x = 1 
def func(a):
    return a+x 

#호출
print(func(1))

#지역변수가 있는 경우
def func2(a):
    x = 5 
    return a+x 

#호출
print(func2(1))


#함수의 기본값
def times(a=10, b=20):
    return a*b 

#호출
print(times())
print(times(5))
print(times(5,6))

#키워드인자방식(디테일기술)
def connectURI(server, port):
    strURL = "https://" + server + ":" + port 
    return strURL 

#호출
print(connectURI("multi.com", "80"))
print(connectURI(port="80", server="naver.com"))


#가변인자 처리 
def union(*ar):
    #지역변수 저장(list)
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result 

#호출(중단점 추가)
print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))


#디버깅 
#교집합 리턴하는 함수 
def intersect(prelist, postlist):
    retList = []
    for x in prelist:
        if x in postlist and x not in retList:
            retList.append(x)
    return retList 


#호출
print( intersect("HAM", "SPAM") )

#람다 함수 
g = lambda x,y:x*y 
print( g(3,4) )
print( g(5,6) )
