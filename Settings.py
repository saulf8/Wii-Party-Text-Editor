# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtCore import Qt
from PySide6.QtCore import QSettings
from ui_previewsettings import Ui_Dialog

def init_settings(keys):
    for key in keys:
        if not Settings.contains(key):
            Settings.setValue(key, default_value(key))


def default_value(key):
    default = {
        "placeholders": [r"\[0\]", r"\[1\]", r"\[2\]", r"\[3\]", r"\[4\]", r"\[5\]"],
        "renderAlpha": True,
        "renderOutline": True,
        "transluscentBox": True,
        "customDimensions": False,
        "boxWidth": 0,
        "boxHeight": 0,
        "boxAlpha": 200,
        "boxSizeIndex": 0,
        "boxColorIndex": 0,
        "imageIndex": 0
    }
    if key in default:
        return default[key]
    return False

def box_sizes(key):
    sizes = {
        0: (2000, 500), #wide party phil
        1: (1440, 500), #narrow party phil
        2: (1100, 800), #game guide
        3: (1725, 300), #friend connection question
        4: (850, 200), #one-line text: fc answer, word bomb themes, etc.
        5: (1700, 800) #system
    }
    if key in sizes:
        return sizes[key]
    return False

def bg_images(key):
    images = {
        0: "menu-pink",
        1: "menu-blue",
        2: "menu-yellow",
        3: "board-game-island",
        4: "balance-boat"
    }
    if key in images:
        return images[key]
    return False

def box_color(key):
    colors = {
        0: "ffffff",
        1: "fd35d8",
        2: "23243d",
        3: "000000"

    }
    if key in colors:
        return colors[key]
    return False

Settings = QSettings("Saulf", "XMSG Editor")
SettingsKeys = ["placeholders", "renderAlpha", "renderOutline", "transluscentBox", "customDimensions", "boxWidth",
    "boxHeight", "boxAlpha", "boxSizeIndex", "boxColorIndex", "imageIndex"]
init_settings(SettingsKeys)

class GameViewSettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Settings")

        self.newSettings = {}

        self.ui.buttonBox.button(QDialogButtonBox.Apply).setDefault(True)
        self.ui.buttonBox.button(QDialogButtonBox.Apply).setFocus()

        placeholders = Settings.value("placeholders")
        self.ui.placeholder0.setText(placeholders[0])
        self.ui.placeholder1.setText(placeholders[1])
        self.ui.placeholder2.setText(placeholders[2])
        self.ui.placeholder3.setText(placeholders[3])
        self.ui.placeholder4.setText(placeholders[4])
        self.ui.placeholder5.setText(placeholders[5])

        self.ui.renderAlpha.setChecked(Settings.value("renderAlpha", defaultValue=False, type=bool))
        self.ui.renderOutline.setChecked(Settings.value("renderOutline", defaultValue=False, type=bool))
        customDimensions = Settings.value("customDimensions", defaultValue=False, type=bool)
        self.ui.customDimensions.setChecked(customDimensions)
        transluscentBox = Settings.value("transluscentBox", defaultValue=True, type=bool)
        self.ui.transluscentBox.setChecked(transluscentBox)
        self.ui.boxWidth.setEnabled(customDimensions)
        self.ui.boxHeight.setEnabled(customDimensions)
        self.ui.selBoxSize.setEnabled(not customDimensions)
        self.ui.boxAlpha.setEnabled(transluscentBox)
        self.ui.boxWidth.setValue(Settings.value("boxWidth", type=int))
        self.ui.boxHeight.setValue(Settings.value("boxHeight", type=int))
        self.ui.boxAlpha.setValue(Settings.value("boxAlpha", type=int))
        self.ui.selBoxSize.setCurrentIndex(Settings.value("boxSizeIndex", type=int))
        self.ui.selBackground.setCurrentIndex(Settings.value("imageIndex", type=int))
        self.ui.boxColor.setCurrentIndex(Settings.value("boxColorIndex", type=int))

        self.ui.placeholder0.textChanged.connect(lambda t: self.updatePlaceholder(0, t))
        self.ui.placeholder1.textChanged.connect(lambda t: self.updatePlaceholder(1, t))
        self.ui.placeholder2.textChanged.connect(lambda t: self.updatePlaceholder(2, t))
        self.ui.placeholder3.textChanged.connect(lambda t: self.updatePlaceholder(3, t))
        self.ui.placeholder4.textChanged.connect(lambda t: self.updatePlaceholder(4, t))
        self.ui.placeholder5.textChanged.connect(lambda t: self.updatePlaceholder(5, t))
        self.ui.renderAlpha.checkStateChanged.connect(lambda s: self.setSettings("renderAlpha", s == Qt.Checked))
        self.ui.renderOutline.checkStateChanged.connect(lambda s: self.setSettings("renderOutline", s == Qt.Checked))
        self.ui.customDimensions.checkStateChanged.connect(self.update_custom_dim)
        self.ui.boxWidth.valueChanged.connect(lambda v: self.setSettings("boxWidth", v))
        self.ui.boxHeight.valueChanged.connect(lambda v: self.setSettings("boxHeight", v))
        self.ui.selBoxSize.currentIndexChanged.connect(lambda i: self.setSettings("boxSizeIndex", i))
        self.ui.selBackground.currentIndexChanged.connect(lambda i: self.setSettings("imageIndex", i))
        self.ui.boxAlpha.valueChanged.connect(lambda v: self.setSettings("boxAlpha", v))
        self.ui.transluscentBox.checkStateChanged.connect(self.update_boxTransluscent)
        self.ui.boxColor.currentIndexChanged.connect(lambda i: self.setSettings("boxColorIndex", i))

        self.ui.buttonBox.clicked.connect(self.on_clicked)

    def setSettings(self, key, value):
        self.newSettings[key] = value

    def on_clicked(self, button):
        standard = self.ui.buttonBox.standardButton(button)
        if standard == QDialogButtonBox.Apply:
            for key in self.newSettings:
                Settings.setValue(key, self.newSettings[key])
            self.accept()
        elif standard == QDialogButtonBox.RestoreDefaults:
            self.ui.placeholder0.setText(default_value("placeholders")[0])
            self.ui.placeholder1.setText(default_value("placeholders")[1])
            self.ui.placeholder2.setText(default_value("placeholders")[2])
            self.ui.placeholder3.setText(default_value("placeholders")[3])
            self.ui.placeholder4.setText(default_value("placeholders")[4])
            self.ui.placeholder5.setText(default_value("placeholders")[5])

            self.ui.renderAlpha.setChecked(default_value("renderAlpha"))
            self.ui.renderOutline.setChecked(default_value("renderOutline"))
            self.ui.customDimensions.setChecked(default_value("customDimensions"))
            self.ui.transluscentBox.setChecked(default_value("transluscentBox"))
            self.ui.boxWidth.setValue(default_value("boxWidth"))
            self.ui.boxHeight.setValue(default_value("boxHeight"))
            self.ui.boxAlpha.setValue(default_value("boxAlpha"))
            self.ui.selBoxSize.setCurrentIndex(default_value("boxSizeIndex"))
            self.ui.selBackground.setCurrentIndex(default_value("imageIndex"))
            self.ui.boxColor.setCurrentIndex(default_value("boxColorIndex"))



    def updatePlaceholder(self, index, text):
        placeholders = Settings.value("placeholders") if not "placeholders" in self.newSettings else self.newSettings["placeholders"]
        placeholders[index] = text
        self.newSettings["placeholders"] = placeholders

    def update_custom_dim(self, s):
        customDimensions = s == Qt.Checked
        self.setSettings("customDimensions", customDimensions)
        self.ui.boxWidth.setEnabled(customDimensions)
        self.ui.boxHeight.setEnabled(customDimensions)
        self.ui.selBoxSize.setEnabled(not customDimensions)

    def update_boxTransluscent(self, s):
        transluscentBox = s == Qt.Checked
        self.setSettings("transluscentBox", transluscentBox)
        self.ui.boxAlpha.setEnabled(transluscentBox)


