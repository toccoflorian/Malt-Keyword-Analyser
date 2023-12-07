

# import fonctions
# import database.Database as DB
# jour_table = db.Jours_table()
# jours = jour_table.get_jours()

# for i in jours:
#     print(i.get_fiches())

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import requests

def scrap(profil_path):
    options = Options()
    # options.add_argument("--headless")
    options.add_argument(f"user-data-dir={profil_path}")
    driver = Chrome( options=options)
    driver.get("https://malt.fr")
    # cookies = driver.get_cookies()
    # print(cookies)
    return driver

# connectedUser = {
#         "identityId": '6395f66912c3b9655d65ac57',
#         "accountId": '6395f66912c3b9655d65ac58',
#         "email": 't.florian181181@gmail.com'
#     }

profil_path = "C:\\Users\\FLO\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3"

# driver = scrap(profil_path)
import requests
config =     {
        "id": "80259e18-1663-4c37-9f95-b5bb65c8d259",
        "name": "malt-keyword-analyser",
        "tokenHint": "",
        "note": "",
        "createdAt": "2023-12-07T11:31:11Z"
    }

# L'URL de l'endpoint
url = f"https://www.malt.fr"
# https://www.malt.fr/s/tags/api-
# Ajoutez ici les en-têtes nécessaires, comme les cookies ou les tokens d'authentification
headers = {
    # "Cookie": "malt-visitorId=e1851531-183e-461a-bcdb-6f4f8fdb3ef4; _gcl_au=1.1.298117618.1700757072; OptanonAlertBoxClosed=2023-11-23T16:31:20.321Z; remember-me=dC5mbG9yaWFuMTgxMTgxJTQwZ21haWwuY29tOjE3MDMwNjg3NDk5NDA6NjBhMThmYWI0OWI0YWZlZjRiMmE1ZmMwMTYxZDU1OGI; cf_clearance=5_mjLWjB.Ks4dXc662xu7UpNhkQgOIB0WkdaUoPiyos-1701942789-0-1-3e86653b.9f355936.69873adb-0.2.1701942789; malt-campaigns=new-signup-client-workflow; malt-variations=new-signup-client-workflow-enabled; XSRF-TOKEN=4961ba5a-3d8e-4715-8e17-1a1559cf74b1; SESSION=YzI1OWJmZjItODRlNy00OThjLWE5MmQtOTEyZTk1OTE3NTIw; hopsi=6395f66912c3b9655d65ac57; __cfruid=068cc52b0226a25756711490e25bc375a90af502-1701947861; i18n=fr-FR; hopbd=true; __cf_bm=KtdJr_3PAvPIhdk3PFbtt9MHoNGeKYCbsiC_03IWyYc-1701951506-0-AfJdsTdKoAeiMWgUMR2HjA/c1BzDwS2r1f996V52/VlZarw03CnX40BvAZHJNRd1UCo+I4FpyzAZMeSTA4AK9Rk/SIbMKnP2xkoXInjIpa0/; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Dec+07+2023+13%3A25%3A07+GMT%2B0100+(heure+normale+d%E2%80%99Europe+centrale)&version=202211.2.0&isIABGlobal=false&hosts=&consentId=f27aa7bd-c17a-4422-a3c7-81415de24a21&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A0%2CC0002%3A0%2CC0004%3A0%2CC0005%3A0&AwaitingReconsent=false&geolocation=%3B",
    # # "User-Agent": "6pDvZ9Q8q7BVa8gbIn62PRi8QT8x73jP",
    # "id": "80259e18-1663-4c37-9f95-b5bb65c8d259",
    # "name": "malt-keyword-analyser",
    # "tokenHint": "6pDvZ9Q8q7BVa8gbIn62PRi8QT8x73jP",
    # "note": "",
    # "createdAt": "2023-12-07T11:31:11Z"
}

response = requests.request("GET", url, headers=headers)

# Vérifier le statut de la réponse
if response.status_code == 200:
    # Traiter la réponse ici
    print(response.text)
else:
    print(f"Erreur: {response.status_code}")


# time.sleep(50)
# try:
#     # Attendre que le bouton soit chargé
#     WebDriverWait(driver, 10).until(
        
#         EC.presence_of_element_located((By.CSS_SELECTOR, "#onetrust-accept-btn-handler"))
#     )
#     time.sleep(5)
#     # Trouver le bouton par son ID et cliquer dessus
#     bouton = driver.find_element(By.CSS_SELECTOR, "#onetrust-accept-btn-handler")
#     time.sleep(5)
#     bouton.click()

    # Autres actions...

# finally:
#     time.sleep(300)
#     driver.quit()

# driver.close()

# print('fin')


# <button class="onetrust-close-btn-handler banner-close-button ot-close-link">Continuer sans accepter</button>

