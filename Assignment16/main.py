from math import *
from sympy import cot
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('form.ui', None)
        self.ui.show()

        self.result = 0
        self.lastOperand = ''
        self.step = 0

        self.ui.btn_0.clicked.connect(self.func_num0)
        self.ui.btn_1.clicked.connect(self.func_num1)
        self.ui.btn_2.clicked.connect(self.func_num2)
        self.ui.btn_3.clicked.connect(self.func_num3)
        self.ui.btn_4.clicked.connect(self.func_num4)
        self.ui.btn_5.clicked.connect(self.func_num5)
        self.ui.btn_6.clicked.connect(self.func_num6)
        self.ui.btn_7.clicked.connect(self.func_num7)
        self.ui.btn_8.clicked.connect(self.func_num8)
        self.ui.btn_9.clicked.connect(self.func_num9)

        self.ui.sum_btn.clicked.connect(self.sum)
        self.ui.sub_btn.clicked.connect(self.sub)
        self.ui.cross_btn.clicked.connect(self.cross)
        self.ui.division_btn.clicked.connect(self.div)
        self.ui.equal_btn.clicked.connect(self.equal)
        self.ui.ac_btn.clicked.connect(self.ac)
        self.ui.dot_btn.clicked.connect(self.dot_func)
        self.ui.percentage_btn.clicked.connect(self.percentage_func)
        self.ui.neg_pos_btn.clicked.connect(self.neg_pos)
        self.ui.sin_btn.clicked.connect(self.sin_func)
        self.ui.cos_btn.clicked.connect(self.cos_func)
        self.ui.tan_btn.clicked.connect(self.tan_func)
        self.ui.cot_btn.clicked.connect(self.cot_func)
        self.ui.log_btn.clicked.connect(self.log_func)
        self.ui.sqrt_btn.clicked.connect(self.sqrt_func)

    def func_num0(self):
        self.ui.textBox.setText(self.ui.textBox.text() + '0')
    def func_num1(self):
        self.ui.textBox.setText(self.ui.textBox.text() + '1')
    def func_num2(self):
        self.ui.textBox.setText(self.ui.textBox.text() + '2')
    def func_num3(self):
        self.ui.textBox.setText(self.ui.textBox.text() + '3')
    def func_num4(self):
        self.ui.textBox.setText(self.ui.textBox.text() + '4')
    def func_num5(self):
        self.ui.textBox.setText(self.ui.textBox.text() + '5')
    def func_num6(self):
        self.ui.textBox.setText(self.ui.textBox.text() + '6')
    def func_num7(self):
        self.ui.textBox.setText(self.ui.textBox.text() + '7')
    def func_num8(self):
        self.ui.textBox.setText(self.ui.textBox.text() + '8')
    def func_num9(self):
        self.ui.textBox.setText(self.ui.textBox.text() + '9')
    
    def dot_func(self):
        if '.' not in self.ui.textBox.text():
            self.ui.textBox.setText(self.ui.textBox.text() + '.')
    def sum(self):
        try:
            self.result += float(self.ui.textBox.text())
            self.lastOperand = '+'
            self.step += 1
            self.ui.textBox.setText('')
        except:
            self.ui.textBox.setText('Error')
            self.result = 0
    def sub(self):
        try:
            if self.step == 0:
                self.result = float(self.ui.textBox.text())
            else:
                self.result -= float(self.ui.textBox.text())
            self.lastOperand = '-'
            self.step += 1
            self.ui.textBox.setText('')
        except:
            self.ui.textBox.setText('Error')
            self.result = 0
    def cross(self):
        try:
            if self.step == 0:
                self.result = float(self.ui.textBox.text())
            else:
                self.result *= float(self.ui.textBox.text())
            self.lastOperand = '*'
            self.step += 1
            self.ui.textBox.setText('')
        except:
            self.ui.textBox.setText('Error')
            self.result = 0
    def div(self):
        try:
            if self.step == 0:
                self.result = float(self.ui.textBox.text())
            else:
                self.result /= float(self.ui.textBox.text())
            self.lastOperand = '/'
            self.step += 1
            self.ui.textBox.setText('')
        except:
            self.ui.textBox.setText('Error')
            self.result = 0
    def equal(self):
        self.last_num = float(self.ui.textBox.text())
        self.step += 1
        if self.lastOperand == '+':
            self.result += self.last_num
        elif self.lastOperand == '-':
            self.result -= self.last_num
        elif self.lastOperand == '*':
            self.result *= self.last_num
        elif self.lastOperand == '/':
            self.result /= self.last_num
        elif self.lastOperand == '%':
            self.result = self.last_num/100
        else:
            self.result = self.last_num
        self.ui.textBox.setText(str(self.result))
        self.result = 0
        self.step = 0
        self.lastOperand = ''
    def ac(self):
        self.result = 0
        self.ui.textBox.setText('')
        self.step = 0
        self.lastOperand = ''
    def percentage_func(self):
        self.ui.textBox.setText(str(float(self.ui.textBox.text())/100))
        self.lastOperand = '%'
        self.step += 1
    def neg_pos(self):
        if '-' in self.ui.textBox.text():
            self.ui.textBox.setText(self.ui.textBox.text()[1:])
        else:
            self.ui.textBox.setText('-' + self.ui.textBox.text())
    def sin_func(self):
        self.ui.textBox.setText(str(round(sin(radians(float(self.ui.textBox.text()))), 4)))
        self.lastOperand = 'sin'
        self.step += 1
    def cos_func(self):
        self.ui.textBox.setText(str(round(cos(radians(float(self.ui.textBox.text()))), 4)))
        self.lastOperand = 'cos'
        self.step += 1
    def tan_func(self):
        self.ui.textBox.setText(str(round(tan(radians(float(self.ui.textBox.text()))), 4)))
        self.lastOperand = 'tan'
        self.step += 1
    def cot_func(self):
        self.ui.textBox.setText(str(round(cot(radians(float(self.ui.textBox.text()))), 4)))
        self.lastOperand = 'cot'
        self.step += 1
    def log_func(self):
        self.ui.textBox.setText(str(round(log(float(self.ui.textBox.text()), 10), 4)))
        self.lastOperand = 'log'
        self.step += 1
    def sqrt_func(self):
        self.ui.textBox.setText(str(round(sqrt(float(self.ui.textBox.text())), 4)))
        self.lastOperand = 'sqrt'
        self.step += 1


app = QApplication([])
window = Window()
app.exec()