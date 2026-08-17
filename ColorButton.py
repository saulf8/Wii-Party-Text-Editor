# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QSize


class ColorButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        #applied only to left
        self.padding_w = 5
        self.padding_h = 5
        #applied evenly to top and bottom
        self.setStyleSheet(f"""
            ColorButton {{
                text-align: left;
                padding-left: {self.padding_w}px;
            }}
        """)

    def sizeHint(self):
        base_size = super().sizeHint()

        #apply padding
        return QSize(
            base_size.width() + self.padding_w,
            base_size.height() + self.padding_h
        )

