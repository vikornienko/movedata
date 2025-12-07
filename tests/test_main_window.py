from pytestqt.qtbot import QtBot
from PySide6.QtCore import Qt

from movedata_gui.ui.main_window import MainWindow


class TestMainWindow:
    def test_window_creation(self, main_window: MainWindow) -> None:
        assert main_window is not None
        assert isinstance(main_window, MainWindow)

    def test_window_title(self, main_window: MainWindow) -> None:
        assert main_window.windowTitle() == "PySide6 Starter"

    def test_window_text(self, main_window: MainWindow) -> None:
        assert main_window.label.text() == "Hello from PySide6!"

    def test_button_exist(self, main_window: MainWindow) -> None:
        assert main_window.button is not None
        assert main_window.button.text() == "Тыц!!!"

    def test_click_button(self, main_window: MainWindow, qtbot: QtBot) -> None:
        assert main_window.label.text() == "Hello from PySide6!"
        """Эмулируем клик левой кнопкой мыши."""
        qtbot.mouseClick(main_window.button, Qt.MouseButton.LeftButton)
        assert main_window.label.text() == "Success!"
