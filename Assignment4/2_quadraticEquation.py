from math import sqrt
import re
def deltaFucn(a,b,c):
    return ((b**2)-4*(a*c))
def quadraticEquationFuc(a,b,c):
    delta=deltaFucn(a,b,c)
    if delta<0:
        print('No answer.')
    elif delta==0:
        print('answer: %f' %((-b)/(2*a)))
    else:
        print('answer: %f   answer: %f' %(((-b)+sqrt(delta))/(2*a), ((-b)-sqrt(delta))/(2*a)))
equationStr = input('Give me a Quadratic Equation: e.g. ax^2+bx+c=0\n')
equationList = re.split('\+|\^|x|\=', equationStr)
equationList = list(filter(None, equationList))
equationList.pop(1)
equationList = list(map(int, equationList))
if equationList[3]!=0:
    equationList[2]-=equationList[3]
quadraticEquationFuc(equationList[0], equationList[1], equationList[2])