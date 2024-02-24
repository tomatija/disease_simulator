import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLineEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Speed slider
        self.speedLabel = QLabel('Speed: 0')
        self.speedSlider = QSlider(Qt.Horizontal)
        self.speedSlider.setMinimum(0)
        self.speedSlider.setMaximum(100)
        self.speedSlider.valueChanged[int].connect(self.changeSpeed)
        layout.addWidget(self.speedLabel)
        layout.addWidget(self.speedSlider)

        # Number slider and input
        self.numberLabel = QLabel('Number: 0')
        self.numberSlider = QSlider(Qt.Horizontal)
        self.numberInput = QLineEdit()
        self.numberSlider.setMinimum(0)
        self.numberSlider.setMaximum(100)
        self.numberSlider.valueChanged[int].connect(self.changeNumber)
        self.numberInput.textChanged[str].connect(self.updateNumberFromInput)
        layout.addWidget(self.numberLabel)
        layout.addWidget(self.numberSlider)
        layout.addWidget(self.numberInput)

        # Resistance slider
        self.resistanceLabel = QLabel('Resistance: 0')
        self.resistanceSlider = QSlider(Qt.Horizontal)
        self.resistanceSlider.setMinimum(0)
        self.resistanceSlider.setMaximum(100)
        self.resistanceSlider.valueChanged[int].connect(self.changeResistance)
        layout.addWidget(self.resistanceLabel)
        layout.addWidget(self.resistanceSlider)

        # Start button
        self.startButton = QPushButton('Start')
        self.startButton.clicked.connect(self.startPressed)  # Connect button to function
        layout.addWidget(self.startButton)

        self.setLayout(layout)
        self.setWindowTitle('Control Panel')

    def changeSpeed(self, value):
        self.speedLabel.setText(f'Speed: {value}')

    def changeNumber(self, value):
        self.numberLabel.setText(f'Number: {value}')
        self.numberInput.setText(str(value))

    def updateNumberFromInput(self, value):
        if value.isdigit():
            self.numberSlider.setValue(int(value))

    def changeResistance(self, value):
        self.resistanceLabel.setText(f'Resistance: {value}')

    def startPressed(self):
        self.close()  # This will hide the window and trigger closing.


def show_gui():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()  # This will make sure the code waits for the GUI to close.
    
