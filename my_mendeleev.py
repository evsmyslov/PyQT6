from PyQt6 import QtWidgets
from my_periodic import Ui_MainWindow
import csv

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.ui.tableWidget.horizontalHeader().setDefaultSectionSize(53)
        self.ui.pushButton.clicked.connect(self.on_clicked)

    def on_clicked(self):
        try:
            self.ui.textEdit.clear()
            self.ui.tableWidget.clearContents()
            self.ui.tableWidget.setRowCount(0)  # Clear table rows

            with open('periodictable.csv') as file:
                reader = csv.reader(file)
                element_data = list(reader)

            columns = ['Atomic Number', 'Symbol', 'Element', 'Origin of name', 'Group', 'Period', 'Atomic weight',
                       'Density', 'Melting point', 'Boiling point', 'Specific heat capacity', 'Electronegativity',
                       'Abundance in earths crust']

            user_input = self.ui.lineEdit.text()
            self.ui.lineEdit.clear()

            for row in element_data:
                if user_input in row:
                    self.add_row_to_table(row, columns)
                    self.show_element_info(row, columns)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, 'Error', f'An error occurred: {str(e)}')

    def add_row_to_table(self, row, columns):
        current_row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(current_row)
        for col_idx, value in enumerate(row):
            item = QtWidgets.QTableWidgetItem(value)
            self.ui.tableWidget.setItem(current_row, col_idx, item)

    def show_element_info(self, row, columns):
        for col_idx, value in enumerate(row):
            true = columns[col_idx].rjust(max(map(len, columns)))
            self.ui.textEdit.append(true + ': ' + value)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.resize(1050, 800)
    window.show()
    sys.exit(app.exec())
