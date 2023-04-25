import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QLineEdit
from PyQt5.QtGui import QIcon
from googletrans import Translator
import pandas as pd


class Janela(QMainWindow):

    def __init__(self):
        super().__init__()
        self.translator = Translator()
        self.traducao = str
        self.resultado = str
        self.idiomaOrigem = str
        self.idiomaEscolhido = str
        self.topo = 100
        self.direita = 10
        self.largura = 800
        self.altura = 200
        self.titulo = "Fast Translate"

        self.caixa_traduz = QLineEdit(self)
        self.caixa_traduz.move(50, 75)
        self.caixa_traduz.resize(250, 50)

        self.caixa_resultado = QLineEdit(self)
        self.caixa_resultado.move(400, 75)
        self.caixa_resultado.resize(250, 50)

        botaoTraduz = QPushButton('Traduzir', self)
        botaoTraduz.move(325, 75)
        botaoTraduz.resize(50, 50)
        botaoTraduz.setStyleSheet(
            'QPushButton {background-color:#43D3E8; font:bold}')
        botaoTraduz.clicked.connect(self.traduz)

        # botaoExibirLista = QPushButton('Exibir lista', self)
        # botaoExibirLista.move(500, 175)
        # botaoExibirLista.resize(100, 50)
        # botaoExibirLista.setStyleSheet(
        #     'QPushButton {background-color:#43D3E8; font:bold}')
        # botaoExibirLista.clicked.connect(self.botao1_click)

        botaoGravarLista = QPushButton('Gravar', self)
        botaoGravarLista.move(675, 75)
        botaoGravarLista.resize(50, 50)
        botaoGravarLista.setStyleSheet(
            'QPushButton {background-color:#43D3E8; font:bold}')
        botaoGravarLista.clicked.connect(self.gravaTraducao)

        self.label_1 = QLabel(self)
        self.label_1.setText("Coloque no campo o que você precisa traduzir!")
        self.label_1.move(400, 175)
        self.label_1.resize(300, 25)
        self.label_1.setStyleSheet('QLabel {font:bold; font-size:10px}')

        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.direita, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.setWindowIcon(QIcon(os.path.join('icone.ico')))
        self.show()

    def botao1_click(self):
        self.label_1.setText("Deseja gravar essa tradução?")

    def mostra_texto(self):
        conteudo = self.caixa_traduz.text()
        self.caixa_resultado.setText(conteudo)
        self.label_1.setText("Deseja gravar essa tradução?")

    def traduz(self):
        traducao = self.caixa_traduz.text()
        translator = Translator()
        idiomaOrigem = 'pt'
        idiomaEscolhido = 'en'
        resultado = translator.translate(
            traducao, src=idiomaOrigem, dest=idiomaEscolhido)
        print(resultado.text)
        self.caixa_resultado.setText(resultado.text)

    def gravaTraducao(self):
        df = pd.DataFrame(columns=['Português', 'Inglês', 'Data'])
        df.loc[0] = ['Teste', 'Test', '20/04/2023']
        df.to_excel('traducao_english.xlsx', index=False)

    def exibirLista(self):
        ...
        dfr = pd.read_excel('traducao_english.xlsx')
        print(dfr)

    def getTraduz(self):
        print(self.traducao)
        print(self.resultado.text)

    def mostra_texto(self):
        conteudo = self.caixa_traduz.text()
        self.caixa_resultado.setText(conteudo)
        self.label_1.setText("Deseja gravar essa tradução?")


aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())
