from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QMainWindow, QTableWidget, QToolBar, QDialog

from PyQt6.QtCore import Qt 
from PyQt6.QtGui import QAction

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

        table_menu_item.addAction(Staff)
        table_menu_item.addAction(Services)
        table_menu_item.addAction(Transactions)

        Services.triggered.connect(self.show_services)
        Staff.triggered.connect(self.show_staff)
        Transactions.triggered.connect(self.show_Transaction)

        

        self.table = QTableWidget()
        self.table.setColumnCount(7)

        
        self.table.setHorizontalHeaderLabels(("PRODUCT_ID", "NAME", "CATEGORY", "SELLING PRICE", "COST PRICE", "QUANTITY", "DESCRIPTION"))

        self.setCentralWidget(self.table)

        

        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        add_products_action = QAction("Add Products", self)
        search_products_action = QAction("Search Products", self)
       

        toolbar.addAction(add_products_action)
        toolbar.addAction(search_products_action)
       

       

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
  



app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()
sys.exit(app.exec())