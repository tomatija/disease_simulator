from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *

import random

color_map = {
    'red': Qt.red,
    'green': Qt.green,
    'blue': Qt.blue,
    'black': Qt.black,
    'white': Qt.white,
    'yellow': Qt.yellow
}

class QGraphicsViewWMouse(QGraphicsView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setMouseTracking(True)
    
    def mousePressEvent(self, event):
        print(event.pos())
        super().mousePressEvent(event)
    
    def keyPressEvent(self, event):
        self._pressed_key(event.key())
        super().keyPressEvent(event)

    def _pressed_key(self, key):
        if key == Qt.Key_Escape:
            self.close()

class SimulationManager(QDialog):
    def __init__(self, height, width, *args, **kwargs):
        self.app = QApplication([])
        super().__init__(*args, **kwargs)
        self.height = height
        self.width = width
        self.setWindowTitle('Simulation Window')
        self.setLayout(QVBoxLayout())
        self.scene = QGraphicsScene(self)
        self.scene.setBackgroundBrush(Qt.black)
        self.view = QGraphicsViewWMouse(self.scene, self)
        self.view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.view.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        self.resize(height, width)
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().addWidget(self.view)
        self.scene.setSceneRect(0, 0, self.view.width(), self.view.height())
        self.view.setSceneRect(0, 0, self.view.width(), self.view.height())
        self.show()
        self.raise_()
    
    def refresh_window(self):
        self.scene.update()
        qApp.processEvents()
    
    def create_circle(self, x, y, radius, color):
        circle = QGraphicsEllipseItem(x, y, 2 * radius, 2 * radius)
        circle.setPen(QPen(QBrush(color_map[color] if color in color_map else Qt.red), 1))
        self.scene.addItem(circle)
        return circle

    def get_random_position_on_window(self):
        return (random.randint(0, self.height), random.randint(0, self.width))

    def wait(self, t):
        import time
        self.refresh_window()
        time.sleep(t)
