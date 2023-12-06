

import fonctions
import database.Database as DB
jour_table = db.Jours_table()
jours = jour_table.get_jours()

for i in jours:
    print(i.get_fiches())