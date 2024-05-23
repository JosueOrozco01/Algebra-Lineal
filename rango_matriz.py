from PyQt6 import QtCore, QtGui, QtWidgets
import numpy as np

class Ui_RangoMatriz(object):
    def setupUi(self, RangoMatriz):
        RangoMatriz.setObjectName("RangoMatriz")
        RangoMatriz.resize(699, 592)
        RangoMatriz.setFixedSize(699, 592)
        self.centralwidget = QtWidgets.QWidget(parent=RangoMatriz)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 701, 551))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Imagenes/fondo.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(120, 0, 451, 81))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-19_175401-removebg-preview.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.spinBox_8 = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_8.setGeometry(QtCore.QRect(390, 140, 151, 31))
        self.spinBox_8.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.spinBox_8.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"")
        self.spinBox_8.setObjectName("spinBox_8")
        self.label_14 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(190, 80, 201, 51))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-13_090242-removebg-preview.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(190, 130, 201, 41))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-13_090913-removebg-preview.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.spinBox_7 = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_7.setGeometry(QtCore.QRect(390, 90, 151, 31))
        self.spinBox_7.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.spinBox_7.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"")
        self.spinBox_7.setObjectName("spinBox_7")
        self.label_24 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(20, 210, 81, 301))
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap("Imagenes/open-bracket.png"))
        self.label_24.setScaledContents(True)
        self.label_24.setObjectName("label_24")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(490, 250, 131, 71))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-19_214549-removebg-preview.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.tableWidget_7 = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget_7.setGeometry(QtCore.QRect(520, 320, 71, 71))
        self.tableWidget_7.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.tableWidget_7.setObjectName("tableWidget_7")
        self.tableWidget_7.setColumnCount(0)
        self.tableWidget_7.setRowCount(0)
        self.pushButton_20 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(500, 410, 111, 41))
        self.pushButton_20.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_20.setStyleSheet("background-color: rgb(0, 129, 185);\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_20.setObjectName("pushButton_20")
        self.tableWidget_6 = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget_6.setGeometry(QtCore.QRect(80, 260, 211, 191))
        self.tableWidget_6.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(0)
        self.tableWidget_6.setRowCount(0)
        self.pushButton_19 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(130, 470, 101, 41))
        self.pushButton_19.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_19.setStyleSheet("background-color: rgb(0, 129, 185);\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_19.setObjectName("pushButton_19")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(120, 190, 141, 81))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-19_214409-removebg-preview.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_25 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(270, 210, 81, 301))
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap("Imagenes/close-bracket.png"))
        self.label_25.setScaledContents(True)
        self.label_25.setObjectName("label_25")
        self.pushButton_21 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(630, 470, 61, 61))
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
        self.pushButton_18 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(350, 340, 121, 41))
        self.pushButton_18.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_18.setStyleSheet("background-color: rgb(0, 129, 185);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_18.setObjectName("pushButton_18")
        RangoMatriz.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=RangoMatriz)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 699, 26))
        self.menubar.setObjectName("menubar")
        RangoMatriz.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=RangoMatriz)
        self.statusbar.setObjectName("statusbar")
        RangoMatriz.setStatusBar(self.statusbar)

        self.retranslateUi(RangoMatriz)
        QtCore.QMetaObject.connectSlotsByName(RangoMatriz)

        self.spinBox_7.valueChanged.connect(self.updateTable)
        self.spinBox_8.valueChanged.connect(self.updateTable)

        self.pushButton_19.clicked.connect(self.clearTableWidget1)  # Botón de limpiar tabla 1
        self.pushButton_20.clicked.connect(self.clearTableWidget2)
        self.pushButton_18.clicked.connect(self.calculateRank)

    def retranslateUi(self, RangoMatriz):
        _translate = QtCore.QCoreApplication.translate
        RangoMatriz.setWindowTitle(_translate("RangoMatriz", "Rango de una Matriz"))
        self.pushButton_20.setText(_translate("RangoMatriz", "Limpiar"))
        self.pushButton_19.setText(_translate("RangoMatriz", "Limpiar"))
        self.pushButton_18.setText(_translate("RangoMatriz", "Calcular Rango"))

    def updateTable(self):
        rows = self.spinBox_7.value()
        cols = self.spinBox_8.value()

        # Actualizar la cantidad de filas y columnas en la primera tabla
        self.tableWidget_6.setRowCount(rows)
        self.tableWidget_6.setColumnCount(cols)

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

    def calculateRank(self):
        rows = self.tableWidget_6.rowCount()
        cols = self.tableWidget_6.columnCount()

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

        # Convertir a numpy array y calcular el rango
        matrix = np.array(matrix)
        rank = np.linalg.matrix_rank(matrix)

        # Mostrar el rango en la tabla 2
        self.tableWidget_7.setRowCount(1)
        self.tableWidget_7.setColumnCount(1)
        self.tableWidget_7.setItem(0, 0, QtWidgets.QTableWidgetItem(str(rank)))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RangoMatriz = QtWidgets.QMainWindow()
    ui = Ui_RangoMatriz()
    ui.setupUi(RangoMatriz)
    RangoMatriz.show()
    sys.exit(app.exec())
