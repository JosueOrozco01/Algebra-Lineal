from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ProductoPunto(object):
    def setupUi(self, ProductoPunto):
        ProductoPunto.setObjectName("ProductoPunto")
        ProductoPunto.resize(551, 337)
        ProductoPunto.setFixedSize(551, 337)
        self.centralwidget = QtWidgets.QWidget(parent=ProductoPunto)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 551, 301))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Imagenes/fondo.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_14 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(70, -20, 401, 81))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-23_003046-removebg-preview.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(160, 140, 81, 31))
        self.plainTextEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.label_15 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(40, 90, 181, 31))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-22_232244-removebg-preview.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(370, 170, 151, 31))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.textBrowser.setObjectName("textBrowser")
        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(370, 120, 141, 51))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-21_190303-removebg-preview.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.pushButton_23 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_23.setGeometry(QtCore.QRect(260, 160, 81, 41))
        self.pushButton_23.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_23.setStyleSheet("background-color: rgb(0, 129, 185);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_27 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_27.setGeometry(QtCore.QRect(460, 220, 61, 61))
        self.pushButton_27.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_27.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(218, 218, 218);\n"
"\n"
"\n"
"border-radius: 30px;\n"
"")
        self.pushButton_27.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagenes/files.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_27.setIcon(icon)
        self.pushButton_27.setObjectName("pushButton_27")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(160, 200, 81, 31))
        self.plainTextEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.label_16 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(50, 140, 91, 31))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-23_003247-removebg-preview.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(50, 200, 81, 31))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-23_003322-removebg-preview.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        ProductoPunto.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=ProductoPunto)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 551, 26))
        self.menubar.setObjectName("menubar")
        ProductoPunto.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=ProductoPunto)
        self.statusbar.setObjectName("statusbar")
        ProductoPunto.setStatusBar(self.statusbar)

        self.retranslateUi(ProductoPunto)
        QtCore.QMetaObject.connectSlotsByName(ProductoPunto)

        self.pushButton_23.clicked.connect(self.calcular_producto_punto)

    def retranslateUi(self, ProductoPunto):
        _translate = QtCore.QCoreApplication.translate
        ProductoPunto.setWindowTitle(_translate("ProductoPunto", "Producto Punto de Vectores"))
        self.pushButton_23.setText(_translate("ProductoPunto", "Calcular"))

    def calcular_producto_punto(self):
        # Obtener valores de las tablas de entrada
        try:
            x = list(map(float, self.plainTextEdit_3.toPlainText().replace(',', ' ').split()))
            y = list(map(float, self.plainTextEdit_4.toPlainText().replace(',', ' ').split()))
        except ValueError:
            QtWidgets.QMessageBox.critical(None, "Error", "Por favor, ingrese números válidos en las tablas.")
            return

        # Verificar que los vectores tengan la misma longitud
        if len(x) != len(y):
            QtWidgets.QMessageBox.critical(None, "Error", "Los vectores deben tener la misma longitud.")
            return

        # Realizar la multiplicación elemento por elemento y luego sumar los resultados
        resultado_x = 1
        resultado_y = 1
        for num in x:
            resultado_x *= num
        for num in y:
            resultado_y *= num
        suma_total = resultado_x + resultado_y

        # Mostrar resultado en la tabla de resultados
        self.textBrowser.setPlainText(f"({resultado_x}, {resultado_y}) La suma es: {suma_total}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProductoPunto = QtWidgets.QMainWindow()
    ui = Ui_ProductoPunto()
    ui.setupUi(ProductoPunto)
    ProductoPunto.show()
    sys.exit(app.exec())
