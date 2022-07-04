from PyQt6.QtWidgets import QApplication
from window import window_loader

app = QApplication([])
window = window_loader.LoaderWindow()
app.exec()
