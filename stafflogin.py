from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QMainWindow, QTableWidget, QToolBar, QDialog, QTableWidgetItem, QPushButton, QMessageBox, QComboBox, QStatusBar, QHBoxLayout, QSizePolicy
import time 
 

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
import sqlite3
import sys 



class staffLoginWindow(QWidget):
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

        self.setStyleSheet("""
                QWidget {
                    background-color: white;
                    border: 2px solid blue;
                    border-radius: 10px;
                }
                QLabel, QLineEdit {
                    background-color: white;
                    color: black;
                    border: 1px solid gray;
                    border-radius: 5px;
                    padding: 5px;
                }
                QPushButton {
                    background-color: green;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    padding: 7px;
                }
                QPushButton:hover {
                    background-color: lightgreen;
                }
                QLabel#status {
                    color: red;
                }
            """)


    def connectTodb(self):
        self.connections = sqlite3.connect("database.db")
        self.cursor = self.connections.cursor()
    
    def checkCredential(self):
        username = self.lineEdits['Username'].text()
        password = self.lineEdits['Password'].text()

        query = ('SELECT * FROM staff WHERE STAFF_NAME = :username')
        self.cursor.execute(query, {"username": username})
        self.result = self.cursor.fetchone()
        if self.result:
            if self.result[4] == password:

                time.sleep(1)  
                self.user_window.show()
                # self.user_window.load_data()
                self.user_window.set_username(username)
                self.close()
                
                
            else:
                self.status.setText("Password is Incorrect ")
        else:
            self.status.setText("username is not found")

           
    def set_usermain_window(self, user_window):
        self.user_window = user_window
