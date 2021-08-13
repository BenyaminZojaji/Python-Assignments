from random import randint, choice
from colorama import Fore, Style
from time import time
def draw():
    print()
    for row in range(3):
        for column in range(3):
            if gameBoard[row][column]=='X':
                print(Fore.RED + 'X', end=' ')
                print(Style.RESET_ALL, end='')
            elif gameBoard[row][column]=='O':
                print(Fore.CYAN + 'O', end=' ')
                print(Style.RESET_ALL, end='')
            else:
                print('-', end=' ')
        print()
def validCordinate(x, y):
    if x<=2 and y<=2:
        return True
    else:
        return False
def emptyPosition(x, y):
    if gameBoard[x][y]=='-':
        return True
    else:
        return False
def getPosition(name, sign):
    while True:
        temp = list(map(int, input('\n%s\'s turn.\nrow and column: e.g. 0 2\n' %name).split()))
        if validCordinate(temp[0], temp[1]):
            if emptyPosition(temp[0], temp[1]):
                gameBoard[temp[0]][temp[1]]=sign
                return
            else:
                print('This cordinate is already filled.\n')
        else:
            print('This cordinate isn\'t valid. try again.\n')
def winCheck():
    for i in range(3):
        o, x= 0, 0
        for j in range(3):
            temp = gameBoard[i][j]
            if temp=='X':
                x+=1
            elif temp=='O':
                o+=1
        if x==3 or o==3:
            return True
    for i in range(3):
        o, x= 0, 0
        for j in range(3):
            temp = gameBoard[j][i]
            if temp=='X':
                x+=1
            elif temp=='O':
                o+=1
        if x==3 or o==3:
            return True
    if gameBoard[0][0]==gameBoard[1][1]==gameBoard[2][2] and gameBoard[0][0]!='-':
        return True
    elif gameBoard[0][2]==gameBoard[1][1]==gameBoard[2][0] and gameBoard[0][2]!='-':
        return True
    return False
def drawCheck():
    for i in range(3):
        for j in range(3):
            if gameBoard[i][j]=='-':
                return False
    return True
def stateCheck():
    if winCheck():
        return 'win'
    elif drawCheck():
        return 'draw'
    else:
        return 'nothing'
def endGameFunc(event, name):
    if event=='win':
        print('\n%s win this round. GG well played.\n' %name)
    elif event=='draw':
        print('\nDraw.\n')
def playerVsUnknown(who):
    player1Sign = choice(['X', "O"])
    player1 = input('player1 name: ')
    player2Sign = 'X' if player1Sign=='O' else 'O'
    player2 = input('player2 name: ') if who=='human' else 'Eliot-AI'
    turn = choice(['X', "O"])
    while True:
        turn = player1Sign
        draw()
        getPosition(player1, turn)
        temp = stateCheck()
        if temp=='win' or temp=='draw':
            endGameFunc(temp, player1)
            break
        draw()
        turn = player2Sign
        if who=='human':
            getPosition(player2, turn)
        else:
            while True:
                randX = randint(0, 2)
                randY = randint(0, 2)
                if emptyPosition(randX, randY):
                    gameBoard[randX][randY]=turn
                    break
        temp = stateCheck()
        if temp=='win' or temp=='draw':
            endGameFunc(temp, player2)
            break
while True:
    gameBoard = [['-']*3, ['-']*3, ['-']*3]
    playMode = input('\n1.play vs AI\n2.two players\n3.Quit\n')
    if playMode=='1' or playMode=='play vs AI':
        start = time()
        playerVsUnknown('ai')
        print(f"Ellapsed time: {round(time() - start, 2)} s")
    elif playMode=='2' or playMode=='two players':
        start = time()
        playerVsUnknown('human')
        print(f"Ellapsed time: {round(time() - start, 2)} s")
    elif playMode=='3' or playMode=='Quit':
        exit()