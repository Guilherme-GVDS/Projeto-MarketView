from selenium.webdriver.common.by import By
import requests
import yfinance as yf
from selenium import webdriver

class Acoes:
    def __init__(self):
        oculto = webdriver.ChromeOptions()
        oculto.add_argument('--headless=new')  # usa o novo modo headless
        oculto.add_argument('--disable-gpu')
        oculto.add_argument('--window-size=1920,1080')
        self.nav = webdriver.Chrome(options=oculto)
        self.buscar_info()
        
    
    def buscar_info(self):
        self.nav.get("https://investidor10.com.br/acoes/")
        self.nav.implicitly_wait(10)
        self.lista_acoes = []




        # Seleciona todas as linhas da tabela de moedas
        acoes = self.nav.find_elements(By.CSS_SELECTOR, "table tbody tr")
        cont = 0
        for acao in acoes:
            if cont <20:
                ticker = acao.find_element(By.CLASS_NAME, "font-semibold").text
                nome = acao.find_element(By.CSS_SELECTOR,'span.group-hover\\:font-semibold').text

                dic_empresa ={f'Nome':nome, 'Ticker': ticker}
                self.lista_acoes.append(dic_empresa)
                #Quando o nome da classe contém caracteres especiais como : é preciso usar \\

                logo  = acao.find_element(By.CLASS_NAME, 'ticker-img').get_attribute('src')
                header = {"User-Agent": "Mozilla/5.0"}
                logo_file = requests.get(logo, headers=header).content        
                with open(f"imagens/{ticker}.jpg", "wb") as f:
                    f.write(logo_file)
                #print(f'{nome}  {ticker}')
                cont+=1

            else:
                self.nav.quit()
                break
    
        self.lista_cotacao_acoes = []
        for acao in self.lista_acoes:
            ticker_sa = acao['Ticker']+'.SA'
            
            tk = yf.Ticker(ticker_sa)
            info = tk.info
            nome = acao['Nome']
            ticker = acao['Ticker']
            ultimo_preco = str(info.get("regularMarketPrice", None))
            ultimo_preco = ('R$ '+ultimo_preco)
            dic_empresa ={f'Nome':nome, 'Ticker': ticker, 'Cotação': ultimo_preco}
            self.lista_cotacao_acoes.append(dic_empresa)
        print(self.lista_cotacao_acoes)

    def retornar_lista(self):
        return self.lista_cotacao_acoes
    

    

