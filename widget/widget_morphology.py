from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton
from database.db_reader import get_unique_column_values, get_data_by_columns
from widget.widget_ext_combo_box import ExtendedComboBox


class MorphologyWidget(QWidget):

    def __init__(self):
        super(MorphologyWidget, self).__init__()
        uic.loadUi('ui/morphology.ui', self)

        self.label_found: QLabel = self.findChild(QtWidgets.QLabel, 'label_found')
        self.push_button_find: QPushButton = self.findChild(QtWidgets.QPushButton, 'push_button_find')

        self.combo_box_species: ExtendedComboBox = self.findChild(ExtendedComboBox, 'combo_box_species')
        self.combo_box_species.addItems(sorted(get_unique_column_values("species")))

        self.push_button_find.clicked.connect(self.find_btn_clicked)

    def find_btn_clicked(self):
        data = get_data_by_columns([("species", self.combo_box_species.currentText())])
        self.label_found.setText(f'Найдено: {len(data)}')
