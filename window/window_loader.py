import threading
from os import getcwd

from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QThread
from PyQt6.QtWidgets import QFileDialog

from database.db_utils import load_tables_to_DB
from utils import Data
from window.dialog_load_tables import TableLoadDialog
from window.window_main import MainWindow


class LoaderWindow(QtWidgets.QMainWindow):
    STATUS_NOT_SELECTED = "Не выбрана"
    CSS_NOT_SELECTED = "color:rgb(255, 0, 0);"
    CSS_SELECTED = "color:rgb(80, 200, 120);"

    def __init__(self):
        super(LoaderWindow, self).__init__()
        uic.loadUi('ui/w_loader.ui', self)
        self.buttons = []
        self.status_labels = []
        self.files = [None for i in range(0, 4)]
        self.load_dialog: TableLoadDialog | None = None
        for i in range(1, 4):
            i_str = str(i)
            button = self.findChild(QtWidgets.QPushButton, 'load_button_' + i_str)
            self.buttons.append(button)
            button.clicked.connect(lambda _, button_id=i: self.load_button_clicked(button_id))
            self.status_labels.append(self.findChild(QtWidgets.QLabel, 'load_label_status_' + i_str))
        button_continue = self.findChild(QtWidgets.QPushButton, 'load_button_continue')
        self.buttons.append(button_continue)
        button_continue.clicked.connect(self.continue_button_clicked)
        if Data.IS_DEBUG: button_continue.setEnabled(True)
        self.show()

    def update(self):
        all_files = True
        for i in range(0, 3):
            label: QtWidgets.QLabel = self.status_labels[i]
            path: str | None = self.files[i]
            if path is not None:
                label.setText(path.split('/')[-1])
                label.setStyleSheet(LoaderWindow.CSS_SELECTED)
            else:
                all_files = False
                label.setText(LoaderWindow.STATUS_NOT_SELECTED)
                label.setStyleSheet(LoaderWindow.CSS_NOT_SELECTED)
        self.buttons[3].setEnabled(all_files)

    def continue_button_clicked(self):
        self.load_dialog = TableLoadDialog(self)
        self.load_dialog.exec()
        Data.active_window = MainWindow()
        self.close()

    def load_button_clicked(self, button_id: int):
        tmp = QFileDialog.getOpenFileName(self, 'Выбор таблицы', getcwd(), "Excel файлы (*.xlsx *.xls)")
        if tmp[0].endswith("xlsx") or tmp[0].endswith("xls"):
            self.files[button_id - 1] = tmp[0]
        else:
            self.files[button_id - 1] = None
        self.update()
