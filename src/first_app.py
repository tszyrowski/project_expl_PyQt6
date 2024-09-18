from pathlib import Path
import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QFont, QPixmap


class EmptyWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(200, 100, 600, 800)  # Adjusted window size
        self.setWindowTitle("First window")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.y = 15  # Using self.y as an instance variable

        # Create the main title label
        main_lbl = QLabel(self)
        main_lbl.setText("App info")
        main_lbl.setFont(QFont("Arial", 20))
        main_lbl.adjustSize()
        main_lbl.move(105, self.y)
        self.y += main_lbl.height() + 10

        # Handle the first image
        img1 = f"{Path(__file__).parents[1]}/images/image1.png"
        try:
            with open(img1):
                img_lbl = QLabel(self)
                pixmap = QPixmap(img1)
                img_lbl.setPixmap(pixmap)
                img_lbl.adjustSize()
                img_lbl.move(25, self.y)
                self.y += img_lbl.height() + 10
        except FileNotFoundError as e:
            err_lbl = QLabel(self)
            err_lbl.setText(f"{img1}\n{e.strerror}")
            err_lbl.adjustSize()
            err_lbl.move(25, self.y)
            self.y += err_lbl.height() + 10

        self.createImageLabels()

    def createImageLabels(self):
        images = [
            f"{Path(__file__).parents[1]}/images/image2.png",
            f"{Path(__file__).parents[1]}/images/image3.png",
        ]

        for img in images:
            try:
                with open(img):
                    # Create label for the description
                    lbl_txt = QLabel(self)
                    lbl_txt.setText(f"Description for:\n{img}")
                    lbl_txt.adjustSize()
                    lbl_txt.move(25, self.y)
                    self.y += lbl_txt.height() + 5  # Update self.y

                    # Create label for the image
                    lbl_img_inner = QLabel(self)
                    pixmap = QPixmap(img)
                    lbl_img_inner.setPixmap(pixmap)
                    lbl_img_inner.adjustSize()
                    lbl_img_inner.move(25, self.y)
                    self.y += lbl_img_inner.height() + 10  # Update self.y
            except FileNotFoundError as e:
                err_lbl = QLabel(self)
                err_lbl.setText(f"{img}\n{e.strerror}")
                err_lbl.adjustSize()
                err_lbl.move(25, self.y)
                self.y += err_lbl.height() + 10  # Update self.y


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmptyWindow()
    sys.exit(app.exec())
