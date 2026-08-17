# This Python file uses the following encoding: utf-8
import sys, os, copy, traceback, ctypes
import xmsg, tree_helper, color_helper
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QInputDialog, QMessageBox, QColorDialog
from PySide6.QtGui import QColor, QPixmap, QKeySequence, QFontDatabase, QPalette, QDesktopServices, QIcon
from PySide6.QtCore import QUrl
from Settings import Settings, GameViewSettingsDialog
from AboutDialog import AboutDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        #add fonts
        font_id = QFontDatabase.addApplicationFont(":/fonts/AOTFShinGoProRegular.otf")
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            app.setStyleSheet(f"QWidget {{ font-family: '{font_family}'; }}")

        #set palette
        app_palette = QPalette()
        app_palette.setColor(QPalette.ColorRole.Highlight, QColor(228, 20, 100, 200))
        app_palette.setColor(QPalette.ColorRole.Accent, QColor(228, 20, 100, 200))
        app.setPalette(app_palette)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setAcceptDrops(True)
        self.orig_deser = xmsg.XMSG()
        self.deser = xmsg.XMSG()

        #tree elements that hold messages
        self.trees = [self.ui.minigames, self.ui.house, self.ui.menu, self.ui.party, self.ui.pair, self.ui.system, self.ui.searched]
        #ui elements that are disabled when no message is selected to edit
        self.can_lock = [self.ui.newText, self.ui.selected_expr, self.ui.expr_width, self.ui.expr_height, self.ui.expr_hp, self.ui.expr_vp,
            self.ui.color_revert, self.ui.outline_revert, self.ui.width_revert, self.ui.height_revert, self.ui.hp_revert,
            self.ui.vp_revert, self.ui.sel_expr_revert, self.ui.expr_phil_revert, self.ui.start_expr, self.ui.middle_expr,
            self.ui.end_expr, self.ui.expr_color, self.ui.expr_outline]
        #ui elements or actions that are disabled when no file is opened
        self.needs_file = [self.ui.actionSave, self.ui.actionSave_As, self.ui.actionClose, self.ui.actionFind, self.ui.actionSnap_to_selected,
            self.ui.menuEdit]
        for elem in self.needs_file:
            elem.setEnabled(False)
        tree_helper.set_up_trees(self)
        tree_helper.adjust_tree_height(self.ui.searched)

        #menu bar actions
        self.ui.actionOpen.triggered.connect(self.open_file_dialog)
        self.ui.actionSnap_to_selected.triggered.connect(lambda: tree_helper.focus_on_selected_node(self))
        self.ui.actionSave.triggered.connect(self.save_opened_file)
        self.ui.actionSave_As.triggered.connect(self.save_as_new_file)
        self.ui.actionClose.triggered.connect(self.close_opened_file)
        self.ui.actionFind.triggered.connect(self.open_find_dialog)
        self.ui.actionExit.triggered.connect(self.close)
        #cannot be set in designer because it closes the window
        self.ui.actionExit.setShortcut(QKeySequence("Alt+F4"))
        self.ui.actionAbout.triggered.connect(self.open_about_dialog)
        self.ui.actionGamebanana.triggered.connect(lambda: QDesktopServices.openUrl(QUrl("https://gamebanana.com/tools/22886")))
        self.ui.gameViewSettings.clicked.connect(self.open_settings_dialog)

        self.ui.newText.textChanged.connect(self.update_deser)
        self.ui.selected_expr.valueChanged.connect(self.update_expr)
        self.ui.expr_width.valueChanged.connect(self.update_expr_width)
        self.ui.expr_height.valueChanged.connect(self.update_expr_height)
        self.ui.expr_hp.valueChanged.connect(self.update_expr_hp)
        self.ui.expr_vp.valueChanged.connect(self.update_expr_vp)
        self.ui.start_expr.currentIndexChanged.connect(self.update_start_state)
        self.ui.middle_expr.currentIndexChanged.connect(self.update_middle_state)
        self.ui.end_expr.currentIndexChanged.connect(self.update_end_state)
        self.ui.expr_color.clicked.connect(self.choose_expr_color)
        self.ui.expr_outline.clicked.connect(self.choose_expr_outline)

        self.ui.color_revert.clicked.connect(self.revert_expr_color)
        self.ui.outline_revert.clicked.connect(self.revert_expr_outline)
        self.ui.width_revert.clicked.connect(self.revert_expr_width)
        self.ui.height_revert.clicked.connect(self.revert_expr_height)
        self.ui.hp_revert.clicked.connect(self.revert_expr_hp)
        self.ui.vp_revert.clicked.connect(self.revert_expr_vp)
        self.ui.sel_expr_revert.clicked.connect(self.revert_expr_sel)
        self.ui.expr_phil_revert.clicked.connect(self.revert_expr_phil)
        sys.excepthook = self.exception_handler

#updaters
    def update_deser(self):
        if self.selected_message is not None:
            self.unsaved_changes = True
            self.deser.messages[self.selected_message].text = self.sender().toPlainText()
            color_helper.render_game_view(self)

    def update_expr(self, value):
        if self.selected_message is not None:
            self.unsaved_changes = True
            self.deser.messages[self.selected_message].exp_index = value
            for elem in self.can_lock:
                elem.blockSignals(True)
            tree_helper.update_expressions(self)
            for elem in self.can_lock:
                elem.blockSignals(False)
            color_helper.render_game_view(self)

    def update_expr_width(self, value):
        self.unsaved_changes = True
        self.deser.expressions[self.ui.selected_expr.value()].width = value
        color_helper.render_game_view(self)

    def update_expr_height(self, value):
        self.unsaved_changes = True
        self.deser.expressions[self.ui.selected_expr.value()].height = value
        color_helper.render_game_view(self)

    def update_expr_hp(self, value):
        self.unsaved_changes = True
        self.deser.expressions[self.ui.selected_expr.value()].horizontal_spacing = value
        color_helper.render_game_view(self)

    def update_expr_vp(self, value):
        self.unsaved_changes = True
        self.deser.expressions[self.ui.selected_expr.value()].vertical_spacing = value
        color_helper.render_game_view(self)

    def update_start_state(self, index):
        self.unsaved_changes = True
        self.deser.expressions[self.ui.selected_expr.value()].states[0] = index

    def update_middle_state(self, index):
        self.unsaved_changes = True
        self.deser.expressions[self.ui.selected_expr.value()].states[1] = index

    def update_end_state(self, index):
        self.unsaved_changes = True
        self.deser.expressions[self.ui.selected_expr.value()].states[0] = index

    def choose_expr_color(self):
        expr_color = color_helper.hexRgba_to_hexArgb(self.deser.expressions[self.ui.selected_expr.value()].color)
        color = QColorDialog.getColor(
            QColor(expr_color),
            None,
            "Choose a color",
            QColorDialog.ColorDialogOption.ShowAlphaChannel)
        color_helper.set_color(self, "color", self.ui.expr_color, color)
        self.unsaved_changes = True
        color_helper.render_game_view(self)

    def choose_expr_outline(self):
        expr_outline = color_helper.hexRgba_to_hexArgb(self.deser.expressions[self.ui.selected_expr.value()].outline)
        color = QColorDialog.getColor(
            QColor(expr_outline),
            None,
            "Choose an outline color",
            QColorDialog.ColorDialogOption.ShowAlphaChannel)
        color_helper.set_color(self, "outline", self.ui.expr_outline, color)
        self.unsaved_changes = True
        color_helper.render_game_view(self)

#reverters
    def revert_expr_sel(self):
        self.ui.selected_expr.setValue(self.orig_deser.messages[self.selected_message].exp_index)

    def revert_expr_color(self):
        exp_index = self.ui.selected_expr.value()
        self.deser.expressions[exp_index].color = self.orig_deser.expressions[exp_index].color
        color_helper.set_color(self, "color", self.ui.expr_color, QColor(color_helper.hexRgba_to_hexArgb(self.orig_deser.expressions[exp_index].color)))
        color_helper.render_game_view(self)

    def revert_expr_outline(self):
        exp_index = self.ui.selected_expr.value()
        self.deser.expressions[exp_index].outline = self.orig_deser.expressions[exp_index].outline
        color_helper.set_color(self, "outline", self.ui.expr_outline, QColor(color_helper.hexRgba_to_hexArgb(self.orig_deser.expressions[exp_index].outline)))
        color_helper.render_game_view(self)

    def revert_expr_width(self):
        self.ui.expr_width.setValue(self.orig_deser.expressions[self.ui.selected_expr.value()].width)

    def revert_expr_height(self):
        self.ui.expr_height.setValue(self.orig_deser.expressions[self.ui.selected_expr.value()].height)

    def revert_expr_hp(self):
        self.ui.expr_hp.setValue(self.orig_deser.expressions[self.ui.selected_expr.value()].horizontal_spacing)

    def revert_expr_vp(self):
        self.ui.expr_vp.setValue(self.orig_deser.expressions[self.ui.selected_expr.value()].vertical_spacing)

    def revert_expr_phil(self):
        self.ui.start_expr.setCurrentIndex(self.orig_deser.expressions[self.ui.selected_expr.value()].states[0])
        self.ui.middle_expr.setCurrentIndex(self.orig_deser.expressions[self.ui.selected_expr.value()].states[1])
        self.ui.end_expr.setCurrentIndex(self.orig_deser.expressions[self.ui.selected_expr.value()].states[2])

#--------------------------
#event handlers
#--------------------------

    #make all exceptions show up in a window
    def exception_handler(self, exctype, value, tb):
        if not exctype.__name__ == 'Warning':
            error_msg = f"{exctype.__name__}: {value}"
        else:
            error_msg = str(value)
        if QApplication.instance():
            QMessageBox.critical(self, 'An unexpected error has occured', error_msg)

    def dragEnterEvent(self, event):
           if event.mimeData().hasUrls() and len(event.mimeData().urls()) == 1:
               event.acceptProposedAction()
           else:
               event.ignore()

    def dropEvent(self, event):
        if len(event.mimeData().urls()) == 1:
            event.mimeData().urls()[0].toLocalFile()
            for url in event.mimeData().urls():
                filepath = str(url.toLocalFile())
                self.process_file(filepath)
            event.accept()
        event.ignore()

    def closeEvent(self, event):
        if self.close_opened_file():
            event.accept()
            app.quit()
        event.ignore()

#--------------------------
#things that directly interact with events - opening files, etc
#--------------------------

#deserialize and populate the ui
    def parse_file(self, file_path):
        _, extension = os.path.splitext(file_path)
        extension = extension.lower()
        with open(file_path, 'rb') as raw_mess:
            file_magic = raw_mess.read(8)
            if(file_magic == xmsg.MAGIC):
                raw_mess.seek(0)
                mess = raw_mess.read()
                mess = bytearray(mess)

                self.deser = xmsg.deserialize(mess)
                if len(self.deser.expressions) == 0:
                    raise AttributeError("Your file has no style data!")
                self.deser.messages = sorted(self.deser.messages, key=lambda m: m.type)
                self.orig_deser = copy.deepcopy(self.deser)
                self.file_type = ".bin"

                tree_helper.populate_xmsg(self)
                return True
            elif extension == ".xml":
                try:
                    self.deser = xmsg.deserialize_xml(file_path)
                except:
                    raise Warning("The XML is invalid and cannot be read.")
                if len(self.deser.expressions) == 0:
                    raise AttributeError("The XML has no style data.")
                self.deser.messages = sorted(self.deser.messages, key=lambda m: m.type)
                self.orig_deser = copy.deepcopy(self.deser)
                self.file_type = ".xml"

                tree_helper.populate_xmsg(self)
                return True
        return False

#deals with opening a new file, given a filepath
    def process_file(self, file_path):
        if file_path:
            last_folder = os.path.dirname(file_path)
            Settings.setValue("last_file_directory", last_folder)
            if self.unsaved_changes:
                reply = self.unsaved_changes_dialog()
                if reply == QMessageBox.StandardButton.Save:
                    self.save_opened_file()
                elif reply == QMessageBox.StandardButton.Cancel:
                    return

            if self.parse_file(file_path):
                self.file_path = file_path
                self.setWindowTitle(f"Wii Party Text Editor - {self.file_path}")
                for elem in self.needs_file:
                    elem.setEnabled(True)
            else:
                QMessageBox.warning(self, "Invalid file", f"The provided file ({file_path.removeprefix(last_folder + "/")}) either could not be opened or is not supported.")
        else:
            QMessageBox.warning(self, "Invalid filepath", "The directory is invalid or could not be opened.")

#dialogs
    def unsaved_changes_dialog(self):
        return (QMessageBox.question(
            self,
            "Closing",
            "Save changes?",
            QMessageBox.StandardButton.Save |
            QMessageBox.StandardButton.Discard |
            QMessageBox.StandardButton.Cancel,
            QMessageBox.StandardButton.Save
        ))

    def open_file_dialog(self):
        default_dir = os.path.expanduser("~")
        last_dir = Settings.value("last_file_directory", default_dir)
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open File",        # Window Title
            last_dir,                 # Default directory (empty means current)
            "All supported files (*.bin *.xml);;Wii Party Text (*.bin);;XML Files (*.xml);;All Files (*.*)"
        )

        if file_path:
            self.process_file(file_path)

    def open_find_dialog(self):
        text, ok_pressed = QInputDialog.getText(
            self, "Search", "Text to search for:"
                )
        if ok_pressed:
            #text is not empty
            if(text.strip()):
                tree_helper.populate_search_tree(self, text)

    def open_about_dialog(self):
        dialog = AboutDialog()
        dialog.exec()

    def open_settings_dialog(self):
        dialog = GameViewSettingsDialog()
        dialog.exec()
        self.ui.gameView.setBackground(Settings.value("imageIndex", type=int))
        color_helper.render_game_view(self)


    def save_opened_file(self):
        try:
            if(self.unsaved_changes):
                if(self.file_type == ".bin"):
                    self.unsaved_changes = False
                    xmsg.serialize(self.deser, self.file_path)
                elif (self.file_type == ".xml"):
                    self.unsaved_changes = False
                    xmsg.serialize_to_xml(self.deser, self.file_path)
            else:
                QMessageBox.information(self, "", "No changes have been made.")

        except AttributeError:
            #no file is opened
            pass

    def save_as_new_file(self):
        if(self.file_path):
            fileorder = "All supported files (*.bin *.xml);;Wii Party Text (*.bin);;XML Files (*.xml);;All Files (*.*)"
            filepath, _ = QFileDialog.getSaveFileName(
                self,
                "Save As",
                self.file_path,
                fileorder
            )
            if(filepath):
                _, extension = os.path.splitext(filepath)
                extension = extension.lower()
                self.unsaved_changes = False
                self.file_path = filepath
                self.file_type = extension
                if(extension == ".xml" or extension == ".xmsg"):
                    xmsg.serialize_to_xml(self.deser, self.file_path)
                else:
                    xmsg.serialize(self.deser, self.file_path)
                self.setWindowTitle(f"Wii Party Text Editor - {self.file_path}")

    def close_opened_file(self):
        try:
            if(self.unsaved_changes):
                reply = self.unsaved_changes_dialog()
                if reply == QMessageBox.StandardButton.Save:
                    self.save_opened_file()
                elif reply == QMessageBox.StandardButton.Cancel:
                    return False
            tree_helper.clear_all(self)
            self.orig_deser = xmsg.XMSG()
            self.deser = xmsg.XMSG()
        except AttributeError:
            #no file is opened
            pass
        for elem in self.needs_file:
            elem.setEnabled(False)
        return True

#--------------------------
#beginning of execution
#--------------------------

if __name__ == "__main__":
    try:
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('saulf.xmsgedit')
    except AttributeError:
        pass


    app = QApplication(sys.argv)

    icon = QIcon(":/icons/icon.ico")
    app.setWindowIcon(icon)
    app.setStyle("Fusion")
    widget = MainWindow()
    widget.setWindowIcon(icon)
    widget.show()
    sys.exit(app.exec())
