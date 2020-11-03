import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randrange
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)

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
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(x, y, x + d, x + d)
        self.fl = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())