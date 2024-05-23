from PyQt6 import QtCore, QtGui, QtWidgets
import numpy as np

class Ui_MultiplicacionMatrices(object):
    def setupUi(self, MultiplicacionMatrices):
        MultiplicacionMatrices.setObjectName("MultiplicacionMatrices")
        MultiplicacionMatrices.resize(810, 958)
        MultiplicacionMatrices.setFixedSize(810, 958)
        self.centralwidget = QtWidgets.QWidget(parent=MultiplicacionMatrices)
        self.centralwidget.setObjectName("centralwidget")

        # Definir los elementos visuales para la primera matriz
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 811, 921))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Imagenes/fondo.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, -20, 541, 131))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-16_002740-removebg-preview.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 90, 491, 51))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-16_003925-removebg-preview.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.spinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(580, 100, 151, 31))
        self.spinBox.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.spinBox.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n")
        self.spinBox.setObjectName("spinBox")

        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 150, 491, 31))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-16_004149-removebg-preview.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")

        self.spinBox_2 = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(580, 150, 151, 31))
        self.spinBox_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.spinBox_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n")
        self.spinBox_2.setObjectName("spinBox_2")

        # Definir los elementos visuales para la segunda matriz
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 210, 281, 81))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-13_092053-removebg-preview.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(510, 190, 281, 101))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-13_092542-removebg-preview.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")

        # Definir los elementos visuales para la multiplicación de matrices
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(270, 500, 281, 81))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-13_092939-removebg-preview.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")

        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(60, 290, 211, 191))
        self.tableWidget.setStyleSheet("color: rgb(0, 0, 0);\nbackground-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.tableWidget_2 = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(550, 290, 211, 191))
        self.tableWidget_2.setStyleSheet("color: rgb(0, 0, 0);\nbackground-color: rgb(255, 255, 255);")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)

        self.tableWidget_3 = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget_3.setGeometry(QtCore.QRect(310, 590, 211, 191))
        self.tableWidget_3.setStyleSheet("color: rgb(0, 0, 0);\nbackground-color: rgb(255, 255, 255);")
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)

        # Definir los botones adicionales
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(320, 380, 181, 41))
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_10.setStyleSheet("background-color: rgb(0, 129, 185);\n color: rgb(255, 255, 255);")
        self.pushButton_10.setObjectName("pushButton_10")

        self.label_15 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(350, 290, 121, 111))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("Imagenes/multiplication.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")

        self.label_16 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(0, 230, 81, 301))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("Imagenes/open-bracket.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")

        self.label_17 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(250, 230, 81, 301))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("Imagenes/close-bracket.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")

        self.label_18 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(490, 230, 81, 301))
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("Imagenes/open-bracket.png"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")

        self.label_19 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(740, 230, 81, 301))
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("Imagenes/close-bracket.png"))
        self.label_19.setScaledContents(True)
        self.label_19.setObjectName("label_19")

        self.label_20 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(250, 530, 81, 301))
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap("Imagenes/open-bracket.png"))
        self.label_20.setScaledContents(True)
        self.label_20.setObjectName("label_20")

        self.label_21 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(500, 530, 81, 301))
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("Imagenes/close-bracket.png"))
        self.label_21.setScaledContents(True)
        self.label_21.setObjectName("label_21")

        self.pushButton_11 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(110, 500, 101, 41))
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_11.setStyleSheet("background-color: rgb(0, 129, 185);\n color: rgb(255, 255, 255);")
        self.pushButton_11.setObjectName("pushButton_11")

        self.pushButton_12 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(370, 800, 101, 41))
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_12.setStyleSheet("background-color: rgb(0, 129, 185);\n color: rgb(255, 255, 255);")
        self.pushButton_12.setObjectName("pushButton_12")

        self.pushButton_13 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(610, 500, 101, 41))
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_13.setStyleSheet("background-color: rgb(0, 129, 185);\n color: rgb(255, 255, 255);")
        self.pushButton_13.setObjectName("pushButton_13")

        MultiplicacionMatrices.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MultiplicacionMatrices)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 26))
        self.menubar.setObjectName("menubar")
        MultiplicacionMatrices.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MultiplicacionMatrices)
        self.statusbar.setObjectName("statusbar")
        MultiplicacionMatrices.setStatusBar(self.statusbar)

        self.retranslateUi(MultiplicacionMatrices)
        QtCore.QMetaObject.connectSlotsByName(MultiplicacionMatrices)

        self.spinBox.valueChanged.connect(self.actualizar_tabla)
        self.spinBox_2.valueChanged.connect(self.actualizar_tabla)

        self.pushButton_11.clicked.connect(self.limpiar_tabla1)
        self.pushButton_13.clicked.connect(self.limpiar_tabla2)
        self.pushButton_12.clicked.connect(self.limpiar_resultado)

        self.pushButton_10.clicked.connect(self.hacer_multiplicacion)

    def retranslateUi(self, MultiplicacionMatrices):
        _translate = QtCore.QCoreApplication.translate
        MultiplicacionMatrices.setWindowTitle(_translate("MultiplicacionMatrices", "Multiplicación de Matrices"))
        self.pushButton_10.setText(_translate("MultiplicacionMatrices", "Hacer Multiplicación"))
        self.pushButton_11.setText(_translate("MultiplicacionMatrices", "Limpiar"))
        self.pushButton_12.setText(_translate("MultiplicacionMatrices", "Limpiar"))
        self.pushButton_13.setText(_translate("MultiplicacionMatrices", "Limpiar"))

    def actualizar_tabla(self):
        # Obtener el número de filas y columnas desde los spin boxes
        filas_matriz1 = self.spinBox.value()
        columnas_matriz2 = self.spinBox_2.value()

        # Actualizar el número de filas y columnas en las tablas
        self.tableWidget.setRowCount(filas_matriz1)
        self.tableWidget.setColumnCount(columnas_matriz2)
        self.tableWidget_2.setRowCount(columnas_matriz2)
        self.tableWidget_2.setColumnCount(filas_matriz1)
        self.tableWidget_3.setRowCount(filas_matriz1)  # Ajuste adicional para las filas
        self.tableWidget_3.setColumnCount(columnas_matriz2)  # Ajuste adicional para las columnas

        # Ajustar automáticamente el tamaño de las columnas
        self.adjustColumnWidths(self.tableWidget)
        self.adjustColumnWidths(self.tableWidget_2)
        self.adjustColumnWidths(self.tableWidget_3)  # Ajuste adicional para la tabla 3

    def adjustColumnWidths(self, tableWidget):
        if tableWidget.columnCount() == 0:
            return

        # Ancho base de la columna
        base_width = 3

        # Calcular el ancho de cada columna basado en el contenido más largo
        for col in range(tableWidget.columnCount()):
            max_width = base_width
            for row in range(tableWidget.rowCount()):
                item = tableWidget.item(row, col)
                if item is not None and item.text():
                    text_width = tableWidget.fontMetrics().boundingRect(item.text()).width()
                    max_width = max(max_width, text_width + base_width)

            # Establecer el ancho de la columna
            tableWidget.setColumnWidth(col, max_width)

    def limpiar_tabla1(self):
        # Limpiar la primera tabla
        self.tableWidget.clear()

    def limpiar_tabla2(self):
        # Limpiar la segunda tabla
        self.tableWidget_2.clear()

    def limpiar_resultado(self):
        # Limpiar la tabla de resultado
        self.tableWidget_3.clear()

    def hacer_multiplicacion(self):
        # Obtener las matrices de las tablas
        matriz1 = self.obtener_matriz_desde_tabla(self.tableWidget)
        matriz2 = self.obtener_matriz_desde_tabla(self.tableWidget_2)

        # Realizar la multiplicación
        resultado = self.multiplicar_matrices(matriz1, matriz2)

        # Mostrar el resultado en la tabla
        self.mostrar_matriz_en_tabla(resultado, self.tableWidget_3)

    def obtener_matriz_desde_tabla(self, tableWidget):
        matriz = []
        for fila in range(tableWidget.rowCount()):
            fila_matriz = []
            for columna in range(tableWidget.columnCount()):
                item = tableWidget.item(fila, columna)
                if item is not None:
                    try:
                        valor = float(item.text())
                        fila_matriz.append(valor)
                    except ValueError:
                        fila_matriz.append(0.0)
            matriz.append(fila_matriz)
        return matriz

    def multiplicar_matrices(self, matriz1, matriz2):
        # Convertir las listas a matrices de numpy
        matriz1_np = np.array(matriz1)
        matriz2_np = np.array(matriz2)

        # Verificar que el número de columnas en la primera matriz es igual al número de filas en la segunda matriz
        if matriz1_np.shape[1] != matriz2_np.shape[0]:
            return "Error: El número de columnas en la primera matriz debe ser igual al número de filas en la segunda matriz"

        # Realizar la multiplicación
        resultado = np.dot(matriz1_np, matriz2_np)

        return resultado.tolist()

    def mostrar_matriz_en_tabla(self, matriz, tableWidget):
        if matriz is None:
            return

        # Limpiar la tabla antes de mostrar el resultado
        tableWidget.clear()

        # Obtener el tamaño de la matriz
        filas = len(matriz)
        columnas = len(matriz[0]) if filas > 0 else 0

        # Establecer el número de filas y columnas en la tabla
        tableWidget.setRowCount(filas)
        tableWidget.setColumnCount(columnas)

        # Mostrar los datos en la tabla
        for fila in range(filas):
            for columna in range(columnas):
                item = QtWidgets.QTableWidgetItem(str(matriz[fila][columna]))
                tableWidget.setItem(fila, columna, item)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MultiplicacionMatrices = QtWidgets.QMainWindow()
    ui = Ui_MultiplicacionMatrices()
    ui.setupUi(MultiplicacionMatrices)
    MultiplicacionMatrices.show()
    sys.exit(app.exec())
