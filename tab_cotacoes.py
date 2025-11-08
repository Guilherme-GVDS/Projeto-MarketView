import customtkinter as ctk
from center import centralizar_janela
from PIL import Image
from acoes_investidor_10 import Acoes
from pathlib import Path
import os

class Interface_ativos:
    def __init__(self):
        self.lista_acoes = Acoes().retornar_lista()
        self.janela = ctk.CTk()
        self.interface()
    

    def interface(self):
        ctk.set_appearance_mode('dark')
        centralizar_janela(self.janela,1024,500)
        self.janela.title ('Error')

        self.tabview = ctk.CTkTabview(self.janela,width=1020, height=495,anchor='nw')
        self.tabview.grid(row=0, column=0, padx=1, pady=1)
        
        self.tab_acoes = self.tabview.add ('Ações')
        self.tab_cripto = self.tabview.add ('Criptomoedas')


        self.bg = ctk.CTkImage(light_image= Image.open(
                                'bg.jpg'),
                               dark_image=Image.open('bg.jpg'),
                               size=(1024,500))
        self.bg_label = ctk.CTkLabel (self.tab_acoes, text='', image= self.bg)

        self.bg_label.place(x=0,y=0)       

        self.criar_frame(self.tab_acoes, self.lista_acoes)
        self.janela.protocol("WM_DELETE_WINDOW", self.apagar_img)
        self.janela.mainloop()


        
    def criar_frame(self,tabview,lista):
        self.images_foldes = Path.cwd() /'imagens'
        count = 0
        coluna = 0
        linha = 0
        for ativo in lista:
            frame = ctk.CTkFrame (tabview, width=187, height= 93,
                                            fg_color="#000022",)
            frame.grid_propagate(False)  
            if count >4:
                linha+=1
                coluna = 0
                count = 0
            frame.grid(row=linha,column= coluna,padx =7, pady = 9)
            count +=1
            coluna +=1
            
            label_nome = ctk.CTkLabel(frame, text= ativo['Nome'], anchor='center',width=60,
                                      height=20, font=('Calibri',20))

            img_path = self.images_foldes / f"{ativo['Ticker']}.jpg"

            # Abre, copia e fecha automaticamente
            with Image.open(img_path) as img_file:
                img_copy = img_file.copy()

            self.img = ctk.CTkImage(light_image= img_copy, dark_image=img_copy,
                               size=(20,20))

            self.img_label = ctk.CTkLabel (frame, text='', image= self.img)

            label_ticker = ctk.CTkLabel(frame, text=ativo['Ticker'],font=('Calibri',20))

            label_cotacao = ctk.CTkLabel(frame, text=ativo['Cotação'],font=('Calibri',20))
            
            label_nome.place(x=1,y=1,anchor='nw')                        
            self.img_label.place(x=6,y=33) 
            label_ticker.place(x=40,y=33)
            label_cotacao.place(x=1,y=63)

    def apagar_img(self):
        pasta_imagens = Path('imagens')
        for arquivo in pasta_imagens.glob('*.jpg'):
            os.remove(arquivo)   
        self.janela.destroy()

    


        # Criar um contador para definir a posição dos frames, lembrando que no 6° em diante,
        # tem que ir para a segunda linha


