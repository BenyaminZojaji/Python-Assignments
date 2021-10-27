from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import database

class Popup(QWindow):
    def __init__(self, id):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('popup.ui', None)
        self.ui.show()

        # get and assign data to labels
        details = database.get_detail(id)
        self.ui.id_label.setText(f'{details[0][0]}')
        self.ui.title_label.setText(f'{details[0][1]}')
        self.ui.description_label.setText(f'{details[0][2]}')
        self.ui.time_label.setText(f'{details[0][3]}')
        if details[0][4]==1:
            self.ui.done_label.setText('YES')
        else:
            self.ui.done_label.setText('NO')
        
        self.ui.back_btn.clicked.connect(self.back)
    
    def back(self):
        self.ui = MainWindow()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('todolist.ui', None)
        self.ui.show()

        self.lastID = 0

        self.readFromDataBase()

        self.ui.add_btn.clicked.connect(self.addNewTaskToDataBase)
        self.ui.tabWidget.currentChanged.connect(self.tabChange)

    def clearUI_complete(self):
        #print(f'objects{self.ui.gridLayout_comp.count()}')
        for i in reversed(range(self.ui.gridLayout_comp.count())): 
            self.ui.gridLayout_comp.itemAt(i).widget().deleteLater()

    def tabChange(self):
        self.clearUI_complete()
        # complete
        result = database.get_all()
        for i in range(len(result)):
            if result[i][4]==1:
                id_label_comp = QLabel() # id
                id_label_comp.setText(str(result[i][0]))
                title_label_comp = QLabel() # title
                title_label_comp.setText(result[i][1])
                title_label_comp.setStyleSheet('font-size:18px')
                desc_label_comp = QLabel() # description
                desc_label_comp.setText(result[i][2])
                desc_label_comp.setStyleSheet('font-size:18px')
                time_label_comp = QLabel() # time
                time_label_comp.setText(str(result[i][3]))
                time_label_comp.setStyleSheet('font-size:18px')

                self.ui.gridLayout_comp.addWidget(id_label_comp, i, 0)
                self.ui.gridLayout_comp.addWidget(title_label_comp, i, 1)
                self.ui.gridLayout_comp.addWidget(desc_label_comp, i, 2)
                self.ui.gridLayout_comp.addWidget(time_label_comp, i, 3)

    def readFromDataBase(self):
        result = database.get_all()
        self.lastID = 0
        for i in range(len(result)):
            self.lastID += 1

            done_checkbox = QCheckBox()
            done_checkbox.setObjectName(f'done_{result[i][0]}')
            done_checkbox.stateChanged.connect(self.doneTask)
            if result[i][4]==1:
                done_checkbox.setChecked(True)

            id_label = QLabel() # id
            id_label.setText(str(result[i][0]))

            title_label = QLabel() # title
            title_label.setText(result[i][1])

            desc_label = QLabel() # description
            desc_label.setText(result[i][2])

            time_label = QLabel() # time
            time_label.setText(str(result[i][3]))

            prio_btn = QPushButton() # priority
            prio_btn.setObjectName(f'prio_btn_{result[i][0]}')
            prio_btn.clicked.connect(self.priority)
            if result[i][5]==1:
                prio_btn.setIcon(QIcon('images/pin.png'))
            else:
                prio_btn.setIcon(QIcon('images/unpin.png'))

            detail_btn = QPushButton() # detail
            detail_btn.setObjectName(f'detail_btn_{result[i][0]}')
            detail_btn.setIcon(QIcon('images/detail.png'))
            detail_btn.clicked.connect(self.detail)

            dlt_btn = QPushButton() # delete
            dlt_btn.setObjectName(f'delete_btn_{result[i][0]}')
            dlt_btn.clicked.connect(self.delete)
            dlt_btn.setText('❌')

            # tasks layout
            self.ui.gridLayout.addWidget(id_label, i, 0)
            self.ui.gridLayout.addWidget(title_label, i, 1)
            self.ui.gridLayout.addWidget(desc_label, i, 2)
            self.ui.gridLayout.addWidget(time_label, i, 3)
            self.ui.gridLayout.addWidget(done_checkbox, i, 4)
            self.ui.gridLayout.addWidget(prio_btn, i, 5)
            self.ui.gridLayout.addWidget(detail_btn, i, 6)
            self.ui.gridLayout.addWidget(dlt_btn, i, 7)

    def doneTask(self):
        id = self.sender().objectName().split('_')[-1]
        if self.sender().isChecked():
            database.update_done(id, 1)
        else:
            database.update_done(id, 0)

    def clearUI_tasks(self):
        for i in reversed(range(self.ui.gridLayout.count())): 
            self.ui.gridLayout.itemAt(i).widget().deleteLater()

    def detail(self):
        id = self.sender().objectName().split('_')[-1]
        self.ui = Popup(id)

    def delete(self):
        id = self.sender().objectName().split('_')[-1]
        database.delete(id)
        self.clearUI_tasks()
        self.readFromDataBase()

    def priority(self):
        id = self.sender().objectName().split('_')[-1]
        priority = database.get_detail(id)[0][5]
        if priority==1:
            database.update_priority(id, 0)
        else:
            database.update_priority(id, 1)
        self.clearUI_tasks()
        self.readFromDataBase()

    def addNewTaskToDataBase(self):
        title = self.ui.tb_title.text()
        description = self.ui.tb_description.text()
        time = self.ui.tb_time.text()
        id = self.lastID + 1

        database.add(id, title, description, time)

        self.clearUI_tasks()
        self.readFromDataBase()

        self.ui.tb_title.setText('')
        self.ui.tb_description.setText('')
        self.ui.tb_time.setText('')

app = QApplication([])
window = MainWindow()
app.exec()