
import os,sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQuick import *
from PyQt5.Qt import *

if __name__ == '__main__':
    # создаём экземпляр приложения
    app = QApplication(sys.argv)
    # создаем qml движок
    engine = QQmlApplicationEngine()
    # загружаем файл qml в движок
    engine.load(QUrl.fromLocalFile("main.qml"))
    sys.exit(app.exec_())
