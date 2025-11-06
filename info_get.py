from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



navegador = webdriver.Chrome()
navegador.get('https://coinmarketcap.com/')

buscar_acao = navegador.find_elements(By.CLASS_NAME,'cmc-link')
for elemento in buscar_acao:
    preco = elemento.find_element(By.CSS_SELECTOR, "p.coin-item-name")
    print (preco.text)