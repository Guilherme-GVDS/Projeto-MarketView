from acoes_investidor_10 import Acao_selenium
import customtkinter
from selenium import webdriver

if __name__ == '__main__':
    login = webdriver.Chrome()
    Acao_selenium(login)



