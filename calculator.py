from PyQt5.QtWidgets import (QApplication, QShortcut, QDialog, QGroupBox, QLineEdit, QHBoxLayout,
                             QLabel, QVBoxLayout, QButtonGroup, QGridLayout, QPushButton, QStyleFactory,
                              QCheckBox)
import sys
from PyQt5 import QtGui
from PyQt5 import QtCore


class Window1(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "Simple Calculator"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 400
        self.setFixedSize(350, 350)
        #self.setStyleSheet("background-color: PaleTurquoise")
        self.setStyle(QStyleFactory.create('Fusion'))

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.groupbox()
        self.shortcut()

        self.change_style = QCheckBox(" &Dark Mode")
        self.change_style.toggled.connect(self.darkMode)

        vbox = QVBoxLayout()
        vbox.addWidget(self.change_style)
        vbox.addWidget(self.grpbox1)
        vbox.addWidget(self.grpbox2)
        self.setLayout(vbox)

        self.show()
    def darkMode(self):
        if self.change_style.isChecked():
            self.dark_palette = QtGui.QPalette()
            self.dark_palette.setColor( QtGui.QPalette.Window, QtGui.QColor( 32,32,32 ) )
            self.dark_palette.setColor( QtGui.QPalette.Foreground, QtGui.QColor( 255,255,255 ) )
            self.dark_palette.setColor( QtGui.QPalette.WindowText, QtGui.QColor(224, 224, 224) )
            self.dark_palette.setColor( QtGui.QPalette.Base, QtGui.QColor( 96,96,96 ) )
            self.dark_palette.setColor( QtGui.QPalette.PlaceholderText, QtGui.QColor(255, 255, 255))
            self.dark_palette.setColor( QtGui.QPalette.Text, QtGui.QColor(224, 224, 224) )
            self.dark_palette.setColor( QtGui.QPalette.Button, QtGui.QColor(96, 96, 96) )
            self.dark_palette.setColor( QtGui.QPalette.ButtonText, QtCore.Qt.black )
            self.setPalette( self.dark_palette )        

            App.setPalette(self.dark_palette)
        else:
            self.white_palette = QtGui.QPalette()
            self.white_palette.setColor( QtGui.QPalette.Window, QtGui.QColor( 224,224,224 ) )
            self.white_palette.setColor( QtGui.QPalette.WindowText, QtGui.QColor(32, 32, 32) )
            self.white_palette.setColor( QtGui.QPalette.Base, QtGui.QColor( 255,255,255 ) )
            self.white_palette.setColor( QtGui.QPalette.Text, QtGui.QColor(32, 32, 32) )
            self.white_palette.setColor( QtGui.QPalette.Button, QtGui.QColor(224, 224, 224) )
            self.white_palette.setColor( QtGui.QPalette.ButtonText, QtCore.Qt.black )
            self.setPalette( self.white_palette )        

            App.setPalette(self.white_palette)

    

    def groupbox(self):
        self.grpbox1 = QGroupBox()
        vbox1 = QVBoxLayout()
        self.label = QLabel(self)
        self.label.setFixedHeight(30)
        self.label.setFont(QtGui.QFont("sanserif", 20))

        self.input_field = QLineEdit()
        self.input_field.setFixedSize(300, 30)
        #self.input_field.setStyleSheet("background-color: white")
        self.input_field.setFont(QtGui.QFont("sanserif", 15))

        input_hbox = QHBoxLayout()
        input_hbox.addWidget(self.input_field)

        vbox1.addLayout(input_hbox)
        vbox1.addWidget(self.label)
        self.grpbox1.setLayout(vbox1)

        self.grpbox2 = QGroupBox()
        grid_layout = QGridLayout()

        #Button and Properties
        btn1 = QPushButton("C")
        btn1.setFixedHeight(30)
        btn1.setDefault(False)
        btn1.setAutoDefault(False)
        btn1.clicked.connect(self.onclear)
        btn2 = QPushButton("Delete")
        btn2.setFixedHeight(30)
        btn2.setDefault(False)
        btn2.setAutoDefault(False)
        btn2.clicked.connect(self.ondelete)
        btn3 = QPushButton("/")
        btn3.setFixedHeight(30)
        btn3.setDefault(False)
        btn3.setAutoDefault(False)
        btn3.clicked.connect(lambda: self.onbutton('/'))

        btn4 = QPushButton("+")
        btn4.setFixedHeight(30)
        btn4.setFont(QtGui.QFont("sanserif", 15))
        btn4.setDefault(False)
        btn4.setAutoDefault(False)
        btn4.setFixedHeight(65)
        #btn4.setFixedSize(70, 65)
        btn4.clicked.connect(lambda: self.onbutton('+'))

        grid_layout.addWidget(btn1, 0, 0)
        grid_layout.addWidget(btn2, 0, 1)
        grid_layout.addWidget(btn3, 0, 2)
        grid_layout.addWidget(btn4, 0, 3, 2, 1)

        btn5 = QPushButton("7", clicked=lambda: self.onbutton('7'))
        btn5.setFixedHeight(30)
        btn5.setDefault(False)
        btn5.setAutoDefault(False)
        btn6 = QPushButton("8")
        btn6.setFixedHeight(30)
        btn6.setDefault(False)
        btn6.setAutoDefault(False)
        btn6.clicked.connect(lambda: self.onbutton('8'))
        btn7 = QPushButton("9")
        btn7.setFixedHeight(30)
        btn7.setDefault(False)
        btn7.setAutoDefault(False)
        btn7.clicked.connect(lambda: self.onbutton('7'))
        btn8 = QPushButton("*")
        btn8.setFixedHeight(30)
        btn8.setDefault(False)
        btn8.setAutoDefault(False)
        btn8.setFont(QtGui.QFont("sanserif", 15))
        btn8.clicked.connect(lambda: self.onbutton("*"))

        grid_layout.addWidget(btn5, 1, 0)
        grid_layout.addWidget(btn6, 1, 1)
        grid_layout.addWidget(btn7, 1, 2)
        grid_layout.addWidget(btn8, 2, 3)

        btn9 = QPushButton("4")
        btn9.setFixedHeight(30)
        btn9.setDefault(False)
        btn9.setAutoDefault(False)
        btn9.clicked.connect(lambda: self.onbutton('4'))
        btn10 = QPushButton("5")
        btn10.setFixedHeight(30)
        btn10.setDefault(False)
        btn10.setAutoDefault(False)
        btn10.clicked.connect(lambda: self.onbutton('5'))
        btn11 = QPushButton("6")
        btn11.setFixedHeight(30)
        btn11.setDefault(False)
        btn11.setAutoDefault(False)
        btn11.clicked.connect(lambda: self.onbutton('6'))
        btn12 = QPushButton("-")
        btn12.setFixedHeight(30)
        btn12.setFont(QtGui.QFont("sanserif", 15))
        btn12.setDefault(False)
        btn12.setAutoDefault(False)
        btn12.clicked.connect(lambda: self.onbutton('-'))

        grid_layout.addWidget(btn9, 2, 0)
        grid_layout.addWidget(btn10, 2, 1)
        grid_layout.addWidget(btn11, 2, 2)
        grid_layout.addWidget(btn12, 3, 3)

        btn13 = QPushButton("1")
        btn13.setFixedHeight(30)
        btn13.setDefault(False)
        btn13.setAutoDefault(False)
        btn13.clicked.connect(lambda: self.onbutton('1'))
        btn14 = QPushButton("2")
        btn14.setFixedHeight(30)
        btn14.setDefault(False)
        btn14.setAutoDefault(False)
        btn14.clicked.connect(lambda: self.onbutton('2'))
        btn15 = QPushButton("3")
        btn15.setFixedHeight(30)
        btn15.setDefault(False)
        btn15.setAutoDefault(False)
        btn15.clicked.connect(lambda: self.onbutton('3'))
        btn16 = QPushButton("=")
        btn16.setFixedHeight(30)
        btn16.setFont(QtGui.QFont("sanserif", 15))
        btn16.setDefault(True)
        btn16.setAutoDefault(True)
        btn16.clicked.connect(self.result)

        grid_layout.addWidget(btn13, 3, 0)
        grid_layout.addWidget(btn14, 3, 1)
        grid_layout.addWidget(btn15, 3, 2)
        grid_layout.addWidget(btn16, 4, 3)

        btn17 = QPushButton("Pow")
        btn17.setFixedHeight(30)
        btn17.setDefault(False)
        btn17.setAutoDefault(False)
        btn17.clicked.connect(lambda: self.onbutton('**'))

        btn18 = QPushButton("0")
        btn18.setFixedHeight(30)
        btn18.setDefault(False)
        btn18.setAutoDefault(False)
        btn18.clicked.connect(lambda: self.onbutton('0'))
        btn19 = QPushButton(".")
        btn19.setFixedHeight(30)
        btn19.setDefault(False)
        btn19.setAutoDefault(False)
        btn19.clicked.connect(lambda: self.onbutton('.'))

        grid_layout.addWidget(btn17, 4, 0)
        grid_layout.addWidget(btn18, 4, 1)
        grid_layout.addWidget(btn19, 4, 2)

        self.grpbox2.setLayout(grid_layout)
    
    def shortcut(self):
        eqaul_shortcut = QShortcut(QtGui.QKeySequence("Enter"), self)
        eqaul_shortcut.activated.connect(self.result)

        delete = QShortcut(QtGui.QKeySequence("Backspace"), self)
        delete.activated.connect(self.ondelete)

    def onbutton(self, number):
        self.input_field.setText(self.input_field.text() + number)

    def ondelete(self):
        self.input_field.setText(self.input_field.text()[0:-1])

    def onclear(self):
        self.input_field.setText(self.input_field.clear())
        self.label.clear()

    def result(self):
        expression = self.input_field.text()
        try:
            answer = eval(expression)
        except (SyntaxError, ValueError, NameError):
            self.label.setText("Syntax Error")
        else:
            print(str(answer))
            self.label.setText("=" + str(answer))


App = QApplication(sys.argv)
window = Window1()
sys.exit(App.exec())
