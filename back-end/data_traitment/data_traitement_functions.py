import time
import datetime

from Jour import Jour, Fiche

# obtenir la date de jour au format 01-01-1970
def get_str_time():
    return datetime.datetime.fromtimestamp(int(time.time())).strftime("%d-%m-%Y")


# convertir les dict de data en objets. 
# data = {"0": {"keyword": ,"apparitions": ,"position": }, "1": {...}}
def create_object(data):
    jour = Jour(get_str_time(), len(data)) #int(time.time())
    for i in data:
        if data[i]["keyword"] != "florian tocco":
            jour.add_fiche(Fiche(data[i]["keyword"], data[i]["apparitions"], data[i]["position"]))
    return jour


# extraire les données du html et retourne un dictionnaire contenant 
# les mots clés. format: {"0": {"keyword": "exemple", "apparitions": 5, "position": 2}, "1": {...}}
def extract_data_from_html_string(data):
    from bs4 import BeautifulSoup as Soup
    import json
    try:
        divs = Soup(data, "html.parser").find_all("div", class_="keywords__row")
        new_jour = {}

        for i, div in enumerate(divs):
            spans = Soup(str(div), "html.parser").find_all("span")
            new_jour[str(i)] = {
                "keyword": spans[0].text, 
                "apparitions": spans[1].text, 
                "position": spans[2].text}
        return new_jour

    except Exception as e:
        return json.dumps("Un problème est survenue lors de l'éxtraxtion des données. Veuillez verifiez votre saisie et réessayer.")