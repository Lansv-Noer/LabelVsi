# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\mokan\OneDrive\Softwares\LabelU\UI\dialogprocess.ui',
# licensing of 'C:\Users\mokan\OneDrive\Softwares\LabelU\UI\dialogprocess.ui' applies.
#
# Created: Sun Sep  1 22:47:04 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Slot, Signal
from PySide2.QtCore import QThread
import sys
import os
import imagesources_rc

class Ui_DialogProcess(object):
    def setupUi(self, DialogProcess):
        DialogProcess.setObjectName("DialogProcess")
        DialogProcess.resize(400, 105)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/Small/icon100_com_213.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogProcess.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogProcess)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.progressBar = QtWidgets.QProgressBar(DialogProcess)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_time_remain = QtWidgets.QLabel(DialogProcess)
        self.label_time_remain.setObjectName("label_time_remain")
        self.horizontalLayout.addWidget(self.label_time_remain)
        self.label_time_used = QtWidgets.QLabel(DialogProcess)
        self.label_time_used.setObjectName("label_time_used")
        self.horizontalLayout.addWidget(self.label_time_used)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_time_comment = QtWidgets.QLabel(DialogProcess)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_time_comment.setFont(font)
        self.label_time_comment.setObjectName("label_time_comment")
        self.verticalLayout.addWidget(self.label_time_comment)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(DialogProcess)
        QtCore.QMetaObject.connectSlotsByName(DialogProcess)

    def retranslateUi(self, DialogProcess):
        DialogProcess.setWindowTitle(QtWidgets.QApplication.translate("DialogProcess", "Process", None, -1))
        self.label_time_remain.setText(QtWidgets.QApplication.translate("DialogProcess", "Remaining Time:", None, -1))
        self.label_time_used.setText(QtWidgets.QApplication.translate("DialogProcess", "Used Time:", None, -1))
        self.label_time_comment.setText(QtWidgets.QApplication.translate("DialogProcess", "Comments", None, -1))


class ProcessDialog(QtWidgets.QDialog):

    def __init__(self, parent: QtWidgets.QWidget = None):

        if parent is None:
            super(ProcessDialog, self).__init__()
        elif isinstance(parent, QtWidgets.QWidget):
            super(ProcessDialog, self).__init__(parent)

        self.ui = Ui_DialogProcess()
        self.ui.setupUi(self)
        self.ui.progressBar.setMaximum(100)
        self.ui.progressBar.setValue(0)
        self.setCursor(QtCore.Qt.WaitCursor)

    @Slot(list)
    def slot_set_value_comments(self, signalprocess: list):

        print("receive {}".format(signalprocess))
        value, time_used = signalprocess
        self.ui.label_time_used.setText("Used Time: {}".format(self.time_format(time_used,
                                                                                display_millisecond=True)))
        self.ui.label_time_remain.setText("Remaining Time: {}".format(self.time_format(time_used * (100 - value) / value,
                                                                                       display_millisecond=True)))
        self.ui.progressBar.setValue(value)
        if value < 99:
            if int(value) % 2 == 1:
                self.ui.label_time_comment.setText("Writing...")
            else:
                self.ui.label_time_comment.setText("Writing......")
        elif 99 <= value < 100:
            self.ui.label_time_comment.setText("Finishing......")
        elif value == 100:
            self.ui.label_time_comment.setText("End")

    def time_format(self, seconds, display_millisecond: bool=False):

        if display_millisecond:
            return "{hour}:{minute}:{second}:{millisecond}".format(hour=int(seconds // 3600),
                                                                   minute=int(seconds % 3600 // 60),
                                                                   second=int(seconds % 60 // 1),
                                                                   millisecond=int(seconds % 1 * 100))
        else:
            seconds = int(seconds)
            return "{hour}:{minute}:{second}".format(hour=(seconds // 3600),
                                                     minute=(seconds % 3600 // 60),
                                                     second=(seconds % 60 // 1))

import time
from multiprocessing import Process


def timer(sec: float, turns: int, dialog:QtWidgets.QDialog):
    for i in range(turns):
        time.sleep(sec)
        print(i)


class ProcessThread(QThread):

    SignalProgress = Signal(float)

    def __init__(self):

        super(ProcessThread, self).__init__()

    def run(self):

        print("running")
        for i in range(10):
            time.sleep(0.4)
            print("emit {}".format((i + 1) / 10 * 100))
            self.SignalProgress.emit((i + 1) / 10 * 100)
        self.quit()
        self.wait(1)




class Window(QtWidgets.QMainWindow):

    def __init__(self):

        super(Window, self).__init__()
        self.button = QtWidgets.QPushButton(self)
        self.layoutH = QtWidgets.QHBoxLayout()
        self.layoutH.addWidget(self.button)

        self.thread = ProcessThread()

        self.button.clicked.connect(self.slot_button_click)

    @Slot()
    def slot_button_click(self):

        dialog = ProcessDialog(self)
        dialog.ui.progressBar.setValue(0)
        dialog.show()
        self.thread.SignalProgress.connect(dialog.slot_set_value_comments)
        self.thread.finished.connect(dialog.close)
        self.thread.start()




if __name__ == '__main__':

    qapp = QtWidgets.QApplication()
    window = Window()
    window.show()
    sys.exit(qapp.exec_())

