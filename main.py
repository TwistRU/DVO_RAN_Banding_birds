from PyQt6.QtWidgets import QApplication

from database.setup import setup_DB
from utils import Data
from window import window_loader

app = QApplication([])
Data.app = app
setup_DB()
Data.active_window = window_loader.LoaderWindow()
app.setActiveWindow(Data.active_window)
app.exec()
