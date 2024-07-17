import os
import json
import gspread as gs
from time import sleep
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

# Obter usuário e senha das variáveis de ambiente
username = os.getenv('LINKEDIN_USERNAME')
password = os.getenv('LINKEDIN_PASSWORD')

# URL abaixo procura por 'tech recruiter' em 'Estonia' ou 'Tallin, Estonia', filtrando apenas pessoas e conexões de 2º grau
# URL = "https://www.linkedin.com/search/results/people/?geoUrn=%5B%22115081480%22%2C%22102974008%22%5D&keywords=tech%20recruiter&network=%5B%22S%22%5D&origin=FACETED_SEARCH&sid=4Sb"

# URL abaixo procura por 'tech recruiter' em geral
URL = "https://www.linkedin.com/search/results/people/?keywords=Tech%20Recruiter&origin=SWITCH_SEARCH_VERTICAL&sid=yN)"
LOGIN = "https://www.linkedin.com/login/pt"
c = 0

def login_linkedin(username, password):
    # Abre pagina do LinkedIn para autenticar
    nav.get(LOGIN)
    
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="username"]'))).send_keys(username)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]'))).send_keys(password)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="organic-div"]/form/div[3]/button'))).click()
    
    # Pausar para verificação de duas etapas manual
    input("Por favor, complete a verificação de duas etapas e pressione Enter para continuar...")
    
    nav.get(URL)

def find_connect_buttons():
    return nav.find_elements(By.XPATH, "//button/span[text()='Conectar']")

def click_send_button():
    try:
        send_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button/span[text()="Enviar"]')))
        send_button.click()
    except NoSuchElementException:
        print("Botão 'Send' não encontrado. A janela não apareceu.")
    except Exception as e:
        print(f"Erro ao clicar no botão Send: {e}")

def click_connect_buttons(connect_buttons):
    global c  # Adicione esta linha para usar a variável global 'c'
    if connect_buttons != []:
        for button in connect_buttons:
            if c > 100:
                break
            else:
                try:
                    button.click()
                    sleep(3)  # Aguarde um pouco entre cada clique para evitar problemas de carregamento
                    click_send_button()  # Clique no botão "Send" na janela que aparece
                    c+=1
                    print(c, " conexões enviadas")
                except Exception as e:
                    print(f"Erro ao clicar no botão Connect ou Send: {e}")

def go_to_next_page():
    try:
        sleep(5)
        nav.find_element(By.XPATH, "//button/span[text()='Avançar']").click()
        return True
    except NoSuchElementException:
        print("Botão 'Próxima página' não encontrado. Provavelmente estamos na última página.")
        return False

service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=service)

wait = WebDriverWait(nav, 10)

login_linkedin(username, password)
i = 1
max = 60
while i <= 60:
    print("Page: ", i)
    sleep(10)  # Aguarde um pouco para a página carregar completamente
    print("Aguardei os 10s")
    connect_buttons = find_connect_buttons()
    click_connect_buttons(connect_buttons)
    nav.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    has_next_page = go_to_next_page()
    if not has_next_page:
        break
    i+=1
