import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt
from random import randint

class GuessNumberGame(QWidget):
    def __init__(self):
        super().__init__()

        self.secret_number = randint(1, 100)
        self.attempts_left = 5

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Угадай число')
        self.setGeometry(300, 300, 300, 200)

        self.label = QLabel('Угадай число от 1 до 100', self)
        self.entry = QLineEdit(self)
        self.submit_button = QPushButton('Попробовать', self)
        self.result_label = QLabel(self)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.entry)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.result_label)

        self.submit_button.clicked.connect(self.check_guess)

        self.show()

    def check_guess(self):
        guess = self.entry.text()
        if guess.isdigit():
            guess = int(guess)

            if guess == self.secret_number:
                self.result_label.setText('Поздравляем! Вы угадали число!')
                self.submit_button.setEnabled(False)
            else:
                self.attempts_left -= 1
                if guess < self.secret_number:
                    hint = 'Загаданное число больше.'
                else:
                    hint = 'Загаданное число меньше.'

                if self.attempts_left > 0:
                    self.result_label.setText(f'Неправильно. {hint} У вас осталось {self.attempts_left} попыток.')
                else:
                    self.result_label.setText(f'Вы проиграли. Загаданное число было {self.secret_number}.')
                    self.submit_button.setEnabled(False)
        else:
            self.result_label.setText('Пожалуйста, введите число.')

def main():
    app = QApplication(sys.argv)
    game = GuessNumberGame()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
