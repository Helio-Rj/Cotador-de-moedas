from tkinter import *
import requests

root = Tk()


class Aplication:
    def __init__(self):
        self.root = root  # Equivalência
        self.tela()  # toda a função "tela()"
        self.menus()  # Barra de menus
        self.frames_tela()  # Chamada da função "frames_tela()"
        self.widiget_frame()  # Função dos botões.

        root.mainloop()  # loop

    def tela(self):
        self.root.title("Cotação de Moedas ")  # definição do texto título
        self.root.config(bg="white")  # configuração de cores fundo
        self.root.geometry("400x200")  # Altura e largura da tela em Pixels
        self.root.resizable(True, True)  # Impede a maximização da janela quando em "False"
        self.root.maxsize(width=650, height=650)  # Máximo tamanho permitido.
        self.root.minsize(width=250, height=350)  # Minimo tamanho permitido.

    # Frame
    def frames_tela(self):
        self.frame = Frame(self.root, bd=4, bg='#ffff00', highlightbackground='#1a0080',
                           highlightthickness=3)  # fina borda
        self.frame.place(relx=0.02, rely=0.02, relwidth=0.96,
                         relheight=0.96)  # método para enquadramento de janela (Relative) por cordenadas

    # Widgets
    def widiget_frame(self):
        # Botão GO
        self.btn_go = Button(self.frame, text='GO', command=self.cotar, bd=2, bg="#4169E1", fg="#ffffff",
                             font=('verdana', 8, 'bold'),
                             )  # Esse botão fica dentro do frame 1
        self.btn_go.place(relx=0.80, rely=0.10, relwidth=0.12, relheight=0.06)  # Posicionamento do botão limpar

        # botão Limpar
        self.btn_limpar = Button(self.frame, text='Clear', bd=2, bg="#3CB371", fg="#ffffff",
                                 font=('verdana', 8, 'bold'),
                                 command=self.limpar_tela)  # Esse botão fica dentro do frame
        self.btn_limpar.place(relx=0.77, rely=0.85, relwidth=0.15, relheight=0.07)  # Posicionamento do botão limpar

        # Label_title
        self.lb_text = Label(self.frame, text="Clique no botão para obter as cotações ", bg="#ffff00", fg="#4169E1",
                             font=('verdana', 9, 'bold'))
        self.lb_text.place(relx=0.05, rely=0.10)

        # Label Dolar
        self.lb_dolar = Label(self.frame, text="USD", bg="#ffff00", fg="#4169E1",
                              font=('verdana', 8, 'bold'))
        self.lb_dolar.place(relx=0.05, rely=0.20)

        # Entry
        self.entry_dolar = Entry(self.frame, bg="#FFFFF0", fg="#000000",
                                 font=('verdana', 8, 'bold'))  # equivalente ao o "input"
        self.entry_dolar.place(relx=0.20, rely=0.20, relwidth=0.72, relheight=0.07)

        # Label Euro
        self.lb_euro = Label(self.frame, text="EUR", bg="#ffff00", fg="#4169E1",
                             font=('verdana', 8, 'bold'))
        self.lb_euro.place(relx=0.05, rely=0.30)

        # Entry Euro
        self.entry_euro = Entry(self.frame, bg="#FFFFF0", fg="#000000",
                                font=('verdana', 8, 'bold'))  # equivalente ao o "input"
        self.entry_euro.place(relx=0.20, rely=0.30, relwidth=0.72, relheight=0.07)

        # Label Bitcoins
        self.lb_btc = Label(self.frame, text="BTC", bg="#ffff00", fg="#4169E1",
                            font=('verdana', 8, 'bold'))
        self.lb_btc.place(relx=0.05, rely=0.40)

        # Entry Bitcoins
        self.entry_btc = Entry(self.frame, bg="#FFFFF0", fg="#000000",
                               font=('verdana', 8, 'bold'))  # equivalente ao o "input"
        self.entry_btc.place(relx=0.20, rely=0.40, relwidth=0.72, relheight=0.07)

        # Label Libas Esterlinas
        self.lb_gbp = Label(self.frame, text="GBP", bg="#ffff00", fg="#4169E1",
                            font=('verdana', 8, 'bold'))
        self.lb_gbp.place(relx=0.05, rely=0.50)

        # Entry Libras Esterlinas
        self.entry_gbp = Entry(self.frame, bg="#FFFFF0", fg="#000000",
                               font=('verdana', 8, 'bold'))  # equivalente ao o "input"
        self.entry_gbp.place(relx=0.20, rely=0.50, relwidth=0.72, relheight=0.07)

        # Label Iene
        self.lb_iene = Label(self.frame, text="JPY", bg="#ffff00", fg="#4169E1",
                             font=('verdana', 8, 'bold'))
        self.lb_iene.place(relx=0.05, rely=0.60)

        # Entry Iene
        self.entry_iene = Entry(self.frame, bg="#FFFFF0", fg="#000000",
                                font=('verdana', 8, 'bold'))  # equivalente ao o "input"
        self.entry_iene.place(relx=0.20, rely=0.60, relwidth=0.72, relheight=0.07)

        # Label Dolar Canadense
        self.lb_cad = Label(self.frame, text="CAD", bg="#ffff00", fg="#4169E1",
                            font=('verdana', 8, 'bold'))
        self.lb_cad.place(relx=0.05, rely=0.70)

        # Entry Dolar Canadense
        self.entry_cad = Entry(self.frame, bg="#FFFFF0", fg="#000000",
                               font=('verdana', 8, 'bold'))  # equivalente ao o "input"
        self.entry_cad.place(relx=0.20, rely=0.70, relwidth=0.72, relheight=0.07)

    # Barra de Menus
    def menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        # Variável para quitar
        def sair(): self.root.destroy()

        menubar.add_cascade(label="Sobre", menu=filemenu2)
        menubar.add_cascade(label="Sair", menu=filemenu)

        filemenu.add_command(label="Sair", command=sair)
        filemenu2.add_command(label="Desenvolvido Pela Puritoka Zaybatsu Inc.")

    def limpar_tela(self):
        self.entry_dolar.delete(0, END)
        self.entry_euro.delete(0, END)
        self.entry_btc.delete(0, END)
        self.entry_gbp.delete(0, END)
        self.entry_iene.delete(0, END)
        self.entry_cad.delete(0, END)

    def cotar(self):
        self.entry_dolar.delete(0, END)
        self.entry_euro.delete(0, END)
        self.entry_btc.delete(0, END)
        self.entry_gbp.delete(0, END)
        self.entry_iene.delete(0, END)
        self.entry_cad.delete(0, END)
        cotacao = requests.get(
            "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,GBP-BRL,JPY-BRL,CAD-BRL")
        requisicao_dic = cotacao.json()
        self.entry_dolar.insert(END, requisicao_dic['USDBRL']['bid'])
        self.entry_euro.insert(END, requisicao_dic['EURBRL']['bid'])
        self.entry_btc.insert(END, requisicao_dic['BTCBRL']['bid'])
        self.entry_gbp.insert(END, requisicao_dic['GBPBRL']['bid'])
        self.entry_iene.insert(END, requisicao_dic['JPYBRL']['bid'])
        self.entry_cad.insert(END, requisicao_dic['CADBRL']['bid'])


Aplication()
# Executar o comando "pyinstaller --onefile --noconsole --windowed tela.py" para fazer o Deploy
