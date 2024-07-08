import sys
from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLineEdit, QComboBox, QPushButton, QGraphicsOpacityEffect
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve

def apply_styles(self):
    self.setStyleSheet("""
        QDialog {
            background-color: #f0f0f0;
        }
        QLineEdit, QComboBox {
            border: 2px solid #ccc;
            border-radius: 5px;
            padding: 5px;
            font-size: 14px;
            background-color: #fff;
        }
        QLineEdit:focus, QComboBox:focus {
            border-color: #0078d7;
        }
        QPushButton {
            background-color: #0078d7;
            color: #fff;
            border: none;
            border-radius: 5px;
            padding: 10px;
            font-size: 14px;
        }
        QPushButton:hover {
            background-color: #0053a0;
        }
        QPushButton:pressed {
            background-color: #003d73;
        }
    """)

def apply_animation(self):
    self.opacity_effect = QGraphicsOpacityEffect(self)
    self.setGraphicsEffect(self.opacity_effect)
    self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
    self.animation.setDuration(1000)
    self.animation.setStartValue(0.0)
    self.animation.setEndValue(1.0)
    self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)
    self.animation.start()


def apply_styleson(self):
    self.setStyleSheet("""
        QMainWindow {
            background-color: #f0f0f0;
        }
        QMenuBar {
            background-color: #404040;
            color: white;
        }
        QMenuBar::item {
            background-color: #404040;
            color: white;
        }
        QMenuBar::item:selected {
            background-color: #0078d7;
        }
        QMenu {
            background-color: #404040;
            color: white;
        }
        QMenu::item:selected {
            background-color: #0078d7;
        }
        QAction {
            padding: 10px;
            font-size: 14px;
        }
    """)

def apply_animationon(self):
    self.opacity_effect = QGraphicsOpacityEffect(self)
    self.setGraphicsEffect(self.opacity_effect)
    self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
    self.animation.setDuration(1000)
    self.animation.setStartValue(0.0)
    self.animation.setEndValue(1.0)
    self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)
    self.animation.start()

def apply_stylesonOndelete(self):
    self.setStyleSheet("""
        QDialog {
            background-color: #f0f0f0;
            border-radius: 10px;
        }
        QLabel {
            font-size: 14px;
            color: #333;
        }
        QPushButton {
            background-color: #0078d7;
            color: #fff;
            border: none;
            border-radius: 5px;
            padding: 5px 10px;
            font-size: 14px;
        }
        QPushButton:hover {
            background-color: #0053a0;
        }
        QPushButton:pressed {
            background-color: #003d73;
        }
    """)

def apply_animationOndelete(self):
    self.opacity_effect = QGraphicsOpacityEffect(self)
    self.setGraphicsEffect(self.opacity_effect)
    self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
    self.animation.setDuration(1000)
    self.animation.setStartValue(0.0)
    self.animation.setEndValue(1.0)
    self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)
    self.animation.start()
