from PyQt6 import QtCore, QtGui, QtWidgets
import numpy as np

class Ui_DeterminanteMatriz(object):
    def setupUi(self, DeterminanteMatriz):
        DeterminanteMatriz.setObjectName("DeterminanteMatriz")
        DeterminanteMatriz.resize(689, 600)
        DeterminanteMatriz.setFixedSize(689, 600)
        self.centralwidget = QtWidgets.QWidget(parent=DeterminanteMatriz)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 691, 561))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Imagenes/fondo.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_25 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(280, 220, 81, 301))
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap("Imagenes/close-bracket.png"))
        self.label_25.setScaledContents(True)
        self.label_25.setObjectName("label_25")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(140, 130, 201, 41))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-13_090913-removebg-preview.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(140, 80, 201, 51))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-13_090242-removebg-preview.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.tableWidget_7 = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget_7.setGeometry(QtCore.QRect(530, 330, 71, 71))
        self.tableWidget_7.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.tableWidget_7.setObjectName("tableWidget_7")
        self.tableWidget_7.setColumnCount(0)
        self.tableWidget_7.setRowCount(0)
        self.pushButton_20 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(510, 420, 111, 41))
        self.pushButton_20.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_20.setStyleSheet("background-color: rgb(0, 129, 185);\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_18 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(350, 350, 141, 41))
        self.pushButton_18.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_18.setStyleSheet("background-color: rgb(0, 129, 185);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(140, 480, 101, 41))
        self.pushButton_19.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_19.setStyleSheet("background-color: rgb(0, 129, 185);\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_19.setObjectName("pushButton_19")
        self.spinBox_5 = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_5.setGeometry(QtCore.QRect(340, 140, 151, 31))
        self.spinBox_5.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.spinBox_5.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"")
        self.spinBox_5.setObjectName("spinBox_5")
        self.label_24 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(30, 220, 81, 301))
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap("Imagenes/open-bracket.png"))
        self.label_24.setScaledContents(True)
        self.label_24.setObjectName("label_24")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(100, -10, 471, 91))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-19_213128-removebg-preview.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.tableWidget_6 = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget_6.setGeometry(QtCore.QRect(90, 270, 211, 191))
        self.tableWidget_6.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(0)
        self.tableWidget_6.setRowCount(0)
        self.spinBox_6 = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_6.setGeometry(QtCore.QRect(340, 90, 151, 31))
        self.spinBox_6.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.spinBox_6.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"")
        self.spinBox_6.setObjectName("spinBox_6")
        self.pushButton_21 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(620, 480, 61, 61))
        self.pushButton_21.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_21.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(218, 218, 218);\n"
"\n"
"\n"
"border-radius: 30px;\n"
"")
        self.pushButton_21.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagenes/files.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_21.setIcon(icon)
        self.pushButton_21.setObjectName("pushButton_21")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(130, 200, 141, 81))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-19_214409-removebg-preview.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(470, 240, 201, 81))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-19_215054-removebg-preview.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        DeterminanteMatriz.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=DeterminanteMatriz)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 689, 26))
        self.menubar.setObjectName("menubar")
        DeterminanteMatriz.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=DeterminanteMatriz)
        self.statusbar.setObjectName("statusbar")
        DeterminanteMatriz.setStatusBar(self.statusbar)

        self.retranslateUi(DeterminanteMatriz)
        QtCore.QMetaObject.connectSlotsByName(DeterminanteMatriz)

        self.spinBox_5.valueChanged.connect(self.updateTable)
        self.spinBox_6.valueChanged.connect(self.updateTable)

        self.pushButton_19.clicked.connect(self.clearTableWidget1)  # Botón de limpiar tabla 1
        self.pushButton_20.clicked.connect(self.clearTableWidget2)
        self.pushButton_18.clicked.connect(self.calculateDeterminant)  # Conectar botón para calcular determinante

    def retranslateUi(self, DeterminanteMatriz):
        _translate = QtCore.QCoreApplication.translate
        DeterminanteMatriz.setWindowTitle(_translate("DeterminanteMatriz", "Determinante de una Matriz"))
        self.pushButton_20.setText(_translate("DeterminanteMatriz", "Limpiar"))
        self.pushButton_18.setText(_translate("DeterminanteMatriz", "Calcular Determinante"))
        self.pushButton_19.setText(_translate("DeterminanteMatriz", "Limpiar"))

    def updateTable(self):
        cols = self.spinBox_5.value()
        rows = self.spinBox_6.value()

        # Actualizar la cantidad de filas y columnas en la primera tabla
        self.tableWidget_6.setRowCount(rows)
        self.tableWidget_6.setColumnCount(cols)

        # Ajustar el tamaño de las columnas en las tablas
        self.adjustColumnWidths(self.tableWidget_6)

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
        self.tableWidget_6.clear()

    # Función para limpiar la tabla 2
    def clearTableWidget2(self):
        self.tableWidget_7.clear()

    def calculateDeterminant(self):
        rows = self.tableWidget_6.rowCount()
        cols = self.tableWidget_6.columnCount()

        if rows != cols:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Error",
                                          "La matriz debe ser cuadrada para calcular el determinante.")
            return

        # Obtener los valores de la tabla 1
        matrix = []
        for row in range(rows):
            rowData = []
            for col in range(cols):
                item = self.tableWidget_6.item(row, col)
                if item and item.text():
                    rowData.append(float(item.text()))
                else:
                    rowData.append(0.0)
            matrix.append(rowData)

        # Convertir a numpy array y calcular el determinante
        matrix = np.array(matrix)
        determinant = np.linalg.det(matrix)

        # Mostrar el determinante en la tabla 2 con tres decimales
        formatted_det = "{:.3f}".format(determinant)
        self.tableWidget_7.setRowCount(1)
        self.tableWidget_7.setColumnCount(1)
        self.tableWidget_7.setItem(0, 0, QtWidgets.QTableWidgetItem(formatted_det))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DeterminanteMatriz = QtWidgets.QMainWindow()
    ui = Ui_DeterminanteMatriz()
    ui.setupUi(DeterminanteMatriz)
    DeterminanteMatriz.show()
    sys.exit(app.exec())
