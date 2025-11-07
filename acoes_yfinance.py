import yfinance as yf


class Acao_yf:
    def __init__(self,):
        #self.lista_acoes = lista_acoes
        self.buscar_info()


    def buscar_info(self):
        lista_acoes = [{'Empresa': 'Petrobrás', 'Ticker': 'PETR4'}, {'Empresa': 'Banco Itaú', 'Ticker': 'ITUB4'}, {'Empresa': 'Vale', 'Ticker': 'VALE3'}, {'Empresa': 'Banco Btg Pactual', 'Ticker': 'BPAC11'}, {'Empresa': 'Ambev', 'Ticker': 'ABEV3'}, {'Empresa': 'Weg', 'Ticker': 'WEGE3'}, {'Empresa': 'Banco Bradesco', 'Ticker': 'BBDC3'}, {'Empresa': 'Eletrobras', 'Ticker': 'ELET3'}, {'Empresa': 'Axia Energia', 'Ticker': 'AXIA3'}, {'Empresa': 'Banco Do Brasil', 'Ticker': 'BBAS3'}]
        lista_cotacao_acoes = []
        for acao in lista_acoes:
            ticker_sa = acao['Ticker']+'.SA'
            
            tk = yf.Ticker(ticker_sa)
            info = tk.info
            nome = acao['Empresa']
            ticker = acao['Ticker']
            ultimo_preco = str(info.get("regularMarketPrice", None))
            ultimo_preco = ('R$ '+ultimo_preco)
            dic_empresa ={f'Empresa':nome, 'Ticker': ticker, 'Cotação': ultimo_preco}
            lista_cotacao_acoes.append(dic_empresa)
        print (lista_cotacao_acoes)
        
Acao_yf()
