from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import sys

class CadastroCliente(QWidget):
    def __init__(self):
        super().__init__()

        # vamos configurar a geometria da tela, setando os valores de posição X e Y, além de largura e altura.
        self.setGeometry(450,250,600,400)

        # texto para a barra de título
        self.setWindowTitle("Cadastrar Cliente")

        # gerenciador de layout vertical
        self.layout_v = QVBoxLayout()

        # labels para os dados do cliente
        self.label_nome = QLabel("Nome do Cliente")
        self.label_nome.setStyleSheet("QLabel{font-size:16pt}")

        self.label_email = QLabel("E-mail do Cliente")
        self.label_email.setStyleSheet("QLabel{font-size:16pt}")

        self.label_telefone = QLabel("Telefone do Cliente")
        self.label_telefone.setStyleSheet("QLabel{font-size:16pt}")

        self.label_idade = QLabel("Idade do Cliente")
        self.label_idade.setStyleSheet("QLabel{font-size:16pt}")

        # LineEdit para o nome do cliente
        self.edit_nome = QLineEdit()
        self.edit_nome.setStyleSheet("QLineEdit{font-size:16pt}")

        # LineEdit para o email do cliente
        self.edit_email = QLineEdit()
        self.edit_email.setStyleSheet("QLineEdit{font-size:16pt}")
        
        # LineEdit para o telefone do cliente
        self.edit_telefone = QLineEdit()
        self.edit_telefone.setStyleSheet("QLineEdit{font-size:16pt}")

        # LineEdit para o idade do cliente
        self.edit_idade = QLineEdit()
        self.edit_idade.setStyleSheet("QLineEdit{font-size:16pt}")

        self.button = QPushButton("Cadastrar")
        self.button.setStyleSheet("QPushButton{background-color:red;color:white;font-size:16pt;font-weight:bold}")

        # adicionar a label nome e o lineedit ao layout vertical
        self.layout_v.addWidget(self.label_nome)
        self.layout_v.addWidget(self.edit_nome)

        self.layout_v.addWidget(self.label_email)
        self.layout_v.addWidget(self.edit_email)

        self.layout_v.addWidget(self.label_telefone)
        self.layout_v.addWidget(self.edit_telefone)

        self.layout_v.addWidget(self.label_idade)
        self.layout_v.addWidget(self.edit_idade)

        self.layout_v.addWidget(self.button)

        # adicionar o layout_v na tela
        self.setLayout(self.layout_v)

app = QApplication(sys.argv)
# Instância da classe CadastroCliente
tela = CadastroCliente()
# exibir a tela durante a execução
tela.show ()
# ao clicar no botão fechar a tela deve fechar e sair da memória
app.exec_()
