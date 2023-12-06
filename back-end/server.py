
from flask import Flask, request
from flask_cors import CORS
import json

import data_traitment.data_traitement_functions as data_traitement_functions
from database.Database import Jours_table


    

#   #   Flask routes    #   #

app = Flask(__name__)
CORS(app)


# recevoir nodes extrait par JS depuis le HTML, les convertir et enregistrer les données dans la base de données
@app.route("/js_to_py/", methods=["POST"]) 
def receive_data():
    try:
        data_dict = dict(json.loads(request.get_data().decode("utf-8")))
        jour = data_traitement_functions.create_object(data_dict)
        jours_table = Jours_table()
        jours_table.save_jour(jour)

    except Exception as e:
        print(json.dumps(e.with_traceback))
        return json.dumps("erreur lors de l'envoie des données au serveur ou de l'enregistrement sur la base de données")
    

# envoyer les jours à react
@app.route("/get_jours/", methods=["GET"])
def send_jours_to_react():
    try:
        jours = {}
        for jour in Jours_table().get_jours():
            serializable = jour.get_json_serializable()
            jours[serializable["date"]] = serializable["content"]
        return json.dumps(jours)
    
    except Exception as e:
        print(json.dumps(e.with_traceback))
        return json.dumps("erreur lors de la demande de données")


# recevoir l'ordre d'afficher les graphiques
@app.route("/show_grahique/", methods=["POST", "GET"])
def show_graphique():
    try:
        requete = request.get_json()
        jour_id, choix_valeur_a_afficher = requete
        jours = Jours_table.get_jours()
        [jour.show_dayly_graphique(requete[choix_valeur_a_afficher]) if jour.date == requete[jour_id] else '' for jour in jours]
        return json.dumps(requete[jour_id])
    
    except Exception as e:
        print(json.dumps(e.with_traceback))
        return json.dumps("erreur lors de l'affichage des graphiques")


if __name__ == '__main__':
    app.run(host="127.0.0.1",debug=True)