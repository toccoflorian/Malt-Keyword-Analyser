
from flask import Flask, request
from flask_cors import CORS
import json

import fonctions
from Jour import Fiche, Jour
from database.Database import Jours_table


# convertir les bytes de data en dict
def convert_data_to_dict(data):
    d = dict(json.loads(data.decode("utf-8")))
    return d

# convertir les dict de data en objets
def create_object(data):
    jour = Jour(fonctions.get_str_time(), len(data)) #int(time.time())
    for i in data:
        if data[i]["keyWord"] != "florian tocco":
            jour.add_fiche(Fiche(data[i]["keyWord"], data[i]["nombre"], data[i]["position"]))
    return jour

# transformer la liste d'objets en format serialisable json
def object_to_jsonifiable():
    jours = fonctions.get_jours()
    jours_jsonifiable = dict()
    for jour in jours:
        jour_list = list()
        for fiche in jour.get_fiches():
            jour_list.append(fiche.get_fiche_data())
        jours_jsonifiable[jour.date] = {"id": jour.id, "fiches": jour_list, "bests": jour.get_bests_keyword()}
    return jours_jsonifiable

# sauvegarder les objets py avec shelve
def save_on_database(jour):
    try:
        jours_table = Jours_table()
        jours_table.save_jour(jour)

    except Exception as e:
        print(e)


    

#   #   Flask routes    #   #

app = Flask(__name__)
CORS(app)

# recevoir nodes extrait par JS depuis le HTML
@app.route("/js_to_py/", methods=["POST"]) 
def receive_data():
    try:
        data_dict = convert_data_to_dict(request.get_data())
        jours = fonctions.create_object(data_dict)
        save_on_database(jours)
        return "OK"
    
    except Exception as e:
        return json.dumps(e.with_traceback)
    
# envoyer les jours à react
@app.route("/get_jours/", methods=["GET"])
def send_jours_to_react():
    try:
        jours = json.dumps(object_to_jsonifiable())
        return jours
    except Exception as e:
        return json.dumps(e.with_traceback)

# recevoir l'ordre d'afficher les graphiques
@app.route("/show_grahique/", methods=["POST", "GET"])
def show_graphique():
    try:
        requete = request.get_json()
        jour_id, choix_valeur_a_afficher = requete
        jours = fonctions.get_jours()
        [jour.show_dayly_graphique(requete[choix_valeur_a_afficher]) if jour.date == requete[jour_id] else '' for jour in jours]
        return json.dumps(requete[jour_id])
    except Exception as e:
        return json.dumps(e.with_traceback)

if __name__ == '__main__':
    app.run(host="127.0.0.1",debug=True)