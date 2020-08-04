# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\mokan\OneDrive\Softwares\LabelU\UI\mainwindows.ui',
# licensing of 'C:\Users\mokan\OneDrive\Softwares\LabelU\UI\mainwindows.ui' applies.
#
# Created: Tue Jul 16 22:29:27 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Slot, Signal

from ui_dialogcategory import CategoryDialog
from ui_dialoglayer import LayerDialog
from ui_dialogdiscard import DiscardDialog
from ui_dialoglog import LogDialog
from ui_dialogprocess import ProcessDialog
import imagesources_rc
from reader import VsiReader, XmlParser
from graphics import TGraphicsScene, TGraphicsView, YGraphicsScene, YGraphicsView, \
    AnnotationType, TStatusBar, TTreeWidget, AboutDialog
from graphics import SceneMode, ItemMark, NodeMark, NodeSingleMark, NodePolyMark, RectangleMark, EdgePoly
from annotationmanager import TileAnnotationManager

import sys
import os
import bioformats
import matplotlib.pyplot as plt
import time
import cv2
import numpy as np
import qimage2ndarray


class TFileDialog(QtWidgets.QFileDialog):
    def __init__(self, parent):
        super(TFileDialog, self).__init__()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/main/paperClipItalic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setMouseTracking(True)
        self.centralscene = YGraphicsScene(self.centralwidget)
        self.centralviewer = YGraphicsView(scene=self.centralscene, parent=self.centralwidget)
        self.centralviewer.setScene(self.centralscene)
        self.centralviewer.setMouseTracking(True)
        layout_H = QtWidgets.QHBoxLayout()
        layout_H.addWidget(self.centralviewer)
        layout_V = QtWidgets.QVBoxLayout()
        layout_V.addItem(layout_H)
        self.centralwidget.setLayout(layout_V)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Edit = QtWidgets.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")
        self.menu_Tools = QtWidgets.QMenu(self.menubar)
        self.menu_Tools.setObjectName("menu_Tools")
        self.menuAnnotations = QtWidgets.QMenu(self.menu_Tools)
        self.menuAnnotations.setObjectName("menuAnnotations")
        self.menu_About = QtWidgets.QMenu(self.menubar)
        self.menu_About.setObjectName("menu_About")
        self.menuWindows = QtWidgets.QMenu(self.menubar)
        self.menuWindows.setObjectName("menuWindows")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = TStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setToolTip("")
        self.toolBar.setStatusTip("")
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidgetAnnotation = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetAnnotation.sizePolicy().hasHeightForWidth())
        self.dockWidgetAnnotation.setSizePolicy(sizePolicy)
        self.dockWidgetAnnotation.setMinimumSize(QtCore.QSize(200, 308))
        self.dockWidgetAnnotation.setObjectName("dockWidgetAnnotation")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents_3)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBoxMode = QtWidgets.QGroupBox(self.dockWidgetContents_3)
        self.groupBoxMode.setMinimumSize(QtCore.QSize(0, 81))
        self.groupBoxMode.setObjectName("groupBoxMode")
        self.layoutWidget = QtWidgets.QWidget(self.groupBoxMode)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 22, 89, 50))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_view = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.radioButton_view.setFont(font)
        self.radioButton_view.setObjectName("radioButton_view")
        self.verticalLayout.addWidget(self.radioButton_view)
        self.radioButton_annotation = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.radioButton_annotation.setFont(font)
        self.radioButton_annotation.setObjectName("radioButton_annotation")
        self.verticalLayout.addWidget(self.radioButton_annotation)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addWidget(self.groupBoxMode, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.dockWidgetContents_3)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_view = QtWidgets.QWidget()
        self.page_view.setObjectName("page_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_view)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label = QtWidgets.QLabel(self.page_view)
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 1)
        self.tableWidget_metadata = QtWidgets.QTableWidget(self.page_view)
        self.tableWidget_metadata.setObjectName("tableView_metadata")
        self.gridLayout_7.addWidget(self.tableWidget_metadata, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_view)
        self.page_annotation = QtWidgets.QWidget()
        self.page_annotation.setObjectName("page_annotation")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_annotation)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 4, 0, 1, 1)
        self.treeWidget = TTreeWidget(self.page_annotation)
        self.treeWidget.setColumnCount(4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.setColumnWidth(0, 100)
        self.treeWidget.headerItem().setTextAlignment(0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.treeWidget.setColumnWidth(1, 40)
        self.treeWidget.headerItem().setTextAlignment(1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.treeWidget.setColumnWidth(2, 40)
        self.treeWidget.headerItem().setTextAlignment(1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.treeWidget.setColumnWidth(3, 40)
        self.treeWidget.headerItem().setTextAlignment(2, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.treeWidget.setColumnWidth(4, 50)
        self.treeWidget.headerItem().setTextAlignment(3, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.treeWidget, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_new = QtWidgets.QPushButton(self.page_annotation)
        self.pushButton_new.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton_new.setObjectName("pushButton_new")
        self.horizontalLayout_5.addWidget(self.pushButton_new)
        self.pushButton_load = QtWidgets.QPushButton(self.page_annotation)
        self.pushButton_load.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton_load.setObjectName("pushButton_load")
        self.horizontalLayout_5.addWidget(self.pushButton_load)
        self.pushButton_delete = QtWidgets.QPushButton(self.page_annotation)
        self.pushButton_delete.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.horizontalLayout_5.addWidget(self.pushButton_delete)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page_annotation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_add = QtWidgets.QPushButton(self.page_annotation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        self.pushButton_add.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout_6.addWidget(self.pushButton_add)
        self.pushButton_save = QtWidgets.QPushButton(self.page_annotation)
        self.pushButton_save.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_6.addWidget(self.pushButton_save)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_annotation)
        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)
        self.dockWidgetAnnotation.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidgetAnnotation)
        self.dockWidgetNavigation = QtWidgets.QDockWidget(MainWindow)
        self.dockWidgetNavigation.setObjectName("dockWidgetNavigation")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.dockWidgetContents_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_topLeft = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_topLeft.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/Small/icon100_com_148.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_topLeft.setIcon(icon1)
        self.pushButton_topLeft.setObjectName("pushButton_leftup")
        self.gridLayout_3.addWidget(self.pushButton_topLeft, 0, 0, 1, 1)
        self.pushButton_top = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_top.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/Small/icon100_com_149.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_top.setIcon(icon2)
        self.pushButton_top.setObjectName("pushButton_up")
        self.gridLayout_3.addWidget(self.pushButton_top, 0, 1, 1, 1)
        self.pushButton_topRight = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_topRight.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/Small/icon100_com_150.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_topRight.setIcon(icon3)
        self.pushButton_topRight.setObjectName("pushButton_rightup")
        self.gridLayout_3.addWidget(self.pushButton_topRight, 0, 2, 1, 1)
        self.pushButton_left = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_left.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/Small/icon100_com_147.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_left.setIcon(icon4)
        self.pushButton_left.setObjectName("pushButton_left")
        self.gridLayout_3.addWidget(self.pushButton_left, 1, 0, 1, 1)
        self.pushButton_right = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_right.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/Small/icon100_com_143.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_right.setIcon(icon5)
        self.pushButton_right.setObjectName("pushButton_right")
        self.gridLayout_3.addWidget(self.pushButton_right, 1, 2, 1, 1)
        self.pushButton_bottomLeft = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_bottomLeft.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/Small/icon100_com_146.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_bottomLeft.setIcon(icon6)
        self.pushButton_bottomLeft.setObjectName("pushButton_leftdown")
        self.gridLayout_3.addWidget(self.pushButton_bottomLeft, 2, 0, 1, 1)
        self.pushButton_bottom = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_bottom.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/Small/icon100_com_145.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_bottom.setIcon(icon7)
        self.pushButton_bottom.setObjectName("pushButton_down")
        self.gridLayout_3.addWidget(self.pushButton_bottom, 2, 1, 1, 1)
        self.pushButton_bottomRight = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_bottomRight.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/Small/icon100_com_144.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_bottomRight.setIcon(icon8)
        self.pushButton_bottomRight.setObjectName("pushButton_rightdown")
        self.gridLayout_3.addWidget(self.pushButton_bottomRight, 2, 2, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.gridLayout_4.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 79, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 79, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem4, 2, 0, 1, 1)
        self.dockWidgetNavigation.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidgetNavigation)
        self.dockWidget_4 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_4.setObjectName("dockWidget_4")
        self.dockWidgetContents_6 = QtWidgets.QWidget()
        self.dockWidgetContents_6.setObjectName("dockWidgetContents_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.dockWidgetContents_6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.dockWidgetContents_6)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_3 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)
        self.graphicsView_overview = TGraphicsView(self.page)
        self.graphicsView_overview.setObjectName("graphicsView_overview")
        self.graphicsScene_overview = TGraphicsScene(self.graphicsView_overview)
        self.graphicsScene_overview.setObjectName("graphicsScene_overview")
        self.graphicsView_overview.setScene(self.graphicsScene_overview)
        self.gridLayout_5.addWidget(self.graphicsView_overview, 1, 0, 1, 1)
        self.stackedWidget_2.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget_2.addWidget(self.page_2)
        self.gridLayout_6.addWidget(self.stackedWidget_2, 0, 0, 1, 1)
        self.dockWidget_4.setWidget(self.dockWidgetContents_6)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_4)
        self.action_Open = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/icons/Small/icon100_com_019.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Open.setIcon(icon9)
        self.action_Open.setObjectName("action_Open")
        self.action_Close = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/icons/Small/icon100_com_123.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Close.setIcon(icon10)
        self.action_Close.setObjectName("action_Close")
        self.action_Quit = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/icons/Small/icon100_com_0.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Quit.setIcon(icon11)
        self.action_Quit.setPriority(QtWidgets.QAction.HighPriority)
        self.action_Quit.setObjectName("action_Quit")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/icons/Small/icon100_com_201.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon12)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRectangleAnnotation = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/icons/Middle/rectangle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRectangleAnnotation.setIcon(icon13)
        self.actionRectangleAnnotation.setObjectName("actionRectangleAnnotation")
        self.actionPolygonAnnotation = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/icons/Middle/poly.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPolygonAnnotation.setIcon(icon14)
        self.actionPolygonAnnotation.setObjectName("actionPolygonAnnotation")
        self.actionSpineAnnotation = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/icons/Middle/spline.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSpineAnnotation.setIcon(icon15)
        self.actionSpineAnnotation.setObjectName("actionSpineAnnotation")
        self.actionDotAnnotation = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icons/icons/Middle/dot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDotAnnotation.setIcon(icon16)
        self.actionDotAnnotation.setObjectName("actionDotAnnotation")
        self.actionDotsetAnnotation = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/icons/icons/Middle/pointset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDotsetAnnotation.setIcon(icon17)
        self.actionDotsetAnnotation.setObjectName("actionDotsetAnnotation")
        self.actionPolygonRnn = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/icons/icons/Small/icon100_com_039.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPolygonRnn.setIcon(icon18)
        self.actionPolygonRnn.setObjectName("actionPolygonRnn")
        self.action_About = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/icons/icons/Small/icon100_com_126.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_About.setIcon(icon19)
        self.action_About.setObjectName("action_About")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/icons/icons/Small/icon100_com_200.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon20)
        self.actionRedo.setObjectName("actionRedo")
        self.action_Export_xml = QtWidgets.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/icons/icons/Small/icon100_com_007.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Export_xml.setIcon(icon21)
        self.action_Export_xml.setObjectName("action_Export_xml")
        self.action_Export_mask = QtWidgets.QAction(MainWindow)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/icons/icons/Small/icon100_com_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Export_mask.setIcon(icon22)
        self.action_Export_mask.setObjectName("action_Export_mask")

        self.action_Log = QtWidgets.QAction(MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/icons/icons/Small/icon100_com_102.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Log.setIcon(icon23)
        self.action_Log.setObjectName("action_Log")

        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Close)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_Edit.addAction(self.actionUndo)
        self.menu_Edit.addAction(self.actionRedo)
        self.menuAnnotations.addAction(self.actionRectangleAnnotation)
        self.menuAnnotations.addAction(self.actionPolygonAnnotation)
        self.menuAnnotations.addAction(self.actionSpineAnnotation)
        self.menuAnnotations.addAction(self.actionDotAnnotation)
        self.menuAnnotations.addAction(self.actionDotsetAnnotation)
        self.menuAnnotations.addSeparator()
        self.menuAnnotations.addAction(self.actionPolygonRnn)
        self.menu_Tools.addAction(self.menuAnnotations.menuAction())
        self.menu_About.addAction(self.action_About)
        self.menu_About.addAction(self.action_Log)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_Tools.menuAction())
        self.menubar.addAction(self.menuWindows.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())
        self.toolBar.addAction(self.action_Open)
        self.toolBar.addAction(self.action_Close)
        self.toolBar.addAction(self.action_Quit)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Export_xml)
        self.toolBar.addAction(self.action_Export_mask)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionRedo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRectangleAnnotation)
        self.toolBar.addAction(self.actionPolygonAnnotation)
        self.toolBar.addAction(self.actionSpineAnnotation)
        self.toolBar.addAction(self.actionDotAnnotation)
        self.toolBar.addAction(self.actionDotsetAnnotation)
        self.toolBar.addAction(self.actionPolygonRnn)
        self.label_2.setBuddy(self.treeWidget)
        self.label_3.setBuddy(self.graphicsView_overview)
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "LabelU", None, -1))
        self.menu_File.setTitle(QtWidgets.QApplication.translate("MainWindow", "&File", None, -1))
        self.menu_Edit.setTitle(QtWidgets.QApplication.translate("MainWindow", "&Edit", None, -1))
        self.menu_Tools.setTitle(QtWidgets.QApplication.translate("MainWindow", "&Tools", None, -1))
        self.menuAnnotations.setTitle(QtWidgets.QApplication.translate("MainWindow", "Annotations", None, -1))
        self.menu_About.setTitle(QtWidgets.QApplication.translate("MainWindow", "&About", None, -1))
        self.menuWindows.setTitle(QtWidgets.QApplication.translate("MainWindow", "Windows", None, -1))
        self.toolBar.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "toolBar", None, -1))
        self.dockWidgetAnnotation.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Annotation Management", None, -1))
        self.groupBoxMode.setTitle(QtWidgets.QApplication.translate("MainWindow", "Mode", None, -1))
        self.radioButton_view.setToolTip(QtWidgets.QApplication.translate("MainWindow", "View Mode", None, -1))
        self.radioButton_view.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "View Mode", None, -1))
        self.radioButton_view.setText(QtWidgets.QApplication.translate("MainWindow", "View", None, -1))
        self.radioButton_annotation.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Annotation Mode", None, -1))
        self.radioButton_annotation.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Annotation Mode", None, -1))
        self.radioButton_annotation.setText(QtWidgets.QApplication.translate("MainWindow", "Annotation", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Detail", None, -1))
        self.treeWidget.headerItem().setText(0, QtWidgets.QApplication.translate("MainWindow", "Group/Name", None, -1))
        self.treeWidget.headerItem().setText(1, QtWidgets.QApplication.translate("MainWindow", "Value", None, -1))
        self.treeWidget.headerItem().setText(2, QtWidgets.QApplication.translate("MainWindow", "Color", None, -1))
        self.treeWidget.headerItem().setText(3, QtWidgets.QApplication.translate("MainWindow", "Count", None, -1))
        self.treeWidget.headerItem().setText(4, QtWidgets.QApplication.translate("MainWindow", "Type", None, -1))
        self.pushButton_delete.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "delete annotations of this image", None, -1))
        self.pushButton_delete.setText(QtWidgets.QApplication.translate("MainWindow", "delete", None, -1))
        self.pushButton_load.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "load a group of annotations for this image.", None, -1))
        self.pushButton_load.setText(QtWidgets.QApplication.translate("MainWindow", "load", None, -1))
        self.pushButton_new.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "creat a category of annotation", None, -1))
        self.pushButton_new.setText(QtWidgets.QApplication.translate("MainWindow", "new", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Annotation", None, -1))
        self.pushButton_add.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "add a annotation file for this image.", None, -1))
        self.pushButton_add.setText(QtWidgets.QApplication.translate("MainWindow", "add", None, -1))
        self.pushButton_save.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "save annotations to a file.", None, -1))
        self.pushButton_save.setText(QtWidgets.QApplication.translate("MainWindow", "save", None, -1))
        self.dockWidgetNavigation.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Navigator", None, -1))
        self.pushButton_topLeft.setToolTip(QtWidgets.QApplication.translate("MainWindow", "left-top", None, -1))
        self.pushButton_topLeft.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "load the block on the left-top.", None, -1))
        self.pushButton_top.setToolTip(QtWidgets.QApplication.translate("MainWindow", "up", None, -1))
        self.pushButton_top.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "load the block above.", None, -1))
        self.pushButton_top.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Up", None, -1))
        self.pushButton_topRight.setToolTip(QtWidgets.QApplication.translate("MainWindow", "right-top", None, -1))
        self.pushButton_topRight.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "load the block on the right-top.", None, -1))
        self.pushButton_left.setToolTip(QtWidgets.QApplication.translate("MainWindow", "left", None, -1))
        self.pushButton_left.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "load the block on the left.", None, -1))
        self.pushButton_left.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Left", None, -1))
        self.pushButton_right.setToolTip(QtWidgets.QApplication.translate("MainWindow", "right", None, -1))
        self.pushButton_right.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "load the block on the right.", None, -1))
        self.pushButton_right.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Right", None, -1))
        self.pushButton_bottomLeft.setToolTip(QtWidgets.QApplication.translate("MainWindow", "left-bottom", None, -1))
        self.pushButton_bottomLeft.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "load the block on the left-bottom.", None, -1))
        self.pushButton_bottom.setToolTip(QtWidgets.QApplication.translate("MainWindow", "down", None, -1))
        self.pushButton_bottom.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "to the block below.", None, -1))
        self.pushButton_bottom.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Down", None, -1))
        self.pushButton_bottomRight.setToolTip(QtWidgets.QApplication.translate("MainWindow", "right-bottom", None, -1))
        self.pushButton_bottomRight.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "load the block on the right-bottom.", None, -1))
        self.dockWidget_4.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "OverMap", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Overview", None, -1))
        self.action_Open.setText(QtWidgets.QApplication.translate("MainWindow", "&Open", None, -1))
        self.action_Open.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Open an image.", None, -1))
        self.action_Close.setText(QtWidgets.QApplication.translate("MainWindow", "&Close", None, -1))
        self.action_Close.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Close an image.", None, -1))
        self.action_Quit.setText(QtWidgets.QApplication.translate("MainWindow", "&Quit", None, -1))
        self.action_Quit.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Quit LabelU", None, -1))
        self.actionUndo.setText(QtWidgets.QApplication.translate("MainWindow", "&Undo", None, -1))
        self.actionUndo.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Undo", None, -1))
        self.actionRectangleAnnotation.setText(QtWidgets.QApplication.translate("MainWindow", "Rectangle Annotation", None, -1))
        self.actionRectangleAnnotation.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "a rectanble annotating tools", None, -1))
        self.actionPolygonAnnotation.setText(QtWidgets.QApplication.translate("MainWindow", "Polygon Annotation", None, -1))
        self.actionPolygonAnnotation.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "a polygon annotating tools", None, -1))
        self.actionSpineAnnotation.setText(QtWidgets.QApplication.translate("MainWindow", "Spine Annotation", None, -1))
        self.actionSpineAnnotation.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "a spline annotating tools", None, -1))
        self.actionDotAnnotation.setText(QtWidgets.QApplication.translate("MainWindow", "Dot Annotation", None, -1))
        self.actionDotAnnotation.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "a dot annotating tools", None, -1))
        self.actionDotsetAnnotation.setText(QtWidgets.QApplication.translate("MainWindow", "Dotset Annotation", None, -1))
        self.actionDotsetAnnotation.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "a dotset annotating annotation", None, -1))
        self.actionPolygonRnn.setText(QtWidgets.QApplication.translate("MainWindow", "PolygonRnn++", None, -1))
        self.action_About.setText(QtWidgets.QApplication.translate("MainWindow", "&About...", None, -1))
        self.action_Log.setText(QtWidgets.QApplication.translate("MainWindow", "&Log...", None, -1))
        self.actionRedo.setText(QtWidgets.QApplication.translate("MainWindow", "&Redo", None, -1))
        self.action_Export_xml.setText(QtWidgets.QApplication.translate("MainWindow", "export to xml", None, -1))
        self.action_Export_xml.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "save all annotations to a xml file", None, -1))
        self.action_Export_mask.setText(QtWidgets.QApplication.translate("MainWindow", "export to image", None, -1))
        self.action_Export_mask.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "export a annotated image", None, -1))


class TMainWindow(QtWidgets.QMainWindow):

    # Signal
    SignalStateButtonGroups = Signal(list)
    SignalCoordinateGlobal = Signal(list)

    def __init__(self):
        super(TMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # flag
        self.FlagExistingImage = False

        # element
        self.reader = None
        self.map = None
        self.numTileX = float("inf")
        self.numTileY = float("inf")
        self.heightTile = 1440
        self.widthTile = 1440
        self.widthCentralImage = float("inf")
        self.heightCentralImage = float("inf")
        self.heightMacroTile = float("inf")
        self.widthMacroTile = float("inf")
        self.widthMacroImage = float("inf")
        self.heightMacroImage = float("inf")
        self.currentTileLocation = (float("inf"), float("inf"))  # (x, y)
        self.imageCentralBGI = None
        self.ratioCM = float("inf")
        self.annotationmanager = None
        self.pathExtrainfo = "./extrainfo"

        # action setup
        # old modality of connect
        # QtCore.QObject.connect(self.ui.action_Open, QtCore.SIGNAL("triggered(bool)"), self.slot_open_filedialog)
        # new and pythonic modality of connect
        self.ui.action_Open.triggered.connect(self.slot_open_filedialog)
        self.ui.action_Close.triggered.connect(self.slot_askfor_close)
        self.ui.action_Quit.triggered.connect(self.slot_askfor_quit)
        self.ui.radioButton_view.toggled.connect(self.slot_view_radiobutton)
        self.ui.radioButton_annotation.toggled.connect(self.slot_annotation_radiobutton)
        self.ui.pushButton_topLeft.clicked.connect(self.slot_topLeft)
        self.ui.pushButton_top.clicked.connect(self.slot_top)
        self.ui.pushButton_topRight.clicked.connect(self.slot_topRight)
        self.ui.pushButton_right.clicked.connect(self.slot_right)
        self.ui.pushButton_bottomRight.clicked.connect(self.slot_bottomRight)
        self.ui.pushButton_bottom.clicked.connect(self.slot_bottom)
        self.ui.pushButton_bottomLeft.clicked.connect(self.slot_bottomLeft)
        self.ui.pushButton_left.clicked.connect(self.slot_left)
        self.SignalStateButtonGroups.connect(self.setPButtonGroupEnable)
        self.ui.actionDotAnnotation.triggered.connect(self.slot_annotation_dot)
        self.ui.actionRectangleAnnotation.triggered.connect(self.slot_annotation_rect)
        self.ui.actionPolygonAnnotation.triggered.connect(self.slot_annotation_polygon)
        self.ui.actionDotsetAnnotation.triggered.connect(self.slot_annotation_dotset)
        self.ui.actionSpineAnnotation.triggered.connect(self.slot_annotation_spline)
        self.ui.actionPolygonRnn.triggered.connect(self.slot_annotation_polyrnnpp)
        self.ui.action_Export_xml.triggered.connect(self.slot_open_filedialog)
        self.ui.action_Export_mask.triggered.connect(self.slot_open_filedialog)
        self.ui.action_About.triggered.connect(self.slot_show_about)
        self.ui.action_Log.triggered.connect(self.slot_show_log)
        self.ui.pushButton_new.clicked.connect(self.slot_open_categorydialog)
        self.ui.pushButton_add.clicked.connect(self.slot_add_group)
        self.ui.pushButton_delete.clicked.connect(self.slot_delete_category_or_group)
        self.ui.treeWidget.itemClicked.connect(self.slot_treeItem)
        self.ui.centralscene.SignalNewNode.connect(self.slot_add_point)
        self.ui.centralscene.SignalDeleteNode.connect(self.slot_delete_point)
        self.ui.centralscene.SignalMoveNode.connect(self.slot_move_point)
        self.ui.centralscene.SignalNewRect.connect(self.slot_add_rect)
        self.ui.centralscene.SignalDeleteRect.connect(self.slot_delete_rect)
        self.ui.centralscene.SignalMoveRect.connect(self.slot_move_rect)
        self.ui.centralscene.SignalInsertNode.connect(self.slot_insert_point)
        self.ui.centralscene.SignalCoordinate.connect(self.slot_map_coordinate)
        self.ui.centralscene.SignalColor.connect(self.ui.statusbar.slot_show_color)
        self.ui.centralviewer.SignalScale.connect(self.slot_show_magnification)
        self.ui.graphicsScene_overview.SignalLocationDBC.connect(self.slot_set_location)
        self.ui.centralscene.SignalPaintFinished.connect(self.slot_add_group)
        self.ui.treeWidget.SignalItem.connect(self.slot_treeItem)

        # initial
        self.initial()

    def initial(self):

        # element
        self.reader = None
        self.map = None
        self.numTileX = float("inf")
        self.numTileY = float("inf")
        self.heightTile = 1440
        self.widthTile = 1440
        self.widthCentralImage = float("inf")
        self.heightCentralImage = float("inf")
        self.heightMacroTile = float("inf")
        self.widthMacroTile = float("inf")
        self.widthMacroImage = float("inf")
        self.heightMacroImage = float("inf")
        self.currentTileLocation = (float("inf"), float("inf"))  # (x, y)
        self.imageCentralBGI = None
        self.ratioCM = float("inf")
        self.annotationmanager = None
        # UI
        self.ui.treeWidget.clear()
        self.ui.tableWidget_metadata.clear()
        self.ui.centralscene.clear()
        image = np.ones((1024, 1024, 3), dtype=np.uint8) * 255
        self.ui.centralscene.drawBGI(image, image.shape[1], image.shape[0])
        self.ui.graphicsScene_overview.drawBGI(image, image.shape[1], image.shape[0])

        # PushButton Groups Initial
        self.ui.pushButton_topLeft.setEnabled(False)
        self.ui.pushButton_top.setEnabled(False)
        self.ui.pushButton_topRight.setEnabled(False)
        self.ui.pushButton_right.setEnabled(False)
        self.ui.pushButton_bottomRight.setEnabled(False)
        self.ui.pushButton_bottom.setEnabled(False)
        self.ui.pushButton_bottomLeft.setEnabled(False)
        self.ui.pushButton_left.setEnabled(False)
        # Annotation Switch
        self.ui.radioButton_annotation.setEnabled(False)
        # Annotation PushButton Initial
        self.ui.pushButton_add.setEnabled(False)
        self.ui.pushButton_save.setEnabled(False)
        self.ui.pushButton_delete.setEnabled(False)
        self.ui.actionRedo.setEnabled(False)
        self.ui.actionUndo.setEnabled(False)

    def hasImage(self):

        return self.FlagExistingImage

    @Slot(list)
    def slot_map_coordinate(self, coordinate):

        coordinateGlobal = [self.currentTileLocation[0] * self.widthTile + coordinate[1],
                            self.currentTileLocation[1] * self.heightTile + coordinate[0]]
        self.SignalCoordinateGlobal.connect(self.ui.statusbar.slot_show_coordiante)
        self.SignalCoordinateGlobal.emit(coordinateGlobal)

    @Slot(float)
    def slot_show_magnification(self, magnification:float):

        self.ui.statusbar.scaleStatus.setText("{:.2f}%".format(magnification * 100))

    @Slot()
    def slot_show_about(self):

        aboutDialog = AboutDialog(self)
        aboutDialog.show()

    @Slot()
    def slot_show_log(self):

        logDialog = LogDialog(self)
        logDialog.show()

    @Slot(RectangleMark)
    def slot_add_rect(self, rect:RectangleMark):

        print("RectMark: ", [*rect.scenePos().toTuple(), *rect.getSize()])
        self.annotationmanager.addRect(self.annotationmanager.getCurrentNameCategory(),
                                       self.annotationmanager.getCurrentIndexGroup(),
                                       self.currentTileLocation, (self.widthTile, self.heightTile),
                                       [*rect.scenePos().toTuple(), *rect.getSize()])
        self.ui.treeWidget.currentItem().setText(3, str(int(self.ui.treeWidget.currentItem().text(3)) + 1))

    @Slot(NodeMark)
    def slot_add_point(self, node:NodeMark):


        self.annotationmanager.addPoint(node.getNameCategory(), node.getIndexGroup(),
                                        self.currentTileLocation, (self.widthTile, self.heightTile), node.scenePos().toTuple())
        self.ui.treeWidget.currentItem().setText(3, str(int(self.ui.treeWidget.currentItem().text(3)) + 1))

    @Slot(NodeMark)
    def slot_insert_point(self, node: NodeMark):

        # set current item in the tree widget
        nameCategory, indexGroup = node.getCategoryGroup()
        itemsCategory = self.ui.treeWidget.findItems(nameCategory, QtCore.Qt.MatchExactly)
        itemGroup = itemsCategory[0].child(indexGroup)
        self.ui.treeWidget.setCurrentItem(itemGroup)

        if node.getIndex() < self.annotationmanager.getCountCategoryGroupTile(node.getNameCategory(),
                                                                              node.getIndexGroup(),
                                                                              node.getCoordinateTile()):
            self.annotationmanager.insertPoint(node.getNameCategory(), node.getIndexGroup(),
                                               node.getCoordinateTile(), (self.widthTile, self.heightTile),
                                               node.getIndex(), node.scenePos().toTuple())
            self.ui.treeWidget.currentItem().setText(3, str(int(self.ui.treeWidget.currentItem().text(3)) + 1))

        elif node.getIndex() == self.annotationmanager.getCountCategoryGroupTile(node.getNameCategory(),
                                                                                 node.getIndexGroup(),
                                                                                 node.getCoordinateTile()):
            self.annotationmanager.addPoint(node.getNameCategory(), node.getIndexGroup(),
                                            node.getCoordinateTile(), (self.widthTile, self.heightTile),
                                            node.scenePos().toTuple())
            self.ui.treeWidget.currentItem().setText(3, str(int(self.ui.treeWidget.currentItem().text(3)) + 1))


    @Slot()
    def slot_add_group(self):

        print("Testing the SignalPaintFinished")
        item = self.ui.treeWidget.currentItem()
        if item.parent() is None:
            itemParent = item
            nameCategory = itemParent.text(0)
            itemGroup = QtWidgets.QTreeWidgetItem(itemParent)
            itemGroup.setText(0, str(self.annotationmanager.getGroupsCount(nameCategory)))
            itemGroup.setText(1, str(self.annotationmanager.getCategoryValue(nameCategory)))
            itemGroup.setTextAlignment(1, QtCore.Qt.AlignCenter)
            itemGroup.setBackground(2, QtGui.QBrush(QtGui.QColor(*self.annotationmanager.getCategoryColor(
                self.annotationmanager.getCurrentNameCategory()))))
            itemGroup.setText(3, str(0))
            itemGroup.setTextAlignment(3, QtCore.Qt.AlignCenter)
            itemGroup.setText(4, str(self.annotationmanager.getCategoryType(
                self.annotationmanager.getCurrentNameCategory())))
            self.ui.treeWidget.currentItem().addChild(itemGroup)
            self.ui.treeWidget.setCurrentItem(itemGroup)
            self.ui.treeWidget.SignalItem.emit(itemGroup, 0)
            self.annotationmanager.addGroup(nameCategory)
            itemParent.setText(3, str(self.annotationmanager.getGroupsCount(nameCategory)))
        else:
            itemParent = item.parent()
            nameCategory = itemParent.text(0)
            itemGroup = QtWidgets.QTreeWidgetItem(itemParent)
            itemGroup.setText(0, str(self.annotationmanager.getGroupsCount(nameCategory)))
            itemGroup.setText(1, str(self.annotationmanager.getCategoryValue(nameCategory)))
            itemGroup.setTextAlignment(1, QtCore.Qt.AlignCenter)
            itemGroup.setBackground(2, QtGui.QBrush(QtGui.QColor(*self.annotationmanager.getCategoryColor(
                self.annotationmanager.getCurrentNameCategory()))))
            itemGroup.setText(3, str(0))
            itemGroup.setTextAlignment(3, QtCore.Qt.AlignCenter)
            itemGroup.setText(4, str(self.annotationmanager.getCategoryType(
                self.annotationmanager.getCurrentNameCategory())))
            self.ui.treeWidget.currentItem().addChild(itemGroup)
            self.ui.treeWidget.setCurrentItem(itemGroup)
            self.ui.treeWidget.SignalItem.emit(itemGroup, 0)
            self.annotationmanager.addGroup(nameCategory)
            itemParent.setText(3, str(self.annotationmanager.getGroupsCount(nameCategory)))

    @Slot(NodeMark)
    def slot_delete_point(self, itemPoint:NodeMark):

        nameCategory, indexGroup = itemPoint.getCategoryGroup()
        itemsCategory = self.ui.treeWidget.findItems(nameCategory, QtCore.Qt.MatchExactly)
        self.annotationmanager.deletePoint(nameCategory, indexGroup, self.currentTileLocation,
                                           itemPoint.getIndex())
        itemGroup = itemsCategory[0].child(indexGroup)
        itemGroup.setText(3, str(int(itemGroup.text(3)) - 1))

    @Slot(RectangleMark)
    def slot_delete_rect(self, itemRect: RectangleMark):

        nameCategory, indexGroup = itemRect.getCategoryGroup()
        itemsCategory = self.ui.treeWidget.findItems(nameCategory, QtCore.Qt.MatchExactly)
        self.annotationmanager.deleteRect(nameCategory, indexGroup, self.currentTileLocation, itemRect.getIndex())
        for itemCategory in itemsCategory:
            itemGroup = itemCategory.child(indexGroup)
            itemGroup.setText(3, str(int(itemGroup.text(3)) - 1))

    @Slot(NodeMark)
    def slot_move_point(self, item:NodeMark):

        self.annotationmanager.movePoint(item.getNameCategory(), item.getIndexGroup(),
                                         self.currentTileLocation, item.getIndex(), item.scenePos().toTuple())

    @Slot(RectangleMark)
    def slot_move_rect(self, item:RectangleMark):

        self.annotationmanager.moveRect(item.getNameCategory(), item.getIndexGroup(),
                                         self.currentTileLocation, item.getIndex(), item.scenePos().toTuple())

    @Slot()
    def slot_delete_category_or_group(self):

        item = self.ui.treeWidget.currentItem()
        if item:
            print(item)
            if item.parent():  # group item
                # item on scene
                nameCategory  = item.parent().text(0)
                indexGroup = int(item.text(0))
                self.func_delete_group_items(nameCategory, indexGroup)
                # content in annotationManager
                self.annotationmanager.deleteGroup(nameCategory, indexGroup)
                # item on treeWidget
                item.parent().setText(3, str(int(item.parent().text(3)) - 1))
                for indexChild in range(item.parent().indexOfChild(item) + 1, item.parent().childCount()):
                    item.parent().child(indexChild).setText(0, str(int(item.parent().child(indexChild).text(0)) - 1))
                item.parent().removeChild(item)
            else:  # category item
                # item on scene
                nameCategory = item.text(0)
                self.func_delete_category_items(nameCategory)
                # content in annotationManager
                self.annotationmanager.deleteCategory(nameCategory)
                # item on treeWidget
                item.treeWidget().takeTopLevelItem(item.treeWidget().indexOfTopLevelItem(item))

    @Slot()
    def func_delete_category_items(self, nameCategory: str):

        if self.ui.centralscene.items():
            itemsScene = self.ui.centralscene.items()
            for itemScene in itemsScene:
                if isinstance(itemScene, ItemMark):
                    if itemScene.getNameCategory() == nameCategory:
                        if isinstance(itemScene, (NodeSingleMark, RectangleMark)):
                            self.ui.centralscene.removeItem(itemScene)
                        elif isinstance(itemScene, NodePolyMark):
                            self.ui.centralscene.removeItem(itemScene.edgeBack())
                            self.ui.centralscene.removeItem(itemScene)
            self.ui.centralscene.update()

    @Slot()
    def func_delete_group_items(self, nameCategory: str, indexGroup: int):

        if self.ui.centralscene.items():
            itemsScene = self.ui.centralscene.items()
            for itemScene in itemsScene:
                if isinstance(itemScene, ItemMark):
                    if itemScene.getNameCategory() == nameCategory:
                        if itemScene.getIndexGroup() == indexGroup:
                            if isinstance(itemScene, (NodeSingleMark, RectangleMark)):
                                self.ui.centralscene.removeItem(itemScene)
                            elif isinstance(itemScene, NodePolyMark):
                                self.ui.centralscene.removeItem(itemScene.edgeBack())
                                self.ui.centralscene.removeItem(itemScene)
                        elif itemScene.getIndexGroup() > indexGroup:
                            itemScene.setIndexGroup(itemScene.getIndexGroup() - 1)
            self.ui.centralscene.update()

    @Slot()
    def slot_treeItem(self, item:QtWidgets.QTreeWidgetItem, column:int):

        # Category item
        if item.parent() is None:
            self.annotationmanager.setCurrentNameCategory(item.text(0))
            self.ui.treeWidget.setCurrentItem(item)
            self.ui.centralscene.setMode(SceneMode.Null)
            # Enable PushButton
            self.ui.pushButton_delete.setEnabled(True)
            self.ui.pushButton_add.setEnabled(True)
        # Group item
        else:
            currentNameCategory = item.parent().text(0)
            currentIndexGroup = int(item.text(0))
            self.annotationmanager.setCurrentNameCategory(currentNameCategory)
            self.annotationmanager.setCurrentIndexGroup(currentIndexGroup)
            self.annotationmanager.setCurrentColor(self.annotationmanager.getCategoryColor(currentNameCategory))
            self.ui.treeWidget.setCurrentItem(item)
            # self.annotationmanager.setCurrentColor(self.annotationmanager.getCategoryColor(
            #     self.annotationmanager.getCurrentNameCategory()))
            self.ui.centralscene.setColorMain(self.annotationmanager.getCurrentColor())
            self.ui.centralscene.setCurrentCategoryGroup(currentNameCategory, currentIndexGroup)
            self.ui.centralscene.setCoordinateTile(self.currentTileLocation)
            if self.map[self.currentTileLocation[1], self.currentTileLocation[0]] is True:
                if not self.annotationmanager.hasAnnotation(currentNameCategory, currentIndexGroup,
                                                            self.currentTileLocation):
                    self.ui.centralscene.setNextIndex(0)
                else:
                    self.ui.centralscene.setNextIndex(len(self.annotationmanager.body[currentNameCategory][
                                                              currentIndexGroup][self.currentTileLocation[0]][
                                                              self.currentTileLocation[1]][1]))
            else:
                self.ui.centralscene.setNextIndex(0)

            # set obvious and others
            for element in self.ui.centralscene.items():
                if isinstance(element, ItemMark):
                    if element.getNameCategory() == currentNameCategory and element.getIndexGroup() == currentIndexGroup:
                        element.setObvious(True)
                    else:
                        element.setObvious(False)
            # Enable PushButton
            self.ui.pushButton_delete.setEnabled(True)
            self.ui.pushButton_add.setEnabled(True)
            # mode
            mode = item.text(4)
            if mode == "Dot":
                self.ui.centralscene.setMode(SceneMode.DotAnnotation)
                print("Scene Mode: ", SceneMode.DotAnnotation)
            elif mode == "DotSet":
                self.ui.centralscene.setMode(SceneMode.DotSetAnnotation)
                print("Scene Mode: ", SceneMode.DotSetAnnotation)
            elif mode == "Rectangle":
                self.ui.centralscene.setMode(SceneMode.RectAnnotation)
                print("Scene Mode: ", SceneMode.RectAnnotation)
            elif mode == "Polygon":
                self.ui.centralscene.setMode(SceneMode.PolygonAnnotion)
                print("Scene Mode: ", SceneMode.PolygonAnnotion)
            elif mode == "Spline":
                self.ui.centralscene.setMode(SceneMode.SplineAnnotation)
                print("Scene Mode: ", SceneMode.SplineAnnotation)


    @Slot(list)
    def setPButtonGroupEnable(self, listState):

        self.ui.pushButton_topLeft.setEnabled(bool(listState[0]))
        self.ui.pushButton_top.setEnabled(bool(listState[1]))
        self.ui.pushButton_topRight.setEnabled(bool(listState[2]))
        self.ui.pushButton_right.setEnabled(bool(listState[3]))
        self.ui.pushButton_bottomRight.setEnabled(bool(listState[4]))
        self.ui.pushButton_bottom.setEnabled(bool(listState[5]))
        self.ui.pushButton_bottomLeft.setEnabled(bool(listState[6]))
        self.ui.pushButton_left.setEnabled(bool(listState[7]))

    def closeEvent(self, event):

        if self.reader is not None:
            self.reader.__delete__()
        print("LabelU Finish")
        QtWidgets.QMainWindow.closeEvent(self, event)

    def setLocation(self, location=(0, 0)):

        assert (0 <= location[0] < self.numTileX) and (0 <= location[1] < self.numTileY), "the location is out of the range"

        self.currentTileLocation = location
        self.map[location[1], location[0]] = True
        self.ui.centralscene.setCoordinateTile(location)
        # central view
        self.imageCentralBGI, (_, (self.widthTile, self.heightTile)) = self.reader.getTile(self.currentTileLocation[0], self.currentTileLocation[1])
        painter = QtGui.QPainter()
        self.ui.centralscene.setBGI(self.imageCentralBGI)
        self.ui.centralscene.setSceneRect(0, 0, self.widthTile, self.heightTile)
        self.ui.centralscene.drawBackground(painter, QtCore.QRectF(0, 0, self.widthTile, self.heightTile))
        # clear point
        if self.ui.centralscene.items() is not None:
            for item in self.ui.centralscene.items():
                self.ui.centralscene.removeItem(item)
        # reload and repaint point
        if self.map[location[1], location[0]] == True:
            if self.annotationmanager is not None:
                if not self.annotationmanager.hasAnnotation(self.annotationmanager.getCurrentNameCategory(),
                                                        self.annotationmanager.getCurrentIndexGroup(),
                                                        self.currentTileLocation):
                    self.ui.centralscene.setNextIndex(0)
                else:
                    self.ui.centralscene.setNextIndex(
                        len(self.annotationmanager.body[self.annotationmanager.getCurrentNameCategory()] \
                                [self.annotationmanager.getCurrentIndexGroup()][self.currentTileLocation[0]][
                                self.currentTileLocation[1]][1]))

                data = self.annotationmanager.getTileAnnotation(self.currentTileLocation)
                for nameCategory, contentCategory in data.items():
                    type = self.annotationmanager.getCategoryType(nameCategory)
                    if type == "Dot":
                        for indexGroup, contentGroup in contentCategory.items():
                            for index, point in enumerate(contentGroup):
                                node = NodeSingleMark(20, nameCategory=nameCategory, indexGroup=indexGroup,
                                                      locationTile=self.currentTileLocation, index=index)
                                node.setColorMain(QtGui.QColor(*self.annotationmanager.getCategoryColor(nameCategory)))
                                node.setPos(point[0], point[1])
                                node.setObvious(False)
                                self.ui.centralscene.addItem(node)
                    elif type == "Rectangle":
                        for indexGroup, contentGroup in contentCategory.items():
                            for index, rectinfo in enumerate(contentGroup):
                                rect = RectangleMark(rectinfo[2:], nameCategory=nameCategory, indexGroup=indexGroup,
                                                      locationTile=self.currentTileLocation, index=index)
                                rect.setColorFrame(QtGui.QColor(*self.annotationmanager.getCategoryColor(nameCategory)))
                                rect.setPos(*rectinfo[:2])
                                rect.setObvious(False)
                                self.ui.centralscene.addItem(rect)
                    elif type == "Polygon":
                        for indexGroup, contentGroup in contentCategory.items():
                            nodeLast = None
                            nodeFirst = None
                            for index, nodePos in enumerate(contentGroup):
                                node = NodePolyMark(2, nameCategory=nameCategory, indexGroup=indexGroup,
                                                      locationTile=self.currentTileLocation, index=index)
                                node.setZValue(3)
                                node.setColorMain(QtGui.QColor(*self.annotationmanager.getCategoryColor(nameCategory)))
                                node.setPos(*nodePos)
                                node.setObvious(False)
                                self.ui.centralscene.addItem(node)
                                if nodeLast is not None:
                                    line = QtCore.QLineF(nodeLast.scenePos(), QtCore.QPointF(*nodePos))
                                    qline = EdgePoly(line)
                                    qline.setPen(
                                        QtGui.QPen(QtGui.QColor(64, 64, 64, 192), 2, QtCore.Qt.PenStyle.SolidLine,
                                                   QtCore.Qt.PenCapStyle.RoundCap))
                                    qline.setNodeFront(nodeLast)
                                    qline.setNodeBack(node)
                                    nodeLast.setEdgeBack(qline)
                                    node.setEdgeFront(qline)
                                    self.ui.centralscene.addItem(qline)
                                    if index == len(contentGroup) - 1:
                                        line = QtCore.QLineF(node.scenePos(), nodeFirst.scenePos())
                                        qline = EdgePoly(line)
                                        qline.setPen(
                                            QtGui.QPen(QtGui.QColor(64, 64, 64, 192), 2, QtCore.Qt.PenStyle.SolidLine,
                                                       QtCore.Qt.PenCapStyle.RoundCap))
                                        qline.setNodeFront(node)
                                        qline.setNodeBack(nodeFirst)
                                        node.setEdgeBack(qline)
                                        nodeFirst.setEdgeFront(qline)
                                        self.ui.centralscene.addItem(qline)
                                else:
                                    nodeFirst = node
                                    self.ui.centralscene.nodeFirst = node
                                nodeLast = node
        self.ui.centralscene.update()
        # macro view
        self.ui.graphicsScene_overview.rect.setRect(0, 0, self.imageCentralBGI.shape[1] / self.ratioCM,
                                                    self.imageCentralBGI.shape[0] / self.ratioCM)
        self.ui.graphicsScene_overview.rect.setPos(self.currentTileLocation[0] * self.widthMacroTile,
                                                   self.currentTileLocation[1] * self.heightMacroTile)
        # direction state
        self.readableIndex = self.indexReadalbe(self.currentTileLocation)
        self.SignalStateButtonGroups.emit(self.readableIndex)

    def indexReadalbe(self, location=(0, 0)):

        assert (0 <= location[0] < self.numTileX) and (0 <= location[1] < self.numTileY), "the location is out of the range"

        indexX = location[0]
        indexY = location[1]
        if indexX == 0:
            if indexY == 0:
                return [0, 0, 0, 1, 1, 1, 0, 0] # left-top, top, right-top, right, right-bottom, bottom, left-bottom, left
            elif indexY == self.numTileY - 1:
                return [0, 1, 1, 1, 0, 0, 0, 0]
            else:
                return [0, 1, 1, 1, 1, 1, 0, 0]
        elif indexX == self.numTileX - 1:
            if indexY == 0:
                return [0, 0, 0, 0, 0, 1, 1, 1]
            elif indexY == self.numTileY - 1:
                return [1, 1, 0, 0, 0, 0, 0, 1]
            else:
                return [1, 1, 0, 0, 0, 1, 1, 1]
        else:
            if indexY == 0:
                return [0, 0, 0, 1, 1, 1, 1, 1]
            elif indexY == self.numTileY - 1:
                return [1, 1, 1, 1, 0, 0, 0, 1]
            else:
                return [1, 1, 1, 1, 1, 1, 1, 1]

    @Slot()
    def slot_topLeft(self):

        self.setLocation((self.currentTileLocation[0] - 1, self.currentTileLocation[1] - 1))

    @Slot()
    def slot_top(self):

        self.setLocation((self.currentTileLocation[0], self.currentTileLocation[1] - 1))

    @Slot()
    def slot_topRight(self):

        self.setLocation((self.currentTileLocation[0] + 1, self.currentTileLocation[1] - 1))

    @Slot()
    def slot_right(self):

        self.setLocation((self.currentTileLocation[0] + 1, self.currentTileLocation[1]))

    @Slot()
    def slot_bottomRight(self):

        self.setLocation((self.currentTileLocation[0] + 1, self.currentTileLocation[1] + 1))

    @Slot()
    def slot_bottom(self):

        self.setLocation((self.currentTileLocation[0], self.currentTileLocation[1] + 1))

    @Slot()
    def slot_bottomLeft(self):

        self.setLocation((self.currentTileLocation[0] - 1, self.currentTileLocation[1] + 1))

    @Slot()
    def slot_left(self):

        self.setLocation((self.currentTileLocation[0] - 1, self.currentTileLocation[1]))

    @Slot()
    def slot_view_radiobutton(self):

        # print("slot_view_radiobutton")
        if self.ui.radioButton_view.isChecked():
            # print("currentt: ", self.ui.stackedWidget.currentIndex())
            self.ui.stackedWidget.setCurrentIndex(0)
            # print("after: ", self.ui.stackedWidget.currentIndex())

    @Slot()
    def slot_annotation_radiobutton(self):

        # print("slot_annotation_radiobutton")
        if self.ui.radioButton_annotation.isChecked():
            # print("currentt: ", self.ui.stackedWidget.currentIndex())
            self.ui.stackedWidget.setCurrentIndex(1)
            self.slot_annotation()
            # print("after: ", self.ui.stackedWidget.currentIndex())
            if not self.annotationmanager:
                if self.hasImage():
                    self.annotationmanager = TileAnnotationManager(pathFile=self.pathFile,
                                                                   categories=0,
                                                                   widthImage=self.widthCentralImage,
                                                                   heightImage=self.heightCentralImage,
                                                                   widthTile=self.widthTile,
                                                                   heightTile=self.heightTile,
                                                                   mainwindow=mainwindow)
                else:
                    self.annotationmanager = TileAnnotationManager(pathFile="",
                                                                   categories=0,
                                                                   widthImage=self.widthCentralImage,
                                                                   heightImage=self.heightCentralImage,
                                                                   widthTile=self.widthTile,
                                                                   heightTile=self.heightTile,
                                                                   mainwindow=mainwindow)

    @Slot()
    def slot_open_filedialog(self):

        if self.sender().objectName() == "action_Open":
            fileDialog = QtWidgets.QFileDialog(self)
            fileDialog.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)
            fileDialog.setWindowTitle("image select")
            if os.path.exists(self.pathExtrainfo):
                with open(self.pathExtrainfo, "r") as file:
                    directoryUsual = file.readline()
                    directory = QtCore.QDir(directoryUsual)
            else:
                directory = QtCore.QDir("F:\\Lab\\yyc")
            fileDialog.setDirectory(directory)
            fileDialog.setNameFilter("Olympus VSI(*.vsi)")
            fileDialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
            fileDialog.show()
            fileDialog.fileSelected.connect(self.slot_open_wsi)
        elif self.sender().objectName() == "action_Export_xml":
            fileDialog = QtWidgets.QFileDialog(self)
            fileDialog.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
            fileDialog.setWindowTitle("xml path setting")
            directory = QtCore.QDir("F:\\Lab")
            fileDialog.setDirectory(directory)
            fileDialog.setNameFilter("Extensible Markup Language(*.xml)")
            fileDialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
            fileDialog.show()
            fileDialog.fileSelected.connect(self.slot_export_xml)
        elif self.sender().objectName() == "action_Export_mask":
            fileDialog = QtWidgets.QFileDialog(self)
            fileDialog.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
            fileDialog.setWindowTitle("mask path setting")
            directory = QtCore.QDir("F:\\Lab")
            fileDialog.setDirectory(directory)
            fileDialog.setNameFilters(["Specified Image Format(*.tif, *.tiff)", "General Image Format(*.png, *jpg)"])
            fileDialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
            fileDialog.show()
            fileDialog.fileSelected.connect(self.slot_export_mask)

    @Slot()
    def slot_open_filedialog_before_close(self):

        fileDialog = QtWidgets.QFileDialog(self)
        fileDialog.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
        fileDialog.setWindowTitle("xml path setting")
        directory = QtCore.QDir("F:\\Lab")
        fileDialog.setDirectory(directory)
        fileDialog.setNameFilter("Extensible Markup Language(*.xml)")
        fileDialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
        fileDialog.show()
        fileDialog.fileSelected.connect(self.slot_export_xml_and_close)

    @Slot()
    def slot_open_filedialog_before_quit(self):

        fileDialog = QtWidgets.QFileDialog(self)
        fileDialog.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
        fileDialog.setWindowTitle("xml path setting")
        directory = QtCore.QDir("F:\\Lab")
        fileDialog.setDirectory(directory)
        fileDialog.setNameFilter("Extensible Markup Language(*.xml)")
        fileDialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
        fileDialog.show()
        fileDialog.fileSelected.connect(self.slot_export_xml_and_quit)

    @Slot(str)
    def slot_export_xml(self, pathFile:str):

        self.annotationmanager.exportXml(pathFile)

    @Slot(str)
    def slot_export_xml_and_close(self, pathFile: str):

        self.annotationmanager.exportXml(pathFile)
        self.slot_close_image()

    @Slot(str)
    def slot_export_xml_and_quit(self, pathFile: str):

        self.annotationmanager.exportXml(pathFile)
        self.close()

    @Slot(str)
    def slot_export_mask(self, pathFile:str):

        self.annotationmanager.exportMask(pathFile)

    @Slot()
    def slot_askfor_close(self):

        if self.annotationmanager is not None:
            discardDialog = DiscardDialog(self)
            discardDialog.setObjectName("mmp")
            # discardDialog.accepted.connect(self.ui.action_Export_xml.trigger)
            discardDialog.accepted.connect(self.slot_open_filedialog_before_close)
            discardDialog.SignalDiscard.connect(self.slot_close_image)
            discardDialog.show()
        else:
            self.slot_close_image()

    @Slot()
    def slot_askfor_quit(self):

        if self.annotationmanager is not None:
            discardDialog = DiscardDialog(self)
            discardDialog.ui.label.setText("Do you want to save annotation file before quit?\n"
                                            "If you don\'t save it, all you did will be lost!")
            discardDialog.accepted.connect(self.slot_open_filedialog_before_quit)
            discardDialog.SignalCancel.connect(self.slot_cancel_quit)
            discardDialog.SignalDiscard.connect(self.close)
            discardDialog.show()
        else:
            self.close()

    @Slot()
    def slot_cancel_quit(self):

        self.FlagQuiting = False

    @Slot()
    def slot_close_image(self):

        print("Closing!")
        self.FlagExistingImage = False
        self.initial()

    @Slot()
    def slot_open_categorydialog(self):

        if self.annotationmanager is None:
            if self.hasImage():
                self.annotationmanager = TileAnnotationManager(pathFile=self.pathFile,
                                                               categories=0,
                                                               widthImage=self.widthCentralImage,
                                                               heightImage=self.heightCentralImage,
                                                               widthTile=self.widthTile,
                                                               heightTile=self.heightTile,
                                                               mainwindow=self)
            else:
                self.annotationmanager = TileAnnotationManager(pathFile="",
                                                               categories=0,
                                                               widthImage=self.widthCentralImage,
                                                               heightImage=self.heightCentralImage,
                                                               widthTile=self.widthTile,
                                                               heightTile=self.heightTile,
                                                               mainwindow=mainwindow)
        nameDefault = "Category_" + str(self.annotationmanager.getCategoryCount())
        categoryDialog = CategoryDialog(self)
        categoryDialog.ui.lineEdit.setText(nameDefault)
        categoryDialog.SignalCategoryInfo.connect(self.slot_add_category)
        categoryDialog.show()

    @Slot()
    def slot_add_category(self, infoCategory):

        print("info: ", infoCategory)
        # tree widget
        itemCategory = QtWidgets.QTreeWidgetItem(self.ui.treeWidget)
        nameCategory = infoCategory[0]
        valueCategory = infoCategory[1]
        colorCategory = infoCategory[2]
        typeCategory = infoCategory[3]
        self.annotationmanager.addCategory(categoryName=nameCategory,
                                           categoryColor=colorCategory,
                                           categoryType=typeCategory,
                                           categoryValue=valueCategory)
        self.annotationmanager.setCurrentNameCategory(nameCategory)
        itemCategory.setText(0, nameCategory)
        itemCategory.setText(1, str(valueCategory))
        itemCategory.setTextAlignment(1, QtCore.Qt.AlignCenter)
        itemCategory.setBackground(2, QtGui.QBrush(QtGui.QColor(*infoCategory[2])))
        itemCategory.setText(3, str(self.annotationmanager.getGroupsCount(nameCategory)))
        itemCategory.setTextAlignment(3, QtCore.Qt.AlignCenter)
        itemCategory.setText(4, typeCategory)
        self.ui.treeWidget.addTopLevelItem(itemCategory)
        self.ui.pushButton_delete.setEnabled(True)

    @Slot()
    def slot_open_wsi(self, pathFile):

        if not os.path.exists(self.pathExtrainfo):
            with open(self.pathExtrainfo, "w") as file:
                file.write(os.path.dirname(pathFile))
        else:
            with open(self.pathExtrainfo, "w") as file:
                file.write(os.path.dirname(pathFile))
        print("slot_open_wsi running")
        print("file selected: ", pathFile)
        self.pathFile = pathFile
        self.setCursor(QtCore.Qt.WaitCursor)
        self.FlagExistingImage = True
        filename = os.path.basename(self.pathFile)
        self.ui.statusbar.filenameStatus.setText(filename)
        self.ui.statusbar.filenameStatus.setToolTip(self.pathFile)
        self.ui.statusbar.scaleStatus.setText("{:.2f}%".format(100.0))
        extension = self.pathFile.split(".")[-1]
        # Olympus VSI(*.vsi)
        if extension == "vsi":
            self.open_vsi(self.pathFile)
        else:
            pass

    def open_vsi(self, pathFile):

        self.reader = VsiReader(pathFile)
        # Information Display
        parser = XmlParser(self.reader.getMetadata())
        dictInfo = parser.vsi_infoextract()
        layerDialog = LayerDialog(self)
        layerDialog.setup(dictInfo)
        layerDialog.SignalLayer.connect(self.slot_set_layer)
        layerDialog.show()
        dictExchange = {"Name": "Title",
                        "SizeY": "Height",
                        "SizeX": "Width",
                        "DimensionOrder": "Order",
                        "Type": "Type",
                        "AcquisitionDate": "Time",
                        "PhysicalSizeY": "umppY",
                        "PhysicalSizeX": "umppX"}
        headerAll = [key for key in dictInfo[0].keys()]
        header = [[key, dictExchange[key]] for key in headerAll if key in dictExchange]
        headerDisplay = [element[1] for element in header]
        headerReal = [element[0] for element in header]
        self.ui.tableWidget_metadata.setColumnCount(len(headerDisplay))
        self.ui.tableWidget_metadata.setRowCount(len(dictInfo))
        self.ui.tableWidget_metadata.setHorizontalHeaderLabels(headerDisplay)
        for index_row in range(len(dictInfo)):
            for index_column in range(len(headerReal)):
                qItem = QtWidgets.QTableWidgetItem(dictInfo[index_row][headerReal[index_column]])
                qItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.tableWidget_metadata.setItem(index_row, index_column, qItem)
        self.ui.tableWidget_metadata.setColumnWidth(0, 120)
        self.ui.tableWidget_metadata.setColumnWidth(1, 50)
        self.ui.tableWidget_metadata.setColumnWidth(2, 50)
        self.ui.tableWidget_metadata.setColumnWidth(3, 50)
        self.ui.tableWidget_metadata.setColumnWidth(4, 50)
        self.ui.tableWidget_metadata.setColumnWidth(5, 50)
        self.ui.tableWidget_metadata.setColumnWidth(6, 50)
        self.ui.tableWidget_metadata.setColumnWidth(7, 50)
        # Hidden some columns
        # infoHidden = ("Order", "Type", "Time", "umppY", "umppX")
        # indexHidden = [index for index, key in enumerate(headerDisplay) if key in infoHidden]
        # print(indexHidden)
        # for index in range(len(indexHidden)):
        #     print(indexHidden[index])
        #     self.ui.tableWidget_metadata.setColumnHidden(indexHidden[index], True)

        # Turn on annotation function
        self.ui.radioButton_annotation.setEnabled(True)

    @Slot(int)
    def slot_set_layer(self, layer:int):

        # Display
        # central image display
        self.reader.setLayer(layer)  # TODO

        self.reader.setTileSize((self.widthTile, self.heightTile))
        self.widthCentralImage, self.heightCentralImage = self.reader.getCurrentSize()
        self.numTileX, self.numTileY = self.reader.getNumTile()
        self.map = np.zeros((self.numTileX, self.numTileY), np.bool)

        # macro image display
        macro_image = self.reader.getImage(0, 0, 0, self.reader.layersCount - 2)  # TODO
        self.widthMacroImage, self.heightMacroImage = self.reader.getSize(self.reader.layersCount - 2)
        self.ratioCM = self.widthCentralImage / self.widthMacroImage
        self.widthMacroTile = self.widthTile / self.ratioCM
        self.heightMacroTile = self.heightTile / self.ratioCM
        rectF = QtCore.QRectF(0, 0, macro_image.shape[1], macro_image.shape[0])
        self.ui.graphicsScene_overview.setSceneRect(rectF)
        self.ui.graphicsScene_overview.drawBGI(macro_image, macro_image.shape[1], macro_image.shape[0])
        self.ui.graphicsScene_overview.rect.update()
        # self.ui.graphicsView_overview.fitInView(QtCore.QRectF(0, 0, qImg.width(), qImg.height()),
        #                                         QtCore.Qt.KeepAspectRatioByExpanding)

        self.setLocation((0, 0))  # initial tile
        self.ui.centralscene.update()
        self.ui.centralwidget.update()
        self.ui.graphicsView_overview.update()
        self.update()
        self.ui.radioButton_view.setChecked(True)
        self.setCursor(QtCore.Qt.ArrowCursor)

    @Slot(list)
    def slot_set_location(self, location:list):

        # print("SignalLocationDBC: ", location)
        self.setLocation((int(location[0] / self.widthMacroTile), int(location[1] / self.heightMacroTile)))

    @Slot()
    def slot_annotation(self):

        # self.ui.centralscene.setMode(SceneMode.DotAnnotation)
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.radioButton_annotation.setChecked(True)

    @Slot()
    def slot_annotation_dot(self):

        self.ui.centralscene.setMode(SceneMode.DotAnnotation)
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.radioButton_annotation.setChecked(True)

    @Slot()
    def slot_annotation_polygon(self):

        self.ui.centralscene.setMode(SceneMode.PolygonAnnotion)
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.radioButton_annotation.setChecked(True)

    @Slot()
    def slot_annotation_rect(self):

        self.ui.centralscene.setMode(SceneMode.RectAnnotation)
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.radioButton_annotation.setChecked(True)

    @Slot()
    def slot_annotation_spline(self):

        self.ui.centralscene.setMode(SceneMode.SplineAnnotation)
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.radioButton_annotation.setChecked(True)

    @Slot()
    def slot_annotation_dotset(self):

        self.ui.centralscene.setMode(SceneMode.DotSetAnnotation)
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.radioButton_annotation.setChecked(True)

    @Slot()
    def slot_annotation_polyrnnpp(self):

        self.ui.centralscene.setMode(SceneMode.PolyRPPAnnotation)
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.radioButton_annotation.setChecked(True)

    # overwrite
    def keyPressEvent(self, event:QtGui.QKeyEvent):

        if event.key() == QtCore.Qt.Key_Delete:
            self.slot_delete_category_or_group()
        else:
            print(False)

if __name__ == "__main__":

    print("Start")
    QApp = QtWidgets.QApplication()
    print("Running...")
    mainwindow = TMainWindow()
    mainwindow.show()
    print("Operating...")
    sys.exit(QApp.exec_())

