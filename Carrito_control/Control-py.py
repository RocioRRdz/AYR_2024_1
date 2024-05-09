import sys
from PyQt5 import uic, QtWidgets
import serial

qtCreatorFile = "Control.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.ser = serial.Serial('COM7', 9600)

        # Conectar los eventos clicked de los QLabel a funciones específicas
        self.btn_A.clicked.connect(self.Izquierda_clicked)
        self.btn_W.clicked.connect(self.Avanzar_clicked)
        self.btn_S.clicked.connect(self.Retroceder_clicked)
        self.btn_D.clicked.connect(self.Derecha_clicked)
        self.btn_X.clicked.connect(self.Detenerse_clicked)

    def Avanzar_clicked(self):
        print("AVANZAR")
        self.enviar(83)

    def Retroceder_clicked(self):
        print("RETROCEDER")
        self.enviar(87)

    def Izquierda_clicked(self):
        print("IZQUIERDA")
        self.enviar(65)

    def Derecha_clicked(self):
        print("DERECHA")
        self.enviar(68)

    def Detenerse_clicked(self):
        print("DETENERSE")
        self.enviar(88) 

    def enviar(self, numero):
        self.ser.write((numero.to_bytes(1, byteorder='big')))
        print("Número enviado: ",numero)

    def closeEvent(self, event):
        self.ser.close()
        event.accept()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
