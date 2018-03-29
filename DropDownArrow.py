from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPen, QPainter, QPolygonF, QColor, QBrush
from PyQt5.QtCore import QTimer, QPointF, Qt, QLineF
from time import sleep
from math import *
import sys


class Vertex:
    def __init__(self, x1, y1, x2, y2):
        self.sx = x1
        self.dx = x2-x1
        self.sy = y1
        self.dy = y2-y1

    def lerp(self, r, scale=1):
        return scale*(self.sx + self.dx*r), scale*(self.sy + self.dy*r)


class DropDownArrow(QWidget):
    step = 0.01

    def __init__(self, parent=None, size=8, speed=5, color=QColor(0, 0, 0), selected=False, updateEquation="self.step*self.speed*(self.end-self.begin)", kernel="self.x", onDown=None, onUp=None):
        QWidget.__init__(self, parent)

        self.setFixedSize(size, size)
        self.speed = speed
        self.color = color
        self.updateEquation = updateEquation
        self.kernel = kernel
        self.selected = selected
        self.changing = False
        self.hiding = False
        self.x = 1 if selected else 0
        self.onDown = onDown
        self.onUp = onUp

        self.verts = [
            Vertex(0.2, 0.1,   0.9, 0.3),
            Vertex(0.2, 0.9,   0.1,   0.3),
            Vertex(0.9, 0.5, 0.5,   0.8)
        ]

        timer = QTimer(self)
        timer.timeout.connect(self.onTick)
        timer.start(20)

    def setSelected(self, selected):
        assert(type(selected) == bool)

        if selected != self.selected:
            self.changing = True

        self.selected = selected

    def setHideVisual(self, hiding):
        assert(type(hiding) == bool)
        self.hiding = hiding

    def isSelected(self):
        return self.selected

    def isHidingVisual(self):
        return self.hiding

    def toggle(self):
        self.setSelected(not self.isSelected())

    def setColor(self, color):
        assert(isinstance(color, QColor))
        self.color = color

    def getColor(self):
        return self.color

    def paintEvent(self, event):
        color = self.color if not self.hiding else QColor(0,0,0,0)

        pen = QPen()
        pen.setWidth(self.width()/8)
        pen.setCapStyle(Qt.RoundCap)
        pen.setColor(color)

        brush = QBrush()
        brush.setStyle(Qt.SolidPattern)
        brush.setColor(color)

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

        if self.selected:
            self.begin = 0
            self.end = 1
            self.dir = 1
        else:
            self.begin = 1
            self.end = 0
            self.dir = -1

        self.x += eval(self.updateEquation)

        if self.x <= 0 and not self.selected:
            self.x = 0

            if self.onUp:
                if self.changing:
                    self.changing = False
                    self.onUp()
            else:
                self.changing=False

        if self.x >= 1 and self.selected:
            self.x = 1

            if self.onDown:
                if self.changing:
                    self.changing = False
                    self.onDown()
            else:
                self.changing = False

        self.update()


if __name__ == '__main__' :
    app = QApplication(sys.argv)

    #create drop-down arrows
    s = 50
    drops = [
        [
            DropDownArrow(
                size=s,
                color=QColor(100, 100, 100)
            ),

            DropDownArrow(
                size=s,
                color=QColor(150, 200, 180),
                kernel='sin(self.x*3.14/2)**10',
                speed=2
            ),

            DropDownArrow(
                size=s,
                updateEquation='self.dir * abs(self.x+0.01)**0.75*self.step*self.speed',
                speed=10
            )
        ],

        [
            DropDownArrow(
                size=s,
                color=QColor(130, 130, 130),
                speed=4
            ),

            DropDownArrow(
                size=s,
                color=QColor(180, 230, 210),
                kernel='sin(self.x*3.14/2)**10',
                speed=1.3
            ),

            DropDownArrow(
                size=s,
                color=QColor(70,70,120),
                updateEquation='self.dir * abs(self.x+0.01)**0.75*self.step*self.speed',
                speed=8
            )
        ],
    ]

    b1 = QPushButton("click to toggle")
    b1.clicked.connect(lambda: [[d.toggle() for d in dl] for dl in drops])
    b2 = QPushButton("quit")
    b2.clicked.connect(QApplication.exit)

    #create layout and add widgets
    layout = QVBoxLayout()
    displaylayout = QHBoxLayout()
    for dl in drops:
        sublayout = QVBoxLayout()
        for d in dl:
            sublayout.addWidget(d)
        displaylayout.addLayout(sublayout)
    layout.addLayout(displaylayout)
    layout.addWidget(b1)
    layout.addWidget(b2)

    #build window and attach layout, then show it
    window = QWidget()
    window.setLayout(layout)
    window.setWindowFlags(Qt.FramelessWindowHint)
    window.show()

    sys.exit(app.exec_())