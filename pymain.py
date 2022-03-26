#Tic Tac Toe Bot Gui By uknaranaw
import numpy as np
import random
import time
from PyQt5 import QtCore, QtGui, QtWidgets

win = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
      [1, 4, 7],
      [2, 5, 8],
      [3, 6, 9],
      [1, 5, 9],
      [3, 5, 7,]]

O = []
X = []

round = 0
playerFlag = 0
botX = 0
playerO = 0

class Ui_MainWindow(object):
    
    def checkWin(self, p):
        for w in win:
            if all(x-1 in p for x in w):
                return True
        return False

    def resetBoard(self):
        global O, X, playerFlag, round
        O = []
        X = [] 
        playerFlag = round = 0

        self.pB1.setEnabled(True)
        self.pB2.setEnabled(True)
        self.pB3.setEnabled(True)
        self.pB4.setEnabled(True)
        self.pB5.setEnabled(True)
        self.pB6.setEnabled(True)
        self.pB7.setEnabled(True)
        self.pB8.setEnabled(True)
        self.pB9.setEnabled(True)
        self.pB1.setText(' ')
        self.pB2.setText(' ')
        self.pB3.setText(' ')
        self.pB4.setText(' ')
        self.pB5.setText(' ')
        self.pB6.setText(' ')
        self.pB7.setText(' ')
        self.pB8.setText(' ')
        self.pB9.setText(' ')

        
    def AI(self):
        validmove = list(set(range(9)) - set(O+X))
    
        V = [-100] * 9
        golden = False
        for m in validmove:
            tempX = X + [m]
            for w in win:
                x = [i-1 in tempX for i in w]
                nx = x.count(True)
                if nx == 3:
                    golden = True
                    V[m], criticalmove = self.evalOX(O,tempX)
                    if len(criticalmove) > 0:
                        move = [i-1 for i in criticalmove if i-1 in validmove]
                        return random.choice(move)
        criticalmove = 0
        if not golden:
            for m in validmove:
                tempX = X + [m]
                V[m], criticalmove = self.evalOX(O,tempX)
            
                if len(criticalmove) > 0:
                    move = [i-1 for i in criticalmove if i-1 in validmove]
                    return random.choice(move)
        maxV = max(V)
        imaxV = [i for i,j in enumerate(V) if j == maxV]
        return random.choice(imaxV)
  
    def evalOX(self, O,X):
        SO, SX, criticalmove = self.calSOX(O,X)
        return 1 + SX - SO, criticalmove

    def calSOX(self, O,X):
        SO = SX = 0
        criticalmove = []
        gold = False
        for w in win:
            o = [i-1 in O for i in w]
            x = [i-1 in X for i in w]
            nX = x.count(True)
            nO = o.count(True)
            if nX == 3:
                gold = True
                criticalmove = w
            elif not any(x):
                if not gold:           
                    SO += nO
                    
                    if nO == 2:
                        criticalmove = w

                    if not any(o):
                        SX += x.count(True)
        return SO,SX,criticalmove

    def btn(self, mark, pos):
        global playerFlag, O, X
        if pos == 0:
            self.pB1.setText(mark)
            self.pB1.setEnabled(False)
        elif pos == 1:
            self.pB2.setText(mark)
            self.pB2.setEnabled(False)
        elif pos == 2:
            self.pB3.setText(mark)
            self.pB3.setEnabled(False)
        elif pos == 3:
            self.pB4.setText(mark)
            self.pB4.setEnabled(False)
        elif pos == 4:
            self.pB5.setText(mark)
            self.pB5.setEnabled(False)
        elif pos == 5:
            self.pB6.setText(mark)
            self.pB6.setEnabled(False)
        elif pos == 6:
            self.pB7.setText(mark)
            self.pB7.setEnabled(False)
        elif pos == 7:
            self.pB8.setText(mark)
            self.pB8.setEnabled(False)
        elif pos == 8:
            self.pB9.setText(mark)
            self.pB9.setEnabled(False)



    def btnclk(self, pos):
        global playerFlag, O, X, botX, playerO, round
        mark = ''
        while True:
            if(playerFlag%2 == 0):
                move = pos
                mark = 'O'
                O.append(move)
                playerFlag += 1
                self.btn(mark, move)
                if self.checkWin(O):
                    #Owin
                    playerO +=1
                    self.Oscore.setText('Player O: '+str(playerO))
                    self.resetBoard()
                    break
                if round == 0 and pos == 4:
                    m = [0,2,6,8]
                    move = random.choice(m)
                    mark = 'X'
                    X.append(move)
                    self.btn(mark, move)
                    playerFlag += 1
                    round +=1
                    break
                if len(O) + len(X) == 9:
                    print(1)
                    #draw
                    self.resetBoard()
                    break
            else:
                mark = 'X'
                '''if 4 not in O+X:
                    move = 4
                    X.append(4)
                    self.btn(mark, move)'''
                if True:
                    move = self.AI()
                    X.append(move)
                    self.btn(mark, move)
                if self.checkWin(X):
                    #Owin
                    botX +=1
                    self.Xscore.setText('Bot X: '+str(botX))
                    self.resetBoard()
                    break
                playerFlag += 1
                round +=1
                break    


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(635, 622)
        MainWindow.setMinimumSize(QtCore.QSize(635, 622))
        MainWindow.setMaximumSize(QtCore.QSize(635, 622))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pngegg1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 631, 441))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName("gridLayout")

        #button8
        self.pB8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pB8.setMinimumSize(QtCore.QSize(209, 140))
        font = QtGui.QFont()
        font.setFamily("Oh Whale")
        font.setPointSize(80)
        font.setBold(False)
        font.setWeight(50)
        self.pB8.setFont(font)
        self.pB8.setText("")
        self.pB8.setObjectName("pB8")
        self.gridLayout.addWidget(self.pB8, 2, 1, 1, 1)
        self.pB8.clicked.connect(lambda: self.btnclk(7))

        #button5
        self.pB5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pB5.setMinimumSize(QtCore.QSize(209, 140))
        font = QtGui.QFont()
        font.setFamily("Oh Whale")
        font.setPointSize(80)
        font.setBold(False)
        font.setWeight(50)
        self.pB5.setFont(font)
        self.pB5.setText("")
        self.pB5.setObjectName("pB5")
        self.gridLayout.addWidget(self.pB5, 1, 1, 1, 1)
        self.pB5.clicked.connect(lambda: self.btnclk(4))

        #button7
        self.pB7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pB7.setMinimumSize(QtCore.QSize(209, 140))
        font = QtGui.QFont()
        font.setFamily("Oh Whale")
        font.setPointSize(80)
        font.setBold(False)
        font.setWeight(50)
        self.pB7.setFont(font)
        self.pB7.setText("")
        self.pB7.setObjectName("pB7")
        self.gridLayout.addWidget(self.pB7, 2, 0, 1, 1)
        self.pB7.clicked.connect(lambda: self.btnclk(6))

        #button2
        self.pB2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pB2.setMinimumSize(QtCore.QSize(209, 140))
        font = QtGui.QFont()
        font.setFamily("Oh Whale")
        font.setPointSize(80)
        font.setBold(False)
        font.setWeight(50)
        self.pB2.setFont(font)
        self.pB2.setText("")
        self.pB2.setObjectName("pB2")
        self.gridLayout.addWidget(self.pB2, 0, 1, 1, 1)
        self.pB2.clicked.connect(lambda: self.btnclk(1))

        #button4
        self.pB4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pB4.setMinimumSize(QtCore.QSize(209, 140))
        font = QtGui.QFont()
        font.setFamily("Oh Whale")
        font.setPointSize(80)
        font.setBold(False)
        font.setWeight(50)
        self.pB4.setFont(font)
        self.pB4.setText("")
        self.pB4.setObjectName("pB4")
        self.gridLayout.addWidget(self.pB4, 1, 0, 1, 1)
        self.pB4.clicked.connect(lambda: self.btnclk(3))

        #button3
        self.pB3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pB3.setMinimumSize(QtCore.QSize(209, 140))
        font = QtGui.QFont()
        font.setFamily("Oh Whale")
        font.setPointSize(80)
        font.setBold(False)
        font.setWeight(50)
        self.pB3.setFont(font)
        self.pB3.setText("")
        self.pB3.setObjectName("pB3")
        self.gridLayout.addWidget(self.pB3, 0, 2, 1, 1)
        self.pB3.clicked.connect(lambda: self.btnclk(2))

        #button6
        self.pB6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pB6.setMinimumSize(QtCore.QSize(209, 140))
        font = QtGui.QFont()
        font.setFamily("Oh Whale")
        font.setPointSize(80)
        font.setBold(False)
        font.setWeight(50)
        self.pB6.setFont(font)
        self.pB6.setText("")
        self.pB6.setObjectName("pB6")
        self.gridLayout.addWidget(self.pB6, 1, 2, 1, 1)
        self.pB6.clicked.connect(lambda: self.btnclk(5))

        #button9
        self.pB9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pB9.setMinimumSize(QtCore.QSize(209, 140))
        font = QtGui.QFont()
        font.setFamily("Oh Whale")
        font.setPointSize(80)
        font.setBold(False)
        font.setWeight(50)
        self.pB9.setFont(font)
        self.pB9.setText("")
        self.pB9.setObjectName("pB9")
        self.gridLayout.addWidget(self.pB9, 2, 2, 1, 1)
        self.pB9.clicked.connect(lambda: self.btnclk(8))

        #button1
        self.pB1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pB1.setMinimumSize(QtCore.QSize(209, 140))
        font = QtGui.QFont()
        font.setFamily("Oh Whale")
        font.setPointSize(80)
        font.setBold(False)
        font.setWeight(50)
        self.pB1.setFont(font)
        self.pB1.setText("")
        self.pB1.setObjectName("pB1")
        self.gridLayout.addWidget(self.pB1, 0, 0, 1, 1)
        self.pB1.clicked.connect(lambda: self.btnclk(0))


        self.Oscore = QtWidgets.QLabel(self.centralwidget)
        self.Oscore.setGeometry(QtCore.QRect(25, 480, 200, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.Oscore.setFont(font)
        self.Oscore.setObjectName("Oscore")
        self.Xscore = QtWidgets.QLabel(self.centralwidget)
        self.Xscore.setGeometry(QtCore.QRect(430, 470, 211, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.Xscore.setFont(font)
        self.Xscore.setObjectName("Xscore")

        self.res = QtWidgets.QPushButton(self.centralwidget)
        self.res.setGeometry(QtCore.QRect(250, 450, 141, 140))
        self.res.setMinimumSize(QtCore.QSize(93, 140))

        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.res.setFont(font)
        self.res.setObjectName("res")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 2, 651, 631))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.gridLayoutWidget.raise_()
        self.Oscore.raise_()
        self.Xscore.raise_()
        self.res.raise_()

        self.res.clicked.connect(self.resetBoard)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tic Tac Toe by uknaranaw"))
        self.Oscore.setText(_translate("MainWindow", "Player O: 0"))
        self.Xscore.setText(_translate("MainWindow", "Bot X: 0"))
        self.res.setText(_translate("MainWindow", "RTESET"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
