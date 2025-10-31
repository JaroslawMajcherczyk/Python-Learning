import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(900, 500, 750, 250)

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("""
            background-color: black;
            border-radius: 5px;
            color: hsl(111, 100%, 40%);
            font-weight: bold;
        """)
        self.setStyleSheet("background-color: black;")

        font_id = QFontDatabase.addApplicationFont("stuff\\DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 200)
        self.time_label.setFont(my_font)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clack = DigitalClock()
    clack.show()
    sys.exit(app.exec_())
