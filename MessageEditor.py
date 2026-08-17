# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QTextEdit

class MessageEditor(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def filter_drag_drop(self, event):
        if event.mimeData().hasUrls():
            event.ignore()
            return False

        if event.mimeData().hasText():
            event.acceptProposedAction()
            return True

        event.ignore()
        return False

    def dragEnterEvent(self, event):
        self.filter_drag_drop(event)

    def dragMoveEvent(self, event):
        self.filter_drag_drop(event)

    def dropEvent(self, event):
        if self.filter_drag_drop(event):
            self.setFocus()
            super().dropEvent(event)

if __name__ == "__main__":
    pass
