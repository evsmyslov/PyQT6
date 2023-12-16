import sys
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
import random, time

class MillionDiceRollSimulator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Million Dice Roll Statistics Simulator')
        layout = QVBoxLayout()

        label = QLabel("Enter how many six-sided dice you want to roll:")
        layout.addWidget(label)

        self.inputField = QLineEdit()
        layout.addWidget(self.inputField)

        button = QPushButton("Simulate Rolls")
        button.clicked.connect(self.simulateRolls)
        layout.addWidget(button)

        self.resultsLabel = QLabel()
        layout.addWidget(self.resultsLabel)

        self.setLayout(layout)

    def simulateRolls(self):
        numberOfDice = int(self.inputField.text())
        results = {}
        for i in range(numberOfDice, (numberOfDice * 6) + 1):
            results[i] = 0

        lastPrintTime = time.time()
        for i in range(1000000):
            if time.time() > lastPrintTime + 1:
                print('{}% done...'.format(round(i / 10000, 1)))
                lastPrintTime = time.time()

            total = 0
            for j in range(numberOfDice):
                total = total + random.randint(1, 6)
            results[total] = results[total] + 1

        resultText = 'TOTAL - ROLLS - PERCENTAGE\n'
        for i in range(numberOfDice, (numberOfDice * 6) + 1):
            roll = results[i]
            percentage = round(results[i] / 10000, 1)
            resultText += f'{i} - {roll} rolls - {percentage}%\n'

        self.resultsLabel.setText(resultText)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MillionDiceRollSimulator()
    widget.show()
    sys.exit(app.exec())