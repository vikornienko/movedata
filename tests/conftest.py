import pytest
from pytestqt.qtbot import QtBot

from movedata_gui.ui.main_window import MainWindow


@pytest.fixture
def main_window(qtbot: QtBot) -> MainWindow:
    """Фикстура для создания основного окна."""
    window = MainWindow()
    qtbot.addWidget(window)
    return window
