import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from random import randrange


class Inter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 700, 700)
        self.setWindowTitle('Окружности')

        self.pushButton = QPushButton('Нарисовать круг!', self)
        self.pushButton.move(320, 640)


class Example(Inter):
    def __init__(self):
        super().__init__()

        self.pushButton.clicked.connect(self.update)

        self.qp = QPainter()
        self.fl = False
        self.d = None

    def paintEvent(self, event):
        self.fl = True
        qp = QPainter()
        qp.begin(self)
        self.draw_flag(qp)
        qp.end()

    def draw_flag(self, qp):
        x, y = randrange(600), randrange(600)
        d = randrange(100)
        qp.setBrush(QColor(randrange(255), randrange(255), randrange(255)))
        qp.drawEllipse(x, y, x + d, x + d)
        self.fl = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())