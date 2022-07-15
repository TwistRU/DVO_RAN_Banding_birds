from sqlite3 import Connection

from PyQt6.QtWidgets import QApplication


class Data:
    IS_DEBUG = False
    app: QApplication = None
    conn: Connection = None
    active_window = None