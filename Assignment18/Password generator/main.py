import string
import secrets
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('passwordGenerator.ui', None)
        self.ui.show()

        self.ui.generate_btn.clicked.connect(self.generate)

    def generate(self):
        if self.ui.rd_weak.isChecked():
            alphabet = string.ascii_letters
            password = ''.join(secrets.choice(alphabet) for i in range(8))
        elif self.ui.rd_good.isChecked():
            alphabet = string.ascii_letters + string.digits
            password = ''.join(secrets.choice(alphabet) for i in range(10))
        elif self.ui.rd_unbreakable.isChecked():
            alphabet = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(secrets.choice(alphabet) for i in range(12))
        self.ui.lineEdit.setText(password)


app = QApplication([])
window = MainWindow()
app.exec()