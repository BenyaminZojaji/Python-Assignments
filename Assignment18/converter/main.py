from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from unit_converter.converter import converts

class Converter(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('unitConverter.ui', None)
        self.ui.show()

        self.ui.convert_btn.clicked.connect(self.convert)
        self.ui.convert_comboBox.currentTextChanged.connect(self.on_unitChange)

    def on_unitChange(self):
        self.ui.fromUnit_comboBox.clear()
        self.ui.toUnit_comboBox.clear()
        if self.ui.convert_comboBox.currentText()=='Mass':
            self.ui.fromUnit_comboBox.addItems(['g','kg','T','P'])
            self.ui.toUnit_comboBox.addItems(['kg','g','T','P'])
        elif self.ui.convert_comboBox.currentText()=='Length':
            self.ui.fromUnit_comboBox.addItems(['mm','cm','m','km','in'])
            self.ui.toUnit_comboBox.addItems(['cm','mm','m','km','in'])
        elif self.ui.convert_comboBox.currentText()=='Value':
            self.ui.fromUnit_comboBox.addItems(['bit','byte','KByte','MByte','GByte','TByte'])
            self.ui.toUnit_comboBox.addItems(['byte','bit','KByte','MByte','GByte','TByte'])
        elif self.ui.convert_comboBox.currentText()=='Temperature':
            self.ui.fromUnit_comboBox.addItems(['°C','°F','°K'])
            self.ui.toUnit_comboBox.addItems(['°F','°C','°K'])

    def convert(self):
        quantity = self.ui.input_textBox.text()
        current_unit = self.ui.fromUnit_comboBox.currentText()
        desired_unit = self.ui.toUnit_comboBox.currentText()
        result = converts(quantity=quantity+current_unit, desired_unit=desired_unit)
        self.ui.output_textBox.setText(str(round(float(result), 2)))

app = QApplication([])
window = Converter()
app.exec()