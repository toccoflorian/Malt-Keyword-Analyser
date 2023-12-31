import os
from dotenv import load_dotenv
import mysql.connector as connector

# établir la connexion avec la base de données 
def connect_DB(host, db_name, user_name, password):
    config = {
        'host': host,
        'database': db_name,
        'user': user_name,
        'password': password,
        'raise_on_warnings': True
        }
    try:
        return connector.connect(**config)
    except connector.Error as e:
        print(e.args)

# callback pour déclencher la connexion à la base de données
def connection_callback(): 
    load_dotenv()
    return connect_DB(os.getenv("HOST"), 
                      os.getenv("DB_NAME"), 
                      os.getenv("USER_NAME"), 
                      os.getenv("PASSWORD"))

