import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from insert_weight import insert_weight
from display_weekly_meal_plan import Ui_wednesday
import sqlite3
from datetime import date
import pandas as pd
from matplotlib import pyplot as plt
import weekly_meal_plan_to_db
from display_groceries_list import Groceries
from GUI_calculate_calories import Calorie_requirement


#Code creates the MainWindow for the User to use every function.

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()  #creating the Layout
        self.calculate = QPushButton('calculate')
        self.weekly_meal_plan = QPushButton('show')
        self.shoppinglist = QPushButton('show')
        self.weight = QLineEdit()  # line where you type in your weight
        self.graph = QPushButton('show graph')  # button to show your weight over time
        self.start_new_plan = QPushButton('start')
        form = QFormLayout()
        form.addRow('Please enter your weight: ', self.weight)
        self.weight.returnPressed.connect(self.save_weight)
        form.addRow('Calculate calories: ', self.calculate)
        form.addRow('Weekly meal plan: ',self.weekly_meal_plan)
        form.addRow('Shoppinglist: ', self.shoppinglist)
        form.addRow('Show weight history: ', self.graph)
        form.addRow('Start a new weekly plan', self.start_new_plan)
        self.graph.clicked.connect(self.show_graph)
        self.weekly_meal_plan.clicked.connect(self.open_weekly_meal_plan)
        self.start_new_plan.clicked.connect(self.start_new_week_plan)
        self.shoppinglist.clicked.connect(self.open_groceries_list)
        self.calculate.clicked.connect(self.open_calculator)
        self.setLayout(form)  # sets the layout, so it can be shown
        self.setWindowTitle('Main window')
        self.show()

    def open_weekly_meal_plan(self):    #in the following functions the code from other modules is connected so that other windows can pop up
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_wednesday()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_groceries_list(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Groceries()
        #self.ui.setupUi(self.window)
        #self.window.show()

    def open_calculator(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Calorie_requirement()

    # this code makes sure that the user can insert his weight. Just type in the weight in the edit line and press enter. The weight is stored automatically.
    # if the user types in two weights on the same day, the weight is updated so that there are not two datasets for one day.
    def save_weight(self):
        connection = sqlite3.connect('meal_prep_calculator.db')
        cursor = connection.cursor()
        df = pd.read_sql_query("SELECT * FROM insert_weight", connection,index_col='date')
        current_date = date.today().strftime(("%d.%m.%Y"))
        weight = float(self.weight.text())
        if current_date in df.index:
            update = "UPDATE insert_weight SET weight = ? WHERE date = ?"
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


    def show_graph(self):   #shows the history graph for the weight
        connection = sqlite3.connect('meal_prep_calculator.db')
        dataframe = pd.read_sql_query("SELECT * FROM insert_weight", connection)
        dataframe.plot(kind='line', x='date', y='weight') #plots the dataframe
        plt.xticks(rotation=50)
        plt.tight_layout()
        plt.show()
        connection.close()

    def start_new_week_plan(self):
        try:
            weekly_meal_plan_to_db.save_weekly_meal_plan()  #does not always work there for the error-handling
        except:
            print('Something went wrong, please try again.')





app = QApplication(sys.argv) #runs the code so you can see the GUI
Main_GUI = MainWindow()
sys.exit(app.exec_())
