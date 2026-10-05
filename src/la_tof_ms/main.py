"""Start the placeholder application."""

import sys

from PySide6.QtWidgets import QApplication

from la_tof_ms.gui.main_window import MainWindow


def main() -> int:
    """Create the application and run its event loop."""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
