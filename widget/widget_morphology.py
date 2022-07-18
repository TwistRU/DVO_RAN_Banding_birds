from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton
from database.db_reader import get_unique_columns_values, morphology_selector
from widget.widget_ext_combo_box import ExtendedComboBox


class MorphologyWidget(QWidget):

    def __init__(self):
        super(MorphologyWidget, self).__init__()
        uic.loadUi('ui/morphology.ui', self)
        self.data = []

        self.label_found: QLabel = self.findChild(QtWidgets.QLabel, 'label_found')
        self.push_button_find: QPushButton = self.findChild(QtWidgets.QPushButton, 'push_button_find')

        self.combo_box_species: ExtendedComboBox = self.findChild(ExtendedComboBox, 'combo_box_species')
        self.combo_box_species.addItems(
            sorted(get_unique_columns_values(["genus", "species"])))

        self.push_button_find.clicked.connect(self.find_btn_clicked)

    def find_btn_clicked(self):
        self.data = morphology_selector(self.combo_box_species.currentText())
        self.label_found.setText(f'Найдено: {len(self.data) - 1}')

    def get_results(self):
        return self.data
