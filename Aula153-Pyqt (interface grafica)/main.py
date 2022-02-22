import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.btn = QPushButton('Texto do Botão')
        self.btn.setStyleSheet('font-size: 30px;')
        self.grid.addWidget(self.btn, 0, 0, 1, 1)  # <- os 4 ultimos parametros (0,0,1,1) é o tamanho da GRID

        self.btn.clicked.connect(self.acao)

        self.setCentralWidget(self.cw)

    def acao(self):
        print('Alguma coisa...')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
