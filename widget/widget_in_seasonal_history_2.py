from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QComboBox
from database.db_reader import get_unique_column_values, get_data_by_columns
from widget.widget_ext_combo_box import ExtendedComboBox


class InSeasonalHistory2Widget(QWidget):

    def __init__(self):
        super(InSeasonalHistory2Widget, self).__init__()
        uic.loadUi('ui/in_seasonal_history_2.ui', self)

        self.var_select_columns = [('weight', 'Вес'),
                                   ('richness', 'Балл жирности'),
                                   ('muscle', 'Балл мышцы'),
                                   ('pneumatization', '% пневматизации'),
                                   ('molting_stage', 'Стадия линьки'),
                                   ('age_EURING', 'Возраст EURING'),
                                   ('biotope_code', 'Код биотопа'),
                                   ('mesh_number', '№ сети')]
        self.var_lists = [get_unique_column_values(i[0]) for i in self.var_select_columns]

        self.label_found: QLabel = self.findChild(QtWidgets.QLabel, 'label_found')
        self.push_button_find: QPushButton = self.findChild(QtWidgets.QPushButton, 'push_button_find')

        self.combo_box_species: ExtendedComboBox = self.findChild(ExtendedComboBox, 'combo_box_species')
        self.combo_box_age: ExtendedComboBox = self.findChild(ExtendedComboBox, 'combo_box_age')
        self.combo_box_gender: ExtendedComboBox = self.findChild(ExtendedComboBox, 'combo_box_gender')
        self.combo_box_var: ExtendedComboBox = self.findChild(ExtendedComboBox, 'combo_box_var')

        self.combo_box_species.addItems(sorted(get_unique_column_values("species")))
        self.combo_box_age.addItems(get_unique_column_values("age"))
        self.combo_box_gender.addItems(sorted(get_unique_column_values("gender")))

        self.combo_box_species.setCurrentText("")
        self.combo_box_age.setCurrentText("")
        self.combo_box_gender.setCurrentText("")

        self.combo_box_var_select: QComboBox = self.findChild(QtWidgets.QComboBox, 'combo_box_var_select')
        self.combo_box_var_select.addItems([i[1] for i in self.var_select_columns])

        self.combo_box_var_select.activated.connect(self.var_select_changed)
        self.push_button_find.clicked.connect(self.find_btn_clicked)

    def var_select_changed(self):
        ind = self.combo_box_var_select.currentIndex()
        self.combo_box_var.clear()
        self.combo_box_var.addItems(sorted(self.var_lists[ind]))

    def find_btn_clicked(self):
        data = get_data_by_columns([("species", self.combo_box_species.currentText()),
                                    ("age", self.combo_box_age.currentText()),
                                    ("gender", self.combo_box_gender.currentText()),
                                    (self.var_select_columns[self.combo_box_var_select.currentIndex()][0],
                                     self.combo_box_var.currentText())])

        self.label_found.setText(f'Найдено: {len(data)}')
