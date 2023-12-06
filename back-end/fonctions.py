import time
import datetime
import matplotlib.pyplot as plt

import database.Database as DB

# obtenir les jours sous forme de liste d'objets
def get_jours():
    jour_table = DB.Jours_table()
    jours = jour_table.get_jours()
    return jours


# obtenir la date de jour au format 01-01-1970
def get_str_time():
    return datetime.datetime.fromtimestamp(int(time.time())).strftime("%d-%m-%Y")

# montrer un graphique tous jours confondus
def show_general_graphique(jours, key="position"):
    
    reverse = True if key == "position" else False
    values = list()
    keys_deja_vues = list()
    for jour in jours:
        for fiche in jour.get_fiches():
            if fiche.keyword not in keys_deja_vues:
                values.append([getattr(fiche, key), fiche.keyword])

    print(values)
    values.sort( key=lambda x: int(x[0]), reverse=reverse )

    plt.barh( [value[1] for value in values], [value[0] for value in values] )
    plt.title("GENERAL GRAPHIQUE - " + key.upper())
    plt.show()