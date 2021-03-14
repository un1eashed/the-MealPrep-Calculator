# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'a.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5.QtWidgets import QWidget, QMessageBox
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from ast import literal_eval
import sqlite3


#at the beginning import the function weekly_meal_plan_to_csv.py
#this does not need to be importet, just needs to be done before


class Ui_wednesday(QWidget):
    def setupUi(self, wednesday):
        wednesday.setObjectName("wednesday")
        wednesday.resize(1072, 600)
        self.centralwidget = QtWidgets.QWidget(wednesday)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(120, 40, 20, 481))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(510, 40, 20, 481))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(250, 40, 20, 481))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(380, 40, 20, 481))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(640, 40, 20, 481))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(770, 40, 20, 481))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label_bf = QtWidgets.QLabel(self.centralwidget)
        self.label_bf.setGeometry(QtCore.QRect(10, 50, 111, 71))
        self.label_bf.setObjectName("label_monday_1")
        self.label_lunch = QtWidgets.QLabel(self.centralwidget)
        self.label_lunch.setGeometry(QtCore.QRect(10, 130, 111, 71))
        self.label_lunch.setObjectName("label_monday_2")
        self.label_dinner = QtWidgets.QLabel(self.centralwidget)
        self.label_dinner.setGeometry(QtCore.QRect(10, 210, 111, 71))
        self.label_dinner.setObjectName("label_monday_3")
        self.label_snack_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_snack_1.setGeometry(QtCore.QRect(10, 290, 111, 71))
        self.label_snack_1.setObjectName("label_monday_4")
        self.label_snack_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_snack_2.setGeometry(QtCore.QRect(10, 370, 111, 71))
        self.label_snack_2.setObjectName("label_monday_5")
        self.label_snack_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_snack_3.setGeometry(QtCore.QRect(10, 450, 111, 71))
        self.label_snack_3.setObjectName("label_monday_6")
        x = 140
        self.label_monday_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_monday_1.setGeometry(QtCore.QRect(x, 50, 111, 71))
        self.label_monday_1.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_monday_1.setObjectName("label_monday_1")
        self.label_monday_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_monday_2.setGeometry(QtCore.QRect(x, 130, 111, 71))
        self.label_monday_2.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_monday_2.setObjectName("label_monday_2")
        self.label_monday_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_monday_3.setGeometry(QtCore.QRect(x, 210, 111, 71))
        self.label_monday_3.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_monday_3.setObjectName("label_monday_3")
        self.label_monday_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_monday_4.setGeometry(QtCore.QRect(x, 290, 111, 71))
        self.label_monday_4.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_monday_4.setObjectName("label_monday_4")
        self.label_monday_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_monday_5.setGeometry(QtCore.QRect(x, 370, 111, 71))
        self.label_monday_5.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_monday_5.setObjectName("label_monday_5")
        self.label_monday_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_monday_6.setGeometry(QtCore.QRect(x, 450, 111, 71))
        self.label_monday_6.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_monday_6.setObjectName("label_monday_6")
        self.label_tuesday_1 = QtWidgets.QLabel(self.centralwidget)
        x = 270
        self.label_tuesday_1.setGeometry(QtCore.QRect(x, 50, 111, 71))
        self.label_tuesday_1.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_tuesday_1.setObjectName("label_tuesday_1")
        self.label_tuesday_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_tuesday_2.setGeometry(QtCore.QRect(x, 130, 111, 71))
        self.label_tuesday_2.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_tuesday_2.setObjectName("label_tuesday_2")
        self.label_tuesday_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_tuesday_3.setGeometry(QtCore.QRect(x, 210, 111, 71))
        self.label_tuesday_3.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_tuesday_3.setObjectName("label_tuesday_3")
        self.label_tuesday_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_tuesday_4.setGeometry(QtCore.QRect(x, 290, 111, 71))
        self.label_tuesday_4.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_tuesday_4.setObjectName("label_tuesday_4")
        self.label_tuesday_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_tuesday_5.setGeometry(QtCore.QRect(x, 370, 111, 71))
        self.label_tuesday_5.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_tuesday_5.setObjectName("label_tuesday_5")
        self.label_tuesday_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_tuesday_6.setGeometry(QtCore.QRect(x, 450, 111, 71))
        self.label_tuesday_6.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_tuesday_6.setObjectName("label_tuesday_6")
        x = 400
        self.label_wednesday_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_wednesday_1.setGeometry(QtCore.QRect(x, 50, 111, 71))
        self.label_wednesday_1.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_wednesday_1.setObjectName("label_wednesday_1")
        self.label_wednesday_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_wednesday_2.setGeometry(QtCore.QRect(x, 130, 111, 71))
        self.label_wednesday_2.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_wednesday_2.setObjectName("label_wednesday_2")
        self.label_wednesday_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_wednesday_3.setGeometry(QtCore.QRect(x, 210, 111, 71))
        self.label_wednesday_3.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_wednesday_3.setObjectName("label_wednesday_3")
        self.label_wednesday_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_wednesday_4.setGeometry(QtCore.QRect(x, 290, 111, 71))
        self.label_wednesday_4.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_wednesday_4.setObjectName("label_wednesday_4")
        self.label_wednesday_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_wednesday_5.setGeometry(QtCore.QRect(x, 370, 111, 71))
        self.label_wednesday_5.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_wednesday_5.setObjectName("label_wednesday_5")
        self.label_wednesday_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_wednesday_6.setGeometry(QtCore.QRect(x, 450, 111, 71))
        self.label_wednesday_6.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_wednesday_6.setObjectName("label_wednesday_6")
        x = 530
        self.label_thursday_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_thursday_1.setGeometry(QtCore.QRect(x, 50, 111, 71))
        self.label_thursday_1.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_thursday_1.setObjectName("label_thursday_1")
        self.label_thursday_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_thursday_2.setGeometry(QtCore.QRect(x, 130, 111, 71))
        self.label_thursday_2.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_thursday_2.setObjectName("label_thursday_2")
        self.label_thursday_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_thursday_3.setGeometry(QtCore.QRect(x, 210, 111, 71))
        self.label_thursday_3.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_thursday_3.setObjectName("label_thursday_3")
        self.label_thursday_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_thursday_4.setGeometry(QtCore.QRect(x, 290, 111, 71))
        self.label_thursday_4.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_thursday_4.setObjectName("label_thursday_4")
        self.label_thursday_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_thursday_5.setGeometry(QtCore.QRect(x, 370, 111, 71))
        self.label_thursday_5.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_thursday_5.setObjectName("label_thursday_5")
        self.label_thursday_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_thursday_6.setGeometry(QtCore.QRect(x, 450, 111, 71))
        self.label_thursday_6.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_thursday_6.setObjectName("label_thursday_6")
        self.label_friday_1 = QtWidgets.QLabel(self.centralwidget)
        x = 660
        self.label_friday_1.setGeometry(QtCore.QRect(x, 50, 111, 71))
        self.label_friday_1.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_friday_1.setObjectName("label_friday_1")
        self.label_friday_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_friday_2.setGeometry(QtCore.QRect(x, 130, 111, 71))
        self.label_friday_2.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_friday_2.setObjectName("label_friday_2")
        self.label_friday_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_friday_3.setGeometry(QtCore.QRect(x, 210, 111, 71))
        self.label_friday_3.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_friday_3.setObjectName("label_friday_3")
        self.label_friday_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_friday_4.setGeometry(QtCore.QRect(x, 290, 111, 71))
        self.label_friday_4.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_friday_4.setObjectName("label_friday_4")
        self.label_friday_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_friday_5.setGeometry(QtCore.QRect(x, 370, 111, 71))
        self.label_friday_5.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_friday_5.setObjectName("label_friday_5")
        self.label_friday_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_friday_6.setGeometry(QtCore.QRect(x, 450, 111, 71))
        self.label_friday_6.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_friday_6.setObjectName("label_friday_6")
        x = 790
        self.label_saturday_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_saturday_1.setGeometry(QtCore.QRect(x, 50, 111, 71))
        self.label_saturday_1.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_saturday_1.setObjectName("label_saturday_1")
        self.label_saturday_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_saturday_2.setGeometry(QtCore.QRect(x, 130, 111, 71))
        self.label_saturday_2.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_saturday_2.setObjectName("label_saturday_2")
        self.label_saturday_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_saturday_3.setGeometry(QtCore.QRect(x, 210, 111, 71))
        self.label_saturday_3.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_saturday_3.setObjectName("label_saturday_3")
        self.label_saturday_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_saturday_4.setGeometry(QtCore.QRect(x, 290, 111, 71))
        self.label_saturday_4.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_saturday_4.setObjectName("label_saturday_4")
        self.label_saturday_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_saturday_5.setGeometry(QtCore.QRect(x, 370, 111, 71))
        self.label_saturday_5.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_saturday_5.setObjectName("label_saturday_5")
        self.label_saturday_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_saturday_6.setGeometry(QtCore.QRect(x, 450, 111, 71))
        self.label_saturday_6.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_saturday_6.setObjectName("label_saturday_6")
        x = 920
        self.label_sunday_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_sunday_1.setGeometry(QtCore.QRect(x, 50, 111, 71))
        self.label_sunday_1.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_sunday_1.setObjectName("label_sunday_1")
        self.label_sunday_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_sunday_2.setGeometry(QtCore.QRect(x, 130, 111, 71))
        self.label_sunday_2.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_sunday_2.setObjectName("label_sunday_2")
        self.label_sunday_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_sunday_3.setGeometry(QtCore.QRect(x, 210, 111, 71))
        self.label_sunday_3.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_sunday_3.setObjectName("label_sunday_3")
        self.label_sunday_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_sunday_4.setGeometry(QtCore.QRect(x, 290, 111, 71))
        self.label_sunday_4.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_sunday_4.setObjectName("label_sunday_4")
        self.label_sunday_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_sunday_5.setGeometry(QtCore.QRect(x, 370, 111, 71))
        self.label_sunday_5.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_sunday_5.setObjectName("label_sunday_5")
        self.label_sunday_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_sunday_6.setGeometry(QtCore.QRect(x, 450, 111, 71))
        self.label_sunday_6.setStyleSheet("background-color: rgb(183, 219, 213);")
        self.label_sunday_6.setObjectName("label_sunday_6")
        self.meal = QtWidgets.QLabel(self.centralwidget)
        self.meal.setGeometry(QtCore.QRect(10, 0, 111, 41))
        self.meal.setStyleSheet("font: 75 italic 12pt \"Calibri\";")
        self.meal.setObjectName("meal")
        self.monday = QtWidgets.QLabel(self.centralwidget)
        self.monday.setGeometry(QtCore.QRect(140, 0, 111, 41))
        self.monday.setStyleSheet("font: 75 italic 12pt \"Calibri\";")
        self.monday.setObjectName("monday")
        self.friday = QtWidgets.QLabel(self.centralwidget)
        self.friday.setGeometry(QtCore.QRect(660, 0, 111, 41))
        self.friday.setStyleSheet("font: 75 italic 12pt \"Calibri\";")
        self.friday.setObjectName("friday")
        self.thursday = QtWidgets.QLabel(self.centralwidget)
        self.thursday.setGeometry(QtCore.QRect(530, 0, 111, 41))
        self.thursday.setStyleSheet("font: 75 italic 12pt \"Calibri\";")
        self.thursday.setObjectName("thursday")
        self.wednesday = QtWidgets.QLabel(self.centralwidget)
        self.wednesday.setGeometry(QtCore.QRect(400, 0, 111, 41))
        self.wednesday.setStyleSheet("font: 75 italic 12pt \"Calibri\";")
        self.wednesday.setObjectName("wednesday_2")
        self.tuesday = QtWidgets.QLabel(self.centralwidget)
        self.tuesday.setGeometry(QtCore.QRect(270, 0, 111, 41))
        self.tuesday.setStyleSheet("font: 75 italic 12pt \"Calibri\";")
        self.tuesday.setObjectName("tuesday")
        self.sunday = QtWidgets.QLabel(self.centralwidget)
        self.sunday.setGeometry(QtCore.QRect(920, 0, 111, 41))
        self.sunday.setStyleSheet("font: 75 italic 12pt \"Calibri\";")
        self.sunday.setObjectName("sunday")
        self.saturday = QtWidgets.QLabel(self.centralwidget)
        self.saturday.setGeometry(QtCore.QRect(790, 0, 111, 41))
        self.saturday.setStyleSheet("font: 75 italic 12pt \"Calibri\";")
        self.saturday.setObjectName("saturday")
        wednesday.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(wednesday)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 942, 21))
        self.menubar.setObjectName("menubar")
        wednesday.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(wednesday)
        self.statusbar.setObjectName("statusbar")
        wednesday.setStatusBar(self.statusbar)
        self.retranslateUi(wednesday)
        QtCore.QMetaObject.connectSlotsByName(wednesday)

    def retranslateUi(self, wednesday):
        _translate = QtCore.QCoreApplication.translate
        wednesday.setWindowTitle(_translate("wednesday", "MainWindow"))
        self.label_monday_1.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_monday_2.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_monday_3.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_monday_4.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_monday_5.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_monday_6.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_tuesday_1.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_tuesday_2.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_tuesday_3.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_tuesday_4.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_tuesday_5.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_tuesday_6.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_wednesday_1.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_wednesday_2.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_wednesday_3.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_wednesday_4.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_wednesday_5.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_wednesday_6.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_thursday_1.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_thursday_2.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_thursday_3.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_thursday_4.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_thursday_5.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_thursday_6.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_friday_1.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_friday_2.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_friday_3.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_friday_4.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_friday_5.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_friday_6.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_saturday_1.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_saturday_2.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_saturday_3.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_saturday_4.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_saturday_5.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_saturday_6.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_sunday_1.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_sunday_2.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_sunday_3.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_sunday_4.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_sunday_5.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.label_sunday_6.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">-</p></body></html>"))
        self.monday.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">Monday</p></body></html>"))
        self.friday.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">Friday</p></body></html>"))
        self.thursday.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">Thursday</p></body></html>"))
        self.wednesday.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">Wednesday</p></body></html>"))
        self.tuesday.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">Tuesday</p></body></html>"))
        self.sunday.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">Sunday</p></body></html>"))
        self.saturday.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">Saturday</p></body></html>"))
        self.meal.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">Meal</p></body></html>"))
        self.label_bf.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">Breakfast:</p></body></html>"))
        self.label_lunch.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">Lunch:</p></body></html>"))
        self.label_dinner.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">Dinner:</p></body></html>"))
        self.label_snack_1.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">Snack 1:</p></body></html>"))
        self.label_snack_2.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">Snack 2:</p></body></html>"))
        self.label_snack_3.setText(_translate("wednesday", "<html><head/><body><p align=\"center\">Snack 3:</p></body></html>"))

        connection = sqlite3.connect('meal_prep_calculator.db')
        self.df = pd.read_sql_query("SELECT * FROM weekly_meal_plan", connection,index_col='meal')

#this now is a shorter version of writing the text of the recipe into the label
#you can make this loop for every meal or one for all. Than the list got to be larger.
        self.lst_breakfast_days = [[self.label_monday_1, 'monday', self.mon_bf],
                               [self.label_tuesday_1, 'tuesday', self.tue_bf],
                               [self.label_wednesday_1, 'wednesday', self.wed_bf],
                               [self.label_thursday_1, 'thursday', self.thu_bf],
                               [self.label_friday_1, 'friday', self.fri_bf],
                               [self.label_saturday_1, 'saturday', self.sat_bf],
                               [self.label_sunday_1, 'sunday', self.sun_bf]]
        for label in range(7):  # range(7) because lst_lunch_days includes seven days
            breakfast = self.df.loc['breakfast', self.lst_breakfast_days[label][1]]
            self.lst_breakfast_days[label][0].setText(breakfast)
            self.lst_breakfast_days[label][0].setWordWrap(True)
            self.lst_breakfast_days[label][0].show()
            self.lst_breakfast_days[label][0].mouseReleaseEvent = self.lst_breakfast_days[label][2]

        self.lst_lunch_days = [[self.label_monday_2,'monday',self.mon_lunch],
                               [self.label_tuesday_2,'tuesday',self.tue_lunch],
                               [self.label_wednesday_2,'wednesday',self.wed_lunch],
                               [self.label_thursday_2,'thursday',self.thu_lunch],
                               [self.label_friday_2,'friday',self.fri_lunch],
                               [self.label_saturday_2,'saturday',self.sat_lunch],
                               [self.label_sunday_2,'sunday',self.sun_lunch]]
        for label in range(7):  #range(7) because lst_lunch_days includes seven days
            lunch = self.df.loc['lunch',self.lst_lunch_days[label][1]]
            self.lst_lunch_days[label][0].setText(lunch)
            self.lst_lunch_days[label][0].setWordWrap(True)
            self.lst_lunch_days[label][0].show()
            self.lst_lunch_days[label][0].mouseReleaseEvent = self.lst_lunch_days[label][2]

        self.lst_dinner_days = [[self.label_monday_3, 'monday', self.mon_dinner],
                               [self.label_tuesday_3, 'tuesday', self.tue_dinner],
                               [self.label_wednesday_3, 'wednesday', self.wed_dinner],
                               [self.label_thursday_3, 'thursday', self.thu_dinner],
                               [self.label_friday_3, 'friday', self.fri_dinner],
                               [self.label_saturday_3, 'saturday', self.sat_dinner],
                               [self.label_sunday_3, 'sunday', self.sun_dinner]]
        for label in range(7):  # range(7) because lst_lunch_days includes seven days
            dinner = self.df.loc['dinner', self.lst_dinner_days[label][1]]
            self.lst_dinner_days[label][0].setText(dinner)
            self.lst_dinner_days[label][0].setWordWrap(True)
            self.lst_dinner_days[label][0].show()
            self.lst_dinner_days[label][0].mouseReleaseEvent = self.lst_dinner_days[label][2]

        self.lst_snack_3_days = [[self.label_monday_6, 'monday', self.mon_sn_3],
                                 [self.label_tuesday_6, 'tuesday', self.tue_sn_3],
                                 [self.label_wednesday_6, 'wednesday', self.wed_sn_3],
                                 [self.label_thursday_6, 'thursday', self.thu_sn_3],
                                 [self.label_friday_6, 'friday', self.fri_sn_3],
                                 [self.label_saturday_6, 'saturday', self.sat_sn_3],
                                 [self.label_sunday_6, 'sunday', self.sun_sn_3]]
        for label in range(7):  # range(7) because lst_lunch_days includes seven days
            snack_3 = self.df.loc['snack_3', self.lst_snack_3_days[label][1]]
            self.lst_snack_3_days[label][0].setText(snack_3)
            if snack_3 == '-':
                self.lst_snack_3_days[label][0].hide()
                self.label_snack_3.hide()
                wednesday.resize(1072, 500)
            self.lst_snack_3_days[label][0].setWordWrap(True)
            self.lst_snack_3_days[label][0].mouseReleaseEvent = self.lst_snack_3_days[label][2]

        self.lst_snack_2_days = [[self.label_monday_5, 'monday', self.mon_sn_2],
                                 [self.label_tuesday_5, 'tuesday', self.tue_sn_2],
                                 [self.label_wednesday_5, 'wednesday', self.wed_sn_2],
                                 [self.label_thursday_5, 'thursday', self.thu_sn_2],
                                 [self.label_friday_5, 'friday', self.fri_sn_2],
                                 [self.label_saturday_5, 'saturday', self.sat_sn_2],
                                 [self.label_sunday_5, 'sunday', self.sun_sn_2]]
        for label in range(7):  # range(7) because lst_lunch_days includes seven days
            snack_2 = self.df.loc['snack_2', self.lst_snack_2_days[label][1]]
            self.lst_snack_2_days[label][0].setText(snack_2)
            if snack_2 == '-':
                self.lst_snack_2_days[label][0].hide()
                self.label_snack_2.hide()
                wednesday.resize(1072, 400)
            self.lst_snack_2_days[label][0].setWordWrap(True)
            self.lst_snack_2_days[label][0].mouseReleaseEvent = self.lst_snack_2_days[label][2]

        self.lst_snack_1_days = [[self.label_monday_4, 'monday', self.mon_sn_1],
                                 [self.label_tuesday_4, 'tuesday', self.tue_sn_1],
                                 [self.label_wednesday_4, 'wednesday', self.wed_sn_1],
                                 [self.label_thursday_4, 'thursday', self.thu_sn_1],
                                 [self.label_friday_4, 'friday', self.fri_sn_1],
                                 [self.label_saturday_4, 'saturday', self.sat_sn_1],
                                 [self.label_sunday_4, 'sunday', self.sun_sn_1]]
        for label in range(7):  # range(7) because lst_lunch_days includes seven days
            snack_1 = self.df.loc['snack_1', self.lst_snack_1_days[label][1]]
            self.lst_snack_1_days[label][0].setText(snack_1)
            if snack_1 == '-':
                self.lst_snack_1_days[label][0].hide()
                self.label_snack_1.hide()
                wednesday.resize(0, 0)
            self.lst_snack_1_days[label][0].setWordWrap(True)
            self.lst_snack_1_days[label][0].mouseReleaseEvent = self.lst_snack_1_days[label][2]



        #this lists can be used to implement something like a for loop to test if the text is different than '-'. If it is:label.show()
        self.monday_lst = [self.label_monday_1,self.label_monday_2,self.label_monday_3,self.label_monday_4,
                           self.label_monday_5,self.label_monday_6]
        self.tuesday_lst = [self.label_tuesday_1, self.label_tuesday_2, self.label_tuesday_3, self.label_tuesday_4,
                            self.label_tuesday_5, self.label_tuesday_6]
        self.wednesday_lst = [self.label_wednesday_1,self.label_wednesday_2,self.label_wednesday_3,self.label_wednesday_4,
                              self.label_wednesday_5,self.label_wednesday_6]
        self.thursday_lst = [self.label_thursday_1, self.label_thursday_2, self.label_thursday_3, self.label_thursday_4,
                             self.label_thursday_5, self.label_thursday_6]
        self.friday_lst = [self.label_friday_1,self.label_friday_2,self.label_friday_3,self.label_friday_4,
                           self.label_friday_5,self.label_friday_6]


    def show_msgbox_meal(self,event,x=None,y=None):    #messagebox for the label on thursday for dinner
        recipe = literal_eval(self.df[x][y]) #x = Spalte und y = Zeile
        new_line_ingredients = ''
        for item in recipe:
           new_line_ingredients = new_line_ingredients + str(item) + '\n'
        box = QMessageBox.about(self, "Recipe", new_line_ingredients)

    def mon_bf(self,event):     #monday breakfast
        return self.show_msgbox_meal('', 'monday','breakfast_recipe')
    def tue_bf(self,event):
        return self.show_msgbox_meal('', 'tuesday','breakfast_recipe')
    def wed_bf(self,event):
        return self.show_msgbox_meal('', 'wednesday','breakfast_recipe')
    def thu_bf(self,event):
        return self.show_msgbox_meal('', 'thursday','breakfast_recipe')
    def fri_bf(self,event):
        return self.show_msgbox_meal('', 'friday','breakfast_recipe')
    def sat_bf(self,event):
        return self.show_msgbox_meal('', 'saturday','breakfast_recipe')
    def sun_bf(self,event):
        return self.show_msgbox_meal('', 'sunday','breakfast_recipe')
    def mon_lunch(self,event):
        return self.show_msgbox_meal('', 'monday','lunch_recipe')
    def tue_lunch(self,event):
        return self.show_msgbox_meal('', 'tuesday','lunch_recipe')
    def wed_lunch(self,event):
        return self.show_msgbox_meal('','wednesday','lunch_recipe')
    def thu_lunch(self,event):
        return self.show_msgbox_meal('', 'thursday','lunch_recipe')
    def fri_lunch(self,event):
        return self.show_msgbox_meal('', 'friday','lunch_recipe')
    def sat_lunch(self,event):
        return self.show_msgbox_meal('', 'saturday','lunch_recipe')
    def sun_lunch(self,event):
        return self.show_msgbox_meal('', 'sunday','lunch_recipe')
    def mon_dinner(self,event):
        return self.show_msgbox_meal('', 'monday','dinner_recipe')
    def tue_dinner(self,event):
        return self.show_msgbox_meal('', 'tuesday','dinner_recipe')
    def wed_dinner(self,event):
        return self.show_msgbox_meal('','wednesday','dinner_recipe')
    def thu_dinner(self,event):
        return self.show_msgbox_meal('', 'thursday','dinner_recipe')
    def fri_dinner(self,event):
        return self.show_msgbox_meal('', 'friday','dinner_recipe')
    def sat_dinner(self,event):
        return self.show_msgbox_meal('', 'saturday','dinner_recipe')
    def sun_dinner(self,event):
        return self.show_msgbox_meal('', 'sunday','dinner_recipe')
    def mon_sn_1(self,event):     #monday snack 1
        return self.show_msgbox_meal('', 'monday','snack_1_recipe')
    def tue_sn_1(self,event):
        return self.show_msgbox_meal('', 'tuesday','snack_1_recipe')
    def wed_sn_1(self,event):
        return self.show_msgbox_meal('', 'wednesday','snack_1_recipe')
    def thu_sn_1(self,event):
        return self.show_msgbox_meal('', 'thursday','snack_1_recipe')
    def fri_sn_1(self,event):
        return self.show_msgbox_meal('', 'friday','snack_1_recipe')
    def sat_sn_1(self,event):
        return self.show_msgbox_meal('', 'saturday','snack_1_recipe')
    def sun_sn_1(self,event):
        return self.show_msgbox_meal('', 'sunday','snack_1_recipe')
    def mon_sn_2(self,event):
        return self.show_msgbox_meal('', 'monday','snack_2_recipe')
    def tue_sn_2(self,event):
        return self.show_msgbox_meal('', 'tuesday','snack_2_recipe')
    def wed_sn_2(self,event):
        return self.show_msgbox_meal('', 'wednesday','snack_2_recipe')
    def thu_sn_2(self,event):
        return self.show_msgbox_meal('', 'thursday','snack_2_recipe')
    def fri_sn_2(self,event):
        return self.show_msgbox_meal('', 'friday','snack_2_recipe')
    def sat_sn_2(self,event):
        return self.show_msgbox_meal('', 'saturday','snack_2_recipe')
    def sun_sn_2(self,event):
        return self.show_msgbox_meal('', 'sunday','snack_2_recipe')
    def mon_sn_3(self,event):     #monday breakfast
        return self.show_msgbox_meal('', 'monday','snack_3_recipe')
    def tue_sn_3(self,event):
        return self.show_msgbox_meal('', 'tuesday','snack_3_recipe')
    def wed_sn_3(self,event):
        return self.show_msgbox_meal('', 'wednesday','snack_3_recipe')
    def thu_sn_3(self,event):
        return self.show_msgbox_meal('', 'thursday','snack_3_recipe')
    def fri_sn_3(self,event):
        return self.show_msgbox_meal('', 'friday','snack_3_recipe')
    def sat_sn_3(self,event):
        return self.show_msgbox_meal('', 'saturday','snack_3_recipe')
    def sun_sn_3(self,event):
        return self.show_msgbox_meal('', 'sunday','snack_3_recipe')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wednesday = QtWidgets.QMainWindow()
    ui = Ui_wednesday()
    ui.setupUi(wednesday)
    wednesday.show()
    sys.exit(app.exec_())
