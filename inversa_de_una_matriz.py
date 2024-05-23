from PyQt6 import QtCore, QtGui, QtWidgets
import numpy as np

def calcular_inversa(matriz):
    try:
        matriz_np = np.array(matriz)
        inversa_np = np.linalg.inv(matriz_np)
        return inversa_np.tolist()
    except np.linalg.LinAlgError:
        return "La matriz no es invertible"

class Ui_InversaMatriz(object):
    def setupUi(self, InversaMatriz):
        InversaMatriz.setObjectName("InversaMatriz")
        InversaMatriz.resize(796, 608)
        InversaMatriz.setFixedSize(796, 608)
        self.centralwidget = QtWidgets.QWidget(parent=InversaMatriz)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 571))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Imagenes/fondo.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 0, 441, 61))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-16_090531-removebg-preview.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_26 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(240, 190, 81, 301))
        self.label_26.setText("")
        self.label_26.setPixmap(QtGui.QPixmap("Imagenes/close-bracket.png"))
        self.label_26.setScaledContents(True)
        self.label_26.setObjectName("label_26")
        self.tableWidget_5 = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget_5.setGeometry(QtCore.QRect(50, 250, 211, 191))
        self.tableWidget_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(0)
        self.tableWidget_5.setRowCount(0)
        self.spinBox_4 = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_4.setGeometry(QtCore.QRect(420, 140, 151, 31))
        self.spinBox_4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.spinBox_4.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"")
        self.spinBox_4.setObjectName("spinBox_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 130, 191, 41))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-13_090913-removebg-preview.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(220, 80, 191, 51))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-13_090242-removebg-preview.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_22 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(480, 190, 81, 301))
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap("Imagenes/open-bracket.png"))
        self.label_22.setScaledContents(True)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(-10, 190, 81, 301))
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap("Imagenes/open-bracket.png"))
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName("label_23")
        self.spinBox_3 = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(420, 90, 151, 31))
        self.spinBox_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.spinBox_3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"")
        self.spinBox_3.setObjectName("spinBox_3")
        self.label_25 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(730, 190, 81, 301))
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap("Imagenes/close-bracket.png"))
        self.label_25.setScaledContents(True)
        self.label_25.setObjectName("label_25")
        self.tableWidget_4 = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget_4.setGeometry(QtCore.QRect(540, 250, 211, 191))
        self.tableWidget_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setRowCount(0)
        self.spinBox_rows = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_rows.setGeometry(QtCore.QRect(420, 140, 151, 31))
        self.spinBox_rows.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.spinBox_rows.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
                                        "")
        self.spinBox_rows.setObjectName("spinBox_rows")
        self.spinBox_rows.valueChanged.connect(self.update_matrix)  # Conectar el cambio de valor a la función
        self.spinBox_columns = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_columns.setGeometry(QtCore.QRect(420, 90, 151, 31))
        self.spinBox_columns.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.spinBox_columns.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
                                           "")
        self.spinBox_columns.setObjectName("spinBox_columns")
        self.spinBox_columns.valueChanged.connect(self.update_matrix)  # Conectar el cambio de valor a la función
        self.pushButton_15 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(310, 340, 181, 41))
        self.pushButton_15.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_15.setStyleSheet("background-color: rgb(0, 129, 185);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_24 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(360, 260, 71, 81))
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap("Imagenes/equal-mathematical-sign.png"))
        self.label_24.setScaledContents(True)
        self.label_24.setObjectName("label_24")
        self.pushButton_14 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(100, 460, 101, 41))
        self.pushButton_14.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_14.setStyleSheet("background-color: rgb(0, 129, 185);\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_16 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(600, 460, 101, 41))
        self.pushButton_16.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_16.setStyleSheet("background-color: rgb(0, 129, 185);\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_16.setObjectName("pushButton_16")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 180, 191, 61))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-16_173423-removebg-preview.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(550, 180, 191, 61))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-16_173553-removebg-preview.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        InversaMatriz.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=InversaMatriz)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 26))
        self.menubar.setObjectName("menubar")
        InversaMatriz.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=InversaMatriz)
        self.statusbar.setObjectName("statusbar")
        InversaMatriz.setStatusBar(self.statusbar)

        self.retranslateUi(InversaMatriz)
        QtCore.QMetaObject.connectSlotsByName(InversaMatriz)

        self.pushButton_16.clicked.connect(self.clearTableWidget1)
        self.pushButton_14.clicked.connect(self.clearTableWidget2)

        self.pushButton_15.clicked.connect(self.invertirMatriz)

    def retranslateUi(self, InversaMatriz):
        _translate = QtCore.QCoreApplication.translate
        InversaMatriz.setWindowTitle(_translate("InversaMatriz", "Inversa de una Matriz"))
        self.pushButton_15.setText(_translate("InversaMatriz", "Invertir Matriz"))
        self.pushButton_14.setText(_translate("InversaMatriz", "Limpiar"))
        self.pushButton_16.setText(_translate("InversaMatriz", "Limpiar"))

    def update_matrix(self):
        columns = self.spinBox_rows.value()
        rows = self.spinBox_columns.value()
        self.tableWidget_5.setRowCount(rows)
        self.tableWidget_5.setColumnCount(columns)
        self.tableWidget_4.setRowCount(rows)
        self.tableWidget_4.setColumnCount(columns)

        self.adjustColumnWidths(self.tableWidget_4)
        self.adjustColumnWidths(self.tableWidget_5)

    def retranslateUi(self, InversaMatriz):
        _translate = QtCore.QCoreApplication.translate
        InversaMatriz.setWindowTitle(_translate("InversaMatriz", "Inversa de una Matriz"))
        self.pushButton_15.setText(_translate("InversaMatriz", "Invertir Matriz"))
        self.pushButton_14.setText(_translate("InversaMatriz", "Limpiar"))
        self.pushButton_16.setText(_translate("InversaMatriz", "Limpiar"))

    def adjustColumnWidths(self, tableWidget):
        if tableWidget.columnCount() == 0:
            return

        # Ancho base de la columna
        base_width = 25

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
        self.tableWidget_4.clear()

    def clearTableWidget2(self):
        self.tableWidget_5.clear()

    def invertirMatriz(self):
        # Obtener los valores de la matriz de la interfaz gráfica
        matriz = []
        for row in range(self.tableWidget_5.rowCount()):
            fila = []
            for column in range(self.tableWidget_5.columnCount()):
                item = self.tableWidget_5.item(row, column)
                if item is not None:
                    fila.append(float(item.text()))
                else:
                    fila.append(0.0)
            matriz.append(fila)

        # Calcular la inversa
        inversa = calcular_inversa(matriz)

        if isinstance(inversa, str):  # Si hay un error en el cálculo
            QtWidgets.QMessageBox.warning(self.centralwidget, "Error", inversa)
        else:
            # Mostrar la inversa en la segunda tablaWidget
            for row in range(len(inversa)):
                for column in range(len(inversa[0])):
                    # Formatear el número con dos decimales
                    item = QtWidgets.QTableWidgetItem("{:.3f}".format(inversa[row][column]))
                    self.tableWidget_4.setItem(row, column, item)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InversaMatriz = QtWidgets.QMainWindow()
    ui = Ui_InversaMatriz()
    ui.setupUi(InversaMatriz)
    InversaMatriz.show()
    sys.exit(app.exec())
