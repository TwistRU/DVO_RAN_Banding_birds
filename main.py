from PyQt6.QtWidgets import QApplication

from database.setup import setup_DB
from utils import Data
from window import window_loader

app = QApplication([])
Data.app = app
setup_DB()
app.setActiveWindow(window_loader.LoaderWindow())
app.exec()
