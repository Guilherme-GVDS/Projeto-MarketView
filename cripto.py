from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from pathlib import Path


class Cripto:

    def __init__(self):
        oculto = webdriver.ChromeOptions()
        oculto.add_argument('--headless=new')  # usa o novo modo headless
        oculto.add_argument('--disable-gpu')
        oculto.add_argument('--window-size=1920,1080')
        self.nav = webdriver.Chrome(options=oculto)
        self.buscar_info()


    def buscar_info(self):
    
        self.nav.get("https://coinmarketcap.com/")
        self.nav.implicitly_wait(10)
            
        # Seleciona todas as linhas da tabela de moedas
        criptos = self.nav.find_elements(By.CSS_SELECTOR, "table tbody tr")
        cont = 0
        self.lista_cotacao_cripto = []
        for cripto in criptos:
            if cont <20:
                nome = cripto.find_element(By.CSS_SELECTOR, "p.coin-item-name").text
                simbolo = cripto.find_element(By.CSS_SELECTOR, "p.coin-item-symbol").text
                preco = cripto.find_element(By.CSS_SELECTOR, "div.eAphWs").text
                logo  = cripto.find_element(By.CSS_SELECTOR, 'img.coin-logo').get_attribute('src')
                logo_file = requests.get(logo).content
                with open(f"imagens/{simbolo}.jpg", "wb") as f:
                    f.write(logo_file)
                dic_criptos ={f'Nome':nome, 'Ticker': simbolo, 'Cotação': preco}
                self.lista_cotacao_cripto.append(dic_criptos)
                cont+=1
            else:
                self.nav.quit()
                break

    def retornar_lista(self):
        return self.lista_cotacao_cripto
            


Cripto()
