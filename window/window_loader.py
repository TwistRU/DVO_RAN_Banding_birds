from os import getcwd

from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QFileDialog


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
        for i in range(1, 4):
            i_str = str(i)
            button = self.findChild(QtWidgets.QPushButton, 'load_button_' + i_str)
            self.buttons.append(button)
            button.clicked.connect(lambda _, button_id=i: self.the_button_was_clicked(button_id))
            self.status_labels.append(self.findChild(QtWidgets.QLabel, 'load_label_status_' + i_str))
        self.buttons.append(self.findChild(QtWidgets.QPushButton, 'load_button_continue'))

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

    def the_button_was_clicked(self, button_id: int):
        tmp = QFileDialog.getOpenFileName(self, 'Выбор таблицы', getcwd(), "Excel файлы (*.xlsx *.xls)")
        if tmp[0].endswith("xlsx") or tmp[0].endswith("xls"):
            self.files[button_id - 1] = tmp[0]
        else:
            self.files[button_id - 1] = None
        self.update()
