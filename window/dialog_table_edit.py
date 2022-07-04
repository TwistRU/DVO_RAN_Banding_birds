from dataclasses import dataclass

from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QLabel, QDialogButtonBox


@dataclass
class TableError:
    row: int
    col: int
    reason: str
    # можно добавить функцию constraint() для проверки, верно ли было исправлено это поле


class TableEditDialog(QtWidgets.QDialog):

    TEXT_ERRORS_FIXED = "Все ошибки были исправлены, можно закрывать окно"

    def __init__(self, headers: list[str], data: list[list[str]], errors: list[TableError]):
        super(TableEditDialog, self).__init__()
        uic.loadUi('ui/d_table_edit.ui', self)
        self.table: QTableWidget = self.findChild(QtWidgets.QTableWidget, 'error_table')
        self.errors_list: QLabel = self.findChild(QtWidgets.QLabel, 'scroll_error_label')
        self.button_box: QDialogButtonBox = self.findChild(QtWidgets.QDialogButtonBox, 'button_box')
        self.table.setRowCount(len(data))
        self.table.setColumnCount(len(data[0]))
        self.table.setHorizontalHeaderLabels(headers)

        for i in range(0, len(data)):
            for j in range(0, len(data[i])):
                self.table.setItem(i, j, QTableWidgetItem(data[i][j]))
        self.table.resizeRowsToContents()
        self.table.resizeColumnsToContents()

        self.error_text_array = []
        self.errors = errors
        for error in errors:
            item = self.table.item(error.row, error.col)
            item.setBackground(QColor.fromRgb(255, 0, 0))
            item.setForeground(QColor.fromRgb(255, 255, 255))
            error_line = "(" + str(error.row) + "," + str(error.col) + "):  " + error.reason
            item.setToolTip(error_line)
            self.error_text_array.append(error_line)
        self.table.itemChanged.connect(self.table_item_changed)
        self.update_text()
        self.update_availability()
        self.exec()

    def table_item_changed(self, item: QTableWidgetItem):
        if item.background().color().red() == 255:
            item.setBackground(QColor.fromRgb(0, 255, 0))
            item.setForeground(QColor.fromRgb(0, 0, 0))
            error_index = next(i for i, v in enumerate(self.errors) if v.col == item.column() and v.row == item.row())
            del self.error_text_array[error_index]
            del self.errors[error_index]
            self.update_text()
            self.update_availability()

    def update_availability(self):
        self.button_box.setEnabled(len(self.errors) == 0)

    def update_text(self):
        error_str = ""
        if len(self.error_text_array) == 0:
            error_str = TableEditDialog.TEXT_ERRORS_FIXED
        else:
            for str in self.error_text_array:
                error_str += str + "\n"
        self.errors_list.setText(error_str)


# Пример вызова диалога с таблицей
def test_table_dialog():
    headers = ['Первый', 'Второй']
    data = [["1", "2"], ["3", "4"], ["4", "01.01.2022"]]
    errors = [TableError(1, 0, "Ошибка в числе"), TableError(2, 1, "Ошибка в дате")]
    TableEditDialog(headers, data, errors)
