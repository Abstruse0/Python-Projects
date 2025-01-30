import sys, operator, time, random
from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QGridLayout, QSizePolicy, QPushButton
from PyQt6.QtGui import QIcon
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
       # Main Layouts/Initlizaitons
        self.insults = ["Nope!",
                        "Try again! ",
                        "Haha, nice try! ",
                        "Stop trying to break my code."]
        
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("pi.png"))
        self.setFixedSize(600,600)
        self.MainLayout = QGridLayout()
        self.NumberWindow = QLineEdit()
        self.setStyleSheet("Background-color:#ff8cfc;")
        self.Center = QWidget()


        self.MainLayout.addWidget(self.NumberWindow,0,0,4,4, Qt.AlignmentFlag.AlignTop)
        self.NumberWindow.setMinimumHeight(125)
        self.NumberWindow.setMinimumWidth(200)
        self.NumberWindow.setStyleSheet("font-weight:bold;"
                                        "font-size:50px;"
                                        "border: none;"
                                        "Color:#fafafa;")
        # Buttons/Operators 
        
        self.buttons = {"1": (QPushButton("1"),1,0), 
                         "2": (QPushButton("2"), 1,1), 
                        "3": (QPushButton("3"), 1,2),
                        "4": (QPushButton("4"), 1,3),
                        "5": (QPushButton("5"), 2,0),
                        "6": (QPushButton("6"), 2,1),
                         "7": (QPushButton("7"), 2,2),
                         "8": (QPushButton("8"), 2,3),
                         "9": (QPushButton("9"), 3,0),
                        "0":(QPushButton("0"), 3,1),
                        
                        "+button": (QPushButton("+"),3,2), 
                         "-button": (QPushButton("-"), 3,3), 
                        "*button": (QPushButton("*"), 4,0),
                        "/button": (QPushButton("/"), 4,1),
                        "button=": (QPushButton("="), 4,2),
                        "buttonclear": (QPushButton("Clear"), 4,3),
                         "delbutton": (QPushButton("Del"), 5,0),
                         "sqrbutton": (QPushButton("^2"), 5,1),
                         "rootbutton": (QPushButton("√"), 5,2),
                        "decimalbutton":(QPushButton("."),5,3)

                                                                }

        for key, (self.button,row,col) in self.buttons.items():
            self.MainLayout.addWidget(self.button)
            self.button.setMinimumSize(75,75)
            self.button.setStyleSheet("Background-color:#c133ff;"
                                 "font-weight:50px;"
                                 )
            self.button.clicked.connect(lambda checked, k=key: self.clicked(k))



    
        self.NumberWindow.setDisabled(False)

        self.Center.setLayout(self.MainLayout)
        self.setCentralWidget(self.Center)

        self.numlist1 = []



    def clicked(self, button_key):
        #Move Operdator ifs above all other data, and set data to go down different path ways depending on the state of the button.
        self.oldtext = self.NumberWindow.text()
        self.randinsults = random.choices(self.insults)


        if button_key == "1":

            self.NumberWindow.setText("1")
            self.newtext = self.oldtext + self.NumberWindow.text()
            self.NumberWindow.setText(self.newtext)
            self.numlist1.append(1)
            print(self.numlist1)


        if button_key == "2":
            self.NumberWindow.setText("2")
            self.newtext = self.oldtext + self.NumberWindow.text()
            self.numlist1.append(2)

            print(self.numlist1)

            self.NumberWindow.setText(self.newtext)

        if button_key == "3":

            self.NumberWindow.setText("3")

            self.newtext = self.oldtext + self.NumberWindow.text()
            self.NumberWindow.setText(self.newtext)
            self.numlist1.append(3)
            print(self.numlist1)

        if button_key == "4":

            self.NumberWindow.setText("4")

            self.newtext = self.oldtext + self.NumberWindow.text()
            self.NumberWindow.setText(self.newtext)
            self.numlist1.append(4)
            print(self.numlist1)
        if button_key == "5":

            self.NumberWindow.setText("5")
            self.newtext = self.oldtext + self.NumberWindow.text()
            self.NumberWindow.setText(self.newtext)

            self.numlist1.append(5)
            print(self.numlist1)

        if button_key == "6":

            self.NumberWindow.setText("6")

            self.newtext = self.oldtext + self.NumberWindow.text()
            self.NumberWindow.setText(self.newtext)
            self.numlist1.append(6)
            print(self.numlist1)

        if button_key == "7":

            self.NumberWindow.setText("7")
            self.newtext = self.oldtext + self.NumberWindow.text()
            self.NumberWindow.setText(self.newtext)
            self.numlist1.append(7)
            print(self.numlist1)

        if button_key == "8":

            self.NumberWindow.setText("8")
            self.newtext = self.oldtext + self.NumberWindow.text()
            self.NumberWindow.setText(self.newtext)
            self.numlist1.append(8)
            print(self.numlist1)

        if button_key == "9":
            self.NumberWindow.setText("9")

            self.newtext = self.oldtext + self.NumberWindow.text()
            self.NumberWindow.setText(self.newtext)
            self.numlist1.append(1)
            print(self.numlist1)

        if button_key == "0":

            self.NumberWindow.setText("0")

            self.newtext = self.oldtext + self.NumberWindow.text()
            self.NumberWindow.setText(self.newtext)
            self.numlist1.append(0)
            print(self.numlist1)

        if button_key == "button=":

            self.NumberWindow.setText("")
            self.newtext = self.oldtext + self.NumberWindow.text()
            self.NumberWindow.setText(self.newtext)
            self.happy()
            try:
                self.answer = str(eval(self.NumberWindow.text()))
                self.NumberWindow.setText(self.answer)
                if self.answer == 0:
                    self.NumberWindow.setText("0")
            except:
                if ZeroDivisionError:
                    self.NumberWindow.setText(f"{str(self.randinsults).replace("[","").replace("]","").replace(",","").replace("'","")}")
            # print(int(self.newtext) + 50) Practice

        
        if button_key == "+button":
            self.NumberWindow.setText("+")
            self.newtext = self.oldtext + self.NumberWindow.text()
            self.numlist1.append("+")
            self.NumberWindow.setText(self.newtext)
            # operators = [operator.add, operator.mul] Not useful yet but looks very pivotal and useful to this project
            print(self.numlist1)

        if button_key == "decimalbutton":

            self.NumberWindow.setText(".")
            self.newtext = self.oldtext + self.NumberWindow.text()
            self.NumberWindow.setText(self.newtext)
            self.numlist1.append(".")
            print(self.numlist1)

        if button_key == "/button":
            self.numlist1.append("/")

            self.NumberWindow.setText("/")
            self.newtext = self.oldtext + self.NumberWindow.text()
            self.NumberWindow.setText(self.newtext)

        if button_key == "-button":
            self.numlist1.append("-")
            self.NumberWindow.setText("-")
            self.newtext = self.oldtext + self.NumberWindow.text()
            self.NumberWindow.setText(self.newtext)

        if button_key == "*button":
            self.numlist1.append("*")

            self.NumberWindow.setText("*")

            self.newtext = self.oldtext + self.NumberWindow.text()
            self.NumberWindow.setText(self.newtext)

        if button_key == "sqrbutton":
            self.numlist1.append("**")

            self.NumberWindow.setText("**")

            self.newtext = self.oldtext + self.NumberWindow.text()
            self.NumberWindow.setText(self.newtext)            

        if button_key == "buttonclear":
            self.NumberWindow.setText("")
            self.numlist1.clear()
            #Clear All lists
            print(self.numlist1)

        if button_key == "delbutton":
            i = -1
            self.newtext = self.NumberWindow.text()
            self.Previous_Chars = []
            for x in (self.newtext):
                self.Previous_Chars.append(x)
                i+=1
            try:
                self.Previous_Chars.pop(i)
            
            except: 
                print("No More Items to Pop") # To see if working properly
            self.NumberWindow.setText(str(self.Previous_Chars).replace("[","").replace("]","").replace("'","").replace(",","").replace(" ",""))
            print(self.NumberWindow.text())


            
            #Find center point in data of window, put operator in the middle, then turn both sides into an int.

    def happy(self):
        print("I Love you :)")
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()