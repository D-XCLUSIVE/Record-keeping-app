from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QMainWindow, QTableWidget, QToolBar, QDialog, QTableWidgetItem, QPushButton, QMessageBox, QComboBox, QStatusBar, QHBoxLayout

from PyQt6.QtCore import Qt 
from PyQt6.QtGui import QAction
import sqlite3
import sys 
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
        toolbar.addAction(self.add_products_action)
        toolbar.addAction(self.add_service_action)
           
        
        self.service_search_bar = self.service_search_bar()
        self.pro_search_bar = self.pro_search_bar()
        self.show_products()
        
        
        

        self.add_products_action.triggered.connect(self.add_product)
        self.add_service_action.triggered.connect(self.add_service)

        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

        self.table.cellClicked.connect(self.cell_clicked_pro)
    
    def show_products(self):
        self.add_products_action.setVisible(True)
        self.add_service_action.setVisible(False)
        self.pro_search_bar.setVisible(True)
        self.service_search_bar.setVisible(False)
        self.table = QTableWidget()
        self.table.verticalHeader().setVisible(False)
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(("PRODUCT_ID", "NAME", "CATEGORY", "SELLING_PRICE", "COST_PRICE", "QUANTITY", "DESCRIPTION"))
        self.setCentralWidget(self.table)
        self.load_data()

        self.table.cellClicked.connect(self.cell_clicked_pro)
    
    def pro_search_bar(self):
        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        self.Pro_search_input = QLineEdit()
        self.Pro_search_input.setPlaceholderText("Search for a product...")
        self.Pro_search_input.setMinimumWidth(400)
        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search_product)
        search_button.setMinimumWidth(100)
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
        self.Service_search_input.setMinimumWidth(400)
        search_button = QPushButton("Search_Services")
        search_button.clicked.connect(self.search_service)
        search_button.setMinimumWidth(100)
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

        delete_button = QPushButton("Delete Record")
        delete_button.clicked.connect(self.delete_pro)


        children = self.findChildren(QPushButton)
        if children:
            for child in children:
                self.statusbar.removeWidget(child)

        self.statusbar.addWidget(edit_button)
        self.statusbar.addWidget(delete_button)


    def cell_clicked_service(self):
        edit_button = QPushButton("Edith Service")
        edit_button.clicked.connect(self.edit_service)

        delete_button = QPushButton("Delete Service")
        delete_button.clicked.connect(self.delete_service)


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
        self.add_products_action.setVisible(False)
        self.staff_table = QTableWidget()
        self.staff_table.setColumnCount(6)
        self.staff_table.setHorizontalHeaderLabels(("StaffID", "Name", "Role", "ContactInfo", "Shedule", "Skill"))
        
        self.setCentralWidget(self.staff_table)

    def show_Transaction(self):
        self.add_products_action.setVisible(False)
        self.Transaction_table = QTableWidget()
        self.Transaction_table.setColumnCount(9)
        self.Transaction_table.setHorizontalHeaderLabels(("TransactionID", "Type", "Date", "ProductID/ServiceID", "Quantity/Duration", "Price", "TotalAmount", "PaymentMethod", "StaffID",))
        
        self.setCentralWidget(self.Transaction_table)

    def edit(self):
        dialog = EditDialog()
        dialog.exec()

    def edit_service(self):
        dialog = EdithService()
        dialog.exec()


    def delete_pro(self):
        dialog = DeleteDialog()
        dialog.exec()
    
    def delete_service(self):
        dialog = DeleteService()
        dialog.exec()

    def add_product(self):
        dialog = AddProducts()
        dialog.exec()
  
    def add_service(self):
        dialog = AddServices()
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
class DeleteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete Product")
        self.setFixedWidth(200)
        self.setFixedHeight(150)

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

        index = main_window.table.currentRow()
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



        button = QPushButton("Update")
        button.clicked.connect(self.update_product)
        layout.addWidget(button)

        self.setLayout(layout)

    def update_product(self):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("update products SET NAME = ?, CATEGORY = ?, SELLING_PRICE = ?, COST_PRICE =?, QUANTITY = ?, DESCRIPTION = ? WHERE PRODUCT_ID = ?", (self.pro_Name.text(), self.pro_Cat_Name.itemText(self.pro_Cat_Name.currentIndex()), self.pro_Sp.text(), self.pro_Cp.text(), self.pro_Quantity.text(),self.pro_Des.text(), self.pro_id))

        connection.commit()
        cursor.close()
        connection.close()
        main_window.load_data()

class EdithService(QDialog):
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
    
    def update_service(self):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("update services SET NAME = ?, PRICE = ?  WHERE SERVICE_ID = ?", (self.service_Name.text(), self.service_Price.text(), self.service_id))

        connection.commit()
        cursor.close()
        connection.close()
        main_window.load_service_data()
        self.close()

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
        

app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()
main_window.load_data()
sys.exit(app.exec())