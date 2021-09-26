from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *


from contador import Ui_Dialog

class TelaPrincipal(QDialog):

    def __init__(self, *args, **argvs):
        super(TelaPrincipal,self).__init__(*args, **argvs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.botao)

    def texto_label(self):
        texto = self.ui.label.text()
        a = self.ui.lineEdit.text()
        if a == "" or a == " ":
            print("Digite um nome valido")
        else:
            texto = self.ui.label.setText("Olá {}".format(a))


    def botao(self):
        return self.texto_label()




if __name__ == "__main__":
    import os, sys
    app = QApplication(sys.argv)
    window = TelaPrincipal()
    window.show()
    sys.exit(app.exec())
