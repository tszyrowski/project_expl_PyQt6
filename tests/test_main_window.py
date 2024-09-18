import pytest
from PyQt6.QtWidgets import QLabel
from src.first_app import MainWindow


@pytest.fixture
def app(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    return window


def test_window_title(app):
    assert app.windowTitle() == "First window"


def test_label_text(app):
    labels = app.findChildren(QLabel)
    main_label_texts = [
        label.text() for label in labels if label.font().pointSize() == 20
    ]
    assert "App info" in main_label_texts


def test_number_of_labels(app):
    labels = app.findChildren(QLabel)
    assert len(labels) >= 1


def test_images_loaded(app):
    labels = app.findChildren(QLabel)
    pixmap_lbls = [label for label in labels if label.pixmap() is not None]
    assert len(pixmap_lbls) >= 1
