from os import getcwd

from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QListWidgetItem, QLabel, QWidget, QFrame, QPushButton, QFileDialog

import mode_dict


class MainWindow(QtWidgets.QMainWindow):
    ABOUT_DEFAULT_TITLE = "Добро пожаловать в программу учета кольцевания птиц!"
    ABOUT_DEFAULT_DESC = "Для начала работы выберите желаемую таблицу из меню слева"

    def __init__(self):
        super(MainWindow, self).__init__()
        self.selected_mode: mode_dict.Mode = None
        uic.loadUi('ui/w_main.ui', self)
        self.mode_list: QtWidgets.QListWidget = self.findChild(QtWidgets.QListWidget, 'main_list_modes')
        for mode in mode_dict.MODE_DICT:
            item = QListWidgetItem(mode.title, self.mode_list)
            item.setData(-1, mode.num)
        self.mode_list.currentItemChanged.connect(self.selection_changed)
        self.about_header: QLabel = self.findChild(QtWidgets.QLabel, 'about_label_header')
        self.about_desc: QLabel = self.findChild(QtWidgets.QLabel, 'about_label_desc')
        self.mode_qframe: QFrame = self.findChild(QtWidgets.QFrame, 'main_frame_widget')
        self.button_export: QPushButton = self.findChild(QtWidgets.QPushButton, 'main_button_export')
        self.button_export.hide()
        self.button_export.clicked.connect(self.export_clicked)
        self.show()

    def export_clicked(self):
        QFileDialog.getSaveFileName(self, 'Сохранение таблицы', getcwd(), "CSV файл (*.csv)")

    def selection_changed(self, new_selection):
        first_launch = self.selected_mode is None
        self.selected_mode = mode_dict.MODE_DICT[new_selection.data(-1) - 1]
        if first_launch:
            self.about_header.setText(MainWindow.ABOUT_DEFAULT_TITLE)
            self.about_desc.setText(MainWindow.ABOUT_DEFAULT_DESC)
        else:
            self.button_export.show()
            self.about_header.setText(self.selected_mode.title)
            self.about_desc.setText(self.selected_mode.desc)
            if self.selected_mode.widget_obj is not None:
                if len(self.mode_qframe.children()) > 1:
                    child = self.mode_qframe.children()[1]
                    self.mode_qframe.children().remove(child)
                    child.setParent(None)
                new_widget: QWidget = self.selected_mode.widget_obj()
                self.mode_qframe.layout().addChildWidget(new_widget)
                new_widget.show()
