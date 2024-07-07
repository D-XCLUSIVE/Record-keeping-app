from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QMainWindow, QTableWidget, QToolBar, QDialog, QTableWidgetItem, QPushButton, QMessageBox, QComboBox, QStatusBar, QHBoxLayout, QSizePolicy
from PyQt6.QtCore import pyqtSlot
import sqlite3
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt
import sys
from main import MainWindow as mw
from functions import table_function
from datetime import datetime
from stafflogin import staffLoginWindow

class DatabaseConnection:
    def __init__(self, database_file="database.db"):
        self.database_file = database_file
    
    def connect(self):
        connections = sqlite3.connect(self.database_file)
        return connections

class UserWindow(QMainWindow):
    def __init__(main_window):
        super().__init__()
        main_window.setWindowTitle("Staff Page")
        main_window.setMinimumSize(800, 600)

        toolbar = QToolBar()
        toolbar.setMovable(False)
        main_window.addToolBar(toolbar)

        main_window.showstaffname = QLabel()
        main_window.services_action = QAction("Service", main_window)
        main_window.products_action = QAction("Products", main_window)
        main_window.transactions_action = QAction("Transactions", main_window)
        toolbar.addAction(main_window.services_action)
        toolbar.addAction(main_window.products_action)
        toolbar.addAction(main_window.transactions_action)

        main_window.services_action.triggered.connect(main_window.show_services)
        main_window.products_action.triggered.connect(main_window.show_products)
        main_window.transactions_action.triggered.connect(main_window.show_transactions)

        
        main_window.statusbar = QStatusBar()
        main_window.setStatusBar(main_window.statusbar)
        sales_button = QPushButton("Make Sales")
        sales_button.clicked.connect(main_window.make_sales)

        services_button = QPushButton("Render Service")
        services_button .clicked.connect(main_window.render_services)
        main_window.statusbar.addWidget(sales_button)
        main_window.statusbar.addWidget(services_button)

        main_window.username_label = QLabel()  # Label to display the username
        main_window.statusbar.addPermanentWidget(main_window.username_label)

        main_window.show_services()
    
    

    def set_username(self, username):
        self.username_label.setText(f"Welcome: {username}")
   
    def show_services(main_window):
        table_function.show_user_services(main_window)
    
    def show_products(main_window):
        table_function.show_user_products(main_window)

    def show_transactions(main_window):
        table_function.show_user_transaction(main_window)

    def load_service_data(main_window):
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM services")
        main_window.service_table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            main_window.service_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                main_window.service_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()

    def load_transaction(main_window):
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT NAME, SELLING_PRICE, QUANTITY, PAYMENT_METHOD, STAFF_NAME, DATE FROM transactions")
        main_window.Transaction_table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            main_window.Transaction_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                main_window.Transaction_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()

    def load_data(self):
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM products")
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()

    def make_sales(main_window):
        dialog = makesales()
        dialog.exec()
    
    def render_services(main_window):
        dialog = renderservice()
        dialog.exec()

class makesales(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sales")
        self.setFixedHeight(500)
        self.setFixedWidth(350)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setSpacing(10)
        self.setLayout(layout)
        name_label = QLabel("PRODUCT NAME:")
        price_label = QLabel("PRODUCT PRICE:")
        grade_label = QLabel("PRODUCT GRADE:")
        method_label = QLabel("PAYEMENT METHOD")
        self.product_name = QComboBox()
        self.product_name.currentIndexChanged.connect(self.update_price)
        self.product_price = QComboBox() 
        self.product_price.currentIndexChanged.connect(self.update_cat)
        self.product_cat = QComboBox()
        self.product_cat.currentIndexChanged.connect(self.select_id)
        self.numberof_pro = QLineEdit()
        self.numberof_pro.setFixedHeight(20)
        self.numberof_pro.setFixedWidth(70)
        self.numberof_pro.setPlaceholderText("N0 of products")
        self.payment_method = QComboBox()
        method = ["CASH", "TRANSFER", "POS"]
        self.payment_method.addItems(method)
        self.staff_name = QLineEdit()
        self.staff_name.setPlaceholderText("staff id")
        self.staff_name.setFixedHeight(20)
        self.staff_name.setFixedWidth(40)
        self.note = QLineEdit()
        self.note.setFixedHeight(30)
        self.note.setFixedWidth(200)
        self.note.setPlaceholderText("If any discount discribe")
        self.pro_id = QLabel()

        self.product_quan = QLabel("Quantity Left: N/A")
        button = QPushButton("POST")
        button.clicked.connect(self.add_transaction)
        

        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("SELECT NAME FROM products")
        for name in cursor.fetchall():
            self.product_name.addItem(name[0])

        
            
        
        layout.addWidget(name_label)
        layout.addWidget(self.product_name)
        layout.addWidget(price_label)
        layout.addWidget(self.product_price)
        layout.addWidget(grade_label)
        layout.addWidget(self.product_cat)
        layout.addWidget(self.numberof_pro)
        layout.addWidget(method_label)
        layout.addWidget(self.payment_method)
        layout.addWidget(self.staff_name)
        layout.addWidget(self.note)
        layout.addWidget(self.product_quan)
        layout.addWidget(self.pro_id)
        layout.addWidget(button)

        layout.addStretch(1)

        self.update_price()
        self.update_cat()
        self.select_id()

    @pyqtSlot()
    def update_price(self):
        product_name = self.product_name.currentText()

        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("SELECT SELLING_PRICE FROM products WHERE NAME = ?", (product_name,))
        prices = cursor.fetchall()

        self.product_price.clear()
        for price in prices:
            self.product_price.addItem(str(price[0]))

        self.pro_quantity() # Update the quantity whenever the price is updated

    


    def update_cat(self):
        product_name = self.product_name.currentText()
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("SELECT CATEGORY FROM products WHERE NAME = ?", (product_name,))
        cats = cursor.fetchall()

        self.product_cat.clear()
        for cat in cats:
            self.product_cat.addItem(str(cat[0]))

        self.select_id()
    
    def select_id(self):
        product_name = self.product_name.currentText()

        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("SELECT PRODUCT_ID FROM products WHERE NAME = ?", (product_name,))
        IDS = cursor.fetchall()

        # self.product_price.clear()
        for ID in IDS:
            self.pro_id.setText(str(ID[0]))

    def pro_quantity(self):
        product_name = self.product_name.currentText()
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("SELECT QUANTITY FROM products WHERE NAME = ?", (product_name,))
        self.quantity = cursor.fetchone()

        if self.quantity:
            self.product_quan.setText(f"Quantity Left: {self.quantity[0]}")
        else:
 
            self.product_quan.setText("Quantity Left: N/A")

    def number(self):
        for a in self.pro_quantity():
            print(a)

    def add_transaction(self):
        dialog = makeorder( self.product_name.currentText(), self.product_price.currentText(), self.product_cat.currentText(), self.payment_method.currentText(), self.numberof_pro.text(), self.staff_name.text(), self.note.text(), self.pro_id.text(), 
        self.quantity)
        dialog.exec()
class makeorder(QDialog):
    def __init__(self, product_name, product_price, product_cat, product_method, numberof_product, staff_name, note, pro_id, product_quan ):
        super().__init__()
        self.setWindowTitle("Confirm Order")
        self.setFixedWidth(250)
        self.setFixedHeight(150)

        layout = QGridLayout()
        confirmation =QLabel("Are you sure you want to make order?")
        yes = QPushButton("Yes")
        no = QPushButton("No")

        self.product_name = product_name
        self.product_price = product_price
        self.product_cat = product_cat
        self.product_method = product_method
        self.numberof_pro = numberof_product
        self.note = note
        self.staff_name = staff_name
        self.pro_id = pro_id
        self.product_quan = product_quan

        layout.addWidget(confirmation, 0, 0, 1, 2)
        layout.addWidget(yes, 1, 0)
        layout.addWidget(no, 1, 1)

        yes.clicked.connect(self.add_transaction)

        self.setLayout(layout)

    def add_transaction(self):
       date = datetime.now()
       date = str(date)

       quantity_left = int(self.product_quan[0])
       number_of_products = int(self.numberof_pro)
        
       new_quantity = quantity_left - number_of_products
       

       connection = DatabaseConnection().connect()
       cursor = connection.cursor()
       if cursor.execute("INSERT  INTO transactions (PRODUCT_ID, NAME, PRO_CAT, SELLING_PRICE, QUANTITY, PAYMENT_METHOD, STAFF_NAME, DATE, NOTE) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (self.pro_id, self.product_name, self.product_cat, self.product_price, self.numberof_pro,  self.product_method, self.staff_name, date, self.note, )):
           cursor.execute("UPDATE products SET QUANTITY = ? WHERE PRODUCT_ID = ?", (new_quantity, self.pro_id))

       

           connection.commit()
           cursor.close()
           connection.close()
           self.accept()  


    
        
       

    
      

class renderservice(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sales")
        self.setFixedHeight(350)
        self.setFixedWidth(300)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setSpacing(10)
        self.setLayout(layout)
        name_label = QLabel("SERVICE NAME:")
        price_label = QLabel("SERVICE PRICE:")
        grade_label = QLabel("SERVICE GRADE:")
        method_label = QLabel("PAYEMENT METHOD")
        self.service_name = QComboBox()
        self.service_name.currentIndexChanged.connect(self.update_serprice)
        self.service_price = QComboBox() 
        self.payment_method = QComboBox()
        method = ["CASH", "TRANSFER", "POS"]
        self.payment_method.addItems(method)
        self.staff_id = QLineEdit()
        self.staff_id.setPlaceholderText("staff_id")
        self.staff_id.setFixedHeight(20)
        self.staff_id.setFixedWidth(40)
        self.note = QLineEdit()
        self.note.setFixedHeight(30)
        self.note.setFixedWidth(200)
        self.note.setPlaceholderText("If any discount discribe")
        self.service_id = QLabel()
        button = QPushButton("POST")
        button.clicked.connect(self.add_servicetransaction)
        

        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("SELECT NAME FROM services")
        for name in cursor.fetchall():
            self.service_name.addItem(name[0])
            
        
        layout.addWidget(name_label)
        layout.addWidget(self.service_name)
        layout.addWidget(price_label)
        layout.addWidget(self.service_price)
        layout.addWidget(method_label)
        layout.addWidget(self.payment_method)
        layout.addWidget(self.staff_id)
        layout.addWidget(self.note)
        layout.addWidget(self.service_id)
        layout.addWidget(button)


        self.update_serprice()
        self.select_id()
        self.accept()

    @pyqtSlot()
    def update_serprice(self):
        service_name = self.service_name.currentText()
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("SELECT PRICE FROM services WHERE NAME = ?", (service_name,))
        prices = cursor.fetchall()

        self.service_price.clear()
        for price in prices:
            self.service_price.addItem(str(price[0]))

        
    
    
    def select_id(self):
        service_name = self.service_name.currentText()

        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("SELECT SERVICE_ID FROM services WHERE NAME = ?", (service_name,))
        IDS = cursor.fetchall()

        # self.service_price.clear()
        for ID in IDS:
            self.service_id.setText(str(ID[0]))

    def add_servicetransaction(self):
        dialog = makeservice( self.service_name.currentText(), self.service_price.currentText(), self.payment_method.currentText(), self.staff_id.text(), self.note.text(), self.service_id.text() )
        dialog.exec()
class makeservice(QDialog):
    def __init__(self, service_name, product_price, payment_method, staff_id, note, service_id ):
        super().__init__()
        self.setWindowTitle("Confirm Order")
        self.setFixedWidth(250)
        self.setFixedHeight(150)

        layout = QGridLayout()
        confirmation =QLabel("Are you sure you want to make order?")
        yes = QPushButton("Yes")
        no = QPushButton("No")

        self.service_name = service_name
        self.service_price = product_price
        self.payment_method = payment_method
        self.note = note
        self.staff_id = staff_id
        self.service_id = service_id

        layout.addWidget(confirmation, 0, 0, 1, 2)
        layout.addWidget(yes, 1, 0)
        layout.addWidget(no, 1, 1)

        yes.clicked.connect(self.add_transaction)

        self.setLayout(layout)

    def add_transaction(self):
       date = datetime.now()
       date = str(date)

       connection = DatabaseConnection().connect()
       cursor = connection.cursor()

       cursor.execute("INSERT  INTO transactions (SERVICE_ID, NAME,  SELLING_PRICE, PAYMENT_METHOD, STAFF_ID, DATE, NOTE) VALUES (?, ?, ?, ?, ?, ?, ?)", (self.service_id, self.service_name,self.service_price, self.payment_method, self.staff_id, date, self.note, ))

       connection.commit()
       cursor.close()
       connection.close()

    
       print(f"{self.service_name}")
       self.accept()  


if __name__ == '__main__':
    app = QApplication(sys.argv)
    user_window = UserWindow()
    login_window = staffLoginWindow()
    login_window.set_usermain_window(user_window)
    
    
    login_window.show()

    sys.exit(app.exec())