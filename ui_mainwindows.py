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

from graphics import SceneMode
from ui_dialogcategory_backup import CategoryDialog
import imagesources_rc
from reader import VsiReader, XmlParser
from graphics import TGraphicsScene, YGraphicsScene, AnnotationType

import sys
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
        self.centralscene = YGraphicsScene(self.centralwidget)
        self.centralviewer = QtWidgets.QGraphicsView(self.centralscene)
        self.centralviewer.setScene(self.centralscene)
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
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
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
        self.treeWidget = QtWidgets.QTreeWidget(self.page_annotation)
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
        self.treeWidget.setColumnWidth(2, 50)
        self.treeWidget.headerItem().setTextAlignment(2, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.treeWidget.setColumnWidth(3, 60)
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
        self.pushButton_clear = QtWidgets.QPushButton(self.page_annotation)
        self.pushButton_clear.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout_5.addWidget(self.pushButton_clear)
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
        self.graphicsView_overview = QtWidgets.QGraphicsView(self.page)
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
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_Tools.menuAction())
        self.menubar.addAction(self.menuWindows.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())
        self.toolBar.addAction(self.action_Open)
        self.toolBar.addAction(self.action_Close)
        self.toolBar.addAction(self.action_Quit)
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
        self.treeWidget.headerItem().setText(1, QtWidgets.QApplication.translate("MainWindow", "Color", None, -1))
        self.treeWidget.headerItem().setText(2, QtWidgets.QApplication.translate("MainWindow", "Count", None, -1))
        self.treeWidget.headerItem().setText(3, QtWidgets.QApplication.translate("MainWindow", "Type", None, -1))
        self.pushButton_clear.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "clear all annotations of this image", None, -1))
        self.pushButton_clear.setText(QtWidgets.QApplication.translate("MainWindow", "clear", None, -1))
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
        self.pushButton_top.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Alt+Up", None, -1))
        self.pushButton_topRight.setToolTip(QtWidgets.QApplication.translate("MainWindow", "right-top", None, -1))
        self.pushButton_topRight.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "load the block on the right-top.", None, -1))
        self.pushButton_left.setToolTip(QtWidgets.QApplication.translate("MainWindow", "left", None, -1))
        self.pushButton_left.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "load the block on the left.", None, -1))
        self.pushButton_left.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Alt+Left", None, -1))
        self.pushButton_right.setToolTip(QtWidgets.QApplication.translate("MainWindow", "right", None, -1))
        self.pushButton_right.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "load the block on the right.", None, -1))
        self.pushButton_right.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Alt+Right", None, -1))
        self.pushButton_bottomLeft.setToolTip(QtWidgets.QApplication.translate("MainWindow", "left-bottom", None, -1))
        self.pushButton_bottomLeft.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "load the block on the left-bottom.", None, -1))
        self.pushButton_bottom.setToolTip(QtWidgets.QApplication.translate("MainWindow", "down", None, -1))
        self.pushButton_bottom.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "to the block below.", None, -1))
        self.pushButton_bottom.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Alt+Down", None, -1))
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
        self.actionRedo.setText(QtWidgets.QApplication.translate("MainWindow", "&Redo", None, -1))


class TMainWindow(QtWidgets.QMainWindow):
    # Signal
    stateButtonGroups = Signal(list)

    def __init__(self):
        super(TMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # flag
        self.existingImage = False

        # element
        self.reader = None
        self.map = None
        self.numTileX = float("inf")
        self.numTileY = float("inf")
        self.heightTile = 720
        self.widthTile = 1280
        self.widthCentralImage = float("inf")
        self.heightCentralImage = float("inf")
        self.heightMacroTile = float("inf")
        self.widthMacroTile = float("inf")
        self.widthMacroImage = float("inf")
        self.heightMacroImage = float("inf")
        self.currentLocation = (float("inf"), float("inf"))  # (x, y)
        self.imageCentralBGI = None
        self.ratioCM = float("inf")
        self.annotationmanager = None

        # action setup
        # old modality of connect
        # QtCore.QObject.connect(self.ui.action_Open, QtCore.SIGNAL("triggered(bool)"), self.slot_open_filedialog)
        # new and pythonic modality of connect
        self.ui.action_Open.triggered.connect(self.slot_open_filedialog)
        self.ui.action_Close.triggered.connect(self.slot_close_image)
        self.ui.action_Quit.triggered.connect(self.close)
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
        self.stateButtonGroups.connect(self.setPButtonGroupEnable)
        self.ui.actionDotAnnotation.triggered.connect(self.slot_annotation_dot)
        self.ui.actionRectangleAnnotation.triggered.connect(self.slot_annotation_rect)
        self.ui.actionPolygonAnnotation.triggered.connect(self.slot_annotation_polygon)
        self.ui.actionDotsetAnnotation.triggered.connect(self.slot_annotation_dotset)
        self.ui.actionSpineAnnotation.triggered.connect(self.slot_annotation_spline)
        self.ui.actionPolygonRnn.triggered.connect(self.slot_annotation_polyrnnpp)
        self.ui.pushButton_new.clicked.connect(self.slot_new_category)
        self.ui.pushButton_add.clicked.connect(self.slot_add_group)
        self.ui.treeWidget.itemClicked.connect(self.slot_treeItem)

        # initial
        self.initial()

    def initial(self):

        # element
        self.reader = None
        self.map = None
        self.numTileX = float("inf")
        self.numTileY = float("inf")
        self.heightTile = 720
        self.widthTile = 1280
        self.widthCentralImage = float("inf")
        self.heightCentralImage = float("inf")
        self.heightMacroTile = float("inf")
        self.widthMacroTile = float("inf")
        self.widthMacroImage = float("inf")
        self.heightMacroImage = float("inf")
        self.currentLocation = (float("inf"), float("inf"))  # (x, y)
        self.imageCentralBGI = None
        self.ratioCM = float("inf")
        self.annotationmanager = None

        # PushButton Groups Initial
        self.ui.pushButton_topLeft.setEnabled(False)
        self.ui.pushButton_top.setEnabled(False)
        self.ui.pushButton_topRight.setEnabled(False)
        self.ui.pushButton_right.setEnabled(False)
        self.ui.pushButton_bottomRight.setEnabled(False)
        self.ui.pushButton_bottom.setEnabled(False)
        self.ui.pushButton_bottomLeft.setEnabled(False)
        self.ui.pushButton_left.setEnabled(False)
        #Annotation Switch
        self.ui.radioButton_annotation.setEnabled(False)
        # Annotation PushButton Initial
        self.ui.pushButton_add.setEnabled(False)
        self.ui.pushButton_save.setEnabled(False)
        self.ui.pushButton_clear.setEnabled(False)

    def hasImage(self):

        return self.existingImage

    @Slot()
    def slot_add_group(self):

        itemParent = self.ui.treeWidget.currentItem()
        nameCategory = itemParent.text(0)
        itemGroup = QtWidgets.QTreeWidgetItem(itemParent)
        itemGroup.setText(0, str(self.annotationmanager.getGroupsCount(nameCategory)))
        itemGroup.setBackground(1, QtGui.QBrush(QtGui.QColor(*self.annotationmanager.getCategoryColor(
            self.annotationmanager.getCurrentNameCategory()))))
        itemGroup.setText(2, str(0))
        itemGroup.setText(3, str(self.annotationmanager.getCategoryType(
            self.annotationmanager.getCurrentNameCategory())))
        self.ui.treeWidget.currentItem().addChild(itemGroup)
        self.annotationmanager.addGroup(nameCategory)
        self.ui.treeWidget.currentItem().setText(2, str(self.annotationmanager.getGroupsCount(nameCategory)))

    @Slot()
    def slot_treeItem(self, item:QtWidgets.QTreeWidgetItem, column:int):

        # Category
        if item.parent() is None:
            self.annotationmanager.currentCategoryName = item.text(0)
            self.ui.treeWidget.setCurrentItem(item)
            # index = self.ui.treeWidget.indexFromItem(item, column).row()
            # Enable PushButton
            self.ui.pushButton_clear.setEnabled(True)
            self.ui.pushButton_add.setEnabled(True)
        # Group
        else:
            self.annotationmanager.currentCategoryName = item.parent().text(0)
            self.ui.treeWidget.setCurrentItem(item)
            self.annotationmanager.setCurrentColor(self.annotationmanager.getCategoryColor(
                self.annotationmanager.getCurrentNameCategory()))
            # index = self.ui.treeWidget.indexFromItem(item, column).row()
            # Enable PushButton
            self.ui.pushButton_clear.setEnabled(True)
            self.ui.pushButton_add.setEnabled(False)
            # mode
            if item.text(3) == "Dot":
                self.ui.centralscene.setMode(SceneMode.DotAnnotation)
                self.ui.centralscene.setColorMain(self.annotationmanager.getCurrentColor())
                self.annotationmanager.setCurrentColor(self.annotationmanager.getCategoryColor(
                    self.annotationmanager.getCurrentNameCategory()))
            elif item.text(3) == "DotSet":
                self.ui.centralscene.setMode(SceneMode.DotSetAnnotation)
            elif item.text(3) == "Rectangle":
                self.ui.centralscene.setMode(SceneMode.RectAnnotation)
            elif item.text(3) == "Polygon":
                self.ui.centralscene.setMode(SceneMode.PolygonAnnotion)
            elif item.text(3) == "Spline":
                self.ui.centralscene.setMode(SceneMode.SplineAnnotation)

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
        QtWidgets.QMainWindow.closeEvent(self, event)
        print("LabelU Finish")

    def setLocation(self, location=(0, 0)):

        assert (0 <= location[0] < self.numTileX) and (0 <= location[1] < self.numTileY), "the location is out of the range"

        self.currentLocation = location
        # central view
        self.imageCentralBGI, (_, (self.widthTile, self.heightTile)) = self.reader.getTile(self.currentLocation[0],                                                                                     self.currentLocation[1])
        painter = QtGui.QPainter()
        self.ui.centralscene.setBGI(self.imageCentralBGI)
        self.ui.centralscene.setSceneRect(0, 0, self.widthTile, self.heightTile)
        self.ui.centralscene.drawBackground(painter, QtCore.QRectF(0, 0, self.widthTile, self.heightTile))
        self.ui.centralscene.update()
        # macro view
        self.ui.graphicsScene_overview.rect.setRect(0, 0, self.imageCentralBGI.shape[1] / self.ratioCM,
                                                    self.imageCentralBGI.shape[0] / self.ratioCM)
        self.ui.graphicsScene_overview.rect.setPos(self.currentLocation[0] * self.widthMacroTile,
                                                   self.currentLocation[1] * self.heightMacroTile)
        # direction state
        self.readableIndex = self.indexReadalbe(self.currentLocation)
        self.stateButtonGroups.emit(self.readableIndex)

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

        self.setLocation((self.currentLocation[0] - 1, self.currentLocation[1] - 1))

    @Slot()
    def slot_top(self):

        self.setLocation((self.currentLocation[0], self.currentLocation[1] - 1))

    @Slot()
    def slot_topRight(self):

        self.setLocation((self.currentLocation[0] + 1, self.currentLocation[1] - 1))

    @Slot()
    def slot_right(self):

        self.setLocation((self.currentLocation[0] + 1, self.currentLocation[1]))

    @Slot()
    def slot_bottomRight(self):

        self.setLocation((self.currentLocation[0] + 1, self.currentLocation[1] + 1))

    @Slot()
    def slot_bottom(self):
        self.setLocation((self.currentLocation[0], self.currentLocation[1] + 1))

    @Slot()
    def slot_bottomLeft(self):

        self.setLocation((self.currentLocation[0] - 1, self.currentLocation[1] + 1))

    @Slot()
    def slot_left(self):

        self.setLocation((self.currentLocation[0] - 1, self.currentLocation[1]))

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
            self.annotationmanager = AnnotationManager(categories=0,
                                                       widthImage=self.widthCentralImage,
                                                       heightImage=self.heightCentralImage,
                                                       widthTile=self.widthTile,
                                                       heightTile=self.heightTile)

    @Slot()
    def slot_open_filedialog(self):

        fileDialog = QtWidgets.QFileDialog(self)
        fileDialog.setWindowTitle("image select")
        directory = QtCore.QDir("K:\\yyc")
        fileDialog.setDirectory(directory)
        fileDialog.setNameFilter("Olympus VSI(*.vsi)")
        fileDialog.show()
        # QtCore.QObject.connect(fileDialog, QtCore.SIGNAL("fileSelected(QString)"), self.slot_open_wsi)
        fileDialog.fileSelected.connect(self.slot_open_wsi)

    @Slot()
    def slot_close_image(self):

        self.existingImage = False
        if self.reader is not None:
            self.reader.__delete__()
        self.initial()

    @Slot()
    def slot_new_category(self):

        if self.annotationmanager is None:
            self.annotationmanager = AnnotationManager(categories=0,
                                                       widthImage=self.widthCentralImage,
                                                       heightImage=self.heightCentralImage,
                                                       widthTile=self.widthTile,
                                                       heightTile=self.heightTile)
        nameDefault = "Category_" + str(self.annotationmanager.categories)
        self.annotationmanager.addCategory(categoryName=nameDefault,
                                           categoryColor=[0, 0, 0, 0],
                                           categoryType=AnnotationType.Dot)
        self.annotationmanager.currentCategornName = nameDefault
        # tree widget
        itemCategory = QtWidgets.QTreeWidgetItem(self.ui.treeWidget)
        itemCategory.setText(0, self.annotationmanager.currentCategoryName)
        itemCategory.setBackground(1, QtGui.QBrush(QtGui.QColor(*self.annotationmanager.getCategoryColor(
            self.annotationmanager.getCurrentCategoryName()))))
        itemCategory.setText(2, str(self.annotationmanager.getGroupsCount(
            self.annotationmanager.getCurrentCategoryName())))
        itemCategory.setText(3, str(self.annotationmanager.getCategoryType(
            self.annotationmanager.getCurrentCategoryName())))
        self.ui.treeWidget.addTopLevelItem(itemCategory)
        self.ui.pushButton_clear.setEnabled(True)
        # dialog
        categoryDialog = CategoryDialog(self)
        categoryDialog.ui.lineEdit.setText(nameDefault)
        categoryDialog.Color.connect(self.slot_annotationcolor)
        categoryDialog.AnnotationType.connect(self.slot_annotationtype)
        categoryDialog.CategoryName.connect(self.slot_categoryname)
        categoryDialog.show()

    @Slot(str)
    def slot_categoryname(self, name:str):

        self.annotationmanager.changeName(name, self.annotationmanager.currentCategoryName)
        self.annotationmanager.currentCategoryName = name
        # Tree Widget
        self.ui.treeWidget.topLevelItem(self.annotationmanager.categoriesInfo[name][3]).setText(0, name)

    @Slot(str)
    def slot_annotationtype(self, typeAnnotation:str):
        """
        :param typeAnnotation:
        Dot = 1
        Polyg = 2
        Rect = 3
        Spline = 4
        DotSet = 5
        """

        self.annotationmanager.changeType(typeAnnotation, self.annotationmanager.currentCategoryName)
        self.ui.treeWidget.topLevelItem(
            self.annotationmanager.categoriesInfo[self.annotationmanager.currentCategoryName][3]).setText(3, typeAnnotation)

    @Slot(list)
    def slot_annotationcolor(self, color:list):

        self.annotationmanager.changeColor(color, self.annotationmanager.currentCategoryName)
        self.ui.treeWidget.topLevelItem(
            self.annotationmanager.categoriesInfo[self.annotationmanager.currentCategoryName][3]).setBackground(
            1, QtGui.QBrush(QtGui.QColor(*color)))


    @Slot()
    def slot_open_wsi(self, pathFile):

        print("slot_open_wsi running")
        print("file selected: ", pathFile)
        self.existingImage = True
        extension = pathFile.split(".")[-1]
        # Olympus VSI(*.vsi)
        if extension == "vsi":
            self.reader = VsiReader(path=pathFile)
            # Information Display
            parser = XmlParser(self.reader.getMetadata())
            dictInfo = parser.vsi_infoextract()
            dictExchange = {"Name":"Title",
                            "SizeY":"Height",
                           "SizeX":"Width",
                           "DimensionOrder":"Order",
                           "Type":"Type",
                           "AcquisitionDate":"Time",
                           "PhysicalSizeY":"umppY",
                           "PhysicalSizeX":"umppX"}
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

            # Image Display
            seriesCount = self.reader.rdr.getSeriesCount()
            # central image display
            self.reader.setLayer(6)  # TODO

            self.reader.setTileSize((self.widthTile, self.heightTile))
            self.widthCentralImage, self.heightCentralImage = self.reader.getCurrentSize()
            self.numTileX, self.numTileY = self.reader.getNumTile()

            # macro image display
            macro_image = self.reader.getImage(0, 0, 0, self.reader.layersCount - 2)  # TODO
            self.widthMacroImage, self.heightCentralImage = self.reader.getSize(self.reader.layersCount - 2)
            self.ratioCM = self.widthCentralImage / self.widthMacroImage
            self.widthMacroTile = self.widthTile / self.ratioCM
            self.heightMacroTile = self.heightTile / self.ratioCM
            qImg = qimage2ndarray.array2qimage(macro_image)
            rectF = QtCore.QRectF(0, 0, qImg.width(), qImg.height())
            self.ui.graphicsScene_overview.setSceneRect(rectF)
            self.ui.graphicsScene_overview.drawBGI(qImg, qImg.width(), qImg.height())
            self.ui.graphicsScene_overview.rect.update()
            # self.ui.graphicsView_overview.fitInView(QtCore.QRectF(0, 0, qImg.width(), qImg.height()),
            #                                         QtCore.Qt.KeepAspectRatioByExpanding)

            self.setLocation((0, 0))  # initial tile
            self.ui.centralscene.update()
            self.ui.centralwidget.update()
            self.ui.graphicsView_overview.update()
            self.update()
            self.ui.radioButton_view.setChecked(True)

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


# annotation item:
    # format: dict
    # first index: x num of tile > {first index:{}}
    # second index: y num of tile > {second index:{}}
    # third index: class / category index of annotation > {third index(name): {color, counter, type, []]}}
    # fourth index: Nth set of a class > [fourth index(int): [dot/dotset]]


# class AnnotationManager(object):
#
#     def __init__(self, categories, widthImage, heightImage, widthTile, heightTile, numTileX=None, numTileY=None):
#
#         super(AnnotationManager, self).__init__()
#         self.categories = categories
#         self.heightTile = heightTile
#         self.widthTile = widthTile
#         self.widthImage = widthImage
#         self.heightImage = heightImage
#         if numTileX is None:
#             self.numTileX = self.widthImage // self.widthTile + \
#                             int(self.widthImage % self.widthTile > 0)
#         if numTileY is None:
#             self.numTileY = self.heightImage // self.heightTile + \
#                             int(self.heightImage % self.heightTile > 0)
#         self.body = {}
#         self.categoriesInfo = {}
#         self.currentCategoryName = None
#         self.currentColor = []
#         self.currentType = None
#
#     def addCategory(self, categoryName=None, categoryColor=(0, 0, 255, 255), counter=0,
#                     categoryType:AnnotationType=AnnotationType.Dot, indexInTree:int=None):
#
#         if categoryName is None:
#             categoryName = "category_" + str(self.categories)
#         self.currentCategoryName = categoryName
#         if indexInTree is None:
#             categoryInfo = [categoryColor, counter, categoryType, self.categories]
#         else:
#             categoryInfo = [categoryColor, counter, categoryType, indexInTree]
#         self.categoriesInfo[categoryName] = categoryInfo
#         self.body[categoryName] = []
#         self.categories += 1
#
#     def addGroup(self, nameCategory:str):
#
#         assert nameCategory in self.categoriesInfo and nameCategory in self.body, "nameCategory Error"
#
#         self.body[nameCategory].append([0, []])
#         self.categoriesInfo[nameCategory][1] += 1
#
#     def addPoint(self, nameCategory, indexGroup, point):
#
#         assert nameCategory in self.categoriesInfo and nameCategory in self.body, "nameCategory Error"
#         assert 0 <= indexGroup < len(self.body[nameCategory]), "indexGroup Error"
#         assert isinstance(point, list) or isinstance(point, tuple), "point Error"
#
#         self.body[nameCategory][indexGroup][1].append(list(point))
#         self.body[nameCategory][indexGroup][0] += 1
#
#     def addPoints(self, nameCategory, indexGroup, *points):
#
#         assert nameCategory in self.categoriesInfo and nameCategory in self.body, "nameCategory Error"
#         assert 0 <= indexGroup < len(self.body[nameCategory]), "indexGroup Error"
#
#         for point in points:
#             self.body[nameCategory][indexGroup][1].append(list(point))
#         self.body[nameCategory][indexGroup][0] += len(points)
#
#     def changeName(self, newName, originalName=None):
#
#         assert newName in self.categoriesInfo or newName != originalName, "NewName Error"
#         if originalName is None:
#             originalName = self.currentCategoryName
#         else:
#             assert originalName in self.categoriesInfo, "originalName Error"
#
#         self.categoriesInfo[newName] = self.categoriesInfo.pop(originalName)
#         self.body[newName] = self.body.pop(originalName)
#
#     def changeColor(self, newColor, targetCategory=None):
#
#         if targetCategory is None:
#             targetCategory = self.currentCategoryName
#         else:
#             assert targetCategory in self.categoriesInfo, "targetCategory Error"
#
#         self.categoriesInfo[targetCategory][0] = newColor
#
#     def changeType(self, newType, targetCategory=None):
#
#         if targetCategory is None:
#             targetCategory = self.currentCategoryName
#         else:
#             assert targetCategory in self.categoriesInfo, "targetCategory Error"
#
#         self.categoriesInfo[targetCategory][2] = newType
#
#     def changeValue(self, newIndex, targetCategory=None):
#
#         if targetCategory is None:
#             targetCategory = self.currentCategoryName
#         else:
#             assert targetCategory in self.categoriesInfo, "targetCategory Error"
#
#         self.categoriesInfo[targetCategory][3] = newIndex
#
#     def setCurrentColor(self, color:str):
#
#         assert isinstance(color, (list, tuple)) and len(color) == 4, "color Error"
#
#         self.currentColor = color
#
#     def setCurrentType(self, type:SceneMode):
#
#         assert isinstance(type, SceneMode), "type Error"
#
#         self.currentType = type
#
#     def printInfo(self):
#
#         print("image size:{}*{}    tile size:{}*{}    tile number:{}*{}".format(self.widthImage, self.heightImage,
#                                                                                 self.widthTile, self.heightTile,
#                                                                                 self.numTileX, self.numTileY))
#         print("Categories: {}".format(self.categories))
#         for key, value in self.categoriesInfo.items():
#             print(key, end="\t")
#             print(value)
#
#     def printCategory(self, nameCategory:str):
#
#         assert nameCategory in self.categoriesInfo, "nameCategory Error"
#
#         print(nameCategory, "[{count}]: ".format(count=len(self.body[nameCategory])))
#         for idx in range(len(self.body[nameCategory])):
#             print(self.body[nameCategory][idx])
#
#     def getCategoryCount(self):
#
#         return self.categories
#
#     def getCurrentCategoryName(self):
#
#         return self.currentCategoryName
#
#     def getCategoryColor(self, nameCategory:str):
#
#         assert nameCategory in self.categoriesInfo, "nameCategory Error"
#
#         return self.categoriesInfo[nameCategory][0] # list
#
#     def getGroupsCount(self, nameCategory:str):
#
#         assert nameCategory in self.categoriesInfo, "nameCategory Error"
#
#         return self.categoriesInfo[nameCategory][1] # int
#
#     def getCategoryType(self, nameCategory:str):
#
#         assert nameCategory in self.categoriesInfo, "nameCategory Error"
#
#         return self.categoriesInfo[nameCategory][2]
#
#     def getCurrentColor(self):
#
#         return self.currentColor
#
#     def getCurrentType(self):
#
#         return self.currentType
#
#     def addLocalBlock(self, x:int, y:int, category:str, content:list):
#
#         pass
#
#     def setup(self):
#
#         pass

if __name__ == "__main__":
    #
    # print("Start")
    # QApp = QtWidgets.QApplication()
    # print("Running...")
    # mainwindow = TMainWindow()
    # mainwindow.show()
    # print("Operating...")
    # sys.exit(QApp.exec_())

    dic = AnnotationManager(0, 100000, 80000, 1024, 1024)
    dic.addCategory("Malignang", [255, 0, 0, 0], 0, AnnotationType.Dot)
    dic.addCategory("Benign", [255, 0, 255], 0, AnnotationType.DotSet)
    dic.addCategory(categoryColor=[129, 0, 0, 230], counter=0, categoryType=AnnotationType.Rect)
    dic.changeName("Normal")
    dic.changeColor([128, 128, 128, 128], "Benign")
    dic.addGroup("Benign")
    dic.addGroup("Benign")
    dic.addPoints("Benign", 1, (100, 120), (1, 3), (4,56))
    dic.addPoint("Benign", 1, (110, 120))
    dic.addPoint("Benign", 0, (110, 120))
    dic.addGroup("Normal")
    dic.printInfo()
    dic.printCategory("Benign")
    # pass

