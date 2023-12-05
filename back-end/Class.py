import datetime
import matplotlib.pyplot as plt

# Jour correspont à un jour de données avec sa date, son set de fiches et son id
class Jour():
    def __init__(self, date, nombre_de_Fiche):
        self.id = date
        self.date = datetime.datetime.fromtimestamp(date).strftime("%d-%m-%Y")
        self.nombre_de_Fiche = nombre_de_Fiche
        self.fiches = set()

    # ajouter une fiche aux set de fiches
    def add_fiche(self, fiche) -> None:
        self.fiches.add(fiche)
    
    # obtenir toutes les fiches sous forme de list
    def get_fiches(self) -> list:
        fiches = list()
        for fiche in self.fiches:
            fiches.append(fiche)
        return fiches
    
    # calculer les 5 meilleurs mots clé par position, score, nombre d'apparitions 
    def get_bests_keyword(self) -> dict:
        fiches = self.get_fiches()

        fiches.sort(key=lambda fiche: int(fiche.get_fiche_data()["nombre_apparition"]), reverse=True)
        top_apparition = [fiche.get_fiche_data() for fiche in fiches[:5]]

        fiches.sort(key=lambda fiche: int(fiche.get_fiche_data()["position"]))
        top_position = [fiche.get_fiche_data() for fiche in fiches[:5]]

        fiches.sort(key=lambda fiche: float(fiche.get_fiche_data()["score"]), reverse=True)
        top_score = [fiche.get_fiche_data() for fiche in fiches[:5]]
        
        return {"top_apparition": top_apparition, "top_position": top_position, "top_score": top_score}

    
    # afficher un graphique du jour, choix possible: "position", "nombre_apparition", "score"
    def show_dayly_graphique(self, key="position", reverse=False) -> None:
        if key != "score":
            reverse = True if key == "position" else False
        values = list()
        keys_deja_vues = list()
        
        for fiche in self.fiches:
            if fiche.keyword not in keys_deja_vues:
                values.append([getattr(fiche, key), fiche.keyword])

        values.sort( key=lambda x: float(x[0]), reverse=reverse )

        for index, value in enumerate(values):
            plt.barh(value[1], value[0])
            plt.text(value[0], index, value[0])
        # plt.barh( [value[1] for value in values], [value[0] for value in values] )
        plt.title(self.date + " - " + key.upper())
        # plt.legend()
        plt.show()


# Fiche correspont à un mot clé avec sa position, son apparition et son score
class Fiche():
    def __init__(self, keyword, nombre_apparition, position) -> None:
        self.keyword = keyword
        self.nombre_apparition = nombre_apparition
        self.position = position
        self.score = self.get_score()
    
    # obtenir la fiche sous forme de dict
    def get_fiche_data(self) -> dict:
        return {"keyword": self.keyword,
                "nombre_apparition": self.nombre_apparition,
                "position": self.position,
                "score": self.score}
    
    # obtenir le score de la fiche selon position et appariton
    def get_score(self) -> float:
        return round((1 / int(self.position)) * int(self.nombre_apparition) * 10, 3)
    
    # montrer un graphique apparition / position
    def show_ratio_graphique(self) -> None:
        plt.plot([0, self.nombre_apparition], [0, self.position])
        plt.ylabel("Nombre d'apparitions")
        plt.xlabel("Psition")
        plt.title(self.keyword)
        plt.show()
