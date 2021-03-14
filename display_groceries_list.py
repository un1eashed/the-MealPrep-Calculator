import sqlite3
from ast import literal_eval

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea, QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow, QCheckBox)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic
import sys
import re

#this Code shows the shoppinglist from the databank in combination with checkboxes. If you click on a checkbox the ingredient disappears from the
# shoppinglist and gets also deleted in the databank.

class Groceries(QMainWindow):
    connection = sqlite3.connect('meal_prep_calculator.db')
    cursor = connection.cursor()

    def __init__(self):
        super().__init__()
        self.title = QLabel('test')  # line where you type in your weight
        self.connection = sqlite3.connect('meal_prep_calculator.db')
        self.cursor = self.connection.cursor()
        self.initUI()

    def initUI(self):
        self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()                 # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()               # The Vertical Box that contains the Horizontal Boxes of  labels and buttons

        lst = []
        ingredients = [ingredients[0] for ingredients in self.cursor.execute("SELECT ingredient FROM shoppinglist")]
        amount = [amount[0] for amount in self.cursor.execute("SELECT amount FROM shoppinglist")]
        for i in range(len(ingredients)):
            combined = amount[i] + ' ' + ingredients[i]
            lst.append(combined)    #creates the whole list to display for the ingredients

        for i in lst:  # sets design of the checkboxes
            self.cb = QCheckBox("{}".format(i), self)
            self.cb.setStyleSheet("QCheckBox::indicator { width: 30px; height: 30px;}")
            self.cb.stateChanged.connect(lambda ch, i=i: self.hide_checkbox(i))  # < ---
            self.vbox.addWidget(self.cb)
        self.widget.setLayout(self.vbox)

        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        #size and design of shoppingslist
        self.setGeometry(500, 100, 500, 600)
        self.setWindowTitle('Groceries list')
        self.setWindowIcon(QIcon('groceries.png'))
        self.show()

        return

    def hide_checkbox(self, i):     #hide checkboxes and deletes the ingredients from the databank
        text = self.sender().text()
        amount_parent = re.findall('[+-]?\d+[,.]?\d*', text)
        amount = amount_parent[0]
        amount_plus_space = str(amount) + ' '
        text = text.replace(amount_plus_space, '')
        read = "DELETE FROM shoppinglist WHERE ingredient = ?"
        data = [text]
        self.cursor.execute(read,data)
        self.connection.commit()
        self.sender().hide()


    cursor.close()
    connection.close()
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    main = Groceries()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()









