from PyQt6.QtWidgets import QApplication
import window_loader

app = QApplication([])
window = window_loader.LoaderWindow()
app.exec()
