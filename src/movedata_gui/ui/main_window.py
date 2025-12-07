from loguru import logger
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("PySide6 Starter")
        self.resize(400, 300)

        # Центральный виджет и лейаут
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Элементы интерфейса
        self.label = QLabel("Hello from PySide6!")
        self.label.setStyleSheet("font-size: 16px; font-weight: bold;")

        self.button = QPushButton("Тыц!!!")
        self.button.setCursor(Qt.CursorShape.PointingHandCursor)

        # Добавление на форму
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # Сигналы
        self.button.clicked.connect(self.on_button_click)

        logger.info("MainWindow was initialized")

    def on_button_click(self) -> None:
        logger.debug("Button was clicked.")
        self.label.setText("Success!")
