import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QHBoxLayout,
                            QVBoxLayout, QPushButton, QLabel, QLineEdit)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.counter = 0

    def init_ui(self):
        label = QLabel("NAME: ")
        name_input = QLineEdit()
        self.button = QPushButton("Clicked: 0")
        # button.clicked.connect(self.click)
        self.button.pressed.connect(self.press)
        self.button.released.connect(self.click)

        h= QHBoxLayout()
        #h.addStretch(1)
        h.addWidget(label)
        h.addWidget(name_input)

        v = QVBoxLayout()
        #v.addStretch(1)
        v.addLayout(h)
        v.addWidget(self.button)

        self.setLayout(v)
        self.setWindowTitle("Horizontal Layout")
        self.show()

    def click(self):
        print("THIS BUTTON HAS BEEN REALISED!!!")

    def press(self):
        print("THIS BUTTON HAS BEEN PRESSED!!!")
        self.counter += 1
        self.button.setText("Clicked: " + str(self.counter))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


