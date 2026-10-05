"""Define the placeholder main window."""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QMainWindow


class MainWindow(QMainWindow):
    """Show a minimal window for the initial project setup."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("LA-TOF-MS-ControlSuite")
        self.resize(800, 500)

        label = QLabel("LA-TOF-MS-ControlSuite\nProject setup complete.")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)
