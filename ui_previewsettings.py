# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'previewsettings.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QSpinBox, QTabWidget, QVBoxLayout, QWidget)
import rc_xmsg_resources

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(581, 431)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_13 = QLabel(self.tab)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setTextFormat(Qt.TextFormat.MarkdownText)

        self.verticalLayout_2.addWidget(self.label_13)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.selBoxSize = QComboBox(self.tab)
        self.selBoxSize.addItem("")
        self.selBoxSize.addItem("")
        self.selBoxSize.addItem("")
        self.selBoxSize.addItem("")
        self.selBoxSize.addItem("")
        self.selBoxSize.addItem("")
        self.selBoxSize.setObjectName(u"selBoxSize")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.selBoxSize)


        self.verticalLayout_2.addLayout(self.formLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 10, -1, -1)
        self.customDimensions = QCheckBox(self.tab)
        self.customDimensions.setObjectName(u"customDimensions")

        self.horizontalLayout_3.addWidget(self.customDimensions)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)

        self.boxWidth = QSpinBox(self.tab)
        self.boxWidth.setObjectName(u"boxWidth")
        self.boxWidth.setMaximum(10000)

        self.horizontalLayout_3.addWidget(self.boxWidth)

        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_3.addWidget(self.label_10)

        self.boxHeight = QSpinBox(self.tab)
        self.boxHeight.setObjectName(u"boxHeight")
        self.boxHeight.setMaximum(10000)

        self.horizontalLayout_3.addWidget(self.boxHeight)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_11)

        self.boxColor = QComboBox(self.tab)
        self.boxColor.addItem("")
        self.boxColor.addItem("")
        self.boxColor.addItem("")
        self.boxColor.addItem("")
        self.boxColor.setObjectName(u"boxColor")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.boxColor)


        self.verticalLayout_2.addLayout(self.formLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.transluscentBox = QCheckBox(self.tab)
        self.transluscentBox.setObjectName(u"transluscentBox")

        self.horizontalLayout_4.addWidget(self.transluscentBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.label_12 = QLabel(self.tab)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_4.addWidget(self.label_12)

        self.boxAlpha = QSpinBox(self.tab)
        self.boxAlpha.setObjectName(u"boxAlpha")
        self.boxAlpha.setMaximum(255)

        self.horizontalLayout_4.addWidget(self.boxAlpha)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.label_14 = QLabel(self.tab)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setTextFormat(Qt.TextFormat.MarkdownText)

        self.verticalLayout_2.addWidget(self.label_14)

        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_2.addWidget(self.label_9)

        self.selBackground = QComboBox(self.tab)
        icon = QIcon()
        icon.addFile(u":/backgrounds/menu-pink.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.selBackground.addItem(icon, "")
        icon1 = QIcon()
        icon1.addFile(u":/backgrounds/menu-blue.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.selBackground.addItem(icon1, "")
        icon2 = QIcon()
        icon2.addFile(u":/backgrounds/menu-yellow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.selBackground.addItem(icon2, "")
        icon3 = QIcon()
        icon3.addFile(u":/backgrounds/board-game-island.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.selBackground.addItem(icon3, "")
        icon4 = QIcon()
        icon4.addFile(u":/backgrounds/balance-boat.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.selBackground.addItem(icon4, "")
        self.selBackground.setObjectName(u"selBackground")

        self.verticalLayout_2.addWidget(self.selBackground)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.renderAlpha = QCheckBox(self.tab)
        self.renderAlpha.setObjectName(u"renderAlpha")

        self.horizontalLayout_2.addWidget(self.renderAlpha)

        self.renderOutline = QCheckBox(self.tab)
        self.renderOutline.setObjectName(u"renderOutline")
        self.renderOutline.setChecked(False)
        self.renderOutline.setAutoRepeat(False)

        self.horizontalLayout_2.addWidget(self.renderOutline)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout = QHBoxLayout(self.tab_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.placeholder0 = QLineEdit(self.tab_2)
        self.placeholder0.setObjectName(u"placeholder0")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.placeholder0)

        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label)

        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.placeholder1 = QLineEdit(self.tab_2)
        self.placeholder1.setObjectName(u"placeholder1")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.placeholder1)

        self.placeholder2 = QLineEdit(self.tab_2)
        self.placeholder2.setObjectName(u"placeholder2")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.placeholder2)

        self.placeholder3 = QLineEdit(self.tab_2)
        self.placeholder3.setObjectName(u"placeholder3")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.placeholder3)

        self.placeholder4 = QLineEdit(self.tab_2)
        self.placeholder4.setObjectName(u"placeholder4")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.placeholder4)

        self.placeholder5 = QLineEdit(self.tab_2)
        self.placeholder5.setObjectName(u"placeholder5")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.placeholder5)


        self.horizontalLayout.addLayout(self.formLayout)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Apply|QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.RestoreDefaults)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout.addWidget(self.buttonBox)

        QWidget.setTabOrder(self.tabWidget, self.selBoxSize)
        QWidget.setTabOrder(self.selBoxSize, self.customDimensions)
        QWidget.setTabOrder(self.customDimensions, self.boxWidth)
        QWidget.setTabOrder(self.boxWidth, self.boxHeight)
        QWidget.setTabOrder(self.boxHeight, self.boxColor)
        QWidget.setTabOrder(self.boxColor, self.transluscentBox)
        QWidget.setTabOrder(self.transluscentBox, self.boxAlpha)
        QWidget.setTabOrder(self.boxAlpha, self.selBackground)
        QWidget.setTabOrder(self.selBackground, self.renderAlpha)
        QWidget.setTabOrder(self.renderAlpha, self.renderOutline)
        QWidget.setTabOrder(self.renderOutline, self.placeholder0)
        QWidget.setTabOrder(self.placeholder0, self.placeholder1)
        QWidget.setTabOrder(self.placeholder1, self.placeholder2)
        QWidget.setTabOrder(self.placeholder2, self.placeholder3)
        QWidget.setTabOrder(self.placeholder3, self.placeholder4)
        QWidget.setTabOrder(self.placeholder4, self.placeholder5)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"### Textbox", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Textbox Size", None))
        self.selBoxSize.setItemText(0, QCoreApplication.translate("Dialog", u"Wide (2000x500)", None))
        self.selBoxSize.setItemText(1, QCoreApplication.translate("Dialog", u"Narrow (1440x500)", None))
        self.selBoxSize.setItemText(2, QCoreApplication.translate("Dialog", u"Game Guide (1100x800)", None))
        self.selBoxSize.setItemText(3, QCoreApplication.translate("Dialog", u"FC Question (1725x300)", None))
        self.selBoxSize.setItemText(4, QCoreApplication.translate("Dialog", u"One-line (850x200)", None))
        self.selBoxSize.setItemText(5, QCoreApplication.translate("Dialog", u"System (1700x800)", None))

        self.customDimensions.setText(QCoreApplication.translate("Dialog", u"Custom Dimensions", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Width", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Height", None))
        self.boxHeight.setPrefix("")
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Textbox Color", None))
        self.boxColor.setItemText(0, QCoreApplication.translate("Dialog", u"White", None))
        self.boxColor.setItemText(1, QCoreApplication.translate("Dialog", u"Pink", None))
        self.boxColor.setItemText(2, QCoreApplication.translate("Dialog", u"Dark Blue", None))
        self.boxColor.setItemText(3, QCoreApplication.translate("Dialog", u"Black", None))

        self.transluscentBox.setText(QCoreApplication.translate("Dialog", u"Transluscent Textbox", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Alpha", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"### Background", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Preview background", None))
        self.selBackground.setItemText(0, QCoreApplication.translate("Dialog", u"Menu (Pink)", None))
        self.selBackground.setItemText(1, QCoreApplication.translate("Dialog", u"Menu (Blue)", None))
        self.selBackground.setItemText(2, QCoreApplication.translate("Dialog", u"Menu (Yellow)", None))
        self.selBackground.setItemText(3, QCoreApplication.translate("Dialog", u"Board Game Island", None))
        self.selBackground.setItemText(4, QCoreApplication.translate("Dialog", u"Balance Boat", None))

#if QT_CONFIG(statustip)
        self.renderAlpha.setStatusTip(QCoreApplication.translate("Dialog", u"Testting", None))
#endif // QT_CONFIG(statustip)
        self.renderAlpha.setText(QCoreApplication.translate("Dialog", u"Render Text Alpha", None))
        self.renderOutline.setText(QCoreApplication.translate("Dialog", u"Render Text Outline", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"Textbox", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\\[0\\]", None))
        self.placeholder0.setText(QCoreApplication.translate("Dialog", u"\\[0\\]", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\\[1\\]", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\\[2\\]", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\\[3\\]", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\\[4\\]", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\\[5\\]", None))
        self.placeholder1.setText(QCoreApplication.translate("Dialog", u"\\[1\\]", None))
        self.placeholder2.setText(QCoreApplication.translate("Dialog", u"\\[2\\]", None))
        self.placeholder3.setText(QCoreApplication.translate("Dialog", u"\\[3\\]", None))
        self.placeholder4.setText(QCoreApplication.translate("Dialog", u"\\[4\\]", None))
        self.placeholder5.setText(QCoreApplication.translate("Dialog", u"\\[5\\]", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"Placeholders", None))
    # retranslateUi

