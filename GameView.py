# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QPainter, QFontDatabase
from Settings import Settings, bg_images

class GameView(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._pixmap = None
        self.setBackground(Settings.value("imageIndex", type=int))
        self.font_id = QFontDatabase.addApplicationFont(":/fonts/AOTFShinGoProMedium.otf")

    def setPixmap(self, pixmap):
        if pixmap == None:
            pixmap = QPixmap()
        self._pixmap = pixmap
        super().setPixmap(self._scaled())

    def resizeEvent(self, event):
        if self._pixmap:
            super().setPixmap(self._scaled())

    def _scaled(self):
        return self._pixmap.scaled(
            self.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

    def setBackground(self, index):
        self._bg_pixmap = QPixmap(f":/backgrounds/{bg_images(index)}.png")
        self.update()

    def paintEvent(self, event):
        # 1. Draw background first
        if not self._bg_pixmap.isNull():
            painter = QPainter(self)
            scaled = self._bg_pixmap.scaled(
                self.size(),
                Qt.KeepAspectRatioByExpanding,
                Qt.SmoothTransformation
            )
            x = (scaled.width() - self.width()) // 2
            y = (scaled.height() - self.height()) // 2
            painter.drawPixmap(-x, -y, scaled)
            painter.end()

        # 2. Your existing paintEvent logic runs on top
        super().paintEvent(event)

