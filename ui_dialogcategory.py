# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\mokan\OneDrive\Softwares\LabelU\UI\dialogcategory.ui',
# licensing of 'C:\Users\mokan\OneDrive\Softwares\LabelU\UI\dialogcategory.ui' applies.
#
# Created: Thu Aug 22 21:31:33 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Signal, Slot
import imagesources_rc
from graphics import SceneMode
import sys

class Ui_DialogCategory(object):
    def setupUi(self, DialogCategory):
        DialogCategory.setObjectName("DialogCategory")
        DialogCategory.resize(365, 300)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/Small/icon100_com_194.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogCategory.setWindowIcon(icon)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogCategory.sizePolicy().hasHeightForWidth())
        DialogCategory.setSizePolicy(sizePolicy)
        self.splitter = QtWidgets.QSplitter(DialogCategory)
        self.splitter.setGeometry(QtCore.QRect(20, 30, 231, 74))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_category = QtWidgets.QLabel(self.layoutWidget)
        self.label_category.setObjectName("label_category")
        self.gridLayout.addWidget(self.label_category, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_value = QtWidgets.QLabel(self.layoutWidget)
        self.label_value.setObjectName("label_value")
        self.gridLayout.addWidget(self.label_value, 1, 0, 1, 1)
        self.spinBox_value = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_value.setMaximum(255)
        self.spinBox_value.setObjectName("spinBox_value")
        self.gridLayout.addWidget(self.spinBox_value, 1, 1, 1, 1)
        self.label_type = QtWidgets.QLabel(self.layoutWidget)
        self.label_type.setObjectName("label_type")
        self.gridLayout.addWidget(self.label_type, 2, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 2, 1, 1, 1)
        self.groupBox_color = QtWidgets.QGroupBox(DialogCategory)
        self.groupBox_color.setGeometry(QtCore.QRect(10, 110, 347, 147))
        self.groupBox_color.setObjectName("groupBox_color")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_color)
        self.groupBox.setGeometry(QtCore.QRect(200, 20, 121, 119))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.toolButton_red = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_red.setGeometry(QtCore.QRect(9, 15, 30, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/purecolor/icons/PureColor/red.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_red.setIcon(icon)
        self.toolButton_red.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_red.setObjectName("toolButton_red")
        self.toolButton_blue = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_blue.setGeometry(QtCore.QRect(46, 15, 30, 30))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/purecolor/icons/PureColor/blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_blue.setIcon(icon1)
        self.toolButton_blue.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_blue.setAutoRepeatDelay(0)
        self.toolButton_blue.setAutoRepeatInterval(0)
        self.toolButton_blue.setObjectName("toolButton_blue")
        self.toolButton_green = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_green.setGeometry(QtCore.QRect(82, 15, 30, 30))
        self.toolButton_green.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/purecolor/icons/PureColor/green.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_green.setIcon(icon2)
        self.toolButton_green.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_green.setObjectName("toolButton_green")
        self.toolButton_megenta = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_megenta.setGeometry(QtCore.QRect(46, 50, 30, 30))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/purecolor/icons/PureColor/magenta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_megenta.setIcon(icon3)
        self.toolButton_megenta.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_megenta.setAutoRepeatDelay(0)
        self.toolButton_megenta.setAutoRepeatInterval(0)
        self.toolButton_megenta.setObjectName("toolButton_megenta")
        self.toolButton_yellow = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_yellow.setGeometry(QtCore.QRect(82, 50, 30, 30))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/purecolor/icons/PureColor/yellow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_yellow.setIcon(icon4)
        self.toolButton_yellow.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_yellow.setObjectName("toolButton_yellow")
        self.toolButton_cyan = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_cyan.setGeometry(QtCore.QRect(10, 50, 30, 30))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/purecolor/icons/PureColor/cyan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_cyan.setIcon(icon5)
        self.toolButton_cyan.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_cyan.setObjectName("toolButton_cyan")
        self.toolButton_black = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_black.setGeometry(QtCore.QRect(10, 85, 30, 30))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/purecolor/icons/PureColor/black.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_black.setIcon(icon6)
        self.toolButton_black.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_black.setObjectName("toolButton_black")
        self.toolButton_white = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_white.setGeometry(QtCore.QRect(46, 85, 30, 30))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/purecolor/icons/PureColor/white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_white.setIcon(icon7)
        self.toolButton_white.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_white.setObjectName("toolButton_white")
        self.toolButton_grey = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_grey.setGeometry(QtCore.QRect(82, 85, 30, 30))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/purecolor/icons/PureColor/grey.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_grey.setIcon(icon8)
        self.toolButton_grey.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_grey.setObjectName("toolButton_grey")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_color)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 20, 151, 119))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layoutWidget1.sizePolicy().hasHeightForWidth())
        self.layoutWidget1.setSizePolicy(sizePolicy)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_red = QtWidgets.QLabel(self.layoutWidget1)
        self.label_red.setAlignment(QtCore.Qt.AlignCenter)
        self.label_red.setObjectName("label_red")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_red)
        self.spinBox_red = QtWidgets.QSpinBox(self.layoutWidget1)
        self.spinBox_red.setMaximum(255)
        self.spinBox_red.setObjectName("spinBox_red")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox_red)
        self.label_green = QtWidgets.QLabel(self.layoutWidget1)
        self.label_green.setAlignment(QtCore.Qt.AlignCenter)
        self.label_green.setObjectName("label_green")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_green)
        self.spinBox_green = QtWidgets.QSpinBox(self.layoutWidget1)
        self.spinBox_green.setMaximum(255)
        self.spinBox_green.setObjectName("spinBox_green")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBox_green)
        self.label_blue = QtWidgets.QLabel(self.layoutWidget1)
        self.label_blue.setAlignment(QtCore.Qt.AlignCenter)
        self.label_blue.setObjectName("label_blue")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_blue)
        self.spinBox_blue = QtWidgets.QSpinBox(self.layoutWidget1)
        self.spinBox_blue.setMaximum(255)
        self.spinBox_blue.setObjectName("spinBox_blue")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBox_blue)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_advanced = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_advanced.setObjectName("pushButton_advanced")
        self.horizontalLayout.addWidget(self.pushButton_advanced)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_displaycolor = QtWidgets.QLabel(self.groupBox_color)
        self.label_displaycolor.setGeometry(QtCore.QRect(10, 24, 21, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_displaycolor.sizePolicy().hasHeightForWidth())
        self.label_displaycolor.setSizePolicy(sizePolicy)
        self.label_displaycolor.setAutoFillBackground(True)
        self.label_displaycolor.setLineWidth(2)
        self.label_displaycolor.setText("")
        self.label_displaycolor.setAlignment(QtCore.Qt.AlignCenter)
        self.label_displaycolor.setObjectName("label_displaycolor")
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogCategory)
        self.buttonBox.setGeometry(QtCore.QRect(30, 270, 321, 23))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.label_category.setBuddy(self.lineEdit)
        self.label_value.setBuddy(self.spinBox_value)
        self.label_type.setBuddy(self.comboBox)
        self.label_red.setBuddy(self.spinBox_red)
        self.label_green.setBuddy(self.spinBox_green)
        self.label_blue.setBuddy(self.spinBox_blue)

        self.retranslateUi(DialogCategory)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DialogCategory.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DialogCategory.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogCategory)

    def retranslateUi(self, DialogCategory):
        DialogCategory.setWindowTitle(QtWidgets.QApplication.translate("DialogCategory", "DialogCategory", None, -1))
        self.label_category.setText(QtWidgets.QApplication.translate("DialogCategory", "Category Name", None, -1))
        self.label_value.setText(QtWidgets.QApplication.translate("DialogCategory", "Value", None, -1))
        self.label_type.setText(QtWidgets.QApplication.translate("DialogCategory", "Annotation Type", None, -1))
        self.comboBox.setItemText(0, QtWidgets.QApplication.translate("DialogCategory", "Dot", None, -1))
        self.comboBox.setItemText(1, QtWidgets.QApplication.translate("DialogCategory", "DotSet", None, -1))
        self.comboBox.setItemText(2, QtWidgets.QApplication.translate("DialogCategory", "Polygon", None, -1))
        self.comboBox.setItemText(3, QtWidgets.QApplication.translate("DialogCategory", "Spline", None, -1))
        self.comboBox.setItemText(4, QtWidgets.QApplication.translate("DialogCategory", "Rectangle", None, -1))
        self.groupBox_color.setTitle(QtWidgets.QApplication.translate("DialogCategory", "Color", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("DialogCategory", "Classical", None, -1))
        self.toolButton_red.setText(QtWidgets.QApplication.translate("DialogCategory", "Red", None, -1))
        self.toolButton_blue.setText(QtWidgets.QApplication.translate("DialogCategory", "Blue", None, -1))
        self.toolButton_green.setText(QtWidgets.QApplication.translate("DialogCategory", "Green", None, -1))
        self.toolButton_megenta.setText(QtWidgets.QApplication.translate("DialogCategory", "magenta", None, -1))
        self.toolButton_yellow.setText(QtWidgets.QApplication.translate("DialogCategory", "yellow", None, -1))
        self.toolButton_cyan.setText(QtWidgets.QApplication.translate("DialogCategory", "cyan", None, -1))
        self.toolButton_black.setText(QtWidgets.QApplication.translate("DialogCategory", "black", None, -1))
        self.toolButton_white.setText(QtWidgets.QApplication.translate("DialogCategory", "white", None, -1))
        self.toolButton_grey.setText(QtWidgets.QApplication.translate("DialogCategory", "grey", None, -1))
        self.label_red.setText(QtWidgets.QApplication.translate("DialogCategory", "R", None, -1))
        self.label_green.setText(QtWidgets.QApplication.translate("DialogCategory", "G", None, -1))
        self.label_blue.setText(QtWidgets.QApplication.translate("DialogCategory", "B", None, -1))
        self.pushButton_advanced.setText(QtWidgets.QApplication.translate("DialogCategory", "&Advanced...", None, -1))



class CategoryDialog(QtWidgets.QDialog):

    SignalCategoryInfo = Signal(list)

    def __init__(self, parent:QtWidgets.QWidget=None):

        if parent is None:
            super(CategoryDialog, self).__init__()
        else:
            super(CategoryDialog, self).__init__(parent)

        self.ui = Ui_DialogCategory()
        self.ui.setupUi(self)
        self.dialogColor = QtWidgets.QColorDialog(self)
        self.colorCurrent = []

        self.ui.pushButton_advanced.clicked.connect(self.slot_open_dialogcolor)
        self.ui.toolButton_cyan.clicked.connect(self.slot_set_cyan)
        self.ui.toolButton_black.clicked.connect(self.slot_set_black)
        self.ui.toolButton_white.clicked.connect(self.slot_set_white)
        self.ui.toolButton_red.clicked.connect(self.slot_set_red)
        self.ui.toolButton_green.clicked.connect(self.slot_set_green)
        self.ui.toolButton_blue.clicked.connect(self.slot_set_blue)
        self.ui.toolButton_yellow.clicked.connect(self.slot_set_yellow)
        self.ui.toolButton_megenta.clicked.connect(self.slot_set_megenta)
        self.ui.toolButton_grey.clicked.connect(self.slot_set_grey)

    @Slot()
    def accept(self):

        self.SignalCategoryInfo.emit([self.ui.lineEdit.text(),
                                      self.ui.spinBox_value.value(),
                                      self.colorCurrent,
                                      self.ui.comboBox.currentText()])

        QtWidgets.QDialog.accept(self)

    @Slot()
    def slot_open_dialogcolor(self):

        dialogColor = QtWidgets.QColorDialog(self)
        dialogColor.setWindowTitle("Select color")
        dialogColor.setCurrentColor(QtGui.QColor(*self.colorCurrent))
        dialogColor.show()
        dialogColor.colorSelected.connect(self.slot_set_color)

    @Slot(QtGui.QColor)
    def slot_set_color(self, color:QtGui.QColor):

        self.colorCurrent = list(color.toTuple())
        red, green, blue, alpha = self.colorCurrent
        self.ui.spinBox_red.setValue(red)
        self.ui.spinBox_blue.setValue(blue)
        self.ui.spinBox_green.setValue(green)
        self.ui.label_displaycolor.setStyleSheet("background-color: rgba({r}, {g}, {b}, {a});".format(
            r=red, g=green, b=blue, a=alpha
        ))

    @Slot()
    def  slot_set_cyan(self):

        self.colorCurrent = [0, 255, 255, 255]
        red, green, blue, alpha = self.colorCurrent
        self.ui.spinBox_red.setValue(red)
        self.ui.spinBox_blue.setValue(blue)
        self.ui.spinBox_green.setValue(green)
        self.ui.label_displaycolor.setStyleSheet("background-color: rgba({r}, {g}, {b}, {a});".format(
            r=red, g=green, b=blue, a=alpha
        ))

    @Slot()
    def slot_set_black(self):

        self.colorCurrent = [0, 0, 0, 255]
        red, green, blue, alpha = self.colorCurrent
        self.ui.spinBox_red.setValue(red)
        self.ui.spinBox_blue.setValue(blue)
        self.ui.spinBox_green.setValue(green)
        self.ui.label_displaycolor.setStyleSheet("background-color: rgba({r}, {g}, {b}, {a});".format(
            r=red, g=green, b=blue, a=alpha
        ))

    @Slot()
    def slot_set_red(self):

        self.colorCurrent = [255, 0, 0, 255]
        red, green, blue, alpha = self.colorCurrent
        self.ui.spinBox_red.setValue(red)
        self.ui.spinBox_blue.setValue(blue)
        self.ui.spinBox_green.setValue(green)
        self.ui.label_displaycolor.setStyleSheet("background-color: rgba({r}, {g}, {b}, {a});".format(
            r=red, g=green, b=blue, a=alpha
        ))

    @Slot()
    def slot_set_green(self):

        self.colorCurrent = [0, 255, 0, 255]
        red, green, blue, alpha = self.colorCurrent
        self.ui.spinBox_red.setValue(red)
        self.ui.spinBox_blue.setValue(blue)
        self.ui.spinBox_green.setValue(green)
        self.ui.label_displaycolor.setStyleSheet("background-color: rgba({r}, {g}, {b}, {a});".format(
            r=red, g=green, b=blue, a=alpha
        ))


    @Slot()
    def slot_set_blue(self):

        self.colorCurrent = [0, 0, 255, 255]
        red, green, blue, alpha = self.colorCurrent
        self.ui.spinBox_red.setValue(red)
        self.ui.spinBox_blue.setValue(blue)
        self.ui.spinBox_green.setValue(green)
        self.ui.label_displaycolor.setStyleSheet("background-color: rgba({r}, {g}, {b}, {a});".format(
            r=red, g=green, b=blue, a=alpha
        ))

    @Slot()
    def slot_set_megenta(self):

        self.colorCurrent = [255, 0, 255, 255]
        red, green, blue, alpha = self.colorCurrent
        self.ui.spinBox_red.setValue(red)
        self.ui.spinBox_blue.setValue(blue)
        self.ui.spinBox_green.setValue(green)
        self.ui.label_displaycolor.setStyleSheet("background-color: rgba({r}, {g}, {b}, {a});".format(
            r=red, g=green, b=blue, a=alpha
        ))

    @Slot()
    def slot_set_grey(self):

        self.colorCurrent = [128, 128, 128, 255]
        red, green, blue, alpha = self.colorCurrent
        self.ui.spinBox_red.setValue(red)
        self.ui.spinBox_blue.setValue(blue)
        self.ui.spinBox_green.setValue(green)
        self.ui.label_displaycolor.setStyleSheet("background-color: rgba({r}, {g}, {b}, {a});".format(
            r=red, g=green, b=blue, a=alpha
        ))

    @Slot()
    def slot_set_white(self):

        self.colorCurrent = [255, 255, 255, 255]
        red, green, blue, alpha = self.colorCurrent
        self.ui.spinBox_red.setValue(red)
        self.ui.spinBox_blue.setValue(blue)
        self.ui.spinBox_green.setValue(green)
        self.ui.label_displaycolor.setStyleSheet("background-color: rgba({r}, {g}, {b}, {a});".format(
            r=red, g=green, b=blue, a=alpha
        ))

    @Slot()
    def slot_set_yellow(self):

        self.colorCurrent = [255, 255, 0, 255]
        red, green, blue, alpha = self.colorCurrent
        self.ui.spinBox_red.setValue(red)
        self.ui.spinBox_blue.setValue(blue)
        self.ui.spinBox_green.setValue(green)
        self.ui.label_displaycolor.setStyleSheet("background-color: rgba({r}, {g}, {b}, {a});".format(
            r=red, g=green, b=blue, a=alpha
        ))


if __name__ == '__main__':

    qapp = QtWidgets.QApplication()
    dialog = CategoryDialog()
    dialog.show()
    sys.exit(qapp.exec_())

