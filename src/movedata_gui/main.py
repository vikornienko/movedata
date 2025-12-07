import sys
from loguru import logger
from PySide6.QtWidgets import QApplication
from movedata_gui.ui.main_window import MainWindow


def setup_logging() -> None:
    logger.remove()
    logger.add(
        sys.stderr,
        format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>",
        level="DEBUG",
        colorize=True
    )

def main() -> None:
    setup_logging()
    logger.info("Start application.")

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    exit_code = app.exec()
    logger.info(f"Exit from the application with code: {exit_code}")
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
