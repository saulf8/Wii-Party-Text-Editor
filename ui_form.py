# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QMainWindow, QMenu,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QTextBrowser,
    QToolButton, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

from ColorButton import ColorButton
from GameView import GameView
from MessageEditor import MessageEditor
import rc_xmsg_resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(775, 574)
        palette = QPalette()
        brush = QBrush(QColor(228, 20, 100, 200))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Highlight, brush)
        brush1 = QBrush(QColor(228, 20, 100, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Accent, brush1)
#endif
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Highlight, brush)
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Accent, brush1)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Accent, brush1)
#endif
        MainWindow.setPalette(palette)
        icon = QIcon()
        icon.addFile(u":/icons/icons/Icon.PNG", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentOpen))
        self.actionOpen.setIcon(icon1)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave))
        self.actionSave.setIcon(icon2)
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSaveAs))
        self.actionSave_As.setIcon(icon3)
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionRecent = QAction(MainWindow)
        self.actionRecent.setObjectName(u"actionRecent")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditClear))
        self.actionExit.setIcon(icon4)
        self.actionExit.setMenuRole(QAction.MenuRole.QuitRole)
        self.actionFind = QAction(MainWindow)
        self.actionFind.setObjectName(u"actionFind")
        self.actionSnap_to_selected = QAction(MainWindow)
        self.actionSnap_to_selected.setObjectName(u"actionSnap_to_selected")
        self.actionGamebanana = QAction(MainWindow)
        self.actionGamebanana.setObjectName(u"actionGamebanana")
        self.actionGamebanana.setMenuRole(QAction.MenuRole.AboutRole)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionAbout.setMenuRole(QAction.MenuRole.AboutRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 0, 5, 0)
        self.string_container = QScrollArea(self.centralwidget)
        self.string_container.setObjectName(u"string_container")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.string_container.sizePolicy().hasHeightForWidth())
        self.string_container.setSizePolicy(sizePolicy)
        self.string_container.setMinimumSize(QSize(150, 0))
        self.string_container.setMaximumSize(QSize(250, 16777215))
        self.string_container.setAcceptDrops(False)
        self.string_container.setAutoFillBackground(False)
        self.string_container.setFrameShape(QFrame.Shape.NoFrame)
        self.string_container.setFrameShadow(QFrame.Shadow.Plain)
        self.string_container.setLineWidth(0)
        self.string_container.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 167, 560))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLineWidth(0)

        self.verticalLayout_2.addWidget(self.label_2)

        self.searched = QTreeWidget(self.scrollAreaWidgetContents)
        self.searched.setObjectName(u"searched")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.searched.sizePolicy().hasHeightForWidth())
        self.searched.setSizePolicy(sizePolicy1)
        self.searched.setMinimumSize(QSize(0, 30))
        self.searched.setMaximumSize(QSize(16777215, 40))
        self.searched.setBaseSize(QSize(0, 0))
        self.searched.setFrameShape(QFrame.Shape.StyledPanel)
        self.searched.setFrameShadow(QFrame.Shadow.Sunken)
        self.searched.setLineWidth(0)

        self.verticalLayout_2.addWidget(self.searched)

        self.party = QTreeWidget(self.scrollAreaWidgetContents)
        self.party.setObjectName(u"party")
        self.party.setLineWidth(0)
        self.party.setIndentation(15)

        self.verticalLayout_2.addWidget(self.party)

        self.pair = QTreeWidget(self.scrollAreaWidgetContents)
        self.pair.setObjectName(u"pair")
        self.pair.setIndentation(15)

        self.verticalLayout_2.addWidget(self.pair)

        self.house = QTreeWidget(self.scrollAreaWidgetContents)
        self.house.setObjectName(u"house")
        self.house.setIndentation(15)

        self.verticalLayout_2.addWidget(self.house)

        self.minigames = QTreeWidget(self.scrollAreaWidgetContents)
        self.minigames.setObjectName(u"minigames")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.minigames.sizePolicy().hasHeightForWidth())
        self.minigames.setSizePolicy(sizePolicy2)
        self.minigames.setLineWidth(0)
        self.minigames.setIndentation(15)

        self.verticalLayout_2.addWidget(self.minigames)

        self.menu = QTreeWidget(self.scrollAreaWidgetContents)
        self.menu.setObjectName(u"menu")
        self.menu.setIndentation(15)

        self.verticalLayout_2.addWidget(self.menu)

        self.system = QTreeWidget(self.scrollAreaWidgetContents)
        self.system.setObjectName(u"system")
        self.system.setIndentation(15)

        self.verticalLayout_2.addWidget(self.system)

        self.string_container.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.string_container)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.newText = MessageEditor(self.centralwidget)
        self.newText.setObjectName(u"newText")
        sizePolicy1.setHeightForWidth(self.newText.sizePolicy().hasHeightForWidth())
        self.newText.setSizePolicy(sizePolicy1)
        self.newText.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.IBeamCursor))
        self.newText.setAcceptRichText(False)

        self.horizontalLayout_2.addWidget(self.newText)

        self.origText = QTextBrowser(self.centralwidget)
        self.origText.setObjectName(u"origText")
        sizePolicy1.setHeightForWidth(self.origText.sizePolicy().hasHeightForWidth())
        self.origText.setSizePolicy(sizePolicy1)
        self.origText.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.IBeamCursor))

        self.horizontalLayout_2.addWidget(self.origText)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 10, -1, -1)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.gameViewSettings = QPushButton(self.centralwidget)
        self.gameViewSettings.setObjectName(u"gameViewSettings")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentProperties))
        self.gameViewSettings.setIcon(icon5)

        self.horizontalLayout_6.addWidget(self.gameViewSettings)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.gameView = GameView(self.centralwidget)
        self.gameView.setObjectName(u"gameView")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.gameView.sizePolicy().hasHeightForWidth())
        self.gameView.setSizePolicy(sizePolicy3)
        self.gameView.setScaledContents(False)

        self.verticalLayout_4.addWidget(self.gameView)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout_3.setStretch(1, 3)
        self.verticalLayout_3.setStretch(3, 4)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.expressions = QFrame(self.centralwidget)
        self.expressions.setObjectName(u"expressions")
        sizePolicy.setHeightForWidth(self.expressions.sizePolicy().hasHeightForWidth())
        self.expressions.setSizePolicy(sizePolicy)
        self.expressions.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout = QVBoxLayout(self.expressions)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout.setContentsMargins(1, 0, -1, 1)
        self.horizontalGroupBox = QGroupBox(self.expressions)
        self.horizontalGroupBox.setObjectName(u"horizontalGroupBox")
        palette1 = QPalette()
        brush2 = QBrush(QColor(228, 20, 100, 150))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Highlight, brush2)
        self.horizontalGroupBox.setPalette(palette1)
        self.horizontalGroupBox.setFlat(False)
        self.horizontalGroupBox.setCheckable(False)
        self.exp_index = QHBoxLayout(self.horizontalGroupBox)
        self.exp_index.setSpacing(7)
        self.exp_index.setObjectName(u"exp_index")
        self.exp_index.setContentsMargins(5, 8, 5, -1)
        self.expressionLabel = QLabel(self.horizontalGroupBox)
        self.expressionLabel.setObjectName(u"expressionLabel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.expressionLabel.sizePolicy().hasHeightForWidth())
        self.expressionLabel.setSizePolicy(sizePolicy4)
        self.expressionLabel.setMinimumSize(QSize(0, 0))
        self.expressionLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.exp_index.addWidget(self.expressionLabel)

        self.selected_expr = QSpinBox(self.horizontalGroupBox)
        self.selected_expr.setObjectName(u"selected_expr")
        self.selected_expr.setFrame(True)
        self.selected_expr.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.selected_expr.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.selected_expr.setCorrectionMode(QAbstractSpinBox.CorrectionMode.CorrectToPreviousValue)
        self.selected_expr.setValue(0)
        self.selected_expr.setDisplayIntegerBase(10)

        self.exp_index.addWidget(self.selected_expr)

        self.num_expressions = QLabel(self.horizontalGroupBox)
        self.num_expressions.setObjectName(u"num_expressions")
        sizePolicy4.setHeightForWidth(self.num_expressions.sizePolicy().hasHeightForWidth())
        self.num_expressions.setSizePolicy(sizePolicy4)
        self.num_expressions.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.exp_index.addWidget(self.num_expressions)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.exp_index.addItem(self.horizontalSpacer)

        self.sel_expr_revert = QPushButton(self.horizontalGroupBox)
        self.sel_expr_revert.setObjectName(u"sel_expr_revert")
        self.sel_expr_revert.setMaximumSize(QSize(20, 16777215))
        icon6 = QIcon(QIcon.fromTheme(u"document-revert"))
        self.sel_expr_revert.setIcon(icon6)

        self.exp_index.addWidget(self.sel_expr_revert)


        self.verticalLayout.addWidget(self.horizontalGroupBox)

        self.fields = QGroupBox(self.expressions)
        self.fields.setObjectName(u"fields")
        self.fields.setMinimumSize(QSize(0, 0))
        self.fields.setMaximumSize(QSize(200, 16777215))
        self.gridLayout = QGridLayout(self.fields)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.gridLayout.setContentsMargins(5, -1, 5, -1)
        self.label_11 = QLabel(self.fields)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 9, 0, 1, 1)

        self.label_5 = QLabel(self.fields)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_7 = QLabel(self.fields)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)

        self.expr_vp = QSpinBox(self.fields)
        self.expr_vp.setObjectName(u"expr_vp")
        self.expr_vp.setStyleSheet(u"QSpinBox {\n"
"        padding-top: 0px;\n"
"        padding-bottom: 0px;\n"
"        margin-top: 0px;\n"
"        margin-bottom: 0px;\n"
"    }")
        self.expr_vp.setMaximum(255)

        self.gridLayout.addWidget(self.expr_vp, 9, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.height_revert = QPushButton(self.fields)
        self.height_revert.setObjectName(u"height_revert")
        self.height_revert.setMaximumSize(QSize(20, 16777215))
        self.height_revert.setIcon(icon6)

        self.gridLayout.addWidget(self.height_revert, 6, 4, 1, 1)

        self.outline_revert = QPushButton(self.fields)
        self.outline_revert.setObjectName(u"outline_revert")
        self.outline_revert.setMaximumSize(QSize(20, 16777215))
        self.outline_revert.setIcon(icon6)

        self.gridLayout.addWidget(self.outline_revert, 3, 4, 1, 1)

        self.expr_height = QSpinBox(self.fields)
        self.expr_height.setObjectName(u"expr_height")
        self.expr_height.setStyleSheet(u"QSpinBox {\n"
"        padding-top: 0px;\n"
"        padding-bottom: 0px;\n"
"        margin-top: 0px;\n"
"        margin-bottom: 0px;\n"
"    }")
        self.expr_height.setMaximum(255)

        self.gridLayout.addWidget(self.expr_height, 6, 1, 1, 1)

        self.expr_hp = QSpinBox(self.fields)
        self.expr_hp.setObjectName(u"expr_hp")
        self.expr_hp.setStyleSheet(u"QSpinBox {\n"
"        padding-top: 0px;\n"
"        padding-bottom: 0px;\n"
"        margin-top: 0px;\n"
"        margin-bottom: 0px;\n"
"    }")
        self.expr_hp.setMaximum(255)

        self.gridLayout.addWidget(self.expr_hp, 8, 1, 1, 1)

        self.expr_width = QSpinBox(self.fields)
        self.expr_width.setObjectName(u"expr_width")
        self.expr_width.setStyleSheet(u"QSpinBox {\n"
"        padding-top: 0px;\n"
"        padding-bottom: 0px;\n"
"        margin-top: 0px;\n"
"        margin-bottom: 0px;\n"
"    }")
        self.expr_width.setMaximum(255)

        self.gridLayout.addWidget(self.expr_width, 5, 1, 1, 1)

        self.label_8 = QLabel(self.fields)
        self.label_8.setObjectName(u"label_8")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy5)
        self.label_8.setFrameShape(QFrame.Shape.NoFrame)
        self.label_8.setTextFormat(Qt.TextFormat.MarkdownText)

        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)

        self.color_revert = QPushButton(self.fields)
        self.color_revert.setObjectName(u"color_revert")
        self.color_revert.setMaximumSize(QSize(20, 16777215))
        self.color_revert.setIcon(icon6)

        self.gridLayout.addWidget(self.color_revert, 2, 4, 1, 1)

        self.width_revert = QPushButton(self.fields)
        self.width_revert.setObjectName(u"width_revert")
        self.width_revert.setMaximumSize(QSize(20, 16777215))
        self.width_revert.setIcon(icon6)

        self.gridLayout.addWidget(self.width_revert, 5, 4, 1, 1)

        self.label_9 = QLabel(self.fields)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)

        self.expr_color = ColorButton(self.fields)
        self.expr_color.setObjectName(u"expr_color")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.expr_color.sizePolicy().hasHeightForWidth())
        self.expr_color.setSizePolicy(sizePolicy6)
        self.expr_color.setMinimumSize(QSize(120, 0))
        self.expr_color.setMaximumSize(QSize(120, 16777215))
        self.expr_color.setBaseSize(QSize(0, 0))
        self.expr_color.setCheckable(False)
        self.expr_color.setChecked(False)
        self.expr_color.setAutoRepeat(False)
        self.expr_color.setAutoDefault(False)

        self.gridLayout.addWidget(self.expr_color, 2, 1, 1, 1)

        self.label_6 = QLabel(self.fields)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_13 = QLabel(self.fields)
        self.label_13.setObjectName(u"label_13")
        sizePolicy5.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy5)
        self.label_13.setTextFormat(Qt.TextFormat.MarkdownText)

        self.gridLayout.addWidget(self.label_13, 7, 0, 1, 1)

        self.hp_revert = QPushButton(self.fields)
        self.hp_revert.setObjectName(u"hp_revert")
        self.hp_revert.setMaximumSize(QSize(20, 16777215))
        self.hp_revert.setIcon(icon6)

        self.gridLayout.addWidget(self.hp_revert, 8, 4, 1, 1)

        self.label_12 = QLabel(self.fields)
        self.label_12.setObjectName(u"label_12")
        sizePolicy5.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy5)
        self.label_12.setFrameShape(QFrame.Shape.NoFrame)
        self.label_12.setFrameShadow(QFrame.Shadow.Plain)
        self.label_12.setTextFormat(Qt.TextFormat.MarkdownText)

        self.gridLayout.addWidget(self.label_12, 4, 0, 1, 1)

        self.label_10 = QLabel(self.fields)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 8, 0, 1, 1)

        self.expr_outline = ColorButton(self.fields)
        self.expr_outline.setObjectName(u"expr_outline")
        sizePolicy6.setHeightForWidth(self.expr_outline.sizePolicy().hasHeightForWidth())
        self.expr_outline.setSizePolicy(sizePolicy6)
        self.expr_outline.setMinimumSize(QSize(120, 0))
        self.expr_outline.setMaximumSize(QSize(120, 16777215))
        self.expr_outline.setBaseSize(QSize(0, 0))
        self.expr_outline.setCheckable(False)
        self.expr_outline.setChecked(False)

        self.gridLayout.addWidget(self.expr_outline, 3, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 3, 3, 1, 1)

        self.vp_revert = QToolButton(self.fields)
        self.vp_revert.setObjectName(u"vp_revert")
        self.vp_revert.setMaximumSize(QSize(20, 16777215))
        self.vp_revert.setIcon(icon6)

        self.gridLayout.addWidget(self.vp_revert, 9, 4, 1, 1)

        self.gridLayout.setRowStretch(0, 1)

        self.verticalLayout.addWidget(self.fields)

        self.states_2 = QGroupBox(self.expressions)
        self.states_2.setObjectName(u"states_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.states_2.sizePolicy().hasHeightForWidth())
        self.states_2.setSizePolicy(sizePolicy7)
        self.states_2.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_8 = QVBoxLayout(self.states_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout_8.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.label_16 = QLabel(self.states_2)
        self.label_16.setObjectName(u"label_16")
        sizePolicy5.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy5)
        self.label_16.setTextFormat(Qt.TextFormat.MarkdownText)

        self.horizontalLayout_5.addWidget(self.label_16)

        self.horizontalSpacer_4 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.expr_phil_revert = QPushButton(self.states_2)
        self.expr_phil_revert.setObjectName(u"expr_phil_revert")
        self.expr_phil_revert.setMaximumSize(QSize(20, 16777215))
        self.expr_phil_revert.setIcon(icon6)

        self.horizontalLayout_5.addWidget(self.expr_phil_revert)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.start_expr = QComboBox(self.states_2)
        icon7 = QIcon()
        icon7.addFile(u":/icons/Talking/Neutral.PNG", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.start_expr.addItem(icon7, "")
        icon8 = QIcon()
        icon8.addFile(u":/icons/Start\u2044End/Laughing.PNG", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.start_expr.addItem(icon8, "")
        icon9 = QIcon()
        icon9.addFile(u":/icons/Start\u2044End/Startled.PNG", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.start_expr.addItem(icon9, "")
        icon10 = QIcon()
        icon10.addFile(u":/icons/Start\u2044End/Crying.PNG", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.start_expr.addItem(icon10, "")
        icon11 = QIcon()
        icon11.addFile(u":/icons/Start\u2044End/Excited.PNG", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.start_expr.addItem(icon11, "")
        icon12 = QIcon()
        icon12.addFile(u":/icons/Start\u2044End/Clapping.PNG", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.start_expr.addItem(icon12, "")
        self.start_expr.setObjectName(u"start_expr")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.start_expr.sizePolicy().hasHeightForWidth())
        self.start_expr.setSizePolicy(sizePolicy8)
        self.start_expr.setMinimumSize(QSize(28, 60))
        self.start_expr.setEditable(False)
        self.start_expr.setMaxVisibleItems(10)
        self.start_expr.setMaxCount(6)
        self.start_expr.setIconSize(QSize(40, 64))

        self.horizontalLayout_3.addWidget(self.start_expr)

        self.label_15 = QLabel(self.states_2)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_3.addWidget(self.label_15)

        self.middle_expr = QComboBox(self.states_2)
        self.middle_expr.addItem(icon7, "")
        icon13 = QIcon()
        icon13.addFile(u":/icons/Talking/Happy.PNG", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.middle_expr.addItem(icon13, "")
        icon14 = QIcon()
        icon14.addFile(u":/icons/Talking/Surprised.PNG", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.middle_expr.addItem(icon14, "")
        icon15 = QIcon()
        icon15.addFile(u":/icons/Talking/Sad.PNG", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.middle_expr.addItem(icon15, "")
        icon16 = QIcon()
        icon16.addFile(u":/icons/Talking/Angry.PNG", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.middle_expr.addItem(icon16, "")
        icon17 = QIcon()
        icon17.addFile(u":/icons/Talking/Threatening.PNG", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.middle_expr.addItem(icon17, "")
        self.middle_expr.setObjectName(u"middle_expr")
        sizePolicy8.setHeightForWidth(self.middle_expr.sizePolicy().hasHeightForWidth())
        self.middle_expr.setSizePolicy(sizePolicy8)
        self.middle_expr.setMinimumSize(QSize(28, 60))
        self.middle_expr.setIconSize(QSize(40, 64))

        self.horizontalLayout_3.addWidget(self.middle_expr)

        self.label_14 = QLabel(self.states_2)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_3.addWidget(self.label_14)

        self.end_expr = QComboBox(self.states_2)
        self.end_expr.addItem(icon7, "")
        self.end_expr.addItem(icon8, "")
        self.end_expr.addItem(icon9, "")
        self.end_expr.addItem(icon10, "")
        self.end_expr.addItem(icon11, "")
        self.end_expr.addItem(icon12, "")
        self.end_expr.setObjectName(u"end_expr")
        sizePolicy8.setHeightForWidth(self.end_expr.sizePolicy().hasHeightForWidth())
        self.end_expr.setSizePolicy(sizePolicy8)
        self.end_expr.setMinimumSize(QSize(28, 60))
        self.end_expr.setIconSize(QSize(40, 64))

        self.horizontalLayout_3.addWidget(self.end_expr)


        self.verticalLayout_8.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.states_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.expressions)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 775, 25))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.label_2.setBuddy(self.expressions)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.minigames, self.string_container)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionGamebanana)
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addAction(self.actionSnap_to_selected)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Wii Party Text Editor", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open...", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As...", None))
#if QT_CONFIG(shortcut)
        self.actionSave_As.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionRecent.setText(QCoreApplication.translate("MainWindow", u"Recent Files", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionFind.setText(QCoreApplication.translate("MainWindow", u"Find", None))
#if QT_CONFIG(shortcut)
        self.actionFind.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+F", None))
#endif // QT_CONFIG(shortcut)
        self.actionSnap_to_selected.setText(QCoreApplication.translate("MainWindow", u"Reveal Selection", None))
#if QT_CONFIG(shortcut)
        self.actionSnap_to_selected.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+G", None))
#endif // QT_CONFIG(shortcut)
        self.actionGamebanana.setText(QCoreApplication.translate("MainWindow", u"Gamebanana", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Strings", None))
        ___qtreewidgetitem = self.searched.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Search Results", None))
        ___qtreewidgetitem1 = self.party.headerItem()
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Party Games", None))
        ___qtreewidgetitem2 = self.pair.headerItem()
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"Pair Games", None))
        ___qtreewidgetitem3 = self.house.headerItem()
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"House Party", None))
        ___qtreewidgetitem4 = self.minigames.headerItem()
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"Minigames", None))
        ___qtreewidgetitem5 = self.menu.headerItem()
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u" Menu / UI", None))
        ___qtreewidgetitem6 = self.system.headerItem()
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"System", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Edit:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Original:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Game view", None))
        self.gameViewSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.gameView.setText(QCoreApplication.translate("MainWindow", u"Game view", None))
        self.horizontalGroupBox.setTitle("")
        self.expressionLabel.setText(QCoreApplication.translate("MainWindow", u"Style", None))
        self.selected_expr.setPrefix("")
        self.num_expressions.setText("")
        self.sel_expr_revert.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Vertical", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Text Color", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.height_revert.setText("")
        self.outline_revert.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"**Formatting**", None))
        self.color_revert.setText("")
        self.width_revert.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.expr_color.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Outline Color", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"**Letter Spacing**", None))
        self.hp_revert.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"**Dimensions**", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Horizontal", None))
        self.expr_outline.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.vp_revert.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"**Expressions**", None))
        self.expr_phil_revert.setText("")
        self.start_expr.setItemText(0, "")
        self.start_expr.setItemText(1, "")
        self.start_expr.setItemText(2, "")
        self.start_expr.setItemText(3, "")
        self.start_expr.setItemText(4, "")
        self.start_expr.setItemText(5, "")

        self.start_expr.setCurrentText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
        self.middle_expr.setItemText(0, "")
        self.middle_expr.setItemText(1, "")
        self.middle_expr.setItemText(2, "")
        self.middle_expr.setItemText(3, "")
        self.middle_expr.setItemText(4, "")
        self.middle_expr.setItemText(5, "")

        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
        self.end_expr.setItemText(0, "")
        self.end_expr.setItemText(1, "")
        self.end_expr.setItemText(2, "")
        self.end_expr.setItemText(3, "")
        self.end_expr.setItemText(4, "")
        self.end_expr.setItemText(5, "")

        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi

