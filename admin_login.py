from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QMainWindow, QTableWidget, QToolBar, QDialog, QTableWidgetItem, QPushButton, QMessageBox, QComboBox, QStatusBar, QHBoxLayout, QSizePolicy
import time 
 

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
import sqlite3
import sys 



class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Window")
        self.setFixedHeight(200)
        self.setFixedWidth(600)

        layout = QGridLayout()
        self.setLayout(layout)

        labels = {}
        self.lineEdits = {}

        labels['Username'] = QLabel('Username')
        labels['Password'] = QLabel('Password')
        labels['Username'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        labels['Password'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.lineEdits['Username'] = QLineEdit()
        self.lineEdits['Password'] = QLineEdit()
        self.lineEdits['Password'].setEchoMode(QLineEdit.EchoMode.Password)
        
        layout.addWidget(labels['Username'], 0, 0, 1, 1)

        layout.addWidget(self.lineEdits['Username'], 0, 1, 1, 1)
        layout.addWidget(labels['Password'], 1, 0, 1, 1)
        layout.addWidget(self.lineEdits['Password'], 1, 1, 1, 1)

        button_login = QPushButton('& Login')
        button_login.clicked.connect(self.checkCredential)

        layout.addWidget(button_login,   2, 3, 1, 1)

        self.status = QLabel('')
        self.status.setStyleSheet('font-size: 20px; color: red;')
        layout.addWidget(self.status, 3, 0, 1, 3)

        self.connectTodb()

    def connectTodb(self):
        self.connections = sqlite3.connect("database.db")
        self.cursor = self.connections.cursor()
    
    def checkCredential(self):
        username = self.lineEdits['Username'].text()
        password = self.lineEdits['Password'].text()

        query = ('SELECT * FROM admin WHERE Username = :username')
        self.cursor.execute(query, {"username": username})
        result = self.cursor.fetchone()
        if result:
            if result[2] == password:

                time.sleep(1)  
                self.main_window.show()
                self.main_window.load_data()
                self.close()
            else:
                self.status.setText("Password is Incorrect ")
        else:
            self.status.setText("username is not found")
            
    def set_main_window(self, main_window):
        self.main_window = main_window
