import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class TodoApp(QWidget):    
    def __init__(self):
        super().__init__() 
        self.initializeUI()
  
    def initializeUI(self):
        # Main widget properties
        self.setWindowTitle('My Todo List')
        self.setFixedSize(400, 500)
        self.setStyleSheet("""
            background-color: #fff5e9;
            font-size: 16px;
        """)


        self.titleLabel = QLabel('My Todo List')
        self.titleLabel.setFont(QFont('Arial', 24, QFont.Bold))

        
        self.inputBox = QLineEdit()
        self.inputBox.setStyleSheet('QLineEdit {background: white;}')
        self.inputBox.setMinimumHeight(40)


        self.addButton = QPushButton('Add')
        self.addButton.setStyleSheet('QPushButton {background: #4CAF50; color: white;}')
        self.addButton.clicked.connect(self.addTodo)

        self.updateButton = QPushButton('Update')
        self.updateButton.setStyleSheet('QPushButton {background: #2196f3; color: white;}')
        self.updateButton.clicked.connect(self.updateTodo)

        
        self.todoList = QListWidget()
        self.todoList.setStyleSheet('QListWidget {background: white;}')


        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.titleLabel, alignment=Qt.AlignCenter)
        self.mainLayout.addWidget(self.inputBox)
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.addButton)
        self.buttonLayout.addWidget(self.updateButton)
        self.mainLayout.addLayout(self.buttonLayout)
        self.mainLayout.addWidget(self.todoList)
        self.setLayout(self.mainLayout)

    def addTodo(self):
        item = QListWidgetItem(self.inputBox.text())
        item.setCheckState(Qt.Unchecked)
        self.todoList.addItem(item)
        self.inputBox.clear()

    def updateTodo(self):
        currentItem = self.todoList.currentItem()
        if currentItem:
            itemText = self.inputBox.text()  
            currentItem.setText(itemText)
            self.inputBox.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show() 
    app.exec()
