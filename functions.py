from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QMainWindow, QTableWidget, QToolBar, QDialog, QTableWidgetItem, QPushButton, QMessageBox, QComboBox, QStatusBar, QHBoxLayout, QSizePolicy, QHeaderView
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
        main_window.table.verticalHeader().setVisible(True)
        main_window.table.horizontalHeader().setMinimumHeight(70)
        main_window.table.setColumnCount(7)
        main_window.table.setColumnHidden(0, True)
        main_window.table.setColumnWidth(1, 190)
        main_window.table.setColumnWidth(2, 190)
        main_window.table.setColumnWidth(3, 190)
        main_window.table.setColumnWidth(4, 190)
        main_window.table.setColumnWidth(5, 190)
        main_window.table.setColumnWidth(6, 190)
        main_window.table.setStyleSheet("""
            QTableWidget {
                background-color: #fff;
                alternate-background-color: #f0f0f0; /* Alternate row background color */
                border: 1px solid #ccc;
                gridline-color: #ccc;
            }
            QTableWidget::item {
                padding: 5px;
                border-bottom: 1px solid #ccc;
            }
            QTableWidget::item:selected {
                background-color:#aaa; /* Selected item background color */
                color: black;  
                outline: none;                        
            }
            QHeaderView::section {
                background-color: #f0f0f0;  /* Background color for headers */
                padding: 4px;
                border: 1px solid #ccc;
                font-size: 14px;
            }
                                        
            QHeaderView::section:vertical {
                 background-color: #d0d0d0;  /* Different color for vertical headers if desired */
            }
            QHeaderView::section:hover {
                 background-color: #e0e0e0;  /* Hover effect */
            }
           
        """)
        
        main_window.table.setHorizontalHeaderLabels(("PRODUCT_ID", "NAME", "CATEGORY", "SELLING_PRICE", "COST_PRICE", "QUANTITY", "DESCRIPTION"))
        main_window.setCentralWidget(main_window.table)
        main_window.load_data()

        main_window.table.cellClicked.connect(main_window.cell_clicked_pro)

    
    def show_user_products(main_window):
        main_window.table = QTableWidget()
        main_window.table.verticalHeader().setVisible(False)
        main_window.table.setColumnCount(7)
        main_window.table.setStyleSheet("""
            QTableWidget {
                background-color: #fff;
                alternate-background-color: #f0f0f0; /* Alternate row background color */
                border: 1px solid #ccc;
                gridline-color: #ccc;
            }
            QTableWidget::item {
                padding: 5px;
                border-bottom: 1px solid #ccc;
            }
            QTableWidget::item:selected {
                background-color:#aaa; /* Selected item background color */
                color: black;  
                outline: none;                        
            }
            QHeaderView::section {
                background-color: #f0f0f0;  /* Background color for headers */
                padding: 4px;
                border: 1px solid #ccc;
                font-size: 14px;
            }
                                        
            QHeaderView::section:vertical {
                 background-color: #d0d0d0;  /* Different color for vertical headers if desired */
            }
            QHeaderView::section:hover {
                 background-color: #e0e0e0;  /* Hover effect */
            }
           
        """)
        main_window.table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        main_window.table.setColumnWidth(0, 190)
        main_window.table.setColumnWidth(1, 190)
        main_window.table.setColumnWidth(2, 190)
        main_window.table.setColumnWidth(3, 190)
        main_window.table.setColumnWidth(4, 190)
        main_window.table.setColumnWidth(5, 190)
        main_window.table.setColumnWidth(6, 190)
        main_window.table.setHorizontalHeaderLabels(("PRODUCT_ID", "NAME", "CATEGORY", "SELLING_PRICE", "COST_PRICE", "QUANTITY", "DESCRIPTION"))
        main_window.setCentralWidget(main_window.table)
        main_window.load_data()
        
    def show_services(self):
        self.statusbar.setVisible(True)
        self.add_products_action.setVisible(False)
        self.add_service_action.setVisible(True)
        self.service_search_bar.setVisible(True)
        self.pro_search_bar.setVisible(False)
        self.service_table = QTableWidget()
        self.service_table.verticalHeader().setVisible(True)
        self.service_table.horizontalHeader().setMinimumHeight(70)
        self.service_table.setColumnCount(3)
        self.service_table.setColumnHidden(0, True)
        self.service_table.setStyleSheet("""
            QTableWidget {
                background-color: #fff;
                alternate-background-color: #f0f0f0; /* Alternate row background color */
                border: 1px solid #ccc;
                gridline-color: #ccc;
            }
            QTableWidget::item {
                padding: 5px;
                border-bottom: 1px solid #ccc;
            }
            QTableWidget::item:selected {
                background-color:#aaa; /* Selected item background color */
                color: black;  
                outline: none;                        
            }
            QHeaderView::section {
                background-color: #f0f0f0;  /* Background color for headers */
                padding: 4px;
                border: 1px solid #ccc;
                font-size: 14px;
            }
                                        
            QHeaderView::section:vertical {
                 background-color: #d0d0d0;  /* Different color for vertical headers if desired */
            }
            QHeaderView::section:hover {
                 background-color: #e0e0e0;  /* Hover effect */
            }
           
        """)
        
        self.service_table.setHorizontalHeaderLabels(("ServiceID", "Name", "Price"))
        self.setCentralWidget(self.service_table)
        self.load_service_data()
       
        self.service_table.cellClicked.connect(self.cell_clicked_service)

    def show_user_services(self):
        self.service_table = QTableWidget()
        self.service_table.verticalHeader().setVisible(False)
        self.service_table.setColumnCount(3)
        self.service_table.setStyleSheet("""
            QTableWidget {
                background-color: #fff;
                alternate-background-color: #f0f0f0; /* Alternate row background color */
                border: 1px solid #ccc;
                gridline-color: #ccc;
            }
            QTableWidget::item {
                padding: 5px;
                border-bottom: 1px solid #ccc;
            }
            QTableWidget::item:selected {
                background-color:#aaa; /* Selected item background color */
                color: black;  
                outline: none;                        
            }
            QHeaderView::section {
                background-color: #f0f0f0;  /* Background color for headers */
                padding: 4px;
                border: 1px solid #ccc;
                font-size: 14px;
            }
                                        
            QHeaderView::section:vertical {
                 background-color: #d0d0d0;  /* Different color for vertical headers if desired */
            }
            QHeaderView::section:hover {
                 background-color: #e0e0e0;  /* Hover effect */
            }
           
        """)
        self.service_table.setHorizontalHeaderLabels(("ServiceID", "Name", "Price"))
        self.setCentralWidget(self.service_table)
        self.load_service_data()

    def show_user_transaction(self):
        self.Transaction_table = QTableWidget()
        self.Transaction_table.horizontalHeader().setMinimumHeight(70)
        self.Transaction_table.setStyleSheet("""
            QTableWidget {
                background-color: #fff;
                alternate-background-color: #f0f0f0; /* Alternate row background color */
                border: 1px solid #ccc;
                gridline-color: #ccc;
            }
            QTableWidget::item {
                padding: 5px;
                border-bottom: 1px solid #ccc;
            }
            QTableWidget::item:selected {
                background-color:#aaa; /* Selected item background color */
                color: black;  
                outline: none;                        
            }
            QHeaderView::section {
                background-color: #f0f0f0;  /* Background color for headers */
                padding: 4px;
                border: 1px solid #ccc;
                font-size: 14px;
            }
                                        
            QHeaderView::section:vertical {
                 background-color: #d0d0d0;  /* Different color for vertical headers if desired */
            }
            QHeaderView::section:hover {
                 background-color: #e0e0e0;  /* Hover effect */
            }
           
        """)

        self.Transaction_table.setColumnCount(6)
        self.Transaction_table.setHorizontalHeaderLabels(("NAME", "PRICE", "Quantity", "Payment_Method", "STAFF_NAME", "Date",))
        self.setCentralWidget(self.Transaction_table)
        self.load_transaction()

    def show_staff(self): 
        self.pro_search_bar.setVisible(False)
        self.add_products_action.setVisible(False)
        self.add_service_action.setVisible(False)
        self.service_search_bar.setVisible(False)
        self.add_staff_action.setVisible(True)
        self.staff_table = QTableWidget()
        self.staff_table.horizontalHeader().setMinimumHeight(70)

        self.staff_table.setColumnCount(5)
        self.staff_table.setColumnHidden(0, True)
        self.staff_table.verticalHeader().setVisible(True)
        self.staff_table.setStyleSheet("""
            QTableWidget {
                background-color: #fff;
                alternate-background-color: #f0f0f0; /* Alternate row background color */
                border: 1px solid #ccc;
                gridline-color: #ccc;
            }
            QTableWidget::item {
                padding: 5px;
                border-bottom: 1px solid #ccc;
            }
            QTableWidget::item:selected {
                background-color:#aaa; /* Selected item background color */
                color: black;  
                outline: none;                        
            }
            QHeaderView::section {
                background-color: #f0f0f0;  /* Background color for headers */
                padding: 4px;
                border: 1px solid #ccc;
                font-size: 14px;
            }
                                        
            QHeaderView::section:vertical {
                 background-color: #d0d0d0;  /* Different color for vertical headers if desired */
            }
            QHeaderView::section:hover {
                 background-color: #e0e0e0;  /* Hover effect */
            }
           
        """)
        self.staff_table.setHorizontalHeaderLabels(("StaffID", "Name", "Role", "ContactInfo", "Password"))
        self.load_staff_data()
        self.setCentralWidget(self.staff_table)
        self.staff_table.cellClicked.connect(self.cell_clicked_staff)

    def show_Transaction(self):
        self.pro_search_bar.setVisible(False)
        self.add_products_action.setVisible(False)
        self.Transaction_table = QTableWidget()
        self.Transaction_table.setColumnCount(8)
        self.Transaction_table.horizontalHeader().setMinimumHeight(70)
        self.statusbar.setVisible(False)
        self.Transaction_table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.Transaction_table.setColumnWidth(0, 170)
        self.Transaction_table.setColumnWidth(1, 170)
        self.Transaction_table.setColumnWidth(2, 170)
        self.Transaction_table.setColumnWidth(3, 175)
        self.Transaction_table.setColumnWidth(4, 170)
        self.Transaction_table.setColumnWidth(5, 170)
        self.Transaction_table.setColumnWidth(6, 170)
        self.Transaction_table.setStyleSheet("""
            QTableWidget {
                background-color: #fff;
                alternate-background-color: #f0f0f0; /* Alternate row background color */
                border: 1px solid #ccc;
                gridline-color: #ccc;
            }
            QTableWidget::item {
                padding: 5px;
                border-bottom: 1px solid #ccc;
            }
            QTableWidget::item:selected {
                background-color:#aaa; /* Selected item background color */
                color: black;  
                outline: none;                        
            }
            QHeaderView::section {
                background-color: #f0f0f0;  /* Background color for headers */
                padding: 4px;
                border: 1px solid #ccc;
                font-size: 14px;
            }
                                        
            QHeaderView::section:vertical {
                 background-color: #d0d0d0;  /* Different color for vertical headers if desired */
            }
            QHeaderView::section:hover {
                 background-color: #e0e0e0;  /* Hover effect */
            }
           
        """)
        self.Transaction_table.setHorizontalHeaderLabels(("Category", "Name", "Price", "Quantity",  "PaymentMethod", "Staff Name", "Date", "Note"))
        self.load_transactionsAdmin()
        
        self.setCentralWidget(self.Transaction_table)


    def handle_runtime_error(self, error):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText("Runtime Error select an item")
            msg.setInformativeText(str(error))
            msg.setWindowTitle("Error")
            msg.exec()
