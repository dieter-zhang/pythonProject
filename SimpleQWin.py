import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = QWidget()
    win.show()
    sys.exit(app.exec())
