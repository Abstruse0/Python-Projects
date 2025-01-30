
import sys, operator, time, random, json
from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QGridLayout, QSizePolicy, QPushButton,QTabWidget
from PyQt6.QtGui import QIcon, QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(500,800)
        self.setGeometry(500,50,800,800)

        self.mainlayout = QGridLayout()
        self.but = QPushButton("1")

        self.center = QWidget()
        self.center.setLayout(self.mainlayout)
        #self.but.clicked.connect(lambda:print("Hello, the button is working!"))
        self.setCentralWidget(self.center)




        #Tab Labels



        # Tabs
        self.tabs = QTabWidget() # To Hold all Widgets 
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tablayout = QGridLayout()
        self.tablayout2 = QGridLayout()
        self.tab_button = QPushButton("2")
        #Adding Widgets
        #self.tablayout.addWidget(self.but)
        self.tablayout2.addWidget(self.tab_button)
        #Setting layout of tabs (QGridLayout, QHBoxLayout, etc etc)
        self.tab1.setLayout(self.tablayout)
        self.tab2.setLayout(self.tablayout2)

        self.tabs.addTab(self.tab1, "Tab 1") #To add the name the tabs on the window

        self.mainlayout.addWidget(self.tabs) #To add the tabs to the window

        self.newtablayout = QGridLayout()
        
        self.but.clicked.connect(self.tab1button)
        self.tab_button.clicked.connect(self.tab2button)

        #Tab_Label Handler
        self.tab_labels = {"username":(QLabel("Username:"),1,0,5,0),
                           "password":(QLabel("Password:"),2,0,5,0)}

        self.edit_lines = {"username":(QLineEdit(),1,1,5,1),
                           "password":(QLineEdit(),2,1,5,1)}

        self.register_labels = {
                            "Register":(QLabel("Register Username:"),4,0,9,1),
                           "Password":(QLabel("Register Password:"),5,0,9,1)}
        
        self.edit_lines_register = {"register_username":(QLineEdit(),4,1,9,1),
                           "register_password":(QLineEdit(),5,1,9,1)}

        self.Register = QPushButton("Register")




        #For Username/Login Labels 
        for key, (self.label,row,col,rowspan,colspan) in self.tab_labels.items():
            self.tablayout.addWidget(self.label,row,col,rowspan,colspan)
            self.label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
            self.label.setAlignment(Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignVCenter)    

        # EditLines
        for self.key, (self.lines,row,col,rowspan,colspan) in self.edit_lines.items():
            self.tablayout.addWidget(self.lines,row,col,rowspan,colspan)
            self.lines.setMinimumSize(50,50)
            self.lines.setFont(QFont("Arial",16 ,QFont.Weight.Bold))
            self.lines.setStyleSheet("font-size: 25px;")
            if self.key == "password":
                self.lines.setEchoMode(QLineEdit.EchoMode.Password)
                print(self.lines.text())

            self.lines.setAlignment(Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignVCenter)

            
        # For Registering Labels 
        for key, (self.registeringlabels,row, col, rowspan,colspan) in self.register_labels.items():

            self.tablayout.addWidget(self.registeringlabels, row,col, rowspan, colspan)
            self.registeringlabels.setFont(QFont("Arial",16 ,QFont.Weight.Bold))
            self.registeringlabels.setAlignment(Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        for key, (self.registerlines,row,col,rowspan,colspan) in self.edit_lines_register.items():
            self.tablayout.addWidget(self.registerlines,row,col,rowspan,colspan)
            self.registerlines.setFont(QFont("Arial",16 , QFont.Weight.Bold))
            self.registerlines.setStyleSheet("font-size: 25px;")
            self.registerlines.setMinimumSize(50,50)

        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.get_input)
        self.tablayout.addWidget(submit_button, 4,1,3,1)
        self.tablayout.addWidget(self.Register,10,1,1,1)
        self.Register.clicked.connect(self.register)

    def get_input(self):
        self.logusername = self.edit_lines["username"][0].text()  # Accessing the username 
        self.logpassword = self.edit_lines["password"][0].text()  # Accessing the password QLineEdit
        self.edit_lines["username"][0].setText("")
        self.edit_lines["password"][0].setText("")
        print(f"Username: {self.logusername}, Password: {self.logpassword}")
        self.logindict = {"Username": self.logusername,
                          "Password": self.logpassword}
        #We open the file to read it 
        try:
            with open("UserData.json","r") as file:

                    data2 = json.load(file)
        # if there is an error, we change data2 to an empty list to prevent crashing           
        except (FileNotFoundError, json.JSONDecodeError):
            data2 = []

        # Look for current data in login lines to see if the same data is in str(data2), if not a string, will crash program
        if self.logusername in str(data2):
            self.tabs.addTab(self.tab1, f"User:{self.logusername}")            

            self.tabs.addTab(self.tab2, "Tab 2")
            print("User Found")


            self.tabs.setTabEnabled(0,False)
        else:
            print("User not Found")



    def register(self):

        self.registerusername = self.edit_lines_register["register_username"][0].text()

        self.registerpassword = self.edit_lines_register["register_password"][0].text()

        self.registerdict = {"registerusername":self.registerusername,
                            "registerpassword":self.registerpassword, }
        
        #Important code, helps with formatting of UserData 
        try:
            with open("UserData.json","r") as file:

                    data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        print(self.registerdict) 
        data.append(self.registerdict)

        with open("UserData.json", "w") as file:
            json.dump(data, file, indent=4)


    def tab1button(self):
        print("You're in tab 1")
        # self.tabs.setDisabled(True) :::: You will need to add another TabWidget if you'd like to pause a tab upon button clicked
        # self.tabs.setTabEnabled(1,False) explanation below 
        # self.tabs.addTab(self.tab2, "Tab 2") :::: If you wanted to add a tab upon a condition being met

    def tab2button(self):
        print("You're in tab 2")
        #self.tabs.setTabEnabled(0,False) #:::: Disables tabs starting from 0, looks in index of QTabWidet which would be stored inside tabs variable
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()