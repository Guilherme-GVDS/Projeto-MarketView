import customtkinter as ctk
from center import centralizar_janela

class Login_error:
    def __init__(self, janela):
        self.janela = janela
        self.interface()

    def interface(self):
        ctk.set_appearance_mode('dark')
        centralizar_janela(self.janela,700,400)
        self.janela.title ('Error')

        self.lista_acoes = [{'Empresa': 'Petrobrás', 'Ticker': 'PETR4', 'Cotação': 'R$ 31.1'}, {'Empresa': 'Banco Itaú', 'Ticker': 'ITUB4', 'Cotação': 'R$ 40.05'}, {'Empresa': 'Vale', 'Ticker': 'VALE3', 'Cotação': 'R$ 64.57'}, {'Empresa': 'Banco Btg Pactual', 'Ticker': 'BPAC11', 'Cotação': 'R$ 50.22'}, {'Empresa': 'Ambev', 'Ticker': 'ABEV3', 'Cotação': 'R$ 13.18'}, {'Empresa': 'Weg', 'Ticker': 'WEGE3', 'Cotação': 'R$ 44.03'}, {'Empresa': 'Banco Bradesco', 'Ticker': 'BBDC3', 'Cotação': 'R$ 15.89'}, {'Empresa': 'Eletrobras', 'Ticker': 'ELET3', 'Cotação': 'R$ 57.85'}, {'Empresa': 'Axia Energia', 'Ticker': 'AXIA3', 'Cotação': 'R$ None'}, {'Empresa': 'Banco Do Brasil', 'Ticker': 'BBAS3', 'Cotação': 'R$ 22.61'}]
        self.tabview = ctk.CTkTabview(self.janela,width=699, height=390,anchor='nw')
        self.tabview.grid(row=0, column=0, padx=1, pady=1)
        
        self.tab_acoes = self.tabview.add ('Ações')
        self.tab_acoes = self.tabview.add ('Criptomoedas')

        count = 0
        for acao in self.lista_acoes:
            self.criar_frame(self.tabview)
        # Criar um contador para definir a posição dos frames, lembrando que no 6° em diante,
        # tem que ir para a segunda linha

    def criar_frame(self,tabview):
        self.cotacao = ctk.CTkFrame(tabview, width=70, height= 40)

tabela = ctk.CTk()
Login_error(tabela)
tabela.mainloop()
