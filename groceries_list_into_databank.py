import sqlite3
from ast import literal_eval
import re




def read_from_db():
    connection = sqlite3.connect('meal_prep_calculator.db')
    cursor = connection.cursor()
    read = """SELECT * FROM weekly_meal_plan WHERE (rowid-1)%2"""   #iterates through the ingredients in the databank table "weekly meal plan"
    cursor.execute(read)
    take = cursor.fetchall()
    monday = [el[1] for el in take]
    tuesday = [el[2] for el in take]
    wednesday = [el[3] for el in take]
    thursday = [el[4] for el in take]
    friday = [el[5] for el in take]
    saturday = [el[6] for el in take]
    sunday = [el[7] for el in take]
    all_together = monday + tuesday + wednesday + thursday + friday + saturday + sunday     #all the iterated ingredients are stored in a list
    cursor.close()
    connection.close()
    return all_together


def make_db(list_of_ingredients):   #here the shoppingslist is created. If there are two ingredients with the same name
    # the code sums up the amount of the ingredient for the hole week. So no ingredients with the exact same name pops up twice in the list
    connection = sqlite3.connect('meal_prep_calculator.db')
    cursor = connection.cursor()
    for menu in list_of_ingredients:
        ingredients = literal_eval(menu)
        for ingredient in ingredients:
            if ingredient == '-':   #in an other code we helped us with blank information by inserting '-'. These '-' should not be displayed in the shoppinglist. Therefore they are sorted out by this if-Statement
                pass
            else:
                amount_parent = re.findall('[+-]?\d+[,.]?\d*', ingredient)
                try:
                    amount = amount_parent[0]
                except:
                    amount = 1
                amount_plus_space = str(amount) + ' '
                ingredient_text = ingredient.replace(amount_plus_space,'')
                read = "SELECT * FROM shoppinglist WHERE ingredient = ?"
                data = [ingredient_text]
                cursor.execute(read,data)
                entry = cursor.fetchone()
                if entry is None:   #if ingredient is not in groceries_list yet
                    read = "INSERT INTO shoppinglist VALUES(?,?)"
                    data = (amount,ingredient_text)
                    cursor.execute(read,data)
                    connection.commit()
                else:   #if ingredient is already in shoppinglist
                    read = 'SELECT amount FROM shoppinglist WHERE ingredient=?'
                    data = [ingredient_text]
                    cursor.execute(read,data)
                    amount_parent_in_db = cursor.fetchone()
                    amount_in_db = int(amount_parent_in_db[0])
                    amount = amount_in_db + int(amount)
                    read = "UPDATE shoppinglist SET amount = ? WHERE ingredient = ?"
                    data = (amount,ingredient_text)
                    cursor.execute(read,data)
                    connection.commit()
    cursor.close()
    connection.close()



