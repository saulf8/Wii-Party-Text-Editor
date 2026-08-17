# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt
from ui_aboutdialog import Ui_Dialog

class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("About")
        self.setWindowFlags(
            Qt.Dialog |
            Qt.WindowTitleHint |
            Qt.WindowCloseButtonHint
        )
        self.setFixedSize(400, 250)

