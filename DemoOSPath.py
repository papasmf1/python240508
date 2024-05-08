# DemoOSPath.py 
import os 
import os.path 
import random

print(random.random())
print(random.random())
print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])
print("---샘플링---")
print(random.sample(range(20), 10))
print(random.sample(range(20), 10))
print(random.sample(range(1,46), 5))

fileName = r"c:\python310\python.exe"
print(os.path.abspath("python.exe"))
print(os.path.basename(fileName))

if os.path.exists(fileName):
    print("파일크기:", os.path.getsize(fileName))
else:
    print("파일 없음")

import glob 

print(glob.glob("c:\\work3\\*.py"))

