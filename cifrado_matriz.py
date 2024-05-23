from PyQt6 import QtCore, QtGui, QtWidgets
import numpy as np

class Ui_CifradoMatriz(object):
    def setupUi(self, CifradoMatriz):
        CifradoMatriz.setObjectName("CifradoMatriz")
        CifradoMatriz.resize(830, 483)
        CifradoMatriz.setFixedSize(830, 483)
        self.centralwidget = QtWidgets.QWidget(parent=CifradoMatriz)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 831, 441))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Imagenes/fondo.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(190, -10, 401, 81))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-21_172633-removebg-preview.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(80, 70, 221, 41))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-21_173322-removebg-preview.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(310, 70, 391, 31))
        self.plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "color: rgb(0, 0, 0);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.tableWidget_6 = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget_6.setGeometry(QtCore.QRect(70, 240, 141, 131))
        self.tableWidget_6.setStyleSheet("color: rgb(0, 0, 0);\n"
                                         "background-color: rgb(255, 255, 255);")
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(3)
        self.tableWidget_6.setRowCount(3)
        self.pushButton_19 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(100, 380, 81, 41))
        self.pushButton_19.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_19.setStyleSheet("background-color: rgb(0, 129, 185);\n"
                                         "background-color: rgb(255, 0, 0);\n"
                                         "color: rgb(255, 255, 255);")
        self.pushButton_19.setObjectName("pushButton_19")
        self.label_24 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(10, 200, 81, 221))
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap("Imagenes/open-bracket.png"))
        self.label_24.setScaledContents(True)
        self.label_24.setObjectName("label_24")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(90, 180, 101, 61))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-19_214409-removebg-preview.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_25 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(190, 200, 81, 221))
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap("Imagenes/close-bracket.png"))
        self.label_25.setScaledContents(True)
        self.label_25.setObjectName("label_25")
        self.pushButton_23 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_23.setGeometry(QtCore.QRect(250, 260, 81, 41))
        self.pushButton_23.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_23.setStyleSheet("background-color: rgb(0, 129, 185);\n"
                                         "color: rgb(255, 255, 255);")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_24.setGeometry(QtCore.QRect(750, 350, 61, 61))
        self.pushButton_24.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_24.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(218, 218, 218);\n"
                                         "\n"
                                         "\n"
                                         "border-radius: 30px;\n"
                                         "")
        self.pushButton_24.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagenes/files.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_24.setIcon(icon)
        self.pushButton_24.setObjectName("pushButton_24")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(360, 290, 341, 31))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "color: rgb(0, 0, 0);")
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_20 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(730, 60, 81, 41))
        self.pushButton_20.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_20.setStyleSheet("background-color: rgb(0, 129, 185);\n"
                                         "background-color: rgb(255, 0, 0);\n"
                                         "color: rgb(255, 255, 255);")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(730, 280, 81, 41))
        self.pushButton_21.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_21.setStyleSheet("background-color: rgb(0, 129, 185);\n"
                                         "background-color: rgb(255, 0, 0);\n"
                                         "color: rgb(255, 255, 255);")
        self.pushButton_21.setObjectName("pushButton_21")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(80, 130, 221, 41))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-21_184238-removebg-preview.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(310, 130, 391, 31))
        self.plainTextEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "color: rgb(0, 0, 0);")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.pushButton_22 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(730, 120, 81, 41))
        self.pushButton_22.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_22.setStyleSheet("background-color: rgb(0, 129, 185);\n"
                                         "background-color: rgb(255, 0, 0);\n"
                                         "color: rgb(255, 255, 255);")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_25 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_25.setGeometry(QtCore.QRect(250, 310, 81, 41))
        self.pushButton_25.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_25.setStyleSheet("background-color: rgb(0, 129, 185);\n"
                                         "color: rgb(255, 255, 255);")
        self.pushButton_25.setObjectName("pushButton_25")
        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(460, 240, 141, 51))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-21_190303-removebg-preview.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        CifradoMatriz.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=CifradoMatriz)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 830, 26))
        self.menubar.setObjectName("menubar")
        CifradoMatriz.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=CifradoMatriz)
        self.statusbar.setObjectName("statusbar")
        CifradoMatriz.setStatusBar(self.statusbar)

        self.retranslateUi(CifradoMatriz)
        QtCore.QMetaObject.connectSlotsByName(CifradoMatriz)

        self.tableWidget_6.resizeColumnsToContents()
        self.pushButton_20.clicked.connect(self.clearTableWidget1)
        self.pushButton_22.clicked.connect(self.clearTableWidget2)
        self.pushButton_19.clicked.connect(self.clearTableWidget3)
        self.pushButton_21.clicked.connect(self.clearTableWidget4)
        self.pushButton_23.clicked.connect(self.cifrarTexto)
        self.pushButton_25.clicked.connect(self.descifrarTexto)

    def retranslateUi(self, CifradoMatriz):
        _translate = QtCore.QCoreApplication.translate
        CifradoMatriz.setWindowTitle(_translate("CifradoMatriz", "Cifrado de Matriz"))
        self.pushButton_19.setText(_translate("CifradoMatriz", "Limpiar"))
        self.pushButton_23.setText(_translate("CifradoMatriz", "Cifrar"))
        self.pushButton_20.setText(_translate("CifradoMatriz", "Limpiar"))
        self.pushButton_21.setText(_translate("CifradoMatriz", "Limpiar"))
        self.pushButton_22.setText(_translate("CifradoMatriz", "Limpiar"))
        self.pushButton_25.setText(_translate("CifradoMatriz", "Descifrar"))

    def clearTableWidget1(self):
        self.plainTextEdit.clear()

    def clearTableWidget2(self):
        self.plainTextEdit_2.clear()

    def clearTableWidget3(self):
        self.tableWidget_6.clear()

    def clearTableWidget4(self):
        self.textBrowser.clear()

    def cifrarTexto(self):
        abecedario = "abcdefghijklmnopqrstuvwxyz "
        text = self.plainTextEdit.toPlainText().lower()
        text_num = [abecedario.index(char) + 1 for char in text]

        while len(text_num) % 3 != 0:
            text_num.append(27)  # ' ' en el abecedario es el 27

        matrix_text = np.array(text_num).reshape((-1, 3)).T
        matrix_key = np.zeros((3, 3))

        for i in range(3):
            for j in range(3):
                item = self.tableWidget_6.item(i, j)
                matrix_key[i, j] = int(item.text()) if item is not None else 0

        cifrado = np.dot(matrix_key, matrix_text)
        cifrado_text = cifrado.T.flatten().astype(int)

        resultado = ",".join(map(str, cifrado_text))

        self.textBrowser.setText(resultado)

    def descifrarTexto(self):
        abecedario = "abcdefghijklmnopqrstuvwxyz "
        cifrado_text = list(map(int, self.plainTextEdit_2.toPlainText().replace(',', ' ').split()))

        # Verifica que la longitud del texto cifrado sea un múltiplo de 3
        if len(cifrado_text) % 3 != 0:
            self.textBrowser.setText("El texto cifrado no es válido.")
            return

        # Reshape del texto cifrado
        matrix_cifrado = np.array(cifrado_text).reshape((-1, 3)).T

        # Carga de la clave de la matriz
        matrix_key = np.zeros((3, 3))
        for i in range(3):
            for j in range(3):
                item = self.tableWidget_6.item(i, j)
                if item is not None:
                    try:
                        matrix_key[i, j] = float(item.text())
                    except ValueError:
                        self.textBrowser.setText("La matriz clave contiene valores no válidos.")
                        return
                else:
                    self.textBrowser.setText("La matriz clave no está completamente llena.")
                    return

        try:
            matrix_key_inv = np.linalg.inv(matrix_key)
        except np.linalg.LinAlgError:
            self.textBrowser.setText("No se puede invertir la matriz. Asegúrate de que sea invertible.")
            return

        # Multiplica la matriz cifrada por la inversa de la matriz clave
        descifrado = np.dot(matrix_key_inv, matrix_cifrado)
        descifrado = np.round(descifrado).astype(int)  # Redondear y convertir a entero
        descifrado_text = descifrado.T.flatten()

        # Asegurarse de que los valores estén en el rango de 1 a 27
        descifrado_text = [(num - 1) % 27 + 1 for num in descifrado_text]

        resultado_texto = ""
        for num in descifrado_text:
            if 1 <= num <= 27:
                resultado_texto += abecedario[num - 1]

        self.textBrowser.setText(resultado_texto)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CifradoMatriz = QtWidgets.QMainWindow()
    ui = Ui_CifradoMatriz()
    ui.setupUi(CifradoMatriz)
    CifradoMatriz.show()
    sys.exit(app.exec())
