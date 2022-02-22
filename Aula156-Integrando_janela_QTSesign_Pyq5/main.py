import sys
from layoutApp.design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class Red_Imagem(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnEscolherArquivo.clicked.connect(self.abrir_imagem)
        self.btnRedimensionar.clicked.connect(self.redimensionar)
        self.btnSalvar.clicked.connect(self.salvar)  # O .connect() é para "conectar" a um método feito!

    def abrir_imagem(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir Imagem',
            r'C:\Users\carla\Downloads\serie2'
        )
        self.inputAbrirArquivo.setText(imagem)
        self.original_img = QPixmap(imagem)
        self.labelImg.setPixmap(self.original_img)
        self.inputLargura.setText(str(self.original_img.width()))
        self.inputAltura.setText(str(self.original_img.height()))

    def redimensionar(self):
        largura = int(self.inputLargura.text())
        self.nova_imagem = self.original_img.scaledToWidth(largura)
        self.labelImg.setPixmap(self.nova_imagem)
        self.inputLargura.setText(str(self.nova_imagem.width()))
        self.inputAltura.setText(str(self.nova_imagem.height()))

    def salvar(self):
        imagem, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Salvar Imagem',
            r'C:\Users\carla\Desktop'
        )
        self.nova_imagem.save(imagem + '.png')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Red_Imagem()
    novo.show()
    qt.exec_()
