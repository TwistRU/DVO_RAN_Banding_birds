from PyQt6.QtWidgets import QApplication

from database.setup import setup_DB
from utils import Data
from window.window_loader import LoaderWindow
from window.window_main import MainWindow

app = QApplication([])
Data.app = app
db_exists = setup_DB()
Data.active_window = MainWindow() if db_exists else LoaderWindow()
app.setActiveWindow(Data.active_window)
app.exec()
