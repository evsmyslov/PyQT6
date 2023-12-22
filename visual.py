from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1041, 823)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton("Отправить", parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(920, 370, 101, 25))

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 1011, 341))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(9)
        self.tableWidget.setColumnCount(18)


        header_labels = [str(i) for i in range(1, 19)]
        self.tableWidget.setHorizontalHeaderLabels(header_labels)
        self.tableWidget.setVerticalHeaderLabels(["1", "2", "3", "4", "5", "6", "7", "Ce", "Th"])

        elements = ["H",
                    "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar",
                    "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br",
                    "Kr",
                    "Rd", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sd", "Te", "I",
                    "Kr",
                    "Cs", "Ba", "La", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pd", "Bi", "Po", "At",
                    "Rn",
                    "Fr", "Ra", "Ac", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv",
                    "Ts", "Og"]

        for row in range(9):
            for col in range(18):
                item = QtWidgets.QTableWidgetItem(elements[row * 18 + col] if row * 18 + col < len(elements) else "")
                self.tableWidget.setItem(row, col, item)

        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(790, 370, 113, 25))
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 440, 471, 211))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1041, 22))
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Отправить "))



