from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from pathlib import Path

navegador = webdriver.Chrome()
navegador.get("https://coinmarketcap.com/")
navegador.implicitly_wait(10)
    
# Seleciona todas as linhas da tabela de moedas
criptos = navegador.find_elements(By.CSS_SELECTOR, "table tbody tr")
cont = 0
lista_cotacao_cripto = []
for cripto in criptos:
    if cont <10:
        nome = cripto.find_element(By.CSS_SELECTOR, "p.coin-item-name").text
        simbolo = cripto.find_element(By.CSS_SELECTOR, "p.coin-item-symbol").text
        preco = cripto.find_element(By.CSS_SELECTOR, "div.eAphWs").text
        logo  = cripto.find_element(By.CSS_SELECTOR, 'img.coin-logo').get_attribute('src')
        logo_file = requests.get(logo).content
        with open(f"imagens/{nome}.png", "wb") as f:
            f.write(logo_file)
        dic_empresa ={f'Nome':nome, 'Ticker': simbolo, 'Cotação': preco}
        lista_cotacao_cripto.append(dic_empresa)
        print(lista_cotacao_cripto)
        cont+=1

    else:
        break
    



navegador.quit()
