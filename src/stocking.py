import os
import sys
import _sqlite3
from datetime import date
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

ui, _ = loadUiType('assets/ui/stocking.ui')
db_path = os.path.join('database/', 'stocking.db')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.tabWidget.setCurrentIndex(0)
        self.login_button.clicked.connect(self.login)
        
        self.logout_1.clicked.connect(self.logout)
        self.logout_2.clicked.connect(self.logout)
        self.logout_3.clicked.connect(self.logout)
        
        self.order_entry_1.clicked.connect(self.showOrderEntry)
        self.order_entry_2.clicked.connect(self.showOrderEntry)
        self.order_entry_3.clicked.connect(self.showOrderEntry)
        
        self.edit_orders_1.clicked.connect(self.showEditOrders)
        self.edit_orders_2.clicked.connect(self.showEditOrders)
        self.edit_orders_3.clicked.connect(self.showEditOrders)
        
        self.orders_1.clicked.connect(self.showOrders)
        self.orders_2.clicked.connect(self.showOrders)
        self.orders_3.clicked.connect(self.showOrders)
        
    try:
        db_chk = _sqlite3.connect(db_path)
        db_chk.execute("CREATE TABLE IF NOT EXISTS orders(order_id INTEGER, cx_name TEXT, cx_phno TEXT, product_id INTEGRER, quantity INTEGER, order_date TEXT, order_time TEXT)")
        db_chk.commit()
        print("Created database sucessfully :)\n")
    except:
        print(db_chk.Error)
        
    def login(self):
        usr_pwd = self.login_input.text()
        if usr_pwd == "sagayam":
            self.login_info.setText("")
            self.login_input.setText("")
            self.tabWidget.setCurrentIndex(1)
        else:
            self.login_info.setText("Wrong Password!")
        
    def logout(self):
        self.tabWidget.setCurrentIndex(0)
        
    def showOrderEntry(self):
        self.tabWidget.setCurrentIndex(1)
        
    def showEditOrders(self):
        self.tabWidget.setCurrentIndex(2)
        
    def showOrders(self):
        self.tabWidget.setCurrentIndex(3)


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
