from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ProductoCruz(object):
    def setupUi(self, ProductoCruz):
        ProductoCruz.setObjectName("ProductoCruz")
        ProductoCruz.resize(403, 285)
        ProductoCruz.setFixedSize(403, 285)
        self.centralwidget = QtWidgets.QWidget(parent=ProductoCruz)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 401, 241))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Imagenes/fondo.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_27 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_27.setGeometry(QtCore.QRect(290, 150, 61, 61))
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
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 10, 331, 201))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Imagenes/Captura_de_pantalla_2024-05-23_004946-removebg-preview.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        ProductoCruz.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=ProductoCruz)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 403, 26))
        self.menubar.setObjectName("menubar")
        ProductoCruz.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=ProductoCruz)
        self.statusbar.setObjectName("statusbar")
        ProductoCruz.setStatusBar(self.statusbar)

        self.retranslateUi(ProductoCruz)
        QtCore.QMetaObject.connectSlotsByName(ProductoCruz)

    def retranslateUi(self, ProductoCruz):
        _translate = QtCore.QCoreApplication.translate
        ProductoCruz.setWindowTitle(_translate("ProductoCruz", "Producto Cruz de Vectores"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProductoCruz = QtWidgets.QMainWindow()
    ui = Ui_ProductoCruz()
    ui.setupUi(ProductoCruz)
    ProductoCruz.show()
    sys.exit(app.exec())
