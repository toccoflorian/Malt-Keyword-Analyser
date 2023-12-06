
import matplotlib.pyplot as plt


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