from dataclasses import dataclass
from typing import Type

from PyQt6.QtWidgets import QWidget
from widget.widget_morphology import MorphologyWidget
from widget.widget_in_seasonal_history_2 import InSeasonalHistory2Widget
from widget.widget_in_seasonal_history import InSeasonalHistoryWidget
from widget.widget_time_series_of_primary_numbers import TimeSeriesOfPrimaryNumbersWidget
from widget.widget_time_series_of_accumulated_numbers import TimeSeriesOfAccumulatedNumbersWidget


@dataclass
class Mode:
    num: int
    widget_obj: Type[QWidget]
    title: str
    desc: str


MODE_DICT = [
    Mode(1, TimeSeriesOfPrimaryNumbersWidget, "Временные ряды перв. и отн. численностей", "(Здесь будет описание)"),
    Mode(2, TimeSeriesOfAccumulatedNumbersWidget, "Временные ряды накопленной численности", "(Здесь будет описание)"),
    Mode(3, None, "Внутрисезонная история отловов кольца", "(Здесь будет описание)"),
    Mode(4, InSeasonalHistoryWidget, "Межсезонная история отловов кольца", "(Здесь будет описание)"),
    Mode(5, InSeasonalHistory2Widget, "Внутрисезонная история отловов (на выбор)", "(Здесь будет описание)"),
    Mode(6, MorphologyWidget, "Таблица морфологии", "(Здесь будет описание)"),
]
