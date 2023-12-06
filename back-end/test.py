

# import fonctions
# import database.Database as DB
# jour_table = db.Jours_table()
# jours = jour_table.get_jours()

# for i in jours:
#     print(i.get_fiches())

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time
import requests

def scrap():
    options = Options()
    options.headless = False
    driver = Chrome(options, keep_alive=True)
    driver.get("https://malt.fr")
    cookies = driver.get_cookies()
    print(cookies)
    return driver

connectedUser = {
        "identityId": '6395f66912c3b9655d65ac57',
        "accountId": '6395f66912c3b9655d65ac58',
        "email": 't.florian181181@gmail.com'
    }

driver = scrap()
time.sleep(300)
driver.close()

print('fin')