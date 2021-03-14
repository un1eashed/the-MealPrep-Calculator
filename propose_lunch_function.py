import re
import random
from ast import literal_eval
import sqlite3

#commentaries please look into propose_dinner_function
# the code is mostly identical. The references to the databank are different.



connection = sqlite3.connect('meal_prep_calculator.db')
cursor = connection.cursor()



def import_recipe():
    cursor.execute('SELECT lunch FROM calorie_data WHERE rowid=1')
    x = cursor.fetchone()
    einzuhaltende_kalorien = x[0]

    cursor.execute("SELECT name FROM dinner_lunch_recipes")
    zufall_zahl = random.randint(1,int(len(cursor.fetchall())))
    name = "SELECT name FROM dinner_lunch_recipes WHERE rowid=?"
    cursor.execute(name,[zufall_zahl])
    zufall_name = cursor.fetchone()[0]

    ingredients = "SELECT ingredients FROM dinner_lunch_recipes WHERE rowid=?"
    cursor.execute(ingredients,[zufall_zahl])
    zeile_ingredients = cursor.fetchone()[0]
    zutatenliste_unbearbeitet = literal_eval(zeile_ingredients)
    zutatenliste = []
    for amount in zutatenliste_unbearbeitet:
        specification = amount.replace('k.A.','eine Priese')
        zutatenliste.append(specification)
    kalories = "SELECT kcal FROM dinner_lunch_recipes WHERE rowid=?"
    cursor.execute(kalories,[zufall_zahl])
    kalorien = cursor.fetchone()[0]
    multiplikator_kalorien = einzuhaltende_kalorien/kalorien    #berechnet inwieweit die Portion vergrößert werden kann

    angepasste_liste = []   #in diese Liste wird das neue Rezept gefüllt
    for i in zutatenliste: #nimmt die einzelnen Zutaten, extrahiert die Zahl, multipliziert diese mit dem Faktor aus dem Kalorienverbrauch
        #und führt diese den Rezepten wieder zu.
        anzupassender_wert = re.findall('[+-]?\d+[,.]?\d*', i) #wert aus Ursprung extrahieren
        try:
            anzupassender_wert = int(anzupassender_wert[0]) #in integer umgewandelt und in das erste Element der Liste gepackt, weil re.findall eine Liste erstellt
            angepasster_wert = anzupassender_wert * multiplikator_kalorien
            angepasster_wert = round(angepasster_wert,
                                     0)  # rundet den agepassten Wert damit nicht viele Kommazahlen hier stehen
            angepasster_wert = int(angepasster_wert)  # macht einen integer Wert daraus um Zahlen wie 220.0 zu vermeiden
            i = i.replace(str(anzupassender_wert),
                          str(angepasster_wert))  # fügt die Zahlen in das urspüngliche Rezept ein
            angepasste_liste.append(i)  # fügt alles wieder zusammen
        except:
            angepasste_liste.append(i)  #fügt alles wieder zusammen
    name_und_rezept = [zufall_name,angepasste_liste]


    return name_und_rezept
