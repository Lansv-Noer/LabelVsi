# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\mokan\OneDrive\Softwares\LabelU\UI\dialogdiscard.ui',
# licensing of 'C:\Users\mokan\OneDrive\Softwares\LabelU\UI\dialogdiscard.ui' applies.
#
# Created: Tue Aug 27 16:36:22 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Signal, Slot
import sys
import imagesources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 150)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 90, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Discard|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 30, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 31, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/icons/Small/icon100_com_121.png"))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "Do you want to save annotation file before close?\n"
"If you don\'t save it, all you did will be lost!", None, -1))


class DiscardDialog(QtWidgets.QDialog):

    SignalDiscard = Signal()
    SignalCancel = Signal()

    def __init__(self, parent:QtWidgets.QWidget=None):

        if parent is None:
            super(DiscardDialog, self).__init__()
        elif isinstance(parent, QtWidgets.QWidget):
            super(DiscardDialog, self).__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.clicked.connect(self.slot_click)

    @Slot(QtWidgets.QAbstractButton)
    def slot_click(self, button: QtWidgets.QAbstractButton):

        self.close()
        if button.text() == "Discard":
            self.SignalDiscard.emit()
        elif button.text() == "Cancel":
            self.SignalCancel.emit()
            self.reject()


if __name__ == '__main__':

    qapp = QtWidgets.QApplication()
    layerDialog = DiscardDialog()
    layerDialog.show()
    sys.exit(qapp.exec_())

