from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *


class QGraphicsViewWMouse(QGraphicsView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setMouseTracking(True)
    
    def mousePressEvent(self, event):
        print('Mouse pressed')
        super().mousePressEvent(event)
    
    def keyPressEvent(self, event):
        self._pressed_key(event.key())
        super().keyPressEvent(event)

    def _pressed_key(self, key):
        if key == Qt.Key_Escape:
            self.close()

class SimulationWindow(QDialog):
    def __init__(self, height, width, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Simulation Window')
        self.setLayout(QVBoxLayout())
        self.scene = QGraphicsScene(self)
        self.scene.setBackgroundBrush(Qt.black)
        self.view = QGraphicsViewWMouse(self.scene, self)
        self.view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.view.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        self.resize(height, width)
        self.layout().addWidget(self.view)
        self.scene.setSceneRect(0, 0, self.view.width(), self.view.height())
        self.view.setSceneRect(0, 0, self.view.width(), self.view.height())
        self.show()
        self.raise_()


def create_window(height, width):
    app = QApplication([])
    test = SimulationWindow(height, width)

    while True:
        test.scene.update()
        qApp.processEvents()

create_window(800, 600)