from PyQt5 import *
from PyQt5.QtWidgets import *

class Page(QWidget):
    def __init__(self):
        super(Page, self).__init__(parent=None)

        my_label = QLabel("This is my label")
        layout = QVBoxLayout()

        layout.addWidget(my_label)

        mainLayout = QGridLayout()
        mainLayout.addLayout(layout,0,1)

        self.setLayout(mainLayout)
        self.setWindowTitle("My first pyQT app")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Page()
    window.show()

    sys.exit(app.exec_())






