import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QHBoxLayout,
                            QVBoxLayout, QPushButton, QLabel, QLineEdit)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.label = QLabel("name: ")
        self.text_label = QLabel("No name entered")
        self.name_input = QLineEdit()
        self.button = QPushButton("Clicked: 0")

        self.button.setText("Set name")
        self.button.clicked.connect(self.alterName)

        h = QHBoxLayout()
    #   h.addStretch(1)
        h.addWidget(self.label)
        h.addWidget(self.name_input)

        v = QVBoxLayout()
        v.addWidget(self.text_label)
    #   v.addStretch(1)
        v.addLayout(h)
        v.addWidget(self.button)

        self.setLayout(v)
        self.setWindowTitle("Nothing has been cliked")
        self.show()

    def alterName(self):
        inputted_text = self.name_input.text()
        our_string = "You've entered " + inputted_text
        self.text_label.setText(our_string)
        self.setWindowTitle(inputted_text + "'s Window")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


