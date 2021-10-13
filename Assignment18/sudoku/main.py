from functools import partial
from random import randint
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *


class Sudoku(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('sudoku.ui', None)

        self.file_path = ''

        self.game = [[None for i in range(9)] for j in range(9)]

        for i in range(9):
            for j in range(9):
                tb = QLineEdit()
                tb.setStyleSheet('font-size: 12px')
                tb.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                tb.setAlignment(Qt.AlignCenter) # set Alignment
                self.game[i][j] = tb # back-end
                self.game[i][j].textChanged.connect(self.checkGame) # connect textBoxes to check method
                self.ui.my_grid.addWidget(tb, i, j) # front-end

        self.ui.show()
        self.ui.newgame_btn.clicked.connect(partial(self.setGame, True))
        self.ui.clear_btn.clicked.connect(partial(self.setGame, False))
        self.ui.check_btn.clicked.connect(self.checkGame)
        self.ui.dark_btn.clicked.connect(self.dark)


    def dark(self):
        if self.ui.dark_btn.text()=='🌑':
            self.ui.dark_btn.setText('🌕')
            self.ui.setStyleSheet('background-color: rgb(161, 161, 161)')
        else:
            self.ui.dark_btn.setText('🌑')
            self.ui.setStyleSheet('')

    def checkGame(self):
        flag= True
        # check rows
        for row in range(9):
            for i in range(9):
                for j in range(9):
                    if self.game[row][i].text()==self.game[row][j].text() and i!=j and self.game[row][i].text()!='':
                        self.game[row][j].setStyleSheet('font-size: 12; background-color: pink;')
                        flag=False
        # check columns
        for col in range(9):
            for i in range(9):
                for j in range(9):
                    if self.game[i][col].text()==self.game[j][col].text() and i!=j and self.game[i][col].text()!='':
                        self.game[i][col].setStyleSheet('font-size: 12; background-color: pink;')
                        flag=False
        # check cel
        cel1=[]
        for i in range(0, 3):
            for j in range(0, 3):
                cel1.append(self.game[i][j].text())
        cel2=[]
        for i in range(0, 3):
            for j in range(3, 6):
                cel2.append(self.game[i][j].text())
        cel3=[]
        for i in range(0, 3):
            for j in range(6, 9):
                cel3.append(self.game[i][j].text())
        cel4=[]
        for i in range(3, 6):
            for j in range(0, 3):
                cel4.append(self.game[i][j].text())
        cel5=[]
        for i in range(3, 6):
            for j in range(3, 6):
                cel5.append(self.game[i][j].text())
        cel6=[]
        for i in range(3, 6):
            for j in range(6, 9):
                cel6.append(self.game[i][j].text())
        cel7=[]
        for i in range(6, 9):
            for j in range(0, 3):
                cel7.append(self.game[i][j].text())
        cel8=[]
        for i in range(6, 9):
            for j in range(3, 6):
                cel8.append(self.game[i][j].text())
        cel9=[]
        for i in range(6, 9):
            for j in range(6, 9):
                cel9.append(self.game[i][j].text())
        all_cel = [cel1,cel2,cel3,cel4,cel5,cel6,cel7,cel8,cel9]
        for i in range(9): # allcel count
            for j in range(9): # cell count
                for z in range(9):
                    if all_cel[i][j]==all_cel[i][z] and j!=z and all_cel[i][j]!='':
                        self.game[(int(i/3))*3+int(z/3)][(int(i%3))*3+(z%3)].setStyleSheet('font-size: 12; background-color: pink;')
                        flag=False

        for i in range(9): # check empty
            for j in range(9):
                if all_cel[i][j]=='':
                    flag=False
        if flag:
            msgBox = QMessageBox()
            msgBox.setText('Hooray! You did it! press New Game. ^^')
            msgBox.exec()

    def setGame(self, newGame= False):
        for i in range(9):
            for j in range(9):
                self.game[i][j].setText('')

        try:
            if newGame==True:
                r = randint(1, 6)
                self.file_path = f'data/s{r}.txt'
            f = open(self.file_path, 'r')
            big_text = f.read()
            rows = big_text.split('\n')

            for i in range(9):
                numbers = rows[i].split(' ')
                for j in range(9):
                    if numbers[j] != '0':
                        self.game[i][j].setStyleSheet('font-size: 12px; color: black')
                        self.game[i][j].setText(numbers[j])
                        self.game[i][j].setReadOnly(True) # read only for main self.board numbers
                    else:
                        self.game[i][j].setStyleSheet('font-size: 12px; color: green')
                        self.game[i][j].setReadOnly(False)
        except:
            msgBox = QMessageBox()
            msgBox.setText('Error: data file missing.')
            msgBox.exec()

app = QApplication([])
window = Sudoku()
app.exec()