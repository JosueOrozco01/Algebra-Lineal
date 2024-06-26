from PyQt6 import QtCore, QtGui, QtWidgets
from suma_matrices import Ui_SumaMatrices
from resta_matrices import Ui_RestaMatrices
from division_matrices import Ui_DivisionMatrices
from multiplicacion_matrices import Ui_MultiplicacionMatrices


class Ui_OperacionesMatrices(object):
    def setupUi(self, OperacionesMatrices):
        OperacionesMatrices.setObjectName("OperacionesMatrices")
        OperacionesMatrices.resize(573, 600)
        OperacionesMatrices.setFixedSize(573, 600)
        self.suma_matriz = Ui_SumaMatrices()
        self.resta_matriz = Ui_RestaMatrices()
        self.division_matriz = Ui_DivisionMatrices()
        self.multiplicacion_matriz = Ui_MultiplicacionMatrices()
        self.centralwidget = QtWidgets.QWidget(parent=OperacionesMatrices)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(80, 250, 181, 41))
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_8.setStyleSheet("background-color: rgb(0, 129, 185);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 561))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Imagenes/fondo.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(320, 250, 181, 41))
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_9.setStyleSheet("background-color: rgb(0, 129, 185);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(80, 460, 181, 41))
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_10.setStyleSheet("background-color: rgb(0, 129, 185);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(320, 460, 181, 41))
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_11.setStyleSheet("background-color: rgb(0, 129, 185);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-20, -50, 611, 201))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-11_231011-removebg-preview.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(350, 120, 111, 111))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("Imagenes/less.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(110, 110, 121, 121))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("Imagenes/add.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(350, 330, 111, 111))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("Imagenes/multiplication-sign.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(110, 330, 111, 111))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("Imagenes/division.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.label.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.pushButton_10.raise_()
        self.pushButton_11.raise_()
        self.label_2.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        OperacionesMatrices.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=OperacionesMatrices)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 573, 26))
        self.menubar.setObjectName("menubar")
        OperacionesMatrices.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=OperacionesMatrices)
        self.statusbar.setObjectName("statusbar")
        OperacionesMatrices.setStatusBar(self.statusbar)

        self.retranslateUi(OperacionesMatrices)
        QtCore.QMetaObject.connectSlotsByName(OperacionesMatrices)
        self.pushButton_8.clicked.connect(self.mostrar_suma_matriz)
        self.pushButton_9.clicked.connect(self.mostrar_resta_matriz)
        self.pushButton_10.clicked.connect(self.mostrar_division_matriz)
        self.pushButton_11.clicked.connect(self.mostrar_multiplicacion_matriz)


    def retranslateUi(self, OperacionesMatrices):
        _translate = QtCore.QCoreApplication.translate
        OperacionesMatrices.setWindowTitle(_translate("OperacionesMatrices", "Operaciones entre Matrices"))
        self.pushButton_8.setText(_translate("OperacionesMatrices", "Suma de Matrices"))
        self.pushButton_9.setText(_translate("OperacionesMatrices", "Resta de Matrices"))
        self.pushButton_10.setText(_translate("OperacionesMatrices", "División de Matrices"))
        self.pushButton_11.setText(_translate("OperacionesMatrices", "Multiplicación de Matrices"))

    def mostrar_suma_matriz(self):
        # Crear una instancia de la ventana de operaciones con vectores
        self.ventana_suma = QtWidgets.QMainWindow()
        self.suma_matriz.setupUi(self.ventana_suma)
        self.ventana_suma.show()

    def mostrar_resta_matriz(self):
        # Crear una instancia de la ventana de operaciones con vectores
        self.ventana_resta = QtWidgets.QMainWindow()
        self.resta_matriz.setupUi(self.ventana_resta)
        self.ventana_resta.show()

    def mostrar_division_matriz(self):
        # Crear una instancia de la ventana de operaciones con vectores
        self.ventana_division = QtWidgets.QMainWindow()
        self.division_matriz.setupUi(self.ventana_division)
        self.ventana_division.show()

    def mostrar_multiplicacion_matriz(self):
        # Crear una instancia de la ventana de operaciones con vectores
        self.ventana_multiplcacion = QtWidgets.QMainWindow()
        self.multiplicacion_matriz.setupUi(self.ventana_multiplcacion)
        self.ventana_multiplcacion.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OperacionesMatrices = QtWidgets.QMainWindow()
    ui = Ui_OperacionesMatrices()
    ui.setupUi(OperacionesMatrices)
    OperacionesMatrices.show()
    sys.exit(app.exec())
