import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def setUpMainWindow(self):
        """Создайте QLabel для отображения в главном окне."""
        hello_label = QLabel(self)
        hello_label.setText("Hello")
        hello_label.move(105, 15)
        image = "images/hello.png"
        try:
            with open(image):
                world_label = QLabel(self)
                pixmap = QPixmap(image)
                world_label.setPixmap(pixmap)
                world_label.move(25, 40)
        except FileNotFoundError as error:
            print(f"image not found.\nError:{error}")

    def initializeUI(self):
        """Настройте графический интерфейс приложения."""
        self.setGeometry(100, 100, 250, 250)
        self.setWindowTitle('Primer Qlabel')
        self.setUpMainWindow
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
