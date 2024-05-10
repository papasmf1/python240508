import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import uic 
import sqlite3
import os.path 

# Data handler class for managing database operations
class DataHandler:
    def __init__(self):
        # Check if the database file exists
        if os.path.exists("ProductList.db"):
            self.con = sqlite3.connect("ProductList.db")
            self.cur = self.con.cursor()
        else: 
            self.con = sqlite3.connect("ProductList.db")
            self.cur = self.con.cursor()
            self.cur.execute(
                "create table Products (id integer primary key autoincrement, Name text, Price integer);")

    def addProduct(self, name, price):
        self.cur.execute("insert into Products (Name, Price) values(?,?);", (name, price))
        self.con.commit()

    def updateProduct(self, id, name, price):
        self.cur.execute("update Products set name=?, price=? where id=?;", (name, price, id))
        self.con.commit()

    def removeProduct(self, id):
        strSQL = "delete from Products where id=" + str(id)
        self.cur.execute(strSQL)
        self.con.commit()

    def getProducts(self):
        self.cur.execute("select * from Products;") 
        return self.cur.fetchall()

# UI class
class MainWindow(QMainWindow):
    def __init__(self, data_handler):
        super().__init__()
        self.data_handler = data_handler
        self.loadUi()
        self.setupUi()

    def loadUi(self):
        # Load the UI file
        uic.loadUi("ProductList3.ui", self)

    def setupUi(self):
        # Set up UI components
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setHorizontalHeaderLabels(["제품ID","제품명", "가격"])
        self.tableWidget.setTabKeyNavigation(False)
        self.prodID.returnPressed.connect(lambda: self.focusNextChild())
        self.prodName.returnPressed.connect(lambda: self.focusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.focusNextChild())
        self.tableWidget.doubleClicked.connect(self.doubleClick)
        self.getProduct()

    def addProduct(self):
        name = self.prodName.text()
        price = self.prodPrice.text()
        self.data_handler.addProduct(name, price)
        self.getProduct() 

    def updateProduct(self):
        id = self.prodID.text()
        name = self.prodName.text()
        price = self.prodPrice.text()
        self.data_handler.updateProduct(id, name, price)
        self.getProduct()  

    def removeProduct(self):
        id = self.prodID.text() 
        self.data_handler.removeProduct(id)
        self.getProduct()  

    def getProduct(self):
        self.tableWidget.clearContents()
        products = self.data_handler.getProducts()
        row = 0 
        for item in products: 
            int_as_strID = "{:10}".format(item[0])
            int_as_strPrice = "{:10}".format(item[2])
            itemID = QTableWidgetItem(int_as_strID) 
            itemID.setTextAlignment(Qt.AlignRight) 
            self.tableWidget.setItem(row, 0, itemID)
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))
            itemPrice = QTableWidgetItem(int_as_strPrice) 
            itemPrice.setTextAlignment(Qt.AlignRight) 
            self.tableWidget.setItem(row, 2, itemPrice)
            row += 1

    def doubleClick(self):
        self.prodID.setText(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
        self.prodName.setText(self.tableWidget.item(self.tableWidget.currentRow(), 1).text())
        self.prodPrice.setText(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())

# Create an instance of DataHandler
data_handler = DataHandler()

# Create an instance of QApplication
app = QApplication(sys.argv)

# Create an instance of MainWindow and pass the data handler instance
myWindow = MainWindow(data_handler)
myWindow.show()

# Execute the application
sys.exit(app.exec_())
