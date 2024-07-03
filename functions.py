from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QMainWindow, QTableWidget, QToolBar, QDialog, QTableWidgetItem, QPushButton, QMessageBox, QComboBox, QStatusBar, QHBoxLayout, QSizePolicy
import time 
 

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
import sqlite3
import sys 
from admin_login import LoginWindow 

class table_function:
    @staticmethod
    def show_products(main_window):
            
        main_window.add_products_action.setVisible(True)
        main_window.add_service_action.setVisible(False)
        main_window.add_staff_action.setVisible(False)
        main_window.pro_search_bar.setVisible(True)
        main_window.service_search_bar.setVisible(False)
        main_window.table = QTableWidget()
        main_window.table.verticalHeader().setVisible(False)
        main_window.table.setColumnCount(7)
        main_window.table.setHorizontalHeaderLabels(("PRODUCT_ID", "NAME", "CATEGORY", "SELLING_PRICE", "COST_PRICE", "QUANTITY", "DESCRIPTION"))
        main_window.setCentralWidget(main_window.table)
        main_window.load_data()

        main_window.table.cellClicked.connect(main_window.cell_clicked_pro)
        
    def show_services(self):
        self.statusbar.setVisible(True)
        self.add_products_action.setVisible(False)
        self.add_service_action.setVisible(True)
        self.service_search_bar.setVisible(True)
        self.pro_search_bar.setVisible(False)
        self.service_table = QTableWidget()
        self.service_table.verticalHeader().setVisible(False)
        self.service_table.setColumnCount(3)
        self.service_table.setHorizontalHeaderLabels(("ServiceID", "Name", "Price"))
        self.setCentralWidget(self.service_table)
        self.load_service_data()
        self.service_table.cellClicked.connect(self.cell_clicked_service)

    def show_staff(self): 
        self.pro_search_bar.setVisible(False)
        self.add_products_action.setVisible(False)
        self.add_service_action.setVisible(False)
        self.add_staff_action.setVisible(True)

        self.staff_table = QTableWidget()
        self.staff_table.setColumnCount(5)
        self.staff_table.verticalHeader().setVisible(False)
        self.staff_table.setHorizontalHeaderLabels(("StaffID", "Name", "Role", "ContactInfo", "Password"))
        self.load_staff_data()
        self.setCentralWidget(self.staff_table)
        self.staff_table.cellClicked.connect(self.cell_clicked_staff)

    def show_Transaction(self):
        self.pro_search_bar.setVisible(False)
        self.add_products_action.setVisible(False)
        self.Transaction_table = QTableWidget()
        self.Transaction_table.setColumnCount(9)
        self.Transaction_table.setHorizontalHeaderLabels(("TransactionID", "Type", "Date", "ProductID/ServiceID", "Quantity/Duration", "Price", "TotalAmount", "PaymentMethod", "StaffID",))
        
        self.setCentralWidget(self.Transaction_table)


