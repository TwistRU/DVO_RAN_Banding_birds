from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QComboBox
from database.db_reader import get_unique_columns_values, get_data_by_columns
from widget.widget_ext_combo_box import ExtendedComboBox


class InSeasonalHistoryWidget(QWidget):

    def __init__(self):
        super(InSeasonalHistoryWidget, self).__init__()
        uic.loadUi('ui/in_seasonal_history.ui', self)
        self.data = []


        self.label_found: QLabel = self.findChild(QtWidgets.QLabel, 'label_found')
        self.push_button_find: QPushButton = self.findChild(QtWidgets.QPushButton, 'push_button_find')

        self.combo_box_species: ExtendedComboBox = self.findChild(ExtendedComboBox, 'combo_box_species')
        self.combo_box_age: ExtendedComboBox = self.findChild(ExtendedComboBox, 'combo_box_age')
        self.combo_box_gender: ExtendedComboBox = self.findChild(ExtendedComboBox, 'combo_box_gender')

        self.combo_box_species.addItems(sorted(get_unique_columns_values(["genus", "species"])))
        self.combo_box_age.addItems(get_unique_columns_values(["age"]))
        self.combo_box_gender.addItems(sorted(get_unique_columns_values(["gender"])))

        self.combo_box_species.setCurrentText("")
        self.combo_box_age.setCurrentText("")
        self.combo_box_gender.setCurrentText("")

        self.push_button_find.clicked.connect(self.find_btn_clicked)


    def find_btn_clicked(self):
        self.data = get_data_by_columns([("genus_and_species", self.combo_box_species.currentText()),
                                         ("age", self.combo_box_age.currentText()),
                                         ("gender", self.combo_box_gender.currentText())])

        self.label_found.setText(f'Найдено: {len(self.data)}')

    def get_results(self):
        return self.data
