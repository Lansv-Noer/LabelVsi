# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\mokan\OneDrive\Softwares\LabelU\UI\dialoglayer.ui',
# licensing of 'C:\Users\mokan\OneDrive\Softwares\LabelU\UI\dialoglayer.ui' applies.
#
# Created: Fri Aug 23 14:49:29 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Signal, Slot
import imagesources_rc
import sys


class Ui_LayerDialog(object):
    def setupUi(self, LayerDialog):
        LayerDialog.setObjectName("LayerDialog")
        LayerDialog.resize(500, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/Small/icon100_com_015.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LayerDialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(LayerDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(LayerDialog)
        self.tableWidget.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(LayerDialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(LayerDialog)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(LayerDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.lineEdit)

        self.retranslateUi(LayerDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), LayerDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), LayerDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LayerDialog)

    def retranslateUi(self, LayerDialog):
        LayerDialog.setWindowTitle(QtWidgets.QApplication.translate("LayerDialog", "Layer Select", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("LayerDialog", "Layer", None, -1))


class LayerDialog(QtWidgets.QDialog):

    SignalLayer = Signal(int)

    def __init__(self, parent: QtWidgets.QWidget = None):

        if parent is None:
            super(LayerDialog, self).__init__()
        elif isinstance(parent, QtWidgets.QWidget):
            super(LayerDialog, self).__init__(parent)

        self.ui = Ui_LayerDialog()
        self.ui.setupUi(self)
        self.ui.tableWidget.itemClicked.connect(self.slot_set_item)
        self.ui.tableWidget.setSortingEnabled(False)
        self.rowCurrent = -1

    def setup(self, content):

        dictExchange = {"Name": "Title",
                        "SizeY": "Height",
                        "SizeX": "Width",
                        "DimensionOrder": "Order",
                        "Type": "Type",
                        "AcquisitionDate": "Time",
                        "PhysicalSizeY": "umppY",
                        "PhysicalSizeX": "umppX"}
        headerAll = [key for key in content[0].keys()]
        header = [[key, dictExchange[key]] for key in headerAll if key in dictExchange]
        headerDisplay = [element[1] for element in header]
        headerReal = [element[0] for element in header]
        self.ui.tableWidget.setColumnCount(len(headerDisplay))
        self.ui.tableWidget.setRowCount(len(content))
        self.ui.tableWidget.setHorizontalHeaderLabels(headerDisplay)
        for index_row in range(len(content)):
            for index_column in range(len(headerReal)):
                qItem = QtWidgets.QTableWidgetItem(content[index_row][headerReal[index_column]])
                qItem.setTextAlignment(QtCore.Qt.AlignCenter)
                if index_column == 1 or index_column == 2:
                    qItem.setData(QtCore.Qt.EditRole, 123)
                    qItem.setData(QtCore.Qt.EditRole, int(content[index_row][headerReal[index_column]]))
                self.ui.tableWidget.setItem(index_row, index_column, qItem)
        self.ui.tableWidget.setColumnWidth(0, 120)
        self.ui.tableWidget.setColumnWidth(1, 90)
        self.ui.tableWidget.setColumnWidth(2, 90)
        self.ui.tableWidget.setColumnWidth(3, 140)
        self.ui.tableWidget.setColumnWidth(4, 100)
        self.ui.tableWidget.setColumnWidth(5, 100)
        self.ui.tableWidget.setColumnWidth(6, 100)
        self.ui.tableWidget.setColumnWidth(7, 100)
        # Hidden some columns
        infoHidden = ("Order", "Type", "umppY", "umppX")
        indexHidden = [index for index, key in enumerate(headerDisplay) if key in infoHidden]
        for index in range(len(indexHidden)):
            self.ui.tableWidget.setColumnHidden(indexHidden[index], True)

    @Slot(QtWidgets.QTableWidgetItem)
    def slot_set_item(self, item:QtWidgets.QTableWidgetItem):

        row = item.row()
        content = self.ui.tableWidget.item(row, 0).text() + " (" + self.ui.tableWidget.item(row, 1).text() + ", " + \
                  self.ui.tableWidget.item(row, 2).text() + ")"
        self.rowCurrent = row
        self.ui.lineEdit.setText(" " + str(row) + " - [ " + content + "]")

    def accept(self):

        self.SignalLayer.emit(self.rowCurrent)
        QtWidgets.QDialog.accept(self)


if __name__ == '__main__':

    qapp = QtWidgets.QApplication()
    layerDialog = LayerDialog()
    layerDialog.show()
    sys.exit(qapp.exec_())
