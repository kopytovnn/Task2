from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt5.QtCore import Qt
from PyQt5 import uic
from random import randint


class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.pushButton.clicked.connect(self.circle)

        canvas = QPixmap(531, 581)
        self.label.setPixmap(canvas)

    def circle(self):
        x, y = randint(0, 531), randint(0, 581)
        s = randint(10, 100)
        painter = QPainter(self.label.pixmap())
        painter.brush
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(255, 211, 0))
        painter.setPen(pen)
        painter.drawEllipse(x, y - s, s, s)
        painter.end()
        self.update()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = Test()
    w.show()
    sys.exit(app.exec_())