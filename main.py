from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QMainWindow, QTableWidget, QToolBar, QDialog, QTableWidgetItem, QPushButton

from PyQt6.QtCore import Qt 
from PyQt6.QtGui import QAction
import sqlite3
import sys 

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("TREASURE GOLD BEAUTY SALON")
        self.setMinimumSize(800, 600)

        table_menu_item = self.menuBar().addMenu("&Tables")
        help_menu_item = self.menuBar().addMenu("&Help")

        Services = QAction("Services", self)
        Staff = QAction("Staff", self)
        Transactions = QAction("Transaction", self)
        Products = QAction("Products", self )
        
        table_menu_item.addAction(Products)
        table_menu_item.addAction(Staff)
        table_menu_item.addAction(Services)
        table_menu_item.addAction(Transactions)
       

        Services.triggered.connect(self.show_services)
        Staff.triggered.connect(self.show_staff)
        Transactions.triggered.connect(self.show_Transaction)
        Products.triggered.connect(self.show_products)
        


        

       
        

        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        add_products_action = QAction("Add Products", self)
        search_products_action = QAction("Search Products", self)

        add_products_action.triggered.connect(self.add_prodocut)

        self.show_products()
        
        toolbar.addAction(add_products_action)
        toolbar.addAction(search_products_action)
    

    def show_products(self):
        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(("PRODUCT_ID", "NAME", "CATEGORY", "SELLING_PRICE", "COST_PRICE", "QUANTITY", "DESCRIPTION"))

        self.setCentralWidget(self.table)
        


    def load_data(self):
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM products")
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()
       

    def add_prodocut(self):
        dialog = AddProducts()
        dialog.exec()
       

    def show_services(self):
        self.service_table = QTableWidget()
        self.service_table.setColumnCount(7)
        self.service_table.setHorizontalHeaderLabels(("ServiceID", "Name", "Description", "Category", "Duration", "Price", "StaffIDs"))
        
        self.setCentralWidget(self.service_table)


    def show_staff(self):
        self.staff_table = QTableWidget()
        self.staff_table.setColumnCount(6)
        self.staff_table.setHorizontalHeaderLabels(("StaffID", "Name", "Role", "ContactInfo", "Shedule", "Skill"))
        
        self.setCentralWidget(self.staff_table)

    def show_Transaction(self):
        self.Transaction_table = QTableWidget()
        self.Transaction_table.setColumnCount(9)
        self.Transaction_table.setHorizontalHeaderLabels(("TransactionID", "Type", "Date", "ProductID/ServiceID", "Quantity/Duration", "Price", "TotalAmount", "PaymentMethod", "StaffID",))
        
        self.setCentralWidget(self.Transaction_table)

class AddProducts(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Products")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        self.pro_Name = QLineEdit()
        self.pro_Name.setPlaceholderText("Product_Name")
        layout.addWidget(self.pro_Name)

        self.pro_Cat = QLineEdit()
        self.pro_Cat.setPlaceholderText("Product_Category")
        layout.addWidget(self.pro_Cat)

        self.pro_Sp = QLineEdit()
        self.pro_Sp.setPlaceholderText("Selling Price")
        layout.addWidget(self.pro_Sp)

        self.pro_Cp = QLineEdit()
        self.pro_Cp.setPlaceholderText("Cost Price")
        layout.addWidget(self.pro_Cp)

        self.pro_Quantity = QLineEdit()
        self.pro_Quantity.setPlaceholderText("Quantity")
        layout.addWidget(self.pro_Quantity)

        self.pro_Dec = QLineEdit()
        self.pro_Dec.setPlaceholderText("Description")
        layout.addWidget(self.pro_Dec)

        button = QPushButton("Add")
        button.clicked.connect(self.insert_product)
        
        layout.addWidget(button)

        self.setLayout(layout)

    def insert_product(self):
        name = self.pro_Name.text()
        category = self.pro_Cat.text()
        selling_price = self.pro_Sp.text()
        cost_price = self.pro_Cp.text()
        quantity = self.pro_Quantity.text()
        description = self.pro_Dec.text()

        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO products (NAME, CATEGORY, SELLING_PRICE, COST_PRICE, QUANTITY, DESCRIPTION) VALUES (?, ?, ?, ?, ?, ?)", (name, category, selling_price, cost_price, quantity, description))

        connection.commit()
        cursor.close()
        connection.close()
        main_window.load_data()



app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()
main_window.load_data()
sys.exit(app.exec())