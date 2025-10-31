import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QRadioButton, QButtonGroup, QLineEdit, QPushButton, QWidget, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI")
        # self.setGeometry(1000, 400, 500, 500)
        self.setWindowIcon(QIcon("stuff\\stayhome.png"))
        # self.radio1 = QRadioButton("Visa", self)
        # self.radio2 = QRadioButton("Master Card", self)
        # self.radio3 = QRadioButton("Gift Card", self)
        # self.radio4 = QRadioButton("In-Store", self)
        # self.radio5 = QRadioButton("Online", self)
        # self.button_group1 = QButtonGroup(self)
        # self.button_group2 = QButtonGroup(self)
        # self.line_edit = QLineEdit(self)
        # self.button = QPushButton("Submit", self)
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()
        # ADDING LABEL WITH TEXT
        # label = QLabel("hello world", self)
        # label.setFont(QFont("Arial", 32))
        # label.setGeometry(0, 100, 800, 100)
        # label.setStyleSheet("color: #171c18;"
        #                     "background-color: #224c8a;"
        #                     "font-weight: bold;"
        #                     "font-style: italic;"
        #                     "border-radius: 5px;"
        #                     "text-decoration: underline;"
        #                     )
        # label.setAlignment(Qt.AlignTop)
        # label.setAlignment(Qt.AlignBottom)
        # label.setAlignment(Qt.AlignVCenter)
        # label.setAlignment(Qt.AlignRight)
        # label.setAlignment(Qt.AlignHCenter)
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)


        # ADDING IMAGE ON LABEL
        # label = QLabel(self)
        # label.setGeometry(0,0,250,250)
        # pixmap = QPixmap("stuff\\stayhome.png")
        # label.setPixmap(QPixmap(pixmap))
        #
        # label.setScaledContents(True)
        #
        # label.setGeometry((self.width() - label.width())//2,
        #                   (self.height() - label.height())//2,
        #                   label.width(),
        #                   label.height())




    # def initUI(self):
    #     self.radio1.setGeometry(0,0,300,50)
    #     self.radio2.setGeometry(0,50,300,50)
    #     self.radio3.setGeometry(0,100,300,50)
    #     self.radio4.setGeometry(0,200,300,50)
    #     self.radio5.setGeometry(0,250,300,50)
    #     self.setStyleSheet("QRadioButton{"
    #                        "font-size: 42px;"
    #                        "font-family: Calibri;"
    #                        "padding: 10px;"
    #                        "}")
    #     self.button_group1.addButton(self.radio1)
    #     self.button_group1.addButton(self.radio2)
    #     self.button_group1.addButton(self.radio3)
    #
    #     self.button_group2.addButton(self.radio4)
    #     self.button_group2.addButton(self.radio5)
    #
    #     self.radio1.toggled.connect(self.radio_button_change)
    #     self.radio2.toggled.connect(self.radio_button_change)
    #     self.radio3.toggled.connect(self.radio_button_change)
    #     self.radio4.toggled.connect(self.radio_button_change)
    #     self.radio5.toggled.connect(self.radio_button_change)
    #
    # def radio_button_change(self):
    #     radio_button = self.sender()
    #     if radio_button.isChecked():
    #         print(f"{radio_button.text()} is checked")



    # def initUI(self):
    #     self.line_edit.setGeometry(10,10,250,60)
    #     self.line_edit.setStyleSheet("font-size:26px;"
    #                                  "font-family: Sans Serif;")
    #     self.button.setGeometry(280,10,120,60)
    #     self.button.setStyleSheet("background: green;"
    #                               "border-radius: 5px;"
    #                               "border-style: solid;"
    #                               "border-width: 1px;"
    #                               "font-size: 32px;"
    #                               "font-family: Sans Serif;")
    #
    #     self.button.clicked.connect(self.submit)
    #     self.line_edit.setPlaceholderText("Wpisz co kolwiek...")
    #
    #
    # def submit(self):
    #     text = self.line_edit.text()
    #     print(text)

    def initUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
            QPushButton {
                font-size: 40px;
                font-family: Segoe UI;
                padding: 15px 75px;
                margin: 25px;
                border-radius: 25px;
                border: 3px solid;
            }
            QPushButton#button1 {
                background-color: red;
            }
             QPushButton#button2 {
                background-color: blue;
            }
             QPushButton#button3 {
                background-color: green;
            }
            QPushButton#button1:hover {
                background-color: lightgrey;
            }
             QPushButton#button2:hover {
                background-color: lightblue;
            }
             QPushButton#button3:hover {
                background-color: lightgrin;
            }
        """)

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

