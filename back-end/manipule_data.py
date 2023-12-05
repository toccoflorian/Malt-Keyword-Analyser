

import fonctions


jours = fonctions.get_jours()[-1]

# print(jours)
for i in jours.calcul_bests_keyword():
    print(i)

