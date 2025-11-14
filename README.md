# Projeto-MarketView

Este projeto em Python apresenta, em uma interface gráfica, as cotações das 20 principais ações e criptomoedas com maior volume de mercado. Para isso, foram utilizadas duas ferramentas: web scraping com Selenium e a API Yfinance.  

* Selenium: responsável por coletar dados de criptomoedas no CoinMarketCap e extrair tickers e nomes das ações no Investidor10.  
* Yfinance: utilizado para obter as cotações das ações previamente identificadas pelo Selenium.
  
Na interface, é possível alternar entre as abas de Ações e Criptomoedas na parte superior esquerda.
Ao clicar no ícone de um ativo, o usuário é redirecionado para o site correspondente — CoinMarketCap (para criptomoedas) ou StatusInvest (para ações).

Criei este projeto por interesse pessoal no mercado financeiro, com o objetivo de reunir, em apenas um clique, informações atualizadas sobre os ativos mais relevantes.


### Bibliotecas Utilizadas

* [CustomTkinter](https://customtkinter.tomschimansky.com/) (Criação de Interface)
* [Pillow](https://pypi.org/project/pillow/) (Utilização de imagens)
* [yfinance](https://pypi.org/project/yfinance/) (API para cotação de Ações)
* [Selenium](https://selenium-python.readthedocs.io/) (Utilizado para Web Scraping)
* Requests
* Os
* Pathlib


### Como rodar o projeto

Inicialmente, deve-se executar o arquivo main.exe, que iniciará o sistema para efetuar uma busca e coletar informações necessárias, em seguida abrirá uma interface gráfica, lhe mostrando inicialmente as ações e na parte superior você pode alterar para as criptomoedas, caso você clique em um icone de um ativo, você será direcionado para um site com mais informações técnicas sobre o ativo.




[Linkedin](https://www.linkedin.com/in/guilherme-v-848a1013a/)
