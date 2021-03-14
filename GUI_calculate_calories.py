import pandas as pd
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import numpy as np
from scipy.interpolate import interp1d
from scipy.interpolate import barycentric_interpolate
import sqlite3


connection = sqlite3.connect("meal_prep_calculator.db")
cursor = connection.cursor()



class Calorie_requirement(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel()           # hier werden alle Elemente in dem Layout definiert
        self.female = QRadioButton('female')
        self.female.setChecked(True)
        self.male = QRadioButton('male')
        self.genderButtons = QButtonGroup() #creates a group of the RadioButtons, so only one can be selected
        self.genderButtons.addButton(self.female)
        self.genderButtons.addButton(self.male)
        self.age_edit = QLineEdit()
        self.height = QLineEdit()
        self.wheight = QLineEdit()
        self.sleep = QLineEdit()
        self.job = QComboBox(self)
        self.freetime = QComboBox()
        self.calculate = QPushButton('calculate')
        self.sport = QComboBox()
        self.kinds_of_sport = 'hallo'
        self.percentage_breakfast = QSpinBox()
        self.percentage_lunch = QSpinBox()
        self.percentage_dinner = QSpinBox()
        self.percentage_breakfast.setRange(0,100)
        self.percentage_lunch.setRange(0,100)
        self.percentage_dinner.setRange(0,100)
        self.sport_hours_per_week = QLineEdit()
        self.job_pal = {'predominantly sitting (e.g. office job)':1.45, 'predominantly seated (e.g. bus driver)':1.65,
                        'mainly standing (e.g. waiter)':1.85, 'physically demanding (e.g. farmer)':2.2}
        self.freetime_pal = {'predominantly sitting (e.g. Gaming)':1.45, 'predominantly seated':1.65,
                        'mainly standing (e.g. darts, going out)':1.85, 'physically demanding (lots of sport)':2.2}
        self.end_requirement = 0 #variable we calculate in the function calculate_calories
        self.days_to_goal = QLineEdit('0')
        #self.validator = QtGui.QIntValidator(0,111,self) #result of this is, that you can not type things in other than integer. Problem: if you type in 12.5 as days to reache the goal, the code changes it in 125 days
        #self.days_to_goal.setValidator(self.validator)
        self.wheight_to_goal = QLineEdit('0')
        self.final_calories_a_day = 0





        #creates the layout
        form = QFormLayout()
        form.addRow('Gender: ', self.female)
        form.addRow('        ', self.male)
        form.addRow("Age:", self.age_edit)
        form.addRow("Height in cm:", self.height)
        form.addRow("Weight in kg:", self.wheight)
        #form.addRow('Sleep: ',self.sleep)
        self.job.addItem('Please choose')
        self.job.addItems(self.job_pal.keys())  #adds the keys of the dicitonary "self.job_pal" to the ComboBox
        form.addRow('Job:',self.job)            #adds self.job to the layout
        self.freetime.addItem('--')
        self.freetime.addItems(self.freetime_pal.keys())  #adds the keys of the dicitonary "self.freetime_pal" to the ComboBox
        form.addRow('Freetime:', self.freetime)
        self.kinds_of_sport = self.calories_sports()
        self.sport.addItems(self.kinds_of_sport)
        form.addRow('Sports:',self.sport)
        form.addRow('How many hours per week', self.sport_hours_per_week)
        form.addRow('Weight to lose/gain', self.wheight_to_goal)
        form.addRow('Days to reache the goal:', self.days_to_goal)
        form.addRow("Percentage Breakfast", self.percentage_breakfast)
        form.addRow("Percentage Lunch", self.percentage_lunch)
        form.addRow("Percentage Dinner", self.percentage_dinner)
        form.addRow('      ', self.calculate)
        self.calculate.clicked.connect(self.calculate_calories_to_reach_your_goal)

        self.setLayout(form) #sets the layout, so it can be shown
        self.setWindowTitle('Calorie Calculator')
        self.show()


    def calories_sports(self): #puts the activities from the column "activites" of the .xls-file into a List, so we can use it for the QComboBox
        calories = pd.read_excel('Calories_during_activities.xls', index_col=False)
        lst = calories['activity']
        return lst

    def calculate_calories(self): #takes the inputs in the GUI and calculates the calories you need to hold your wheight
        age = int(self.age_edit.text())
        update = "UPDATE calorie_data SET Age = ? WHERE rowid = ?"
        data = (age, 1)
        cursor.execute(update,data)
        connection.commit()


        wheight = float(self.wheight.text())


        height = int(self.height.text())
        update = "UPDATE calorie_data SET Height = ? WHERE rowid = ?"
        data = (height, 1)
        cursor.execute(update,data)
        connection.commit()


        job = self.job_pal[str(self.job.currentText())] #Value for die chosen attribute in the QComboBox
        update = "UPDATE calorie_data SET job = ? WHERE rowid = ?"
        data = (str(self.job.currentText()), 1)
        cursor.execute(update,data)
        connection.commit()


        freetime = self.freetime_pal[str(self.freetime.currentText())]
        update = "UPDATE calorie_data SET Freetime = ? WHERE rowid = ?"
        data = (str(self.freetime.currentText()), 1)
        cursor.execute(update,data)
        connection.commit()


        sport = str(self.sport.currentText())
        hours_weekly = float(self.sport_hours_per_week.text())
        update = "UPDATE calorie_data SET hours_per_week = ? WHERE rowid = ?"
        data = (hours_weekly, 1)
        cursor.execute(update,data)
        connection.commit()
        
        percentage_breakfast = float(self.percentage_breakfast.value())
        update = "UPDATE calorie_data SET percentage_breakfast = ? WHERE rowid = ?"
        data = (percentage_breakfast, 1)
        cursor.execute(update,data)
        connection.commit()


        percentage_lunch = float(self.percentage_lunch.value())
        update = "UPDATE calorie_data SET percentage_lunch = ? WHERE rowid = ?"
        data = (percentage_lunch, 1)
        cursor.execute(update,data)
        connection.commit()


        percentage_dinner = float(self.percentage_dinner.value())
        update = "UPDATE calorie_data SET percentage_dinner = ? WHERE rowid = ?"
        data = (percentage_dinner, 1)
        cursor.execute(update,data)
        connection.commit()

        percentage_snack = 100 - (percentage_breakfast + percentage_dinner + percentage_lunch)
        update = "UPDATE calorie_data SET percentage_snack = ? WHERE rowid = ?"
        data = (percentage_snack, 1)
        cursor.execute(update,data)
        connection.commit()




        wheights_in_file = np.array([58.96696, 70.30676, 81.64656, 92.98636]) #in kg
        print(wheights_in_file)
        calories_in_file = []
        df = pd.read_excel('Calories_during_activities.xls', index_col=False) #creates the DataFrame of the called .xls file.
        for i in wheights_in_file:
            calories_in_file.append(df[i].values[df[df['activity'] == sport].index.item()])
        calories_in_file_array = np.array(calories_in_file)
        #f1 = interp1d(wheights_in_file, calories_in_file_array,kind='cubic')  # interpolates formula combinde with extrapolation. But results are not very trustworthy
        print('hallo')
        xnew = np.array([float(self.wheight.text())])  # das sind x-Werte für die y-Werte bestimmt werden sollen
        print('xnew: ' + str(xnew))
        calories_per_hour_through_sport = barycentric_interpolate(wheights_in_file, calories_in_file_array, xnew)  # die alten x und y und das neue x
        #calories_per_hour_through_sport = f1(xnew)
        calories_in_file.clear()

        print("Calories per hour: " + str(calories_per_hour_through_sport))


        #calories_per_hour_through_sport = df['130 lb'].values[df[df['activity'] == sport].index.item()] #gets the index of the row
        # of the chooen sport. Then it gets through the index the calories in column 130lb the calories which are burned.
        #if we want to search the calories depending on the wheigt, we have to make a connection here.

        gender = self.genderButtons.checkedButton().text()
        if gender == "female": #here is the actual calculation, it has a different formula for each gender
            basic_nutrition = 65.51 + (9.6 * wheight) + (1.8 * height) - (4.7 * age) #calories you need, when you don't do anything on the day.
            cursor.execute("UPDATE calorie_data SET gender = 'female' WHERE rowid = 1")
            connection.commit()

            
        else:
            basic_nutrition = 66.47 + (13.7 * wheight) + (5 * height) - (6.8 * age)
            cursor.execute("UPDATE calorie_data SET gender = 'male' WHERE rowid = 1")
            connection.commit()


        pal_factor = (7 * 0.95 + 8 * job + (63 - hours_weekly) / 7 * freetime) / (24 - (hours_weekly / 7))
        add_throug_sport = (calories_per_hour_through_sport * hours_weekly) / 7
        self.end_requirement = basic_nutrition * pal_factor + add_throug_sport
        print('basic: ' + str(basic_nutrition*pal_factor))
        print('through sport: ' + str(add_throug_sport))
        print("total daily calories: " + str(self.end_requirement))
        
        lunch = (percentage_lunch/100) * self.end_requirement  # calculating the amount of calories per meal, the rest goes into snacks
        update = "UPDATE calorie_data SET lunch = ? WHERE rowid = ?"
        data = (lunch[0], 1)
        cursor.execute(update,data)
        connection.commit() 

        breakfast = (percentage_breakfast/100) * self.end_requirement
        update = "UPDATE calorie_data SET breakfast = ? WHERE rowid = ?"
        data = (breakfast[0], 1)
        cursor.execute(update,data)
        connection.commit() 

        dinner = (percentage_dinner/100) * self.end_requirement
        update = "UPDATE calorie_data SET dinner = ? WHERE rowid = ?"
        data = (dinner[0], 1)
        cursor.execute(update,data)
        connection.commit()  

        snack = max(self.end_requirement - (lunch + breakfast + dinner),0)
        update = "UPDATE calorie_data SET snack = ? WHERE rowid = ?"
        data = (snack[0], 1)
        cursor.execute(update,data)
        connection.commit()
        print(f"distributed in breakfast: {breakfast}, lunch: {lunch}, dinner: {dinner} and snacks: {snack}")                  # printing the percentages of the single meals 
        
        
        
        
        return self.end_requirement



    def calculate_calories_to_reach_your_goal(self): #in the research I read that you have to have a deficit of or additional 7000kcal to loose/ gain 1 kg. So This is implementet hier
        self.calculate_calories() #calls the function calculate_calories
        days_to_goal = int(self.days_to_goal.text())
        update = "UPDATE calorie_data SET days_to_goal = ? WHERE rowid = ?"
        data = (days_to_goal, 1)
        cursor.execute(update,data)
        connection.commit()

        wheight_to_goal = float(self.wheight_to_goal.text())
        update = "UPDATE calorie_data SET kg_to_lose = ? WHERE rowid = ?"
        data = (wheight_to_goal, 1)
        cursor.execute(update,data)
        connection.commit()

        if wheight_to_goal == 0:
            self.final_calories_a_day = self.end_requirement #if the user doesn't want to lose wheight you don't have to calculate anything
            print("goal:" + str(self.final_calories_a_day))
        else:
            self.final_calories_a_day = ((wheight_to_goal * 7000) / days_to_goal) + self.end_requirement #same formula vor gaining and losing weight.
            print("goal:" + str(self.final_calories_a_day))

        update = "UPDATE calorie_data SET daily_calories = ? WHERE rowid = ?"
        print(self.final_calories_a_day[0])
        data = (self.final_calories_a_day[0], 1)
        cursor.execute(update,data)
        connection.commit()    
        return self.final_calories_a_day



if __name__ == "__main__":
    app = QApplication(sys.argv) #runs the code so you can see the GUI
    calculated_calories = Calorie_requirement()
    sys.exit(app.exec_())