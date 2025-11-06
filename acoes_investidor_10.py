from selenium import webdriver
from selenium.webdriver.common.by import By
import requests, os
from pathlib import Path



class Acao_selenium:
    def __init__(self,navegador):
        self.nav = navegador
        #self.nav = webdriver.Chrome()
        self.buscar_info()
        
    
    def buscar_info(self):
        self.nav.get("https://investidor10.com.br/acoes/")
        self.nav.implicitly_wait(10)
        lista_acoes = []




        # Seleciona todas as linhas da tabela de moedas
        acoes = self.nav.find_elements(By.CSS_SELECTOR, "table tbody tr")
        cont = 0
        for acao in acoes:
            if cont <10:
                ticker = acao.find_element(By.CLASS_NAME, "font-semibold").text
                empresa = acao.find_element(By.CSS_SELECTOR,'span.group-hover\\:font-semibold').text

                dic_empresa ={f'Empresa':{empresa}, 'Ticker': {ticker}}
                lista_acoes.append(dic_empresa)
                #Quando o nome da classe contém caracteres especiais como : é preciso usar \\

                logo  = acao.find_element(By.CLASS_NAME, 'ticker-img').get_attribute('src')
                header = {"User-Agent": "Mozilla/5.0"}
                logo_file = requests.get(logo, headers=header).content        
                with open(f"imagens/{ticker}.jpg", "wb") as f:
                    f.write(logo_file)
                print(f"{empresa} {ticker}")
                cont+=1

            else:
                break
        print(lista_acoes[0]['Empresa'])

        pasta_imagens = Path('imagens')
        for arquivo in pasta_imagens.glob('*.jpg'):
            os.remove(arquivo)


        self.nav.quit()
