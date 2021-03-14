import pandas as pd
import sys
from datetime import date
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
import sqlite3

class insert_weight(QWidget):
    def __init__(self):
        super().__init__()
        self.weight = QLineEdit()   #line where you type in your weight
        self.graph = QPushButton('cd pc') #button to show your weight over time


        form = QFormLayout()
        form.addRow('Please enter your weight: ', self.weight)
        self.weight.returnPressed.connect(self.save_weight)
        form.addRow('Show weight over time: ',self.graph)
        self.graph.clicked.connect(self.show_graph)


        self.setLayout(form)  # sets the layout, so it can be shown
        self.setWindowTitle('Calculator of Calories')
        self.show()


    def save_weight(self):
        connection = sqlite3.connect('meal_prep_calculator.db')
        cursor = connection.cursor()
        df = pd.read_sql_query("SELECT * FROM insert_weight", connection,index_col='date')
        current_date = date.today().strftime(("%d.%m.%Y"))
        weight = float(self.weight.text())
        if current_date in df.index:
            update = "UPDATE insert_weight SET weight = ? WHERE date = ?" # man kann mit ? auch Variablen einsetzen
            data = (weight,current_date)
            cursor.execute(update,data)
            connection.commit()
        else:
            insert = "INSERT INTO insert_weight VALUES(?,?)"
            data = (current_date,weight)
            cursor.execute(insert,data)
            connection.commit()
        self.weight.clear()
        cursor.close()
        connection.close()


    def show_graph(self):
        connection = sqlite3.connect('meal_prep_calculator.db')
        dataframe = pd.read_sql_query("SELECT * FROM insert_weight", connection)
        dataframe.plot(kind='line', x='date', y='weight') #plots the dataframe
        plt.xticks(rotation=50)
        plt.tight_layout()
        plt.show()
        connection.close()


if __name__ == "__main__":
    app = QApplication(sys.argv) #runs the code so you can see the GUI
    edit_your_weight = insert_weight()
    sys.exit(app.exec_())

