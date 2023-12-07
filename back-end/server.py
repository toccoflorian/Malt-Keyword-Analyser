
from flask import Flask, request
from flask_cors import CORS
import json

from database.Database import Jours_table
    

#   #   Flask routes    #   #

app = Flask(__name__)
CORS(app)


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


# ajouter un nouveau jour de données
@app.route("/add_new_jour/", methods=["POST"])
def add_new_jour():
    import data_traitment.data_traitement_functions as data_traitement_functions
    # recevoir les data
    try:
        data = request.get_json()
    except Exception as e:
        print(e.args)
        return json.dumps("Un problème est survenue lors de la réception des données")

    # extraire les informations
    new_jour = data_traitement_functions.extract_data_from_html_string(data)
    if not new_jour:
        print("return if not new_jour:")
        return json.dumps("L'analyse des données n'as donné aucun résultat.")
    
    # enregistrer les informations sur la base de données
    try:
        Jours_table().save_jour(new_jour)
        return json.dumps("Données extraites et enregistrées avec succès. " + str(len(new_jour)) + "mots clés trouvés.")
    except Exception as e:
        print(e.args)
        return json.dumps("Un problème est survenue lors de l'enregistrement des données.")


# recevoir l'ordre d'afficher les graphiques
@app.route("/show_grahique/", methods=["POST", "GET"])
def show_graphique():
    try:
        requete = request.get_json()
        jour_id, choix_valeur_a_afficher = requete
        jours = Jours_table().get_jours()
        [jour.show_dayly_graphique(requete[choix_valeur_a_afficher]) if jour.date == requete[jour_id] else '' for jour in jours]
        return json.dumps(requete[jour_id])
    
    except Exception as e:
        print(e.args)
        return json.dumps("erreur lors de l'affichage des graphiques")


if __name__ == '__main__':
    app.run(host="127.0.0.1",debug=True)