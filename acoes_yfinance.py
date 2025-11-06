import yfinance as yf
import pandas as pd

tickers = ['PETR4.SA', 'ITUB4.SA', 'VALE3.SA', 'BPAC11.SA', 'ABEV3.SA',
           'BBDC3.SA', 'WEGE3.SA', 'ELET3.SA', 'AXIA3.SA', 'ITSA4.SA']
dados = []

for ticker in tickers:
    tk = yf.Ticker(ticker)
    info = tk.info
    nome = (info.get("shortName", None)).split()
    nome = nome[0]
    ultimo_preco = str(info.get("regularMarketPrice", None))
    ultimo_preco = ('R$ '+ultimo_preco)

    print (f'{nome} de ticker {ticker[:-3]} e ultima cotação {ultimo_preco}')
    

