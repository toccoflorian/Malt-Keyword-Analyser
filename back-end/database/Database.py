import database.connection as connection_clbk
import json

from Jour import Jour, Fiche

class Database():
    def __init__(self) -> None:
        self.__cursor = None
        self.__connection = None

    # établir la connexion à la base de données
    def open_connection(self) -> None:
        try:
            self.__connection = connection_clbk.connection_callback()
            self.__cursor = self.__connection.cursor()
            return self.__connection, self.__cursor
    
        except Exception as e:
            print(e)

    # fermer la connexion à la base de données
    def close_connection(self):
        try:
            self.__cursor.close(), self.__connection.close()
            self.__cursor, self.__connection = None, None

        except Exception as e:
            print("ligne 24:", e) 



class User_table(Database):
    def __init__(self) -> None:
        super().__init__()

# table de base de données contenant tout ce qui concerne les mots clés
class Jours_table(Database):
    DB_TABLE = "`malt-keyword-analyser`.`jours`"
    DB_KEYWORDS_BANK = "`malt-keyword-analyser`.`keyword_bank`"
    def __init__(self) -> None:
        super().__init__()

    # executer une requete SQL / 'commit' si enregistrement de données 
    def execute_SQL_request(self, request, args=None, commit=None):
        print(commit)
        try:
            connection, cursor = self.open_connection()
            result = cursor.execute(request, args)
            if commit:
                result = connection.commit()
            self.close_connection()
            return result
        
        except Exception as e:
            print(e.args)


    # enregistrer un jour de données sur la base de données
    def save_jour(self, jour):
        print("start")
        fiches = list()
        for word in jour.get_fiches():
            fiches.append({'keyword': word.keyword, 'apparitions': word.nombre_apparition, 'position': word.position})
        result = self.execute_SQL_request("INSERT INTO " + self.DB_TABLE + " (`date`, `fiches`)  VALUES (%s, %s)", (jour.date, json.dumps(fiches)), True)
        print("stop", result)

    
    # obtenir les objets Jour
    def get_jours(self):
        try:
            jours = []
            connection, cursor = self.open_connection()
            cursor.execute("SELECT * FROM " + self.DB_TABLE)
            datas = cursor.fetchall()
            for data in datas:
                date = data[1]
                fiches = json.loads(data[2])
                id = data[0]
                jour = Jour(date, len(fiches), id)
                for fiche in fiches:
                    jour.add_fiche(Fiche(fiche["keyword"], fiche["apparitions"], fiche["position"],))
                jours.append(jour)
            self.close_connection()
            return jours

        except Exception as e:
            print(e)
            

    # créer une table jours sur la base de données
    def create_jours_table(self):
        self.execute_SQL_request("CREATE TABLE " + self.DB_TABLE + """ (
                                    `id` INT NOT NULL AUTO_INCREMENT,
                                    `date` VARCHAR(45) UNIQUE NULL,
                                    `fiches` JSON NULL,
                                    PRIMARY KEY (`id`)); UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE);""")
        
    # créer une table keyword_bank sur la base de données
    def create_keyword_bank_table(self):
        self.execute_SQL_request("CREATE TABLE " + self.DB_KEYWORDS_BANK + """ (
                                    `id` INT NOT NULL AUTO_INCREMENT,
                                    `keyword` VARCHAR(45) NOT NULL,
                                    `apparitions_totales` INT NOT NULL,
                                    `position_moyenne` INT NOT NULL,
                                    `score_moyen` FLOAT NOT NULL,
                                    `dates` BLOB NOT NULL,
                                    PRIMARY KEY (`id`), UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE);""")

    # supprimer une table de la base de données
    def delete_table(self, table):
        self.open_connection()
        self.get_cursor().execute("DROP TABLE " + table)
        self.close_connection()

