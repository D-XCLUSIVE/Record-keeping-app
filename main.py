from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QMainWindow, QTableWidget, QToolBar, QDialog, QTableWidgetItem, QPushButton, QMessageBox, QComboBox, QStatusBar

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

        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

        self.table.cellClicked.connect(self.cell_clicked)
    

    def show_products(self):
        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(("PRODUCT_ID", "NAME", "CATEGORY", "SELLING_PRICE", "COST_PRICE", "QUANTITY", "DESCRIPTION"))

        self.setCentralWidget(self.table)
        

    def cell_clicked(self):
        edit_button = QPushButton("Edith Record")
        edit_button.clicked.connect(self.edit)

        delete_button = QPushButton("Delete Record")
        delete_button.clicked.connect(self.delete)


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

    def edit(self):
        dialog = EditDialog()
        dialog.exec()

    def delete(self):
        dialog = DeleteDialog()
        dialog.exec()


class DeleteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete Product")
        self.setFixedWidth(200)
        self.setFixedHeight(150)

        layout = QGridLayout()
        confirmation =QLabel("Are you sure you want to delete product ?")
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
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM products WHERE PRODUCT_ID = ?", (pro_id))

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
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("update products SET NAME = ?, CATEGORY = ?, SELLING_PRICE = ?, COST_PRICE =?, QUANTITY = ?, DESCRIPTION = ? WHERE PRODUCT_ID = ?", (self.pro_Name.text(), self.pro_Cat_Name.itemText(self.pro_Cat_Name.currentIndex()), self.pro_Sp.text(), self.pro_Cp.text(), self.pro_Quantity.text(),self.pro_Des.text(), self.pro_id))

        connection.commit()
        cursor.close()
        connection.close()
        main_window.load_data()




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