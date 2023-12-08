from PyQt6 import QtWidgets, QtCore

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel("Hello, world!")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.btnQuit = QtWidgets.QPushButton("Quit")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnQuit)
        self.setLayout(self.vbox)
        self.btnQuit.clicked.connect(QtWidgets.QApplication.instance().quit)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Hello, world!2")
    window.resize(300, 70)
    window.show()
    sys.exit(app.exec())
