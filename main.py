from PyQt6.QtWidgets import QApplication

from utils import Data
from window import window_loader

app = QApplication([])
Data.app = app
app.setActiveWindow(window_loader.LoaderWindow())
app.exec()
