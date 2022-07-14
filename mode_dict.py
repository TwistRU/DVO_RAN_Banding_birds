from dataclasses import dataclass
from typing import Type

from PyQt6.QtWidgets import QWidget
from widget.widget_morphology import MorphologyWidget
from widget.widget_in_seasonal_history_2 import InSeasonalHistory2Widget
from widget.widget_in_seasonal_history import InSeasonalHistoryWidget
from widget.widget_time_series_of_primary_numbers import TimeSeriesOfPrimaryNumbersWidget


@dataclass
class Mode:
    num: int
    widget_obj: Type[QWidget]
    title: str
    desc: str


MODE_DICT = [
    Mode(1, TimeSeriesOfPrimaryNumbersWidget, "Временные ряды перв. и отн. численностей", ""),
    Mode(2, None, "Временные ряды накопленной численности", ""),
    Mode(3, None, "Внутрисезонная история отловов кольца", ""),
    Mode(4, InSeasonalHistoryWidget, "Межсезонная история отловов кольца", ""),
    Mode(5, InSeasonalHistory2Widget, "Внутрисезонная история отловов (на выбор)", ""),
    Mode(6, MorphologyWidget, "Таблица морфологии", ""),
]
