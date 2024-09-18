from pathlib import Path
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap, QAction
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QVBoxLayout,
)

class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(200, 100, 600, 800)  # Adjusted window size
        self.setWindowTitle("First window")
        self.setupMenuBar()
        self.setupStatusBar()
        self.setUpMainWindow()
        self.show()

    def setupMenuBar(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')

        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

    def setupStatusBar(self):
        status_bar = self.statusBar()
        status_bar.showMessage('Ready')

    def setUpMainWindow(self):
        # Create a central widget and set it
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Use a layout for the central widget
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # Create the main title label
        main_lbl = QLabel(self)
        main_lbl.setText("App info")
        main_lbl.setFont(QFont("Arial", 20))
        main_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(main_lbl)

        # Handle the first image
        img1 = f"{Path(__file__).parents[1]}/images/image1.png"
        try:
            with open(img1):
                img_lbl = QLabel()
                pixmap = QPixmap(img1)
                img_lbl.setPixmap(pixmap)
                img_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
                layout.addWidget(img_lbl)
        except FileNotFoundError as e:
            err_lbl = QLabel(f"{img1}\n{e.strerror}")
            err_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(err_lbl)

        self.createImageLabels(layout)

    def createImageLabels(self, layout):
        images = [
            f"{Path(__file__).parents[1]}/images/image2.png",
            f"{Path(__file__).parents[1]}/images/image3.png",
        ]

        for img in images:
            try:
                with open(img):
                    # Create label for the description
                    lbl_txt = QLabel(f"Description for:\n{img}")
                    lbl_txt.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    layout.addWidget(lbl_txt)

                    # Create label for the image
                    lbl_img_inner = QLabel()
                    pixmap = QPixmap(img)
                    lbl_img_inner.setPixmap(pixmap)
                    lbl_img_inner.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    layout.addWidget(lbl_img_inner)
            except FileNotFoundError as e:
                err_lbl = QLabel(f"{img}\n{e.strerror}")
                err_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
                layout.addWidget(err_lbl)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
