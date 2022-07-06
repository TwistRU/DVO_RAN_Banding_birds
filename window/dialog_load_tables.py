from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QProgressBar, QLabel

from utils import Data
from window.window_main import MainWindow


class TableLoadDialog(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi('ui/d_table_loading.ui', self)
        self.progress_bar: QProgressBar = self.findChild(QtWidgets.QProgressBar, 'progress_bar')
        self.progress_bar.setValue(0)
        self.error_label: QLabel = self.findChild(QtWidgets.QLabel, 'error_label')
        self.setModal(True)
        self.show()

    def set_progress(self, progress: int, errors: list[str] = None):
        self.progress_bar.setValue(progress)
        if errors is not None:
            str_errors = '\n'.join(s for s in errors)
            self.error_label.setText(str_errors)
            self.progress_bar.setStyleSheet("color:red;")
        if progress >= 100:
            Data.current_window = MainWindow()
            self.close()