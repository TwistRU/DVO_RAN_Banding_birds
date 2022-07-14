from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QProgressBar, QLabel

from database.db_utils import load_tables_to_DB


class TableLoadThread(QThread):
    on_progress = pyqtSignal()
    max_progress = pyqtSignal(int)
    on_finish = pyqtSignal()

    def __init__(self, files):
        super().__init__()
        self.files = files
        self.start()

    def run(self):
        load_tables_to_DB(self.files, self.on_progress, self.max_progress)
        self.on_finish.emit()


class TableLoadDialog(QtWidgets.QDialog):
    STATUS_LOADING = "Загрузка таблиц..."

    def __init__(self, parent):
        super().__init__()
        uic.loadUi('ui/d_table_loading.ui', self)
        self.progress_bar: QProgressBar = self.findChild(QtWidgets.QProgressBar, 'progress_bar')
        self.status_label: QLabel = self.findChild(QtWidgets.QLabel, 'status_label')
        self.setModal(True)
        self.parent = parent
        self.thread = TableLoadThread(parent.files)
        self.thread.on_progress.connect(self.inc_progress)
        self.thread.max_progress.connect(self.set_max_progress)
        self.thread.on_finish.connect(lambda: self.close())

    def set_max_progress(self, max_progress: int):
        self.progress_bar.setMaximum(max_progress)
        self.progress_bar.setValue(0)

    def inc_progress(self):
        cur_progress = self.progress_bar.value()
        if cur_progress == 0:
            self.status_label.setText(TableLoadDialog.STATUS_LOADING)
        self.progress_bar.setValue(cur_progress + 1)
