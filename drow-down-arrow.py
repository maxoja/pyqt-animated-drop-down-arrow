from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QPen, QPainter, QPolygonF, QColor, QBrush
from PyQt5.QtCore import QTimer, QPointF, Qt, QLineF
import sys
from math import *

class Vertice:
    def __init__(self, x1, y1, x2, y2):
        self.sx = x1
        self.dx = x2-x1
        self.sy = y1
        self.dy = y2-y1

    def lerp(self, r, scale=1):
        return scale*(self.sx + self.dx*r), scale*(self.sy + self.dy*r)


class DropDownArrow(QWidget):
    step = 0.01

    def __init__(self, parent=None, size=50, speed=5, color=QColor(0,0,0), selected=False, updateEquation="self.step*self.speed*(self.end-self.begin)", kernel="self.x"):
        QWidget.__init__(self, parent)

        self.setFixedSize(size, size)
        self.speed = speed
        self.color = color
        self.updateEquation = updateEquation
        self.kernel = kernel
        self.selected = selected
        self.x = 1 if selected else 0

        self.verts = [
            Vertice(0.2, 0.1,   0.9, 0.3),
            Vertice(0.2, 0.9,   0.1,   0.3),
            Vertice(0.9, 0.5, 0.5,   0.8)
        ]

        timer = QTimer(self)
        timer.timeout.connect(self.onTick)
        timer.start(20)

    def setSelected(self, selected):
        self.selected = selected

    def isSelected(self):
        return self.selected

    def setColor(self, color):
        assert(isinstance(color, QColor))
        self.color = color

    def paintEvent(self, event):
        pen = QPen()
        pen.setWidth(self.width()/8)
        pen.setCapStyle(Qt.RoundCap)
        pen.setColor(self.color)

        brush = QBrush()
        brush.setColor(self.color)
        brush.setStyle(Qt.SolidPattern)

        painter = QPainter(self)
        painter.setPen(pen)
        painter.setBrush(brush)

        points = [ QPointF(*v.lerp(eval(self.kernel), self.width())) for v in self.verts ]
        painter.drawLine(QLineF(points[0],points[1]))
        painter.drawLine(QLineF(points[1],points[2]))
        painter.drawLine(QLineF(points[2],points[0]))

        poly = QPolygonF(points)
        painter.drawPolygon(poly)

    def onTick(self):

        if self.selected :
            self.begin = 0
            self.end = 1
            self.dir = 1
            self.x += eval(self.updateEquation)
            self.x = 1 if self.x > 1 else self.x
        else :
            # pass
            self.begin = 1
            self.end = 0
            self.dir = -1
            self.x += eval(self.updateEquation)
            self.x = 0 if self.x < 0 else self.x

        self.update()



if __name__ == '__main__' :
    app = QApplication(sys.argv)

    updateEq = 'self.dir * abs(self.x+0.01)**0.75*self.step*self.speed'
    w = DropDownArrow(updateEquation=updateEq, speed = 10)
    b = QPushButton(w)
    b.clicked.connect(lambda: w.setSelected(not w.isSelected()))
    b.move(35, 35)
    w.show()

    sys.exit(app.exec_())