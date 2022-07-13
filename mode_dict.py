from dataclasses import dataclass

from PyQt6.QtWidgets import QWidget
from widget.widget_morphology import MorphologyWidget


@dataclass
class Mode:
    num: int
    widget_obj: QWidget
    title: str
    desc: str


MODE_DICT = [
    Mode(1, None, "Временные ряды перв. и отн. численностей", ""),
    Mode(2, None, "Временные ряды накопленной численности", ""),
    Mode(3, None, "Внутрисезонная история отловов кольца", ""),
    Mode(4, None, "Межсезонная история отловов кольца", ""),
    Mode(5, None, "Внутрисезонная история отловов (на выбор)", ""),
    Mode(6, MorphologyWidget, "Таблица морфологии", ""),
]
