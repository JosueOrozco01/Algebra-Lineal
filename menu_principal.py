from PyQt6 import QtCore, QtGui, QtWidgets
from menu_operacion_matriz import Ui_OperacionesMatrices
from menu_operaciones_vectores import Ui_operaciones_vectores
from inversa_de_una_matriz import Ui_InversaMatriz
from determinante_matriz import Ui_DeterminanteMatriz
from rango_matriz import Ui_RangoMatriz
from markov import Ui_Markov
from cifrado_matriz import Ui_CifradoMatriz


class Ui_pestana_principal(object):
    def setupUi(self, pestana_principal):

        self.pestana_principal = pestana_principal
        self.operacion_matrices = Ui_OperacionesMatrices()
        self.operaciones_vectores = Ui_operaciones_vectores()
        self.matriz_inversa = Ui_InversaMatriz()
        self.determinantes_matriz = Ui_DeterminanteMatriz()
        self.rango_matriz = Ui_RangoMatriz()
        self.markov = Ui_Markov()
        self.cifrado_matriz = Ui_CifradoMatriz()

        pestana_principal.setObjectName("pestana_principal")
        pestana_principal.resize(687, 841)
        pestana_principal.setIconSize(QtCore.QSize(40, 40))
        pestana_principal.setFixedSize(687, 841)

        self.centralwidget = QtWidgets.QWidget(parent=self.pestana_principal)
        self.centralwidget = QtWidgets.QWidget(parent=pestana_principal)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.centralwidget)

        self.pushButton.setGeometry(QtCore.QRect(140, 260, 181, 41))
        self.pushButton_2.setGeometry(QtCore.QRect(350, 260, 181, 41))
        self.pushButton_3.setGeometry(QtCore.QRect(40, 480, 181, 41))
        self.pushButton_4.setGeometry(QtCore.QRect(250, 480, 181, 41))
        self.pushButton_5.setGeometry(QtCore.QRect(350, 700, 181, 41))
        self.pushButton_6.setGeometry(QtCore.QRect(460, 480, 181, 41))
        self.pushButton_7.setGeometry(QtCore.QRect(140, 700, 181, 41))

        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        self.pushButton.setStyleSheet("background-color: rgb(0, 129, 185);\n" "color: rgb(255, 255, 255);")
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 129, 185);\n" "color: rgb(255, 255, 255);")
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 129, 185);\n" "color: rgb(255, 255, 255);")
        self.pushButton_4.setStyleSheet("background-color: rgb(0, 129, 185);\n" "color: rgb(255, 255, 255);")
        self.pushButton_5.setStyleSheet("background-color: rgb(0, 129, 185);\n" "color: rgb(255, 255, 255);")
        self.pushButton_6.setStyleSheet("background-color: rgb(0, 129, 185);\n" "color: rgb(255, 255, 255);")
        self.pushButton_7.setStyleSheet("background-color: rgb(0, 129, 185);\n" "color: rgb(255, 255, 255);")

        self.pushButton.setObjectName("pushButton")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton.clicked.connect(self.mostrar_operaciones_matrices)
        self.pushButton_2.clicked.connect(self.mostrar_inversa)
        self.pushButton_3.clicked.connect(self.mostrar_determinante)
        self.pushButton_4.clicked.connect(self.mostrar_rango)
        self.pushButton_5.clicked.connect(self.mostrar_cifrado)
        self.pushButton_6.clicked.connect(self.mostrar_markov)
        self.pushButton_7.clicked.connect(self.mostrar_operaciones_vectores)


        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)

        self.label.setGeometry(QtCore.QRect(0, 0, 691, 801))
        self.label_2.setGeometry(QtCore.QRect(350, 110, 181, 141))
        self.label_3.setGeometry(QtCore.QRect(170, 120, 121, 121))
        self.label_4.setGeometry(QtCore.QRect(60, 340, 151, 131))
        self.label_5.setGeometry(QtCore.QRect(260, 330, 151, 141))
        self.label_6.setGeometry(QtCore.QRect(370, 560, 141, 121))
        self.label_7.setGeometry(QtCore.QRect(480, 340, 131, 121))
        self.label_8.setGeometry(QtCore.QRect(160, 560, 141, 121))
        self.label_9.setGeometry(QtCore.QRect(50, 0, 611, 111))

        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.label_7.setText("")
        self.label_8.setText("")
        self.label_9.setText("")

        self.label.setPixmap(QtGui.QPixmap("Imagenes/fondo.jpg"))
        self.label_2.setPixmap(QtGui.QPixmap("Imagenes/opposite.png"))
        self.label_3.setPixmap(QtGui.QPixmap("Imagenes/calculation.png"))
        self.label_4.setPixmap(QtGui.QPixmap("Imagenes/computer.png"))
        self.label_5.setPixmap(QtGui.QPixmap("Imagenes/range.png"))
        self.label_6.setPixmap(QtGui.QPixmap("Imagenes/sign-in.png"))
        self.label_7.setPixmap(QtGui.QPixmap("Imagenes/multiplication-mark.png"))
        self.label_8.setPixmap(QtGui.QPixmap("Imagenes/vector.png"))
        self.label_9.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-11_135940-removebg-preview.png"))

        self.label.setScaledContents(True)
        self.label_2.setScaledContents(True)
        self.label_3.setScaledContents(True)
        self.label_4.setScaledContents(True)
        self.label_5.setScaledContents(True)
        self.label_6.setScaledContents(True)
        self.label_7.setScaledContents(True)
        self.label_8.setScaledContents(True)
        self.label_9.setScaledContents(True)

        self.label.setObjectName("label")
        self.label_2.setObjectName("label_2")
        self.label_3.setObjectName("label_3")
        self.label_4.setObjectName("label_4")
        self.label_5.setObjectName("label_5")
        self.label_6.setObjectName("label_6")
        self.label_7.setObjectName("label_7")
        self.label_8.setObjectName("label_8")
        self.label_9.setObjectName("label_9")

        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()

        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()

        pestana_principal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=pestana_principal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 687, 26))
        self.menubar.setObjectName("menubar")
        pestana_principal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=pestana_principal)
        self.statusbar.setObjectName("statusbar")
        pestana_principal.setStatusBar(self.statusbar)

        self.retranslateUi(pestana_principal)
        QtCore.QMetaObject.connectSlotsByName(pestana_principal)

    def mostrar_operaciones_matrices(self):
        self.ventana_operaciones = QtWidgets.QMainWindow()
        self.operacion_matrices.setupUi(self.ventana_operaciones)
        self.ventana_operaciones.show()

    def mostrar_operaciones_vectores(self):
        self.ventana_vectores = QtWidgets.QMainWindow()
        self.operaciones_vectores.setupUi(self.ventana_vectores)
        self.ventana_vectores.show()

    def mostrar_inversa(self):
        self.ventana_inversa = QtWidgets.QMainWindow()
        self.matriz_inversa.setupUi(self.ventana_inversa)
        self.ventana_inversa.show()

    def mostrar_determinante(self):
        self.ventana_determinante = QtWidgets.QMainWindow()
        self.determinantes_matriz.setupUi(self.ventana_determinante)
        self.ventana_determinante.show()

    def mostrar_rango(self):
        self.ventana_rango = QtWidgets.QMainWindow()
        self.rango_matriz.setupUi(self.ventana_rango)
        self.ventana_rango.show()

    def mostrar_markov(self):
        self.ventana_markov = QtWidgets.QMainWindow()
        self.markov.setupUi(self.ventana_markov)
        self.ventana_markov.show()

    def mostrar_cifrado(self):
        self.ventana_cifrado = QtWidgets.QMainWindow()
        self.cifrado_matriz.setupUi(self.ventana_cifrado)
        self.ventana_cifrado.show()

    def show_principal(self):
        self.pestana_principal.show()

    def retranslateUi(self, pestana_principal):
        _translate = QtCore.QCoreApplication.translate
        pestana_principal.setWindowTitle(_translate("pestana_principal", "Menú"))
        self.pushButton.setText(_translate("pestana_principal", "Operaciones Entre Matrices"))
        self.pushButton_2.setText(_translate("pestana_principal", "Matriz Inversa"))
        self.pushButton_3.setText(_translate("pestana_principal", "Determinante de una Matriz"))
        self.pushButton_4.setText(_translate("pestana_principal", "Rango de una Matriz"))
        self.pushButton_5.setText(_translate("pestana_principal", "Cifrado de Matrices"))
        self.pushButton_6.setText(_translate("pestana_principal", "Cadena Markov"))
        self.pushButton_7.setText(_translate("pestana_principal", "Operaciones con Vectores"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pestana_principal = QtWidgets.QMainWindow()
    ui = Ui_pestana_principal()
    ui.setupUi(pestana_principal)
    pestana_principal.show()
    sys.exit(app.exec())
