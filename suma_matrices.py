from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SumaMatrices(object):
    def setupUi(self, SumaMatrices):
        SumaMatrices.setObjectName("SumaMatrices")
        SumaMatrices.resize(810, 958)
        SumaMatrices.setFixedSize(810, 958)

        self.centralwidget = QtWidgets.QWidget(parent=SumaMatrices)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 811, 921))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Imagenes/fondo.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, -20, 541, 131))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-13_085028-removebg-preview.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 90, 191, 51))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-13_090242-removebg-preview.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.spinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(440, 100, 151, 31))
        self.spinBox.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.spinBox.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"")
        self.spinBox.setObjectName("spinBox")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 140, 191, 41))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-13_090913-removebg-preview.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.spinBox_2 = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(440, 150, 151, 31))
        self.spinBox_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.spinBox_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"")
        self.spinBox_2.setObjectName("spinBox_2")
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
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(270, 500, 281, 81))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-13_092939-removebg-preview.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(60, 290, 211, 191))
        self.tableWidget.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget_2 = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(550, 290, 211, 191))
        self.tableWidget_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_3 = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget_3.setGeometry(QtCore.QRect(310, 590, 211, 191))
        self.tableWidget_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(320, 380, 181, 41))
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_10.setStyleSheet("background-color: rgb(0, 129, 185);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_15 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(380, 310, 51, 51))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("Imagenes/plus 2.png"))
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
        self.pushButton_11.setStyleSheet("background-color: rgb(0, 129, 185);\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(370, 800, 101, 41))
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_12.setStyleSheet("background-color: rgb(0, 129, 185);\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(610, 500, 101, 41))
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_13.setStyleSheet("background-color: rgb(0, 129, 185);\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_13.setObjectName("pushButton_13")
        SumaMatrices.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=SumaMatrices)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 26))
        self.menubar.setObjectName("menubar")
        SumaMatrices.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=SumaMatrices)
        self.statusbar.setObjectName("statusbar")
        SumaMatrices.setStatusBar(self.statusbar)

        self.retranslateUi(SumaMatrices)
        QtCore.QMetaObject.connectSlotsByName(SumaMatrices)

        self.spinBox.valueChanged.connect(self.updateTable)
        self.spinBox_2.valueChanged.connect(self.updateTable)

        self.pushButton_11.clicked.connect(self.clearTableWidget1)  # Botón de limpiar tabla 1
        self.pushButton_13.clicked.connect(self.clearTableWidget2)  # Botón de limpiar tabla 2
        self.pushButton_12.clicked.connect(self.clearTableWidget3)

        self.pushButton_10.clicked.connect(self.addMatrices)

        self.matriz1 = Matrix()
        self.matriz2 = Matrix()

    def retranslateUi(self, SumaMatrices):
        _translate = QtCore.QCoreApplication.translate
        SumaMatrices.setWindowTitle(_translate("SumaMatrices", "Suma de Matrices"))
        self.pushButton_10.setText(_translate("SumaMatrices", "Hacer Suma"))
        self.pushButton_11.setText(_translate("SumaMatrices", "Limpiar"))
        self.pushButton_12.setText(_translate("SumaMatrices", "Limpiar"))
        self.pushButton_13.setText(_translate("SumaMatrices", "Limpiar"))


    def updateTable(self):
        rows = self.spinBox.value()
        cols = self.spinBox_2.value()

        # Actualizar la cantidad de filas y columnas en la primera tabla
        self.tableWidget.setRowCount(rows)
        self.tableWidget.setColumnCount(cols)

        # Actualizar la cantidad de filas y columnas en la segunda tabla
        self.tableWidget_2.setRowCount(rows)
        self.tableWidget_2.setColumnCount(cols)

        # Actualizar la cantidad de filas y columnas en la tercera tabla
        self.tableWidget_3.setRowCount(rows)
        self.tableWidget_3.setColumnCount(cols)

        # Ajustar el tamaño de las columnas en las tablas
        self.adjustColumnWidths(self.tableWidget)
        self.adjustColumnWidths(self.tableWidget_2)
        self.adjustColumnWidths(self.tableWidget_3)

    def adjustColumnWidths(self, tableWidget):
        if tableWidget.columnCount() == 0:
            return

        # Ancho base de la columna
        base_width = 3

        for col in range(tableWidget.columnCount()):
            # Calcular el ancho máximo del contenido en cada columna
            max_width = base_width
            for row in range(tableWidget.rowCount()):
                item = tableWidget.item(row, col)
                if item is not None and item.text():
                    text_width = tableWidget.fontMetrics().boundingRect(item.text()).width()
                    max_width = max(max_width, text_width + base_width)  # Aumentar el ancho base si es necesario

            # Ajustar el ancho de la columna
            tableWidget.setColumnWidth(col, max_width)

    def clearTableWidget1(self):
        self.tableWidget.clear()

    # Función para limpiar la tabla 2
    def clearTableWidget2(self):
        self.tableWidget_2.clear()

    # Función para limpiar la tabla 3
    def clearTableWidget3(self):
        self.tableWidget_3.clear()

    def addition(self):
        try:
            result = addition(self.matriz1, self.matriz2)
            self.displayResult(result)
        except ValueError as e:
            self.showErrorMessage(str(e))

    def displayResult(self, result):
        rows = result.rows
        cols = result.columns
        self.tableWidget_3.setRowCount(rows)
        self.tableWidget_3.setColumnCount(cols)
        for i in range(rows):
            for j in range(cols):
                value = result.get_elemento(i, j)
                item = QtWidgets.QTableWidgetItem(str(value))
                self.tableWidget_3.setItem(i, j, item)

    def showErrorMessage(self, message):
        error_dialog = QtWidgets.QMessageBox()
        error_dialog.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        error_dialog.setText("Error\nDeben de Ser Números")
        error_dialog.setInformativeText(message)
        error_dialog.setWindowTitle("Error")
        error_dialog.exec()

    def addMatrices(self):
        try:
            self.setMatricesFromTables()

            result = addition(self.matriz1, self.matriz2)

            self.displayResult(result)
        except ValueError as e:
            self.showErrorMessage(str(e))

    def setMatricesFromTables(self):
        rows = self.tableWidget.rowCount()
        cols = self.tableWidget.columnCount()

        self.matriz1 = Matrix(rows, cols)
        self.matriz2 = Matrix(rows, cols)

        for i in range(rows):
            for j in range(cols):
                item1 = self.tableWidget.item(i, j)
                if item1 is not None:
                    value1 = float(item1.text()) if item1.text() else 0
                    self.matriz1.set_elemento(i, j, value1)

                item2 = self.tableWidget_2.item(i, j)
                if item2 is not None:
                    value2 = float(item2.text()) if item2.text() else 0
                    self.matriz2.set_elemento(i, j, value2)

class Matrix:
    def __init__(self, rows=0, columns=0):
        self.rows = rows
        self.columns = columns
        self.elements = [[0] * columns for _ in range(rows)]

    def check(self, other):
        return self.rows == other.rows and self.columns == other.columns

    def get_elemento(self, row, col):
        return self.elements[row][col]

    def set_elemento(self, row, col, value):
        self.elements[row][col] = value

    def clear(self):
        self.rows = 0
        self.columns = 0
        self.elements = []


def addition(matriz1, matriz2):
    if not matriz1.check(matriz2):
        raise ValueError("Las matrices deben tener el mismo tamaño para poder sumarlas.")
    resultado = Matrix(matriz1.rows, matriz1.columns)
    for i in range(matriz1.rows):
        for j in range(matriz1.columns):
            suma = matriz1.get_elemento(i, j) + matriz2.get_elemento(i, j)
            resultado.set_elemento(i, j, suma)
    return resultado


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SumaMatrices = QtWidgets.QMainWindow()
    ui = Ui_SumaMatrices()
    ui.setupUi(SumaMatrices)
    SumaMatrices.show()
    sys.exit(app.exec())
