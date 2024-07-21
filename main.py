from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QMainWindow, QTableWidget, QToolBar, QDialog, QTableWidgetItem, QPushButton, QMessageBox, QComboBox, QStatusBar, QHBoxLayout, QSizePolicy, QGraphicsOpacityEffect
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve
import time 
from PyQt6.QtGui import QFont
 

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
import sqlite3
import sys 
from admin_login import LoginWindow
from stafflogin import staffLoginWindow
from user import UserWindow
from styles.stylesheets import apply_animation, apply_styles, apply_animationon, apply_styleson, apply_animationOndelete, apply_stylesonOndelete
from functions import table_function
class DatabaseConnection:
    def __init__(self, database_file="database.db"):
        self.database_file = database_file
    
    def connect(self):
        connections = sqlite3.connect(self.database_file)
        return connections

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
        table_menu_item.addAction(Services)
        table_menu_item.addAction(Staff)
        table_menu_item.addAction(Transactions)
       

        Services.triggered.connect(self.show_services)
        Staff.triggered.connect(self.show_staff)
        Transactions.triggered.connect(self.show_Transaction)
        Products.triggered.connect(self.show_products)
        

        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        self.add_products_action = QAction("Add Products", self)
        self.add_service_action = QAction("Add Services", self)
        self.add_staff_action = QAction("Add Staff", self)
        toolbar.addAction(self.add_products_action)
        toolbar.addAction(self.add_service_action)
        toolbar.addAction(self.add_staff_action )
           
        
        self.service_search_bar = self.service_search_bar()
        self.pro_search_bar = self.pro_search_bar()
        self.show_products()

        self.add_products_action.triggered.connect(self.add_product)
        self.add_service_action.triggered.connect(self.add_service)
        self.add_staff_action.triggered.connect(self.add_staff)

        apply_styleson(self)
        apply_animationon(self)

        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

        self.table.cellClicked.connect(self.cell_clicked_pro)
    
        # self.setStyleSheet("""
        #     /* Menu and toolbar styles */
        #     QMenuBar {
        #         background-color: #333;
        #         color: white;
        #     }
        #     QMenuBar::item {
        #         background-color: #333;
        #         padding: 4px 10px;
        #     }
        #     QMenuBar::item:selected {
        #         background-color: #555;
        #     }
        #     QMenu {
        #         background-color: #333;
        #         border: 1px solid #555;
        #         padding: 5px;
        #     }
        #     QMenu::item {
        #         background-color: transparent;
        #         color: white;
        #         padding: 5px 20px;
        #     }
        #     QMenu::item:selected {
        #         background-color: #555;
        #     }
        #     QToolBar {
        #         background-color: #666;
        #         border: none;
        #     }
        #     QToolBar::handle {
        #         background-color: #888;
        #     }
        #     QToolBar QToolButton {
        #         background-color: #888;
        #         border: none;
        #         padding: 5px;
        #     }
        #     QToolBar QToolButton:hover {
        #         background-color: #aaa;
        #     }
        # """)


    def show_products(self):
        table_function.show_products(self)
    
    def pro_search_bar(self):
        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        self.Pro_search_input = QLineEdit()
        self.Pro_search_input.setPlaceholderText("Search for a product...")
        self.Pro_search_input.setMinimumWidth(400)
        self.Pro_search_input.setStyleSheet("""
            QLineEdit {
                background-color: #fff; /* White background */
                padding: 5px; /* Padding for input */
                border: 1px solid #ccc; /* Remove border */
                border-radius: 3px; /* Rounded corners */
            }
            QLineEdit:focus {
                border: 1px solid #aaa; /* Border color on focus */
            }
        """)
        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search_product)
        search_button.setMinimumWidth(100)
        search_button.setStyleSheet("""
            QPushButton {
                background-color: #888;
                color: white;
                border: none;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #aaa;
            }
        """)
        search_widget = QWidget()
        search_layout = QHBoxLayout(search_widget)

        search_layout.addWidget(self.Pro_search_input)
        search_layout.addWidget(search_button)
        
        toolbar.addWidget(search_widget)


        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

        return toolbar

    def service_search_bar(self):
        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        self.Service_search_input = QLineEdit()
        self.Service_search_input.setPlaceholderText("Search for a services...")
        self.Service_search_input.setStyleSheet("""
            QLineEdit {
                background-color: #fff; /* White background */
                padding: 5px; /* Padding for input */
                border: 1px solid #ccc; /* Remove border */
                border-radius: 3px; /* Rounded corners */
            }
            QLineEdit:focus {
                border: 1px solid #aaa; /* Border color on focus */
            }
        """)
        self.Service_search_input.setMinimumWidth(400)
        search_button = QPushButton("Search_Services")
        search_button.clicked.connect(self.search_service)
        search_button.setMinimumWidth(100)
        search_button.setStyleSheet("""
            QPushButton {
                background-color: #888;
                color: white;
                border: none;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #aaa;
            }
        """)
        search_widget = QWidget()
        search_layout = QHBoxLayout(search_widget)

        search_layout.addWidget(self.Service_search_input)
        search_layout.addWidget(search_button)
        
        toolbar.addWidget(search_widget)

        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

        return toolbar
    
    def search_service(self):
        search_text = self.Service_search_input.text()
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        query = "SELECT * FROM services WHERE NAME LIKE ? OR PRICE LIKE ?"
        params = ('%' + search_text + '%', '%' + search_text + '%')
        result = connection.execute(query, params)
        records = result.fetchall()
        self.service_table.setRowCount(0)
        for row_number, row_data in enumerate(records):
            self.service_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.service_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        cursor.close()
        connection.close()

    def cell_clicked_pro(self):
        edit_button = QPushButton("Edith Record")
        edit_button.clicked.connect(self.edit)
        edit_button.setStyleSheet("""
        QPushButton {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 8px 16px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 14px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 5px;
            transition-duration: 0.4s;
            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        }
        QPushButton:hover {
            background-color: #45a049;
            color: white;
        }
    """)

        delete_button = QPushButton("Delete Record")
        delete_button.clicked.connect(self.delete_pro)
        delete_button.setStyleSheet("""
        QPushButton {
            background-color: #f44336;
            color: white;
            border: none;
            padding: 8px 16px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 14px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 5px;
            transition-duration: 0.4s;
            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        }
        QPushButton:hover {
            background-color: #e53935;
            color: white;
        }
    """)

        children = self.findChildren(QPushButton)
        if children:
            for child in children:
                self.statusbar.removeWidget(child)

        self.statusbar.addWidget(edit_button)
        self.statusbar.addWidget(delete_button)

    def cell_clicked_service(self):
        edit_button = QPushButton("Edith Service")
        edit_button.setStyleSheet("""
        QPushButton {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 8px 16px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 14px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 5px;
            transition-duration: 0.4s;
            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        }
        QPushButton:hover {
            background-color: #45a049;
            color: white;
        }
    """)
        edit_button.clicked.connect(self.edit_service)

        delete_button = QPushButton("Delete Service")
        delete_button = QPushButton("Delete Record")
        delete_button.setStyleSheet("""
        QPushButton {
            background-color: #f44336;
            color: white;
            border: none;
            padding: 8px 16px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 14px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 5px;
            transition-duration: 0.4s;
            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        }
        QPushButton:hover {
            background-color: #e53935;
            color: white;
        }
    """)

        delete_button.clicked.connect(self.delete_service)


        children = self.findChildren(QPushButton)
        if children:
            for child in children:
                self.statusbar.removeWidget(child)

        self.statusbar.addWidget(edit_button)
        self.statusbar.addWidget(delete_button)
        
    def cell_clicked_staff(self):
        edit_button = QPushButton("Edith Staff details")
        edit_button.clicked.connect(self.edit_staff)
        edit_button.setStyleSheet("""
        QPushButton {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 8px 16px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 14px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 5px;
            transition-duration: 0.4s;
            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        }
        QPushButton:hover {
            background-color: #45a049;
            color: white;
        }
    """)
        delete_button = QPushButton("Delete staff")
        delete_button.setStyleSheet("""
        QPushButton {
            background-color: #f44336;
            color: white;
            border: none;
            padding: 8px 16px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 14px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 5px;
            transition-duration: 0.4s;
            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        }
        QPushButton:hover {
            background-color: #e53935;
            color: white;
        }
    """)
        delete_button.clicked.connect(self.delete_staff)


        children = self.findChildren(QPushButton)
        if children:
            for child in children:
                self.statusbar.removeWidget(child)

        self.statusbar.addWidget(edit_button)
        self.statusbar.addWidget(delete_button)


    def load_data(self):
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM products")
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()

    def load_service_data(self):
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM services")
        self.service_table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.service_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.service_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()
    
    def load_staff_data(self):
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM staff")
        self.staff_table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.staff_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.staff_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()

    def load_transactionsAdmin(self):
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT PRO_CAT, NAME, SELLING_PRICE, QUANTITY, PAYMENT_METHOD, STAFF_NAME, DATE, NOTE  FROM transactions")
        self.Transaction_table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.Transaction_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.Transaction_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()

    def show_services(self):
       table_function.show_services(self)
             
    def show_staff(self):
        table_function.show_staff(self)

    def show_Transaction(self):
       table_function.show_Transaction(self)

    def edit(self):
        dialog = EditDialog()
        dialog.exec()

    def edit_service(self):
        dialog = EditService()
        dialog.exec()
    
    def edit_staff(self):
        dialog = EditStaff()
        dialog.exec() 

    def delete_pro(self):
        dialog = DeleteDialog()
        dialog.exec()
    
    def delete_service(self):
        dialog = DeleteService()
        dialog.exec()

    def delete_staff(self):
        dialog = Deletestaff()
        dialog.exec()

    def add_product(self):
        dialog = AddProducts()
        dialog.exec()
  
    def add_service(self):
        dialog = AddServices()
        dialog.exec()
    
    def add_staff(self):
        dialog = Addstaff()
        dialog.exec()

    def search_product(self):
        search_text = self.Pro_search_input.text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        query = "SELECT * FROM products WHERE NAME LIKE ? OR SELLING_PRICE LIKE ?"
        params = ('%' + search_text + '%', '%' + search_text + '%')
        result = connection.execute(query, params)
        records = result.fetchall()
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(records):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        cursor.close()
        connection.close() 

class DeleteService(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete Services")
        self.setFixedWidth(200)
        self.setFixedHeight(150)

        layout = QGridLayout()
        confirmation = QLabel(f"Are you sure you want to delete Service")
        yes = QPushButton("Yes")
        no = QPushButton("No")

        layout.addWidget(confirmation, 0, 0, 1, 2)
        layout.addWidget(yes, 1, 0)
        layout.addWidget(no, 1, 0)

        self.setLayout(layout)

        layout.setHorizontalSpacing(10)
        layout.setVerticalSpacing(20)

       
       
        yes.clicked.connect(self.delete_service)
        no.clicked.connect(self.reject)
        layout.addWidget(yes)
        apply_stylesonOndelete(self)
        apply_animationOndelete(self)
        self.setLayout(layout)
   

    def delete_service(self):
        index = main_window.service_table.currentRow()
        service_id = main_window.service_table.item(index, 0).text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM services WHERE SERVICE_ID = ?", (service_id,))

        connection.commit()
        cursor.close
        connection.close()

        # Refresh the table
        main_window.load_service_data()

        self.close()

        confirmation_widget = QMessageBox()
        confirmation_widget.setWindowTitle("Sucess")
        confirmation_widget.setText("The record was deleted successfully!")
        confirmation_widget.exec()

class Deletestaff(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete Staff")
        self.setFixedHeight(150)
        self.setFixedWidth(200)

        layout  = QGridLayout()

        confirmation =QLabel("Are you sure you want to delete staff ?")
        yes = QPushButton("Yes")
        no = QPushButton("No")

        layout.addWidget(confirmation, 0, 0, 1, 2)
        layout.addWidget(yes, 1, 0)
        layout.addWidget(no, 1, 0)

        self.setLayout(layout)

        layout.setHorizontalSpacing(10)
        layout.setVerticalSpacing(20)

        yes.clicked.connect(self.delete_staff)
        no.clicked.connect(self.reject)
        layout.addWidget(yes)
        apply_stylesonOndelete(self)
        apply_animationOndelete(self)

        self.setLayout(layout)
    
    def delete_staff(self):
        index = main_window.staff_table.currentRow()
        staff_id = main_window.staff_table.item(index, 0).text()
        

        connection =DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM staff WHERE STAFF_ID = ?", (staff_id,))

        connection.commit()
        cursor.close
        connection.close()

        # Refresh the table
        main_window.load_staff_data()

        self.close()

        confirmation_widget = QMessageBox()
        confirmation_widget.setWindowTitle("Sucess")
        confirmation_widget.setText("The record was deleted successfully!")
        confirmation_widget.exec()

class DeleteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete Product")
        self.setFixedWidth(200)
        self.setFixedHeight(150)
        # self.login = LoginWindow()

        layout = QGridLayout()
        confirmation =QLabel("Are you sure you want to delete products ?")
        yes = QPushButton("Yes")
        no = QPushButton("No")

        layout.addWidget(confirmation, 0, 0, 1, 2)
        layout.addWidget(yes, 1, 0)
        layout.addWidget(no, 1, 0)

        self.setLayout(layout)

        layout.setHorizontalSpacing(10)
        layout.setVerticalSpacing(20)

       
        yes.clicked.connect(self.delete_product)
        no.clicked.connect(self.reject)
        layout.addWidget(yes)
        apply_stylesonOndelete(self)
        apply_animationOndelete(self)
        self.setLayout(layout)

    def delete_product(self):
        index = main_window.table.currentRow()
        pro_id = main_window.table.item(index, 0).text()
        

        connection =DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM products WHERE PRODUCT_ID = ?", (pro_id,))

        connection.commit()
        cursor.close
        connection.close()

        # Refresh the table
        main_window.load_data()

        self.close()

        confirmation_widget = QMessageBox()
        confirmation_widget.setWindowTitle("Sucess")
        confirmation_widget.setText("The record was deleted successfully!")
        confirmation_widget.exec()

class EditDialog(QDialog):
    def __init__(self):
    
            super().__init__()
        
            self.setWindowTitle("Update Product Data")
            self.setFixedWidth(300)
            self.setFixedHeight(300)


            layout = QVBoxLayout()
            try:
                index = main_window.table.currentRow()
                if index < 0: 
                    raise RuntimeError("No row selected")
                
                pro_Name = main_window.table.item(index, 1).text()
                self.pro_id = main_window.table.item(index, 0).text()
                self.pro_Name = QLineEdit(pro_Name)
                self.pro_Name.setPlaceholderText("Product Name")
                layout.addWidget(self.pro_Name)

                pro_Cat = main_window.table.item(index, 2).text()
                self.pro_Cat_Name = QComboBox()
                pro_Cat_Grade =["Grade 1", "Grade 2", "Grade 3"]
                self.pro_Cat_Name.addItems(pro_Cat_Grade)
                self.pro_Cat_Name.setCurrentText(pro_Cat)
                layout.addWidget(self.pro_Cat_Name)

                pro_Sp = main_window.table.item(index, 3).text()
                self.pro_Sp = QLineEdit(pro_Sp)
                self.pro_Sp.setPlaceholderText("Selling Price")
                layout.addWidget(self.pro_Sp)

                pro_Cp = main_window.table.item(index, 4).text()
                self.pro_Cp = QLineEdit(pro_Cp)
                self.pro_Sp.setPlaceholderText("Cost Price")
                layout.addWidget(self.pro_Cp)

                pro_Quantity = main_window.table.item(index, 5).text()
                self.pro_Quantity = QLineEdit(pro_Quantity)
                self.pro_Quantity.setPlaceholderText("Quantity")
                layout.addWidget(self.pro_Quantity)

                pro_Des = main_window.table.item(index, 6).text()
                self.pro_Des = QLineEdit(pro_Des)
                self.pro_Des.setPlaceholderText("Description")
                layout.addWidget(self.pro_Des)
            except RuntimeError as e:
                table_function.handle_runtime_error(self, e)
                
            button = QPushButton("Update")
            button.clicked.connect(self.update_product)
            layout.addWidget(button)

            self.setLayout(layout)
            apply_styles(self)
            apply_animation(self)    

        

    def update_product(self):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("update products SET NAME = ?, CATEGORY = ?, SELLING_PRICE = ?, COST_PRICE =?, QUANTITY = ?, DESCRIPTION = ? WHERE PRODUCT_ID = ?", (self.pro_Name.text(), self.pro_Cat_Name.itemText(self.pro_Cat_Name.currentIndex()), self.pro_Sp.text(), self.pro_Cp.text(), self.pro_Quantity.text(),self.pro_Des.text(), self.pro_id))

        connection.commit()
        cursor.close()
        connection.close()
        main_window.load_data()

class EditService(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update Service Data")
        self.setFixedWidth(300)
        self.setFixedWidth(300)

        layout = QVBoxLayout()

        index = main_window.service_table.currentRow()
        self.service_id = main_window.service_table.item(index, 0).text()
        service_Name = main_window.service_table.item(index, 1).text()

        self.service_Name = QLineEdit(service_Name)
        self.service_Name.setPlaceholderText("Service Name")
        layout.addWidget(self.service_Name)

        service_Price = main_window.service_table.item(index, 2).text()
        self.service_Price = QLineEdit(service_Price)
        self.service_Price.setPlaceholderText("Price")
        layout.addWidget(self.service_Price)

        button = QPushButton("Update")
        button.clicked.connect(self.update_service)
        layout.addWidget(button)

        self.setLayout(layout)
        apply_styles(self)
        apply_animation(self)
    
    def update_service(self):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("update services SET NAME = ?, PRICE = ?  WHERE SERVICE_ID = ?", (self.service_Name.text(), self.service_Price.text(), self.service_id))

        connection.commit()
        cursor.close()
        connection.close()
        main_window.load_service_data()
        self.close()
 
class EditStaff(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edit Staff profile")
        self.setFixedHeight(400)
        self.setFixedWidth(250)

        layout = QVBoxLayout()

        index = main_window.staff_table.currentRow()
        self.staff_id = main_window.staff_table.item(index, 0).text()
        staff_name = main_window.staff_table.item(index, 1).text()
        staff_Role = main_window.staff_table.item(index, 2).text()
        staff_Contactinfo = main_window.staff_table.item(index, 3).text()
        staff_Password = main_window.staff_table.item(index, 4).text()

        self.staff_name = QLineEdit(staff_name)
        self.staff_name.setPlaceholderText("staff Name")
        layout.addWidget(self.staff_name)

        self.staff_Role = QLineEdit(staff_Role)
        self.staff_Role.setPlaceholderText("Role")
        layout.addWidget(self.staff_Role)

        self.staff_Contactinfo = QLineEdit( staff_Contactinfo)
        self.staff_Contactinfo.setPlaceholderText("Phone")
        layout.addWidget(self.staff_Contactinfo)

        self.staff_Password  = QLineEdit( staff_Password )
        self.staff_Password .setPlaceholderText("staff password")
        layout.addWidget(self.staff_Password )

        button = QPushButton("Update")
        button.clicked.connect(self.update_staff)
        layout.addWidget(button)

        self.setLayout(layout)
        apply_styles(self)
        apply_animation(self)

    def update_staff(self):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("update staff SET STAFF_NAME = ?, STAFF_ROLE = ?, STAFF_CONTACT = ?, PASSWORD = ? WHERE STAFF_ID = ?", (self.staff_name.text(), self.staff_Role.text(), self.staff_Contactinfo.text(), self.staff_Password.text(), self.staff_id))

        connection.commit()
        cursor.close()
        connection.close()
        main_window.load_staff_data()
        self.close()

class Addstaff(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Staff")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        self.staff_Name = QLineEdit()
        self.staff_Name.setPlaceholderText("Product_Name")
        layout.addWidget(self.staff_Name)

        self.staff_Role = QLineEdit()
        self.staff_Role.setPlaceholderText("Role")
        layout.addWidget(self.staff_Role)

        
        self.staff_contact = QLineEdit()
        self.staff_contact.setPlaceholderText("contact info")
        layout.addWidget(self.staff_contact)

        
        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        layout.addWidget(self.password)

        button = QPushButton("Add staff")
        button.clicked.connect(self.insert_staff)
        layout.addWidget(button)
        self.setLayout(layout)
        apply_styles(self)
        apply_animation(self)

        
    
    def insert_staff(self):
        name = self.staff_Name.text()
        role = self.staff_Role.text()
        contact = self.staff_contact.text()
        password = self.password.text()

        if not name or not role or not contact or not password:
            QMessageBox.warning(self, "Input Error", "All fiels must be filled.")
        
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO staff (STAFF_NAME, STAFF_ROLE, STAFF_CONTACT, PASSWORD) VALUES (?, ?, ?, ?)", (name, role, contact, password))

        connection.commit()
        cursor.close()
        connection.close()
        main_window.load_staff_data()
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

        self.pro_Cat_Name = QComboBox()
        pro_Cat =["Grade 1", "Grade 2", "Grade 3"]
        self.pro_Cat_Name.addItems(pro_Cat)
        layout.addWidget(self.pro_Cat_Name)

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
        apply_styles(self)
        apply_animation(self)

    def insert_product(self):
        name = self.pro_Name.text()
        category = self.pro_Cat_Name.itemText(self.pro_Cat_Name.currentIndex())
        selling_price = self.pro_Sp.text()
        cost_price = self.pro_Cp.text()
        quantity = self.pro_Quantity.text()
        description = self.pro_Dec.text()

        if not name or not category or not selling_price or not cost_price or not quantity or not description:
            QMessageBox.warning(self, "Input Error", "All fields must be filled.")
            return

        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO products (NAME, CATEGORY, SELLING_PRICE, COST_PRICE, QUANTITY, DESCRIPTION) VALUES (?, ?, ?, ?, ?, ?)", (name, category, selling_price, cost_price, quantity, description))

        connection.commit()
        cursor.close()
        connection.close()
        main_window.load_data()

class AddServices(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Services")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        self.Service_Name = QLineEdit()
        self.Service_Name.setPlaceholderText("Service Name")
        layout.addWidget(self.Service_Name)

        self.Service_Price = QLineEdit()
        self.Service_Price.setPlaceholderText("Price")
        layout.addWidget(self.Service_Price)

        button = QPushButton("Add")
        button.clicked.connect(self.insert_service)
        layout.addWidget(button)
        self.setLayout(layout)
        apply_styles(self)
        apply_animation(self)

    def insert_service(self):
        name = self.Service_Name.text()
        price = self.Service_Price.text()

        if not name or not price:
            QMessageBox.warning(self, "Input Error", "All fields must be filled.")
            return
        
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO services (NAME, PRICE) VALUES (?, ?)", (name, price))

        connection.commit()
        cursor.close()
        connection.close()
        main_window.load_service_data()
class option(QWidget):
    def __init__(self):
        super().__init__()  
        self.setWindowTitle("Choose user")
        self.setFixedHeight(200)
        self.setFixedWidth(300)

        layout = QGridLayout()
        self.setLayout(layout)
        
        qestion = QLabel("HOW DO YOU WANT TO LOGIN")
        qestion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        qestion.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        admin = QPushButton("ADMIN")
        admin.setStyleSheet(
            '''
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: 2px solid #1976D2;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
            '''
        )
        
        staff = QPushButton("STAFF")
        staff.setStyleSheet(
            '''
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: 2px solid #388E3C;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #388E3C;
            }
            '''
        )

        layout.addWidget(qestion, 0, 0, 1, 2)
        layout.addWidget(admin, 1, 0)
        layout.addWidget(staff, 1, 1)
        
        layout.setHorizontalSpacing(10)
        layout.setVerticalSpacing(20)

        admin.clicked.connect(self.admin)
        staff.clicked.connect(self.staff)

    def set_main_window(self, main_window, login_window, staff_login):
        self.main_window = main_window
        self.login_window = login_window
        self.staff_login = staff_login
    
    def admin(self):
        self.login_window.show()
        self.close()
        # Add any other actions you want to perform when admin is clicked
    
    def staff(self):
        self.staff_login.show()
        self.close()
        # Add any other actions you want to perform when staff is clicked

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    usermain = UserWindow()
    choose = option()
    login_window = LoginWindow()
    staff_login = staffLoginWindow()

    staff_login.set_usermain_window(usermain)

    login_window.set_main_window(main_window)
    

    choose.set_main_window(main_window, login_window,    staff_login)
    
    choose.show()

    sys.exit(app.exec())

    