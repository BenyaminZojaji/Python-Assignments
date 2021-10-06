from random import choice, randint
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('form.ui', None)
        self.ui.show()

        self.AI = False

        self.x_score = 0
        self.o_score = 0
        self.scoreBoardUpdate()

        self.game = [[self.ui.btn_0, self.ui.btn_1, self.ui.btn_2], [self.ui.btn_3, self.ui.btn_4, self.ui.btn_5],
                     [self.ui.btn_6, self.ui.btn_7, self.ui.btn_8]]

        for i in range(3):
            for j in range(3):
                self.game[i][j].setText('')
                self.game[i][j].setStyleSheet('background-color: skyblue')
                self.game[i][j].clicked.connect(partial(self.play, i, j))
        self.ui.about_btn.clicked.connect(self.about)
        self.ui.newGame_btn.clicked.connect(partial(self.newGame))
        self.turn = choice(['X', 'O'])
        self.ui.rd_btn2.setChecked(True)

    def about(self):
        msgBox = QMessageBox()
        msgBox.setText('Programmer: Benyamin Zojaji\nEmail: benyamin.zojaji@icloud.com\nMade with ❤')
        msgBox.exec()

    def scoreBoardUpdate(self):
        self.ui.scoreboard.setText(str(self.x_score) + ' - ' + str(self.o_score))

    def play(self, i, j):
        if self.ui.rd_btn1.isChecked():
            self.AI = True
        elif self.ui.rd_btn2.isChecked():
            self.AI = False

        if self.game[i][j].text() == '':
            self.set_position(i, j)
            self.check()
            if self.AI:
                x, y = self.get_position()
                self.set_position(x, y)
                self.check()

        else:
            msgBox = QMessageBox()
            msgBox.setText('You can\'t select this position.  ˘︹˘ ')
            msgBox.exec()

    def set_position(self, i, j):
        if self.turn == 'X':
            self.turn = 'O'
            self.game[i][j].setText('X')
            self.game[i][j].setStyleSheet('color: green; background-color: lightgreen')
        else:
            self.turn = 'X'
            self.game[i][j].setText('O')
            self.game[i][j].setStyleSheet('color: red; background-color: pink')

    def get_position(self):
        while True:
            x = randint(0, 2)
            y = randint(0, 2)
            if self.game[x][y].text() == '':
                break
        return x, y

    def check(self):
        state = self.winCheck()
        if state == 'X':
            msgBox = QMessageBox()
            msgBox.setText('X wins.')
            msgBox.exec()
            self.x_score += 1
            self.scoreBoardUpdate()
            self.newGame(False)
        elif state == 'O':
            msgBox = QMessageBox()
            msgBox.setText('O wins.')
            msgBox.exec()
            self.o_score += 1
            self.scoreBoardUpdate()
            self.newGame(False)
        elif state == 'draw':
            msgBox = QMessageBox()
            msgBox.setText('draw.')
            msgBox.exec()
            self.newGame(False)

    def winCheck(self):
        # win check
        for i in range(3):
            o, x = 0, 0
            for j in range(3):
                temp = self.game[i][j].text()
                if temp == 'X':
                    x += 1
                elif temp == 'O':
                    o += 1
            if x == 3:
                return 'X'
            elif o == 3:
                return 'O'
        for i in range(3):
            o, x = 0, 0
            for j in range(3):
                temp = self.game[j][i].text()
                if temp == 'X':
                    x += 1
                elif temp == 'O':
                    o += 1
            if x == 3:
                return 'X'
            elif o == 3:
                return 'O'
        if self.game[0][0].text() == self.game[1][1].text() == self.game[2][2].text() and self.game[0][0].text() == 'X':
            return 'X'
        elif self.game[0][0].text() == self.game[1][1].text() == self.game[2][2].text() and self.game[0][
            0].text() == 'O':
            return 'O'
        elif self.game[0][2].text() == self.game[1][1].text() == self.game[2][0].text() and self.game[0][
            2].text() == 'O':
            return 'O'
        elif self.game[0][2].text() == self.game[1][1].text() == self.game[2][0].text() and self.game[0][
            2].text() == 'X':
            return 'X'
        # draw and continue check
        for i in range(3):
            for j in range(3):
                if self.game[i][j].text() == '':
                    return 'continue'
        return 'draw'

    def newGame(self, score_reset=True):
        for i in range(3):
            for j in range(3):
                self.game[i][j].setText('')
                self.game[i][j].setStyleSheet('color: black; background-color: skyblue')
        self.turn = choice(['X', 'O'])
        if score_reset:
            self.x_score = 0
            self.o_score = 0
            self.scoreBoardUpdate()


app = QApplication([])
window = Window()
app.exec()
