from tkinter import *
from datetime import *
class Aplication:
    def __init__(self, master=None):

        self.agora = datetime.now()
        self.ano = self.agora.year
        self.mes = self.agora.month
        self.dia = self.agora.day
        self.hora = self.agora.hour
        self.minuto = self.agora.minute
        self.segundo = self.agora.second
        self.tudo = '{}:{}:{}--{}/{}/{}'.format(self.hora, self.minuto, self.segundo, self.dia, self.mes, self.ano)

        self.fontePadrao = ('Times New Roman', '10')

        master.title('Calculadora')
        master.geometry('500x555')


        self.primeiroContainer = Frame(master)
        self.primeiroContainer['pady'] = 12
        self.primeiroContainer['padx'] = 12
        self.primeiroContainer.configure(background='#E6E6FA')
        self.primeiroContainer.pack()

        #MENSAGEM
        self.msgContainer1 = Frame(master)
        self.msgContainer1['pady'] = 12
        self.msgContainer1.configure(background='#E6E6FA')
        self.msgContainer1.pack()

        #PRIMEIRIO INPUT CONTAINER
        self.segundoContainer = Frame(master)
        self.segundoContainer['padx'] = 20
        self.segundoContainer['pady'] = 12
        self.segundoContainer.configure(background='#E6E6FA')
        self.segundoContainer.pack()

        # MENSAGEM
        self.msgContainer2 = Frame(master)
        self.msgContainer2['pady'] = 12
        self.msgContainer2.configure(background='#E6E6FA')
        self.msgContainer2.pack()

        #SEGUNDO INPUT CONTAINER
        self.terceiroContainer = Frame(master)
        self.terceiroContainer['padx'] = 20
        self.terceiroContainer['pady'] = 12
        self.terceiroContainer.configure(background='#E6E6FA')
        self.terceiroContainer.pack()

        #RESULTADO
        self.resutaldoContainer = Frame(master)
        self.resutaldoContainer['padx'] = 8
        self.resutaldoContainer['pady'] = 4
        self.resutaldoContainer.configure(background='#E6E6FA')
        self.resutaldoContainer.pack()

        #RESULTADO REAL
        self.resultadoRealContainer = Frame(master)
        self.resultadoRealContainer['padx'] = 8
        self.resultadoRealContainer['pady'] = 8
        self.resultadoRealContainer.configure(background='#E6E6FA')
        self.resultadoRealContainer.pack()

        #OPÇÕES
        self.quintoContainer = Frame(master)
        self.quintoContainer['pady'] = 12
        self.quintoContainer.configure(backgroun='#E6E6FA')
        self.quintoContainer.pack()

        #SAIR
        self.sextoContainer = Frame(master)
        self.sextoContainer['pady'] = 12
        self.sextoContainer.configure(background='#E6E6FA')
        self.sextoContainer.pack()

        #TÍTULO
        self.titulo = Label(self.primeiroContainer, font=('Arial','10','bold'), text='Calculadora Simples')
        self.titulo['bg'] = '#FFF0F5'
        self.titulo['fg'] = 'black'
        self.titulo.pack()


        self.primeiroNumero = Entry(self.segundoContainer)
        self.primeiroNumero['width'] = 10
        self.primeiroNumero['font'] = self.fontePadrao
        self.primeiroNumero['bg'] = '#E6E6FA'
        self.primeiroNumero['fg'] = 'black'
        self.primeiroNumero.pack(side=LEFT)

        self.segundoNumero = Entry(self.terceiroContainer)
        self.segundoNumero['width'] = 10
        self.segundoNumero['font'] = self.fontePadrao
        self.segundoNumero['bg'] = '#E6E6FA'
        self.segundoNumero['fg'] = 'black'
        self.segundoNumero.pack(side=LEFT)

        self.msg = Label(self.msgContainer1)
        self.msg['text'] = 'Insira o 1º valor: '
        self.msg['width'] = 20
        self.msg['font'] = self.fontePadrao
        self.msg['fg'] = 'black'
        self.msg['bg'] = '#E6E6FA'
        self.msg.pack(side=LEFT)

        self.msg2 = Label(self.msgContainer2)
        self.msg2['text'] = 'Insira o 2º valor: '
        self.msg2['width'] = 20
        self.msg2['fg'] = 'black'
        self.msg2['bg'] = '#E6E6FA'
        self.msg2['font'] = self.fontePadrao
        self.msg2.pack(side=LEFT)

        self.resutaldo = Label(self.resutaldoContainer, text='Resultado')
        self.resutaldo['font'] = self.fontePadrao
        self.resutaldo['bg'] = '#E6E6FA'
        self.resutaldo.pack(side=LEFT)

        self.resultadoReal = Label(self.resultadoRealContainer)
        self.resultadoReal['font'] = self.fontePadrao
        self.resultadoReal['fg'] = 'black'
        self.resultadoReal['bg'] = 'white'
        self.resultadoReal['width'] = 100
        self.resultadoReal.pack(side=LEFT)

        self.somaBtn = Button(self.quintoContainer)
        self.somaBtn['text'] = 'SOMAR'
        self.somaBtn['font'] = self.fontePadrao
        self.somaBtn['bg'] = ('#BFEFFF')
        self.somaBtn['command'] = self.somaNumero
        self.somaBtn.pack(side=TOP)

        self.produtoBtn = Button(self.quintoContainer)
        self.produtoBtn['text'] = 'MULTIPLICAR'
        self.produtoBtn['font'] = self.fontePadrao
        self.produtoBtn['bg'] = ('#BFEFFF')
        self.produtoBtn['command'] = self.multiplicaNumero
        self.produtoBtn.pack(side=TOP)

        self.divisaoBtn = Button(self.quintoContainer)
        self.divisaoBtn['text'] = 'DIVIDIR'
        self.divisaoBtn['font'] = self.fontePadrao
        self.divisaoBtn['bg'] = ('#BFEFFF')
        self.divisaoBtn['command'] = self.divideNumero
        self.divisaoBtn.pack(side=TOP)

        self.subtraiBtn = Button(self.quintoContainer)
        self.subtraiBtn['text'] = 'SUBTRAIR'
        self.subtraiBtn['font'] = self.fontePadrao
        self.subtraiBtn['bg'] = ('#BFEFFF')
        self.subtraiBtn['command'] = self.subtraiNumero
        self.subtraiBtn.pack(side=TOP)

        self.elevaBtn = Button(self.quintoContainer)
        self.elevaBtn['text'] = 'ELEVAR'
        self.elevaBtn['font'] = self.fontePadrao
        self.elevaBtn['bg'] = ('#BFEFFF')
        self.elevaBtn['command'] = self.elevaNumero
        self.elevaBtn.pack(side=TOP)

        self.limpaBtn = Button(self.quintoContainer)
        self.limpaBtn['text'] = 'LIMPAR'
        self.limpaBtn['font'] = self.fontePadrao
        self.limpaBtn['bg'] = ('#BFEFFF')
        self.limpaBtn['command'] = self.limpar
        self.limpaBtn.pack(side=TOP)

        self.sairBtn = Button(self.sextoContainer)
        self.sairBtn['text'] = 'SAIR'
        self.sairBtn['font'] = self.fontePadrao
        self.sairBtn['bg'] = ('red')
        self.sairBtn['fg'] = ('black')
        self.sairBtn['command'] = self.sextoContainer.quit
        self.sairBtn.pack(side=TOP)

    def somaNumero(self):
        try:
            primeiro = self.primeiroNumero.get()
            segundo = self.segundoNumero.get()
            primeiroFloat = float(primeiro)
            segundoFloat = float(segundo)
            soma = primeiroFloat + segundoFloat
            soma = float(soma)
            self.resultadoReal['text'] = '{:.2f}'.format(soma)
            CalculoLog = '[{}]: {} + {} = {}\n'.format(self.tudo, str(primeiro), str(segundo), str(round(soma, 1)))
            arq.write(CalculoLog)
        except ValueError:
            primeiro = self.primeiroNumero.get()
            segundo = self.segundoNumero.get()
            self.resultadoReal['text'] = 'Caracteres Inválidos'
            CalculoLog = '[{}]: {} + {} = Cálculo inválido\n'.format(self.tudo, str(primeiro), str(segundo))
            arq.write(CalculoLog)


    def multiplicaNumero(self):
        try:
            primeiro = self.primeiroNumero.get()
            segundo = self.segundoNumero.get()
            primeiroFloat = float(primeiro)
            segundoFloat = float(segundo)
            produto = primeiroFloat * segundoFloat
            produto = float(produto)
            self.resultadoReal['text'] = '{:.2f}'.format(produto)
            CalculoLog = '[{}]: {} x {} = {}\n'.format(self.tudo, str(primeiro), str(segundo), str(round(produto, 1)))
            arq.write(CalculoLog)
        except ValueError:
            primeiro = self.primeiroNumero.get()
            segundo = self.segundoNumero.get()
            self.resultadoReal['text'] = 'Caracteres Inválidos'
            CalculoLog = '[{}]: {} x {} = Cálculo inválido\n'.format(self.tudo, str(primeiro), str(segundo))
            arq.write(CalculoLog)

    def divideNumero(self):
        try:
            primeiro = self.primeiroNumero.get()
            segundo = self.segundoNumero.get()
            primeiroFloat = float(primeiro)
            segundoFloat = float(segundo)
            razao = primeiroFloat / segundoFloat
            razao = float(razao)
            self.resultadoReal['text'] = '{:.2f}'.format(razao)
            CalculoLog = '[{}]: {} ÷ {} = {}\n'.format(self.tudo, str(primeiro), str(segundo), str(round(razao, 1)))
            arq.write(CalculoLog)
        except ValueError:
            primeiro = self.primeiroNumero.get()
            segundo = self.segundoNumero.get()
            self.resultadoReal['text'] = 'Caracteres Inválidos'
            CalculoLog = '[{}]: {} ÷ {} = Cálculo inválido\n'.format(self.tudo, str(primeiro), str(segundo))
            arq.write(CalculoLog)

    def subtraiNumero(self):
        try:
            primeiro = self.primeiroNumero.get()
            segundo = self.segundoNumero.get()
            primeiroFloat = float(primeiro)
            segundoFloat = float(segundo)
            subtracao = primeiroFloat - segundoFloat
            subtracao = float(subtracao)
            self.resultadoReal['text'] = '{:.2f}'.format(subtracao)
            CalculoLog = '[{}]: {} - {} = {}\n'.format(self.tudo, str(primeiro), str(segundo), str(round(subtracao, 1)))
            arq.write(CalculoLog)
        except ValueError:
            primeiro = self.primeiroNumero.get()
            segundo = self.segundoNumero.get()
            self.resultadoReal['text'] = 'Caracteres Inválidos'
            CalculoLog = '[{}]: {} - {} = Cálculo inválido\n'.format(self.tudo, str(primeiro), str(segundo))
            arq.write(CalculoLog)

    def elevaNumero(self):
        try:
            primeiro = self.primeiroNumero.get()
            segundo = self.segundoNumero.get()
            primeiroFloat = float(primeiro)
            segundoFloat = float(segundo)
            elevado = primeiroFloat ** segundoFloat
            elevado = float(elevado)
            self.resultadoReal['text'] = '{:.2f}'.format(elevado)
            CalculoLog = '[{}]: {} ^ {} = {}\n'.format(self.tudo, str(primeiro), str(segundo), str(round(elevado, 1)))
            arq.write(CalculoLog)
        except ValueError:
            primeiro = self.primeiroNumero.get()
            segundo = self.segundoNumero.get()
            self.resultadoReal['text'] = 'Caracteres Inválidos'
            CalculoLog = '[{}]: {} ^ {} = Cálculo inválido\n'.format(self.tudo, str(primeiro), str(segundo))
            arq.write(CalculoLog)

    def limpar(self):
        self.resultadoReal['text'] = ''

global arq
arq = open('CalculoLog.txt', 'w')


root = Tk()
Aplication(root)
root.configure(background='#E6E6FA')
root.mainloop()
arq.close()