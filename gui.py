from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSlider, QPushButton, QLineEdit, QHBoxLayout, QFrame
from PyQt5.QtCore import Qt
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.run_simulation = False
        self.agent_count = 0
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Width and Height input
        self.whlabel = QLabel('Širina in Višina (v pikslih):')
        self.widthInput = QLineEdit()
        self.heightInput = QLineEdit()
        widthHeightLayout = QHBoxLayout()
        widthHeightLayout.addWidget(QLabel('Širina:'))
        widthHeightLayout.addWidget(self.widthInput)
        widthHeightLayout.addWidget(QLabel('Višina:'))
        widthHeightLayout.addWidget(self.heightInput)
        layout.addWidget(self.whlabel)
        layout.addLayout(widthHeightLayout)

        layout.addWidget(QHLine())
        # Speed slider
        self.speedLabel = QLabel('Razdalja premika (v pikslih): 0 (1 - 10)')
        self.speedSlider = QSlider(Qt.Horizontal)
        self.speedSlider.setMinimum(1)
        self.speedSlider.setMaximum(10)
        self.speedSlider.valueChanged[int].connect(self.changeSpeed)
        layout.addWidget(self.speedLabel)
        layout.addWidget(self.speedSlider)

        layout.addWidget(QHLine())
        # Number slider and input
        self.numberLabel = QLabel('Število agentov: 0 (1 - 500)')
        self.numberSlider = QSlider(Qt.Horizontal)
        self.numberInput = QLineEdit()
        self.numberSlider.setMinimum(1)
        self.numberSlider.setMaximum(500)
        self.numberSlider.valueChanged[int].connect(self.changeNumber)
        self.numberInput.textChanged[str].connect(self.updateNumberFromInput)
        layout.addWidget(self.numberLabel)
        layout.addWidget(self.numberSlider)
        layout.addWidget(self.numberInput)

        layout.addWidget(QHLine())
        # Resistance slider and input
        self.resistanceLabel = QLabel('Verjetnost okužbe (%): 0 (0 - 100)')
        self.resistanceSlider = QSlider(Qt.Horizontal)
        self.resistanceSlider.setMinimum(0)
        self.resistanceSlider.setMaximum(100)
        self.resistanceSlider.valueChanged[int].connect(self.changeResistance)
        self.resistanceInput = QLineEdit()
        self.resistanceInput.textChanged[str].connect(self.updateResistanceFromInput)
        layout.addWidget(self.resistanceLabel)
        layout.addWidget(self.resistanceSlider)
        layout.addWidget(self.resistanceInput)

        layout.addWidget(QHLine())
        # Death chance slider
        self.deathChanceLabel = QLabel('Verjetnost smrti (%): 0 (0 - 100)')
        self.deathChanceSlider = QSlider(Qt.Horizontal)
        self.deathInput = QLineEdit()
        self.deathChanceSlider.setMinimum(0)
        self.deathChanceSlider.setMaximum(100)
        self.deathChanceSlider.valueChanged[int].connect(self.changeDeathChance)
        layout.addWidget(self.deathChanceLabel)
        layout.addWidget(self.deathChanceSlider)
        layout.addWidget(self.deathInput)

        layout.addWidget(QHLine())
        # Infection time range slider
        self.infectionTimeLabel = QLabel('Čas trajanja okužbe (v številu iteracij): 0 (0 - 1000)')
        self.infectionTimeSlider = QSlider(Qt.Horizontal)  
        self.infectionInput = QLineEdit()
        self.infectionTimeSlider.setMinimum(0)
        self.infectionTimeSlider.setMaximum(1000)
        self.infectionTimeSlider.valueChanged.connect(self.changeInfectionTimeRange)
        layout.addWidget(self.infectionTimeLabel)
        layout.addWidget(self.infectionTimeSlider)
        layout.addWidget(self.infectionInput)

        layout.addWidget(QHLine())
        # Initial infected agents slider
        self.initialInfectedLabel = QLabel(f'Začetno okuženi agenti: 0 (0 - {self.agent_count})')
        self.initialInfectedSlider = QSlider(Qt.Horizontal)
        self.initialInfectedSlider.setMinimum(0)
        self.initialInfectedSlider.setMaximum(self.agent_count)
        self.initialInfectedSlider.valueChanged[int].connect(self.changeInitialInfected)
        layout.addWidget(self.initialInfectedLabel)
        layout.addWidget(self.initialInfectedSlider)

        layout.addWidget(QHLine())
        # Start button
        self.startButton = QPushButton('Začni')
        self.startButton.clicked.connect(self.startPressed)
        layout.addWidget(self.startButton)

        self.setLayout(layout)
        self.setWindowTitle('Nastavitve simulacije')

    def changeSpeed(self, value):
        self.speedLabel.setText(f'Razdalja premika (v pikslih): {value} (1 - 10)')

    def changeNumber(self, value):
        self.numberLabel.setText(f'Število agentov: {value} (1 - 500)')
        self.numberInput.setText(str(value))
        self.agent_count = value
        self.initialInfectedSlider.setMaximum(self.agent_count)

    def updateNumberFromInput(self, value):
        if value.isdigit() and 1 <= int(value) <= 500:
            self.numberSlider.setValue(int(value))

    def changeResistance(self, value):
        self.resistanceLabel.setText(f'Verjetnost okužbe (%): {value} (0 - 100)')
        self.resistanceInput.setText(str(value))

    def updateResistanceFromInput(self, value):
        if value.isdigit() and 0 <= int(value) <= 100:
            self.resistanceSlider.setValue(int(value))

    def changeDeathChance(self, value):
        self.deathChanceLabel.setText(f'Verjetnost smrti (%): {value} (0 - 100)')
        self.deathInput.setText(str(value))

    def changeInfectionTimeRange(self, max_value):
        self.infectionTimeLabel.setText(f'Čas trajanja okužbe (v številu iteracij): {max_value} (0 - 1000)')

    def changeInitialInfected(self, value):
        self.initialInfectedLabel.setText(f'Začetno število okuženih agentov: {value} (0 - {self.agent_count})')

    def startPressed(self):
        self.run_simulation = True
        self.close()

class QHLine(QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)

def show_gui():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
    return window.run_simulation

if __name__ == "__main__":
    run_simulation = show_gui()
