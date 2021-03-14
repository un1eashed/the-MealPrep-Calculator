import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from insert_weight import insert_weight
from display_weekly_meal_plan import Ui_wednesday
from GUI_calculate_calories import Calorie_requirement

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.calculate = QPushButton('calculate')
        self.edit_weight = QPushButton('insert')
        self.weekly_meal_plan = QPushButton('show')
        self.shoppinglist = QPushButton('show')
        form = QFormLayout()
        form.addRow('Calculate calories: ', self.calculate)
        form.addRow('Insert weight: ', self.edit_weight)
        form.addRow('Weekly meal plan: ',self.weekly_meal_plan)
        form.addRow('Shoppinglist: ', self.shoppinglist)
        self.edit_weight.clicked.connect(self.open_insert_weight)
        self.weekly_meal_plan.clicked.connect(self.open_display_weekly_meal_plan)
        self.calculate.clicked.connect(self.open_Calorie_requirement)


        self.setLayout(form)  # sets the layout, so it can be shown
        self.setWindowTitle('Main window')
        self.show()

    def open_insert_weight(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = insert_weight()
        self.ui.show()

    def open_display_weekly_meal_plan(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_wednesday()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def open_Calorie_requirement(self):
        self.Window = QtWidgets.QMainWindow()
        self.ui = Calorie_requirement()
        self.ui.show()


app = QApplication(sys.argv) #runs the code so you can see the GUI
Main_GUI = MainWindow()
sys.exit(app.exec_())
