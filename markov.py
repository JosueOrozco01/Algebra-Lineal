from PyQt6 import QtCore, QtGui, QtWidgets
import numpy as np

class Ui_Markov(object):
    def setupUi(self, Markov):
        Markov.setObjectName("Markov")
        Markov.resize(700, 525)
        Markov.setFixedSize(700, 525)
        self.centralwidget = QtWidgets.QWidget(parent=Markov)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 701, 481))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Imagenes/fondo.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_14 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(200, 70, 221, 41))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-21_111348-removebg-preview.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.label_24 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(-10, 150, 81, 221))
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap("Imagenes/open-bracket.png"))
        self.label_24.setScaledContents(True)
        self.label_24.setObjectName("label_24")
        self.pushButton_19 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(80, 340, 81, 41))
        self.pushButton_19.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_19.setStyleSheet("background-color: rgb(0, 129, 185);\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_19.setObjectName("pushButton_19")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(70, 130, 101, 61))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-19_214409-removebg-preview.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.pushButton_18 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(430, 240, 81, 41))
        self.pushButton_18.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_18.setStyleSheet("background-color: rgb(0, 129, 185);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_18.setObjectName("pushButton_18")
        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(310, -10, 181, 81))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-21_110935-removebg-preview.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.spinBox_7 = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_7.setGeometry(QtCore.QRect(440, 70, 151, 31))
        self.spinBox_7.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.spinBox_7.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"")
        self.spinBox_7.setObjectName("spinBox_7")
        self.spinBox_7.setMinimum(1)
        self.tableWidget_6 = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget_6.setGeometry(QtCore.QRect(50, 190, 141, 131))
        self.tableWidget_6.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(3)
        self.tableWidget_6.setRowCount(3)
        self.label_25 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(170, 150, 81, 221))
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap("Imagenes/close-bracket.png"))
        self.label_25.setScaledContents(True)
        self.label_25.setObjectName("label_25")
        self.pushButton_22 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(630, 410, 61, 61))
        self.pushButton_22.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_22.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(218, 218, 218);\n"
"\n"
"\n"
"border-radius: 30px;\n"
"")
        self.pushButton_22.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagenes/files.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_22.setIcon(icon)
        self.pushButton_22.setObjectName("pushButton_22")
        self.tableWidget_7 = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget_7.setGeometry(QtCore.QRect(320, 190, 61, 131))
        self.tableWidget_7.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.tableWidget_7.setObjectName("tableWidget_7")
        self.tableWidget_7.setColumnCount(1)
        self.tableWidget_7.setRowCount(3)
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(200, 210, 101, 101))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("Imagenes/multiplication.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.tableWidget_8 = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget_8.setGeometry(QtCore.QRect(560, 190, 61, 131))
        self.tableWidget_8.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.tableWidget_8.setObjectName("tableWidget_8")
        self.tableWidget_8.setColumnCount(1)
        self.tableWidget_8.setRowCount(3)
        self.label_15 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(300, 130, 101, 61))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-21_111532-removebg-preview.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(500, 130, 171, 61))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-21_111911-removebg-preview.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.label_26 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(260, 150, 81, 221))
        self.label_26.setText("")
        self.label_26.setPixmap(QtGui.QPixmap("Imagenes/open-bracket.png"))
        self.label_26.setScaledContents(True)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(360, 150, 81, 221))
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap("Imagenes/close-bracket.png"))
        self.label_27.setScaledContents(True)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(500, 150, 81, 221))
        self.label_28.setText("")
        self.label_28.setPixmap(QtGui.QPixmap("Imagenes/open-bracket.png"))
        self.label_28.setScaledContents(True)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(600, 150, 81, 221))
        self.label_29.setText("")
        self.label_29.setPixmap(QtGui.QPixmap("Imagenes/close-bracket.png"))
        self.label_29.setScaledContents(True)
        self.label_29.setObjectName("label_29")
        self.pushButton_20 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(310, 350, 81, 41))
        self.pushButton_20.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_20.setStyleSheet("background-color: rgb(0, 129, 185);\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(550, 350, 81, 41))
        self.pushButton_21.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_21.setStyleSheet("background-color: rgb(0, 129, 185);\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_21.setObjectName("pushButton_21")
        Markov.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Markov)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 26))
        self.menubar.setObjectName("menubar")
        Markov.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Markov)
        self.statusbar.setObjectName("statusbar")
        Markov.setStatusBar(self.statusbar)

        self.retranslateUi(Markov)
        QtCore.QMetaObject.connectSlotsByName(Markov)

        # Ajustar el tamaño de las columnas según el contenido
        self.tableWidget_6.resizeColumnsToContents()
        self.tableWidget_7.resizeColumnsToContents()
        self.tableWidget_8.resizeColumnsToContents()

        self.pushButton_19.clicked.connect(self.clearTableWidget1)
        self.pushButton_20.clicked.connect(self.clearTableWidget2)
        self.pushButton_21.clicked.connect(self.clearTableWidget3)
        self.pushButton_18.clicked.connect(self.calculate_markov)


    def retranslateUi(self, Markov):
        _translate = QtCore.QCoreApplication.translate
        Markov.setWindowTitle(_translate("Markov", "Markov"))
        self.pushButton_19.setText(_translate("Markov", "Limpiar"))
        self.pushButton_18.setText(_translate("Markov", "Calcular"))
        self.pushButton_20.setText(_translate("Markov", "Limpiar"))
        self.pushButton_21.setText(_translate("Markov", "Limpiar"))

    def clearTableWidget1(self):
        self.tableWidget_6.clear()

    def clearTableWidget2(self):
        self.tableWidget_7.clear()

    def clearTableWidget3(self):
        self.tableWidget_8.clear()

    def calculate_markov(self):
        # Obtener la matriz principal
        main_matrix = np.zeros((3, 3))
        for i in range(3):
            for j in range(3):
                item = self.tableWidget_6.item(i, j)
                if item and item.text():
                    main_matrix[i][j] = float(item.text())

        # Obtener la matriz inicial
        initial_matrix = np.zeros((3, 1))
        for i in range(3):
            item = self.tableWidget_7.item(i, 0)
            if item and item.text():
                initial_matrix[i][0] = float(item.text())

        # Obtener el número de multiplicaciones
        num_iterations = self.spinBox_7.value()

        # Calcular el resultado
        result_matrix = np.linalg.matrix_power(main_matrix, num_iterations).dot(initial_matrix)

        # Mostrar el resultado en la tercera tabla
        for i in range(3):
            self.tableWidget_8.setItem(i, 0, QtWidgets.QTableWidgetItem(f"{result_matrix[i][0]:.2f}"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Markov = QtWidgets.QMainWindow()
    ui = Ui_Markov()
    ui.setupUi(Markov)
    Markov.show()
    sys.exit(app.exec())
