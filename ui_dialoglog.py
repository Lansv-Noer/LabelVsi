# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\mokan\OneDrive\Softwares\LabelU\UI\dialoglog.ui',
# licensing of 'C:\Users\mokan\OneDrive\Softwares\LabelU\UI\dialoglog.ui' applies.
#
# Created: Sat Aug 31 19:50:26 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import sys
import os
import imagesources_rc

class Ui_DialogLog(object):
    def setupUi(self, DialogLog):
        DialogLog.setObjectName("DialogLog")
        DialogLog.resize(400, 280)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/Small/icon100_com_102.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogLog.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogLog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.textBrowser = QtWidgets.QTextBrowser(DialogLog)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 381, 221))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(DialogLog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DialogLog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DialogLog.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogLog)

    def retranslateUi(self, DialogLog):
        DialogLog.setWindowTitle(QtWidgets.QApplication.translate("DialogLog", "Log", None, -1))


class LogDialog(QtWidgets.QDialog):

    def __init__(self, parent: QtWidgets.QWidget = None):

        if parent is None:
            super(LogDialog, self).__init__()
        elif isinstance(parent, QtWidgets.QWidget):
            super(LogDialog, self).__init__(parent)

        self.ui = Ui_DialogLog()
        self.ui.setupUi(self)
        self.setLogText()

    def setLogText(self):

        path_log = ".\\log.txt"
        if os.path.exists(path_log):
            with open(path_log, "r") as file:
                content = file.read()
                content = "<br/>".join(content.split("\n"))
                self.ui.textBrowser.setText(content)

if __name__ == '__main__':

    qapp = QtWidgets.QApplication()
    logdialog = LogDialog()
    logdialog.show()
    sys.exit(qapp.exec_())
