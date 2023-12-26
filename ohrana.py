from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
import sys
from PyQt6.QtCore import QDateTime, Qt
import sqlite3
import random

class SecurityTerminal(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # Создаем поля ввода для данных охранника
        self.name_label = QLabel("Фамилия:")
        self.name_input = QLineEdit(self)
        self.username_label = QLabel("Имя:")
        self.username_input = QLineEdit(self)
        self.patronymic_label = QLabel("Отчество:")
        self.patronymic_input = QLineEdit(self)

        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.patronymic_label)
        layout.addWidget(self.patronymic_input)

        # Создаем кнопку для входа и выхода
        self.check_in_button = QPushButton('Войти', self)
        self.check_in_button.clicked.connect(self.check_in)
        layout.addWidget(self.check_in_button)

        self.check_out_button = QPushButton('Выйти', self)
        self.check_out_button.clicked.connect(self.check_out)
        layout.addWidget(self.check_out_button)

        # Добавляем кнопку временного пропуска
        self.skip_button = QPushButton('Временный пропуск', self)
        self.skip_button.clicked.connect(self.generate_random_numbers)
        layout.addWidget(self.skip_button)

        # Создаем метку для вывода сообщений
        self.message_label = QLabel(self)
        layout.addWidget(self.message_label)

        self.setLayout(layout)
        self.setWindowTitle('Учет посещаемости сотрудников')

    def check_in(self):
        name = self.name_input.text()
        surname = self.username_input.text()
        second_name = self.patronymic_input.text()

        if name and surname and second_name:
            connect = sqlite3.connect("base_data.db")
            cursor = connect.cursor()

            cursor.execute("select * from base_data where name = ? and surname = ? and second_name = ?",
                           (name, surname, second_name))
            result = cursor.fetchone()

            if result:
                self.message_label.setText("Пожалуйста, пройдите через турникет")
                connect_2 = sqlite3.connect("base_data_2.db")
                cursor_2 = connect_2.cursor()
                time = QDateTime.currentDateTime().toString(Qt.DateFormat.ISODate)

                cursor_2.execute("INSERT INTO base_data_2 (name, surname,entrance_time) VALUES (?, ?, ?)",
                                 (name, surname, time))

                connect_2.commit()
                cursor_2.close()
                connect_2.close()
            else:
                self.message_label.setText("Простите, вас нет в списке")
            connect.close()

    def check_out(self):
        name = self.name_input.text()
        surname = self.username_input.text()
        second_name = self.patronymic_input.text()

        if name and surname and second_name:
            connect = sqlite3.connect("base_data.db")
            cursor = connect.cursor()

            cursor.execute("select * from base_data where name = ? and surname = ? and second_name = ?",
                           (name, surname, second_name))
            result = cursor.fetchone()

            if result:
                self.message_label.setText("Доступ разрешен")
                connect_2 = sqlite3.connect("base_data_2.db")
                cursor_2 = connect_2.cursor()
                time = QDateTime.currentDateTime().toString(Qt.DateFormat.ISODate)

                cursor_2.execute("INSERT INTO base_data_2 (name, surname,entrance_time) VALUES (?, ?, ?)",
                                 (name, surname, time))

                connect_2.commit()
                cursor_2.close()
                connect_2.close()
            else:
                self.message_label.setText("Доступ запрещен")
            connect.close()

    def generate_random_numbers(self):
        random_numbers = [random.randint(0, 9) for _ in range(4)]
        self.message_label.setText(f'Временный пропуск: {random_numbers}')

    def passage_time(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SecurityTerminal()
    window.show()
    sys.exit(app.exec())
