# DemoForm2.py 
# DemoForm2.ui(화면단) + DemoForm2.py(로직단)
import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic 

#디자인 파일 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]

#폼클래스 정의(QMainWindow)
class DemoForm(QMainWindow, form_class):
    #초기화 메서드
    def __init__(self):
        super().__init__() 
        self.setupUi(self)
    #슬롯메서드
    def firstClick(self):
        self.label.setText("첫번째 버튼을 클릭")
    def secondClick(self):
        self.label.setText("두번째 버튼을 클릭~~")
    def thirdClick(self):
        self.label.setText("세번째 버튼을 클릭")

#진입점체크(모듈을 직접 실행했는지 체크)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm() 
    demoForm.show() 
    app.exec_() 