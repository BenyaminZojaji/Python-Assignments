import math
from sympy import cot

print('what do you want to do? \n+ -  *  /  radical  sin  cos  tan  cot  factorial')
tempOperator=input()
if tempOperator=='-':
    n1, n2=input('pls give me two values: ').split()
    print(round(float(n1)-float(n2), 4))
elif tempOperator=='+':
    n1, n2=input('pls give me two values: ').split()
    print(float(n1)+float(n2))
elif tempOperator=='*':
    n1, n2=input('pls give me two values: ').split()
    print(round(float(n1)*float(n2),4))
elif tempOperator=='/':
    n1, n2=input('pls give me two values: ').split()
    if n2 != '0':
        print(round(float(n1)/float(n2),4))
    else:
        print('cannot devide by Zero !')
elif tempOperator=='radical':
    n1=float(input('pls give me one value: '))
    if n1>=0:
        print(math.sqrt(n1))
    else:
        print('Invalid Input')
elif tempOperator=='sin':
    tempOp=input('degree or radian ? ')
    if tempOp=='degree':
        n1=float(input('give me a degree: '))
        print(round(math.sin(math.radians(n1)), 4))
    elif tempOp=='radian':
        n1=input('give me a radian: e.g. 2  or  0.5 pi: ')
        if n1.isnumeric():
            print(round(math.sin(float(n1)), 4))
        else:
            n1=n1[:n1.find('pi')].strip()
            print(round(math.sin(float(n1)*math.pi), 4))
elif tempOperator=='cos':
    tempOp=input('degree or radian ? ')
    if tempOp=='degree':
        n1=float(input('give me a degree: '))
        print(round(math.cos(math.radians(n1)), 4))
    elif tempOp=='radian':
        n1=input('give me a radian: e.g. 2  or  0.5 pi: ')
        if n1.isnumeric():
            print(round(math.cos(float(n1)), 4))
        else:
            n1=n1[:n1.find('pi')].strip()
            print(round(math.cos(float(n1)*math.pi), 4))
elif tempOperator=='tan':
    tempOp=input('degree or radian ? ')
    if tempOp=='degree':
        n1=float(input('give me a degree: '))
        print(round(math.tan(math.radians(n1)), 4))
    elif tempOp=='radian':
        n1=input('give me a radian: e.g. 2  or  0.5 pi: ')
        if n1.isnumeric():
            print(round(math.tan(float(n1)), 4))
        else:
            n1=n1[:n1.find('pi')].strip()
            print(round(math.tan(float(n1)*math.pi), 4))
elif tempOperator=='cot':
    tempOp=input('degree or radian ? ')
    if tempOp=='degree':
        n1=float(input('give me a degree: '))
        print(round(cot(math.radians(n1)), 4))
    elif tempOp=='radian':
        n1=input('give me a radian: e.g. 2  or  0.5 pi: ')
        if n1.isnumeric():
            print(round(cot(float(n1)), 4))
        else:
            n1=n1[:n1.find('pi')].strip()
            print(round(cot(float(n1)*math.pi), 4))
elif tempOperator=='factorial':
    n1=int(input('pls give me a number: '))
    print(math.factorial(n1))
