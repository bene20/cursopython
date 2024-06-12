import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TIME_TO_WAIT=10

def make_chrome_browser(*options: str) -> webdriver.Chrome:
    ROOT_DIR: str = os.path.dirname(__file__)
    CHROME_DRIVER_PATH: str = ROOT_DIR + '/drivers/chromedriver'

    if not os.path.exists(CHROME_DRIVER_PATH):
        raise FileNotFoundError('Driver do Chrome não encontrado em', CHROME_DRIVER_PATH)

    chrome_service = Service(executable_path=CHROME_DRIVER_PATH)

    chrome_options = webdriver.ChromeOptions()
    if options is not None:
        for option in options:
            print('Adicionando opção', option)
            chrome_options.add_argument(option)

    chrome_browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    
    return chrome_browser

# Abrindo o Chrome browser
url: str = 'https://www.google.com/'
options= ()
browser = make_chrome_browser(*options)
browser.get(url)

# Aguardando o input de pesquisa (cujo atributo 'name' é igual a 'q') ser carregado
search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
    EC.presence_of_element_located((By.NAME, 'q'))
)

# Digitando um texto na caixa de pesquisa e pressionando o 'Enter'
search_input.send_keys('Olá mundo')
search_input.send_keys(Keys.ENTER)

# Clicando no primeiro link da lista d resultados
results = browser.find_element(By.ID, 'search') # A div com o resultados tem ID igual a 'search'
links = results.find_elements(By.TAG_NAME, 'a') # dentro de results, quero encontrar todas as tags de link (nome 'a')
links[0].click() # Clicando no primeiro link da lista de links obtidos
time.sleep(2)