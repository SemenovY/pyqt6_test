import sys
from PyQt6.QtWidgets import QApplication, QWidget

class EmptyWindow(QWidget):
    def __init__(self):
        """Конструктор для класса "Пустое окно"""
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Настройка приложения."""
        self.setGeometry(200, 100, 400, 300)
        self.setWindowTitle('Пустое окно в PyQt')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmptyWindow()
    sys.exit(app.exec())
