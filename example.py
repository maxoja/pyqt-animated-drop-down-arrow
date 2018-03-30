from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
from TWidget import DropDownArrow

import sys

app = QApplication(sys.argv)

# create drop-down arrows
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
            kernel='sin(self.x*3.14/2)',
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
            color=QColor(70, 70, 120),
            updateEquation='self.dir * abs(self.x+0.01)**0.75*self.step*self.speed',
            speed=8
        )
    ],
]

b1 = QPushButton("click to toggle")
b1.clicked.connect(lambda: [[d.toggle() for d in dl] for dl in drops])
b2 = QPushButton("quit")
b2.clicked.connect(QApplication.exit)

# create layout and add widgets
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

# build window and attach layout, then show it
window = QWidget()
window.setLayout(layout)
window.setWindowFlags(Qt.FramelessWindowHint)
window.show()

sys.exit(app.exec_())