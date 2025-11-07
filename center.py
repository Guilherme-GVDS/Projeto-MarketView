def centralizar_janela(janela, largura, altura):
    # Obtém largura e altura da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    
    # Calcula a posição central
    pos_x = (largura_tela // 2) - (largura // 2)
    pos_y = (altura_tela // 2) - (altura // 2)
    
    # Define a geometria da janela
    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")