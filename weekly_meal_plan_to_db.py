import pandas as pd
import propose_lunch_function
import propose_dinner_function
import propose_breakfast_function
import propose_snack_function
import groceries_list_into_databank
import sqlite3

#thera are a lot of python files which propose different kinds of meals. They are all run in this file and stored together in a table in the databank.


def save_weekly_meal_plan():
    connection = sqlite3.connect('meal_prep_calculator.db')
    cursor = connection.cursor()

    lst_breakfast = []
    for day in range(7):
        breakfast = propose_breakfast_function.import_recipe()
        lst_breakfast.append(breakfast)

    lst_lunch = []
    for day in range(7):
        lunch = propose_lunch_function.import_recipe()
        lst_lunch.append(lunch)

    lst_dinner = []
    for day in range(7):
        dinner = propose_dinner_function.import_recipe()
        lst_dinner.append(dinner)

    lst_snack = []
    cursor.execute('SELECT snack FROM calorie_data WHERE rowid=1')
    x = cursor.fetchone()
    einzuhaltende_kalorien = x[0]

    snack_anzahl = 0
    if einzuhaltende_kalorien == 0:
        snack_anzahl = 0
    elif 0 < einzuhaltende_kalorien <= 700:
        snack_anzahl = 1
    elif 700 < einzuhaltende_kalorien < 1400:
        snack_anzahl = 2
    elif einzuhaltende_kalorien > 1400:
        snack_anzahl = 3

    for i in range(snack_anzahl):  #y stands for amount of snacks a day
        for day in range(7):
            snack = propose_snack_function.import_recipe()
            lst_snack.append(snack)
    if snack_anzahl == 0:   # if there are not enough snacks to fill out the whole table in the databank, then '-' is used as a placeholder
        for i in range(21):     #amount of '-' thats get put in the databank
            lst_snack.append(['-',['-']])
    elif snack_anzahl == 1:
        for i in range(14):
            lst_snack.append(['-',['-']])
    elif snack_anzahl == 2:
        for i in range(7):
            lst_snack.append(['-',['-']])



    #the dictionary has every meal for the week. So you have every meal in a dicitonary to make further work easier
    dict = {'meal': ['breakfast', 'breakfast_recipe','lunch', 'lunch_recipe', 'dinner', 'dinner_recipe','snack_1','snack_1_recipe','snack_2','snack_2_recipe','snack_3','snack_3_recipe'],
            'monday': [lst_breakfast[0][0], lst_breakfast[0][1],lst_lunch[0][0], lst_lunch[0][1],lst_dinner[0][0], lst_dinner[0][1],lst_snack[0][0],lst_snack[0][1],lst_snack[7][0],lst_snack[7][1],lst_snack[14][0],lst_snack[14][1]],
            'tuesday': [lst_breakfast[1][0], lst_breakfast[1][1],lst_lunch[1][0],lst_lunch[1][1],lst_dinner[1][0], lst_dinner[1][1],lst_snack[1][0],lst_snack[1][1],lst_snack[8][0],lst_snack[8][1],lst_snack[15][0],lst_snack[15][1]],
            'wednesday': [lst_breakfast[2][0], lst_breakfast[2][1],lst_lunch[2][0],lst_lunch[2][1],lst_dinner[2][0], lst_dinner[2][1],lst_snack[2][0],lst_snack[2][1],lst_snack[9][0],lst_snack[9][1],lst_snack[16][0],lst_snack[16][1]],
            'thursday': [lst_breakfast[3][0], lst_breakfast[3][1],lst_lunch[3][0],lst_lunch[3][1],lst_dinner[3][0], lst_dinner[3][1],lst_snack[3][0],lst_snack[3][1],lst_snack[10][0],lst_snack[10][1],lst_snack[17][0],lst_snack[17][1]],
            'friday': [lst_breakfast[4][0], lst_breakfast[4][1],lst_lunch[4][0],lst_lunch[4][1],lst_dinner[4][0], lst_dinner[4][1],lst_snack[4][0],lst_snack[4][1],lst_snack[11][0],lst_snack[11][1],lst_snack[18][0],lst_snack[18][1]],
            'saturday': [lst_breakfast[5][0], lst_breakfast[5][1],lst_lunch[5][0],lst_lunch[5][1],lst_dinner[5][0], lst_dinner[5][1],lst_snack[5][0],lst_snack[5][1],lst_snack[12][0],lst_snack[12][1],lst_snack[19][0],lst_snack[19][1]],
            'sunday': [lst_breakfast[6][0], lst_breakfast[6][1],lst_lunch[6][0],lst_lunch[6][1],lst_dinner[6][0], lst_dinner[6][1],lst_snack[6][0],lst_snack[6][1],lst_snack[13][0],lst_snack[13][1],lst_snack[20][0],lst_snack[20][1]]}
    df = pd.DataFrame(dict)  # index = [0] so that the column 'meal' of the dataframe is the index column


    for x in range(1,13):    #updates the table in the databank
        sql_update_query = """Update weekly_meal_plan SET monday = ?, tuesday = ?, wednesday = ?, thursday = ?, friday = ?, saturday = ?, sunday = ? WHERE rowid = ?"""
        data = (str(dict['monday'][x-1]),str(dict['tuesday'][x-1]),str(dict['wednesday'][x-1]),str(dict['thursday'][x-1]),
                str(dict['friday'][x-1]),str(dict['saturday'][x-1]),str(dict['sunday'][x-1]),x)
        cursor.execute(sql_update_query, data)
        connection.commit()

    cursor.execute("DELETE FROM shoppinglist")      #deletes shoppinglist, so you dont have ingredients in your shoppinglist for example from last week
    connection.commit()
    groceries_list_into_databank.make_db(groceries_list_into_databank.read_from_db())
    cursor.close()
    connection.close()

