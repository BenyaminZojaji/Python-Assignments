from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from googletrans import Translator

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('translator.ui', None)
        self.ui.show()
        
        self.ui.translate_btn.clicked.connect(self.translate_func)
        self.ui.lang_btn.clicked.connect(self.langChange)   

    def langChange(self):
        if self.ui.lang_btn.text()=='En -> Fa':
            self.ui.lang_btn.setText('Fa -> En')
        else:
            self.ui.lang_btn.setText('En -> Fa')

    def translate_func(self):
        try:
            if self.ui.srcText.text()!='':
                translator = Translator()
                if self.ui.lang_btn.text()=='En -> Fa':
                    translate_text = translator.translate(self.ui.srcText.text(), src='en', dest='fa')
                else:
                    translate_text = translator.translate(self.ui.srcText.text(), src='fa', dest='en')
                self.ui.destText.setText(translate_text.text)
            else:
                self.ui.destText.setText('')
                msgBox = QMessageBox()
                msgBox.setText('There is nothing to translate.')
                msgBox.exec()
        except:
            self.ui.destText.setText('Connection Error')

app = QApplication([])
window = MainWindow()
app.exec()