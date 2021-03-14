import pandas as pd
import propose_meal_function
import sqlite3
import propose_breakfast_function
import propose_snack_function
#snacks have to be integrated
#how many snacks shall we integrate?

# sometimes there is an error with the propose_dinner_function. If it is run again, it may run. The error must be corrected.

# gets the meals for the whole week and stores them in a csv file. In here right now it gets lunch and dinner.
# import function from Frank for the part of dinner. When bigger than 0 then do this.

lst_breakfast = []
for da in range(7):
    breakfast = propose_breakfast_function.import_recipe()
    lst_breakfast.append(breakfast)

lst_lunch = []
for day in range(7):
    lunch = propose_meal_function.import_recipe()
    lst_lunch.append(lunch)

lst_dinner = []
for day in range(7):
    dinner = propose_meal_function.import_recipe()
    lst_dinner.append(dinner)

lst_snack = []
y = 0 #here must be the amout of snacks per day (between 0 and 3)
for i in range(y):  #y stands for amount of snacks a day
    for day in range(7):
        snack = propose_snack_function.import_recipe()
        lst_snack.append(snack)
if y == 0:
    for i in range(21):     #amount of '-' thats get put in the databank
        lst_snack.append(['-',['-']])
elif y == 1:
    for i in range(14):
        lst_snack.append(['-',['-']])
elif y == 2:
    for i in range(7):
        lst_snack.append(['-',['-']])



# still needs to implement snacks in here. Maybe just add one list and make it like this: lst_snack[0][0],lst_snack[0][1],lst_snack[1][0],lst_snack[1][1],lst_snack[2][0],lst_snack[2][1],...
#and on tuesday you start with lst_snack[3][0],lst_snack[3][1] and so on...
dict = {'meal': ['breakfast', 'breakfast_recipe','lunch', 'lunch_recipe', 'dinner', 'dinner_recipe','snack_1','snack_1_recipe','snack_2','snack_2_recipe','snack_3','snack_3_recipe'],
        'monday': [lst_breakfast[0][0], lst_breakfast[0][1],lst_lunch[0][0], lst_lunch[0][1],lst_dinner[0][0], lst_dinner[0][1],lst_snack[0][0],lst_snack[0][1],lst_snack[7][0],lst_snack[7][1],lst_snack[14][0],lst_snack[14][1]],
        'tuesday': [lst_breakfast[1][0], lst_breakfast[1][1],lst_lunch[1][0],lst_lunch[1][1],lst_dinner[1][0], lst_dinner[1][1],lst_snack[1][0],lst_snack[1][1],lst_snack[8][0],lst_snack[8][1],lst_snack[15][0],lst_snack[15][1]],
        'wednesday': [lst_breakfast[2][0], lst_breakfast[2][1],lst_lunch[2][0],lst_lunch[2][1],lst_dinner[2][0], lst_dinner[2][1],lst_snack[2][0],lst_snack[2][1],lst_snack[9][0],lst_snack[9][1],lst_snack[16][0],lst_snack[16][1]],
        'thursday': [lst_breakfast[3][0], lst_breakfast[3][1],lst_lunch[3][0],lst_lunch[3][1],lst_dinner[3][0], lst_dinner[3][1],lst_snack[3][0],lst_snack[3][1],lst_snack[10][0],lst_snack[10][1],lst_snack[17][0],lst_snack[17][1]],
        'friday': [lst_breakfast[4][0], lst_breakfast[4][1],lst_lunch[4][0],lst_lunch[4][1],lst_dinner[4][0], lst_dinner[4][1],lst_snack[4][0],lst_snack[4][1],lst_snack[11][0],lst_snack[11][1],lst_snack[18][0],lst_snack[18][1]],
        'saturday': [lst_breakfast[5][0], lst_breakfast[5][1],lst_lunch[5][0],lst_lunch[5][1],lst_dinner[5][0], lst_dinner[5][1],lst_snack[5][0],lst_snack[5][1],lst_snack[12][0],lst_snack[12][1],lst_snack[19][0],lst_snack[19][1]],
        'sunday': [lst_breakfast[6][0], lst_breakfast[6][1],lst_lunch[6][0],lst_lunch[6][1],lst_dinner[6][0], lst_dinner[6][1],lst_snack[6][0],lst_snack[6][1],lst_snack[13][0],lst_snack[13][1],lst_snack[20][0],lst_snack[20][1]]}
# print(dict)
df = pd.DataFrame(dict)  # index = [0] so that the column 'meal' of the dataframe is the index column

connection = sqlite3.connect('meal_prep_calculator.db')     #name der Datenbank
cursor = connection.cursor()

for x in range(1,13):    #updates the table from row 1 to 4
    sql_update_query = """Update weekly_meal_plan SET monday = ?, tuesday = ?, wednesday = ?, thursday = ?, friday = ?, saturday = ?, sunday = ? WHERE rowid = ?"""
    data = (str(dict['monday'][x-1]),str(dict['tuesday'][x-1]),str(dict['wednesday'][x-1]),str(dict['thursday'][x-1]),
            str(dict['friday'][x-1]),str(dict['saturday'][x-1]),str(dict['sunday'][x-1]),x)
    cursor.execute(sql_update_query, data)
    connection.commit()

cursor.close()
connection.close()