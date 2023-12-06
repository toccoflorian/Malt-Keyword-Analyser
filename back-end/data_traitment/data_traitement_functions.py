import time
import datetime

from Jour import Jour, Fiche

# obtenir la date de jour au format 01-01-1970
def get_str_time():
    return datetime.datetime.fromtimestamp(int(time.time())).strftime("%d-%m-%Y")


# convertir les dict de data en objets
def create_object(data):
    jour = Jour(get_str_time(), len(data)) #int(time.time())
    for i in data:
        if data[i]["keyWord"] != "florian tocco":
            jour.add_fiche(Fiche(data[i]["keyWord"], data[i]["nombre"], data[i]["position"]))
    return jour