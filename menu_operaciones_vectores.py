from PyQt6 import QtCore, QtGui, QtWidgets
from suma_vectores import Ui_SumaVectores
from producto_cruz import Ui_ProductoCruz
from producto_punto import Ui_ProductoPunto


class Ui_operaciones_vectores(object):
    def setupUi(self, operaciones_vectores):
        operaciones_vectores.setObjectName("operaciones_vectores")
        operaciones_vectores.resize(532, 600)
        operaciones_vectores.setFixedSize(532, 600)
        self.Suma_vectores = Ui_SumaVectores()
        self.producto_punto = Ui_ProductoPunto()
        self.producto_cruz = Ui_ProductoCruz()
        self.centralwidget = QtWidgets.QWidget(parent=operaciones_vectores)
        self.centralwidget.setObjectName("centralwidget")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(-20, -20, 561, 131))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-12_175934-removebg-preview.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(210, 110, 111, 111))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("Imagenes/plus.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(170, 240, 181, 41))
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_8.setStyleSheet("background-color: rgb(0, 129, 185);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(50, 450, 181, 41))
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_9.setStyleSheet("background-color: rgb(0, 129, 185);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(300, 450, 181, 41))
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_10.setStyleSheet("background-color: rgb(0, 129, 185);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(50, 280, 181, 181))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("Imagenes/dot-inside-a-circle.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(330, 320, 111, 111))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("Imagenes/remove.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 531, 561))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Imagenes/fondo.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.pushButton_10.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        operaciones_vectores.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=operaciones_vectores)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 532, 26))
        self.menubar.setObjectName("menubar")
        operaciones_vectores.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=operaciones_vectores)
        self.statusbar.setObjectName("statusbar")
        operaciones_vectores.setStatusBar(self.statusbar)

        self.retranslateUi(operaciones_vectores)
        QtCore.QMetaObject.connectSlotsByName(operaciones_vectores)

        self.pushButton_8.clicked.connect(self.mostrar_suma_vectoras)
        self.pushButton_9.clicked.connect(self.mostrar_producto_punto)
        self.pushButton_10.clicked.connect(self.mostrar_producto_cruz)

    def retranslateUi(self, operaciones_vectores):
        _translate = QtCore.QCoreApplication.translate
        operaciones_vectores.setWindowTitle(_translate("operaciones_vectores", "Operaciones con Vectores"))
        self.pushButton_8.setText(_translate("operaciones_vectores", "Suma de Vectores"))
        self.pushButton_9.setText(_translate("operaciones_vectores", " Producto Punto de Vectores"))
        self.pushButton_10.setText(_translate("operaciones_vectores", " Producto Cruz de Vectores"))

    def mostrar_suma_vectoras(self):
        self.ventana_suma_vectores = QtWidgets.QMainWindow()
        self.Suma_vectores.setupUi(self.ventana_suma_vectores)
        self.ventana_suma_vectores.show()

    def mostrar_producto_punto(self):
        self.ventana_producto_punto = QtWidgets.QMainWindow()
        self.producto_punto.setupUi(self.ventana_producto_punto)
        self.ventana_producto_punto.show()

    def mostrar_producto_cruz(self):
        self.ventana_producto_cruz = QtWidgets.QMainWindow()
        self.producto_cruz.setupUi(self.ventana_producto_cruz)
        self.ventana_producto_cruz.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    operaciones_vectores = QtWidgets.QMainWindow()
    ui = Ui_operaciones_vectores()
    ui.setupUi(operaciones_vectores)
    operaciones_vectores.show()
    sys.exit(app.exec())
