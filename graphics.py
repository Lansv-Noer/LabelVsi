from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import Slot, Signal
import numpy as np
import sys
import cv2
import qimage2ndarray
from reader import VsiReader
from enum import IntEnum
import math
import imagesources_rc

class SceneMode(IntEnum):

    Null = 0
    DotAnnotation = 1
    PolygonAnnotion = 2
    RectAnnotation = 3
    SplineAnnotation = 4
    DotSetAnnotation = 5
    PolyRPPAnnotation = 6

class AnnotationType(IntEnum):

    Dot = 1
    Polygon = 2
    Rect = 3
    Spline = 4
    DotSet = 5


class ImageItem(QtWidgets.QGraphicsPixmapItem):
    def __init__(self, image):
        assert isinstance(image, np.ndarray), "image must be numpy.ndarray"

        if image.dtype == np.uint8:
            pass
        elif image.dtype == np.uint16:
            image = (image / 256).astype(np.uint8)

        if image.ndim == 3:
            if image.shape[2] == 3:
                self.qImg = QtGui.QImage(image.data.tobytes(), image.shape[1], image.shape[0], image.shape[1] * image.shape[2],
                                    QtGui.QImage.Format_RGB888)
            elif image.shape[2] == 4:
                self.qImg = QtGui.QImage(image.data.tobytes(), image.shape[1], image.shape[0], image.shape[1] * image.shape[2],
                                    QtGui.QImage.Format_RGBA8888)
            else:
                print("the channels of image is invalid")
        elif image.ndim == 2:
            self.qImg = QtGui.QImage(image.data.tobytes(), image.shape[1], image.shape[0], image.shape[1] * 1,
                                QtGui.QImage.Format_Grayscale8)
        else:
            print("the dimensions of image is invalid")
        pixmap = QtGui.QPixmap.fromImage(self.qImg)
        super(ImageItem, self).__init__(pixmap)

    def setImage(self, image):
        assert isinstance(image, np.ndarray), "image must be numpy.ndarray"

        if image.dtype == np.uint8:
            pass
        elif image.dtype == np.uint16:
            image = (image / 256).astype(np.uint8)

        if image.ndim == 3:
            if image.shape[2] == 3:
                qImg = QtGui.QImage(image.data.tobytes(), image.shape[1], image.shape[0], image.shape[1] * image.shape[2],
                                    QtGui.QImage.Format_RGB888)
            elif image.shape[2] == 4:
                qImg = QtGui.QImage(image.data.tobytes(), image.shape[1], image.shape[0], image.shape[1] * image.shape[2],
                                    QtGui.QImage.Format_RGBA8888)
            else:
                print("the channels of image is invalid")
        elif image.ndim == 2:
            qImg = QtGui.QImage(image.data.tobytes(), image.shape[1], image.shape[0], image.shape[1] * 1,
                                QtGui.QImage.Format_Grayscale8)
        else:
            print("the dimensions of image is invalid")
        pixmap = QtGui.QPixmap.fromImage(qImg)
        self.setPixmap(pixmap)


class TTreeWidget(QtWidgets.QTreeWidget):

    SignalItem = Signal(QtWidgets.QTableWidgetItem, int)

    def __init__(self, parent:QtWidgets.QWidget=None):

        if parent is None:
            super(TTreeWidget, self).__init__()
        elif isinstance(parent, QtWidgets.QWidget):
            super(TTreeWidget, self).__init__(parent)





class TGraphicsScene(QtWidgets.QGraphicsScene):

    SignalLocationDBC = Signal(list)

    def __init__(self, parent, image:QtGui.QImage=None):

        if image is not None:
            assert isinstance(image, QtGui.QImage), "Error Image"

        if parent is None:
            super(TGraphicsScene, self).__init__()
        elif isinstance(parent, QtWidgets.QWidget):
            super(TGraphicsScene, self).__init__(parent)

        self.imageQBackground = image
        self.rect = QtWidgets.QGraphicsRectItem()
        self.rect.setZValue(1)
        self.rect.setPen(QtGui.QPen(QtGui.QBrush(QtGui.QColor(30, 200, 255, 200)), 2,
                                    QtCore.Qt.PenStyle.SolidLine, QtCore.Qt.PenCapStyle.SquareCap))
        self.addItem(self.rect)

    def drawBackground(self, painter:QtGui.QPainter, rect:QtCore.QRectF):

        if self.imageQBackground is None:
            return
        else:
            qImg = qimage2ndarray.array2qimage(self.imageQBackground)
            painter.drawImage(QtCore.QRectF(0, 0, self.imageQBackground.shape[1], self.imageQBackground.shape[0]), qImg)

    def setBGI(self, image:np.ndarray):  # BGI = Back Ground Image

        assert isinstance(image, np.ndarray), "Error Image"

        self.imageQBackground = image

    def drawBGI(self, image, width, height):

        assert isinstance(image, np.ndarray), "Error Image"

        self.setBGI(image)
        painter = QtGui.QPainter()
        self.drawBackground(painter, QtCore.QRectF(0, 0, width, height))

    def mouseDoubleClickEvent(self, event:QtWidgets.QGraphicsSceneMouseEvent):

        self.SignalLocationDBC.emit(list(event.scenePos().toTuple()))
        QtWidgets.QGraphicsScene.mouseDoubleClickEvent(self, event)


class TGraphicsView(QtWidgets.QGraphicsView):

    def __init__(self, parent: QtWidgets.QWidget=None):

        if parent is None:
            super(TGraphicsView, self).__init__()
        elif isinstance(parent, QtWidgets.QWidget):
            super(TGraphicsView, self).__init__(parent)

    def resizeEvent(self, event:QtGui.QResizeEvent):

        if self.scene():
            self.fitInView(self.scene().sceneRect(), QtCore.Qt.KeepAspectRatio)


# class TestGraphicsScene(QtWidgets.QGraphicsScene):
#
#     def __init__(self, parent, image:QtGui.QImage=None):
#
#         if image is not None:
#             assert isinstance(image, QtGui.QImage), "Error Image"
#
#         super(TestGraphicsScene, self).__init__(parent=parent)
#         self.imageQBackground = image
#         # self.rect = QtWidgets.QGraphicsRectItem()
#         # self.rect.setZValue(1)
#         # self.rect.setPen(QtGui.QColor(30, 200, 255, 200))
#         # self.addItem(self.rect)
#
#         # rest
#         self.currentEdge = None
#         self.flagPolygoning = False
#         eventfilter = testEventFilter(self.flagPolygoning)
#         self.installEventFilter(eventfilter)
#         self.itemsGroup = TItemsGroup()
#         self.addItem(self.itemsGroup)
#
#         # feature
#         self.mode = SceneMode.DotAnnotation
#
#     def mouseDoubleClickEvent(self, event:QtWidgets.QGraphicsSceneMouseEvent):
#
#         scenePos = event.scenePos()
#         if self.mode == SceneMode.DotAnnotation:
#             qTrans = QtGui.QTransform(1, 0, 0, 1, 0, 0)
#             itemLocal = self.itemAt(scenePos, qTrans)
#             if itemLocal is None or itemLocal is not Node:
#                 node = Node(10)
#                 node.setPos(scenePos)
#                 if self.itemsGroup is not None:
#                     clr = (128, 0, 128, 128)
#                     self.itemsGroup.setColor(QtGui.QColor(*clr))
#                     self.parent().parent()
#                     node.setColorMain(self.itemsGroup.getColor())
#                     node.setColorSub(self.itemsGroup.getColor())
#                     self.itemsGroup.addToGroup(node)
#                     node.setParentItem(self.itemsGroup)
#                 self.addItem(node)
#                 self.update()
#                 # QtWidgets.QGraphicsScene.mouseDoubleClickEvent(self, event)
#         elif self.mode == SceneMode.PolygonAnnotion:
#             qTrans = QtGui.QTransform(1, 0, 0, 1, 0, 0)
#             # print("pos: ", event.scenePos())
#             itemLocal = self.itemAt(scenePos, qTrans)
#             if (itemLocal is None) or type(itemLocal) is not Node:
#                 self.flagPolygoning = True
#                 node = Node(10)
#                 node.setPos(scenePos)
#                 self.addItem(node)
#                 self.currentEdge = Edge(event.scenePos())
#                 self.addItem(self.currentEdge)
#                 self.update()
#                 # QtWidgets.QGraphicsScene.mouseDoubleClickEvent(self, event)
#             else:
#                 print("occupied: ", type(itemLocal))
#                 print("shape in scene: ", itemLocal.shape())
#                 print("event pos: ", event.pos())
#                 print("type: ", itemLocal.contains(event.pos()))
#                 print("anchor: ", itemLocal.pointAnchor)
#
#     def mouseMoveEvent(self, event:QtWidgets.QGraphicsSceneMouseEvent):
#
#         if self.flagPolygoning == True:
#             self.currentEdge.setSlave(event.scenePos())
#             self.currentEdge.update()
#             self.update()
#         QtWidgets.QGraphicsScene.mouseMoveEvent(self, event)  # 我吃柠檬，挺甜的
#
#     def setMode(self, mode:SceneMode):
#
#         assert mode in SceneMode, "Mode Error"
#         self.mode = mode
#
#     def drawBackground(self, painter:QtGui.QPainter, rect:QtCore.QRectF):
#
#         if self.imageQBackground is None:
#             return
#         else:
#             painter.drawImage(QtCore.QRectF(0, 0, self.imageQBackground.width(), self.imageQBackground.height()),
#                               self.imageQBackground)
#
#     def setBGI(self, image:QtGui.QImage):  # BGI = Back Ground Image
#
#         assert isinstance(image, QtGui.QImage), "Error Image"
#
#         self.imageQBackground = image
#
#     def drawBGI(self, image, width, height):
#
#         assert isinstance(image, QtGui.QImage), "Error Image"
#
#         self.setBGI(image)
#         painter = QtGui.QPainter()
#         self.drawBackground(painter, QtCore.QRectF(0, 0, width, height))
#
class ItemMark(QtWidgets.QGraphicsItem):

    def __init__(self, nameCategory="", indexGroup=-1, locationTile=(-1, -1), index=1, parent:QtWidgets.QWidget=None):

        if parent is None:
            super(ItemMark, self).__init__()
        else:
            super(ItemMark, self).__init__(parent)

        # variable
        self.nameCategory = nameCategory
        self.indexGroup = indexGroup
        self.xTile, self.yTile = locationTile
        self.index = index

        #appearance
        self.obvious = True

    # self function
    def setObvious(self, obvious:bool=True):

        self.obvious = obvious
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, enabled=self.obvious)

    def setCoordinateTile(self, location: (int, int)):

        assert isinstance(location, (tuple, list)) and len(location) == 2, "Location Error"
        self.xTile, self.yTile = location

    def getXCoordinateTile(self):

        return self.xTile

    def getYCoordinateTile(self):

        return self.yTile

    def getCoordinateTile(self):

        return self.xTile, self.yTile

    def setNameCategory(self, nameCategory: str):

        self.nameCategory = nameCategory

    def getNameCategory(self):

        return self.nameCategory

    def setIndexGroup(self, indexGroup: int):

        self.indexGroup = indexGroup

    def setIndex(self, index: int):

        self.index = index

    def getIndex(self):

        return self.index

    def getIndexGroup(self):

        return self.indexGroup

    def getCategoryGroup(self):

        return self.nameCategory, self.indexGroup


class PolygonMark(ItemMark):

    def __init__(self, parent:QtWidgets.QGraphicsItem=None):

        if parent is None:
            super(PolygonMark, self).__init__()
        elif isinstance(parent, QtWidgets.QGraphicsItem):
            super(PolygonMark, self).__init__()
        else:
            raise Exception("Parent Type Error")

        self.polygon = QtGui.QPolygonF()
        self.closed = False
        self.pointFirst = None
        self.pointLast = None
        self.pointCurrent = None
        self.pointNext = None
        self.lineCurrent = None

        # appearance
        self.colorPoint = QtGui.QColor(0, 255, 0, 255)
        self.colorPointSelected = QtGui.QColor(255, 20, 20, 128)
        self.colorLine = QtGui.QColor(0, 0, 255, 255)
        self.colorLineSelected = QtGui.QColor(0, 100, 200, 128)
        self.widthLine = 3
        self.radiusPoint = 15

        # flag-public
        self.setAcceptHoverEvents(True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, enabled=True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, enabled=True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, enabled=True)
        self.setZValue(4)
        # flag-private
        self.FlagKeys = {"Ctrl": False, "Alt": False, "Shift": False}
        self.FlagButtons = {"Left": False, "Middle": False, "Right": False}
        self.FlagPainting = True


    def boundingRect(self) -> QtCore.QRectF:

        bbox = self.polygon.boundingRect()
        bbox.adjust(-self.radiusPoint, -self.radiusPoint, self.radiusPoint, self.radiusPoint)
        return bbox

    def shape(self) -> QtGui.QPainterPath:

        path = QtGui.QPainterPath()
        path.addPolygon(self.polygon)
        painter = QtGui.QPainter()
        painter.setPen(QtCore.Qt.NoPen)
        brush = QtGui.QBrush(QtGui.QColor(50, 255, 230, 100))
        painter.fillPath(path, brush)
        return path

    def paint(self, painter:QtGui.QPainter, option:QtWidgets.QStyleOptionGraphicsItem, widget:QtWidgets.QWidget=...):

        painter.setRenderHint(painter.Antialiasing)
        colorLine = self.colorLine
        colorPoint = self.colorPoint
        if option.state & QtWidgets.QStyle.State_MouseOver:
            colorPoint.setAlphaF(0.4)
            colorLine.setAlphaF(0.4)
            # print("state: mouseover")
            # if option.state & QtWidgets.QStyle.State_Sunken:
            #     pen = QtGui.QPen(QtGui.QColor(0, 255, 0))
        elif option.state & QtWidgets.QStyle.State_Selected:
            # print("state: selected")
            colorPoint.setAlphaF(0.8)
            colorLine.setAlphaF(0.8)
        else:
            pass
            # print("state: normal")
            colorPoint.setAlphaF(1)
            colorLine.setAlphaF(1)
        # print("ColorPoint: ", self.colorPoint)
        # print("ColorLine: ", self.colorLine)
        # draw Edge
        penLine = QtGui.QPen(QtGui.QBrush(colorLine), self.widthLine)
        painter.setPen(penLine)
        painter.drawPolyline(self.polygon)
        # draw Current Edge
        if self.lineCurrent is not None:
            penLine = QtGui.QPen(QtGui.QBrush(self.colorLineSelected), self.widthLine,
                                 QtCore.Qt.PenStyle.SolidLine, QtCore.Qt.PenCapStyle.RoundCap)
            painter.save()
            painter.setPen(penLine)
            painter.drawLine(self.polygon.at(self.lineCurrent), self.polygon.at(self.lineCurrent + 1))
            painter.restore()
        if self.FlagPainting is True:
            if self.pointNext is not None:
                painter.save()
                penLine = QtGui.QPen(QtGui.QBrush(self.colorLineSelected), self.widthLine,
                                     QtCore.Qt.PenStyle.DotLine, QtCore.Qt.PenCapStyle.RoundCap)
                painter.setPen(penLine)
                painter.drawLine(self.polygon.at(self.polygon.count() - 1), self.pointNext)
        # draw Node
        # for indexPoint in range(self.polygon.count()):
        penPoint = QtGui.QPen(QtGui.QBrush(colorPoint), self.radiusPoint,
                              QtCore.Qt.PenStyle.SolidLine, QtCore.Qt.PenCapStyle.RoundCap)
        painter.setPen(penPoint)
        painter.drawPoints(self.polygon)

        # draw current Node
        if self.pointCurrent is not None:
            penCurrentPoint = QtGui.QPen(QtGui.QBrush(self.colorPointSelected), self.radiusPoint, QtCore.Qt.PenStyle.SolidLine, QtCore.Qt.PenCapStyle.RoundCap)
            painter.save()
            painter.setPen(penCurrentPoint)
            painter.drawPoint(self.polygon.at(self.pointCurrent))
            painter.restore()

    def mousePressEvent(self, event:QtWidgets.QGraphicsSceneMouseEvent):

        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, enabled=True)
        if event.button() == QtCore.Qt.LeftButton:
            self.FlagButtons["Left"] = True
        # self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, enabled=True)
        pos = event.pos()
        flagPointHit = False
        for indexPoint in range(self.polygon.count()):
            point = self.polygon.at(indexPoint)
            if self.distancePP(point, pos) < self.radiusPoint:
                self.pointCurrent = indexPoint
                self.lineCurrent = None
                flagPointHit = True
                break
        if not flagPointHit:
            if self.isClosed():
                for indexPoint in range(self.polygon.count() - 1):
                    distance = self.distancePL(pos, self.polygon.at(indexPoint),
                                               self.polygon.at(indexPoint + 1))
                    if distance < 2 * self.widthLine:
                        self.lineCurrent = indexPoint
                        self.pointCurrent = None
            else:
                for indexPoint in range(self.polygon.count()):
                    distance = self.distancePL(pos, self.polygon.at(indexPoint),
                                               self.polygon.at(indexPoint + 1))
                    if distance < 2 * self.widthLine:
                        self.lineCurrent = indexPoint
                        self.pointCurrent = None
            if self.lineCurrent is not None:
                pointOnLine = self.pointPL(pos, self.polygon.at(self.lineCurrent), self.polygon.at(self.lineCurrent + 1))
                self.polygon.insert(self.lineCurrent + 1, pointOnLine)
        self.update()
        # QtWidgets.QGraphicsItem.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event:QtWidgets.QGraphicsSceneMouseEvent):

        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, enabled=False)
        if event.button() == QtCore.Qt.LeftButton:
            self.FlagButtons["Left"] = True
            self.pointCurrent = None
            self.lineCurrent = None
        print("poly: ", self.polygon)
        path = QtGui.QPainterPath()
        path.addPolygon(self.polygon)
        print("polyBox: ", path.boundingRect())
        print("bbox: ", self.boundingRect())
        self.update()
        # QtWidgets.QGraphicsItem.mouseReleaseEvent(self, event)

    def mouseMoveEvent(self, event:QtWidgets.QGraphicsSceneMouseEvent):

        pos = event.pos()
        if self.FlagButtons["Left"] is True:
            if self.pointCurrent is not None:
                if self.isClosed():
                    if self.pointCurrent == 0 or self.pointCurrent == self.polygon.count() - 1:
                        self.polygon.replace(0, pos)
                        self.polygon.replace(self.polygon.count() - 1, pos)
                    else:
                        self.polygon.replace(self.pointCurrent, pos)
                else:
                    self.movePoint(self.pointCurrent, pos)
        self.update()
        # QtWidgets.QGraphicsItem.mouseMoveEvent(self, event)

    def mouseDoubleClickEvent(self, event:QtWidgets.QGraphicsSceneMouseEvent):

        print("position: ", event.pos())
        print("Shape: ", self.shape())
        print("bbox: ", self.boundingRect())
        pos = event.pos()
        if self.FlagButtons["Left"] is True:
            if self.isClosed():
                for indexPoint in range(self.polygon.count() - 1):
                    distance = self.distancePL(pos, self.polygon.at(indexPoint),
                                               self.polygon.at(indexPoint + 1))
                    if distance < 2 * self.widthLine:
                        self.lineCurrent = indexPoint
                        self.pointCurrent = None
            else:
                for indexPoint in range(self.polygon.count()):
                    distance = self.distancePL(pos, self.polygon.at(indexPoint),
                                               self.polygon.at(indexPoint + 1))
                    if distance < 2 * self.widthLine:
                        self.lineCurrent = indexPoint
                        self.pointCurrent = None
            if self.lineCurrent is not None:
                pointOnLine = self.pointPL(pos, self.polygon.at(indexPoint), self.polygon.at(indexPoint + 1))
                self.addPoint(self.lineCurrent + 1, pointOnLine)
                print("added")
        QtWidgets.QGraphicsItem.mouseDoubleClickEvent(self, event)

    def distancePP(self, pointA:QtCore.QPointF, pointB:QtCore.QPointF):

        assert isinstance(pointA, QtCore.QPointF), "pointA Error"
        assert isinstance(pointB, QtCore.QPointF), "pointB Error"

        diff = pointA - pointB
        return (diff.x() ** 2 + diff.y() ** 2) ** (0.5)

    def distancePL(self, point:QtCore.QPointF, pointLineA:QtCore.QPointF, pointLineB:QtCore.QPointF):

        vectorA = point - pointLineA
        vectorB = pointLineB - pointLineA
        distance = abs(vectorA.x() * vectorB.y() - vectorA.y() * vectorB.x()) / \
                   ((vectorB.x() ** 2 + vectorB.y() ** 2) ** 0.5)
        return distance

    def pointPL(self, point:QtCore.QPointF, pointLineA:QtCore.QPointF, pointLineB:QtCore.QPointF):

        vectorA = point - pointLineA
        vectorB = pointLineB - pointLineA
        point = vectorB * (vectorB.x() * vectorA.x() + vectorB.y() * vectorA.y()) / \
                (vectorB.x() ** 2 + vectorB.y() ** 2) + pointLineA
        return point

    def addPoint(self, index:int, point:(QtCore.QPointF, list, tuple)):

        assert (index < self.polygon.count()), "index Error"
        assert isinstance(point, (tuple, list, QtCore.QPointF)), "point type Error"

        if isinstance(point, (list, tuple)):
            assert len(point) == 2, "point number Error"
            point = QtCore.QPointF(*point)

        self.polygon.insert(index, point)

    def appendPoint(self, point:(QtCore.QPointF, list, tuple)):

        assert isinstance(point, (tuple, list, QtCore.QPointF)), "point type Error"
        if isinstance(point, (list, tuple)):
            assert len(point) == 2, "point number Error"
            point = QtCore.QPointF(*point)

        self.polygon.append(point)

    def movePoint(self, index:int, point:(QtCore.QPointF, list, tuple)):

        assert (index < self.polygon.count()), "index Error"
        assert isinstance(point, (tuple, list, QtCore.QPointF)), "point type Error"

        if isinstance(point, (list, tuple)):
            assert len(point) == 2, "point number Error"
            point = QtCore.QPointF(*point)

        self.polygon.replace(index, point)

    def removePoint(self, index:int):

        assert (index < self.polygon.count()), "index Error"

        self.polygon.remove(index)

    def setPolygon(self, points:(list, tuple)):

        assert isinstance(points, (list, tuple)), "Points Error"

        self.polygon.clear()
        for point in points:
            self.polygon.append(QtCore.QPointF(*point))

    def setClosed(self, close:bool=True):

        self.polygon.append(self.polygon.front())
        self.update()

    def isClosed(self):

        return self.polygon.isClosed()

    def setColorPoint(self, color:(int, QtGui.QColor)):

        if isinstance(color, list):
            assert len(color) == 4, "color length Error"
            self.colorPoint = QtGui.QColor(*color)
        elif isinstance(color, QtGui.QColor):
            self.colorPoint = color

    def getColorPoint(self):

        return self.colorPoint

    def setColorLine(self, color: (int, QtGui.QColor)):

        if isinstance(color, list):
            assert len(color) == 4, "color length Error"
            self.colorLine = QtGui.QColor(*color)
        elif isinstance(color, QtGui.QColor):
            self.colorLine = color

    def getColorLine(self):

        return self.colorLine


class NodeMark(ItemMark):

    def __init__(self, radius=20, nameCategory="", indexGroup=-1, locationTile=(-1, -1),
                 index=1, parent:QtWidgets.QGraphicsItem=None):
        if parent is None:
            super(NodeMark, self).__init__(nameCategory=nameCategory, indexGroup=indexGroup,
                                           locationTile=locationTile, index=index)
        elif type(parent) is QtWidgets.QGraphicsItem:
            super(NodeMark, self).__init__(nameCategory=nameCategory, indexGroup=indexGroup,
                                           locationTile=locationTile, index=index, parent=parent)
        else:
            assert False, "Parent Error"

        # feature
        # self-feature
        self.radius = radius
        self.colorMain = QtGui.QColor(0, 255, 255, 192)
        self.colorSub = QtGui.QColor(20, 40, 150, 128)
        self.setAcceptHoverEvents(True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, enabled=True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, enabled=True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, enabled=False)
        self.setZValue(2)
        self.setCursor(QtCore.Qt.PointingHandCursor)
        # motion

        # variable

    def boundingRect(self) -> QtCore.QRectF:

        expand = 2.0
        return QtCore.QRectF(-(self.radius / 2) - expand, -(self.radius / 2) - expand,
                             self.radius + 2 * expand, self.radius + 2 * expand)

    def shape(self) -> QtGui.QPainterPath:

        path = QtGui.QPainterPath()
        path.addEllipse(-self.radius / 2, -self.radius / 2, self.radius, self.radius)
        return path

    def paint(self, painter:QtGui.QPainter, option:QtWidgets.QStyleOptionGraphicsItem, widget:QtWidgets.QWidget=...):

        colorBrush = self.colorMain
        if self.obvious:
            pass
        else:
            colorHsv = colorBrush.toHsv()
            colorBrush = colorHsv.fromHsvF(colorHsv.hueF(), 0.4 * colorHsv.saturationF(), colorHsv.valueF(), 1)
            colorBrush = colorBrush.toRgb()

        if option.state & QtWidgets.QStyle.State_MouseOver:
            colorBrush.setAlphaF(0.5)
            pen = QtCore.Qt.NoPen
            if option.state & QtWidgets.QStyle.State_Sunken:
                pen = QtGui.QPen(QtGui.QBrush(QtGui.QColor(0, 255, 0)), 1)
        else:
            colorBrush.setAlphaF(1)
            pen = QtCore.Qt.NoPen
        painter.setPen(pen)
        painter.setBrush(QtGui.QBrush(colorBrush))
        painter.drawEllipse(-self.radius / 2, -self.radius / 2, self.radius, self.radius)

        if option.state & QtWidgets.QStyle.State_Selected:
            pen = QtGui.QPen(QtGui.QBrush(QtGui.QColor(255, 0, 0)), 1)
            painter.setBrush(QtGui.QBrush(colorBrush))
            painter.drawEllipse(-self.radius / 2, -self.radius / 2, self.radius, self.radius)

    def setColorMain(self, color:QtGui.QColor):

        self.colorMain = color
        self.update()

    def setColorSub(self, color: QtGui.QColor):

        self.colorSub = color
        self.update()


class RectangleMark(ItemMark):

    def __init__(self, size: (int, int)=(0, 0), nameCategory="", indexGroup=-1,
                 locationTile=(-1, -1), index=1, parent:QtWidgets.QWidget=None):

        if parent is None:
            super(RectangleMark, self).__init__(nameCategory=nameCategory, indexGroup=indexGroup,
                                           locationTile=locationTile, index=index)
        elif type(parent) is QtWidgets.QGraphicsItem:
            super(RectangleMark, self).__init__(nameCategory=nameCategory, indexGroup=indexGroup,
                                           locationTile=locationTile, index=index, parent=parent)

        # feature
        self.width, self.height = size
        self.colorFrame = QtGui.QColor(0, 0, 0, 255)
        self.colorFill = QtGui.QColor(0, 0, 0, 0)

        # flag
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, enabled=True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, enabled=True)
        self.setAcceptHoverEvents(True)

    def shape(self) -> QtGui.QPainterPath:

        path = QtGui.QPainterPath()
        path.addRect(0, 0, self.width, self.height)
        return path

    def boundingRect(self) -> QtCore.QRectF:

        expand = 2.0
        return QtCore.QRectF(-expand, -expand, self.width + expand, self.height + expand)

    def paint(self, painter:QtGui.QPainter, option:QtWidgets.QStyleOptionGraphicsItem, widget:QtWidgets.QWidget=...):

        colorFrame = self.colorFrame
        if self.obvious:
            pass
        else:
            colorHsv = colorFrame.toHsv()
            colorFrame = colorHsv.fromHsvF(colorHsv.hueF(), 0.4 * colorHsv.saturationF(), colorHsv.valueF(), 1)
            colorFrame = colorFrame.toRgb()

        painter.setRenderHint(painter.Antialiasing)
        if option.state & QtWidgets.QStyle.State_MouseOver:
            colorBrush = QtGui.QColor(128, 255, 200, 60)
            pen = QtCore.Qt.NoPen
            if option.state & QtWidgets.QStyle.State_Sunken:
                pen = QtGui.QPen(QtGui.QColor(0, 255, 0))
        else:
            colorBrush = self.colorFill
            pen = QtGui.QPen(colorFrame)

        painter.setPen(pen)
        painter.setBrush(colorBrush)
        painter.drawRect(0, 0, self.width, self.height)

        if option.state & QtWidgets.QStyle.State_Selected:
            expand = 1
            pen = QtGui.QPen(QtGui.QColor(255, 0, 0))
            brush = QtCore.Qt.NoBrush
            painter.setPen(pen)
            painter.setBrush(brush)
            painter.drawRect(expand, expand, self.width - 2 * expand, self.height - 2 * expand)

    def mousePressEvent(self, event:QtWidgets.QGraphicsSceneMouseEvent):

        if event.button() is QtCore.Qt.LeftButton:
            self.update()
        # QtWidgets.QGraphicsItem.mousePressEvent(self, event)

    def mouseReleaseEvent(self, event:QtWidgets.QGraphicsSceneMouseEvent):

        self.update()
        QtWidgets.QGraphicsItem.mouseReleaseEvent(self, event)

    def mouseMoveEvent(self, event:QtWidgets.QGraphicsSceneMouseEvent):

        self.update()
        QtWidgets.QGraphicsItem.mouseMoveEvent(self, event)

    def setWidth(self, width:int):

        self.width = width
        self.update()

    def setHeitht(self, height:int):

        self.height = height
        self.update()

    def setSize(self, size:(list, tuple)):

        assert isinstance(size, (list, tuple)) and len(size) == 2, "size Error"
        self.width, self.height = size
        self.update()

    def setSubPoint(self, point:(list, tuple, QtCore.QPointF, QtCore.QPoint)):

        mainPoint = self.scenePos()
        if isinstance(point, (list, tuple)):
            subPoint = QtCore.QPointF(*point)
            self.width, self.height = (subPoint - mainPoint).toTuple()
        elif isinstance(point, (QtCore.QPoint, QtCore.QPointF)):
            self.width, self.height = (point - mainPoint).toTuple()
        self.update()

    def getWidth(self):

        return self.width

    def getHeight(self):

        return self.height

    def getSize(self):

        return self.width, self.height

    def setColorFrame(self, color:(int, QtGui.QColor)):

        if isinstance(color, list):
            assert len(color) == 4, "color length Error"
            self.colorFrame = QtGui.QColor(*color)
        elif isinstance(color, QtGui.QColor):
            self.colorFrame = color

    def getColorFrame(self):

        return self.colorFrame

    def setColorFill(self, color: (int, QtGui.QColor)):

        if isinstance(color, list):
            assert len(color) == 4, "color length Error"
            self.colorFill = QtGui.QColor(*color)
        elif isinstance(color, QtGui.QColor):
            self.colorFill = color

    def getColorFill(self):

        return self.colorFill


class RectMark(ItemMark):

    def __init__(self, size: (int, int) = (0, 0), nameCategory="", indexGroup=-1,
                 locationTile=(-1, -1), index=1, parent: QtWidgets.QWidget = None):

        if parent is None:
            super(RectMark, self).__init__(nameCategory=nameCategory, indexGroup=indexGroup,
                                                locationTile=locationTile, index=index)
        elif type(parent) is QtWidgets.QGraphicsItem:
            super(RectMark, self).__init__(nameCategory=nameCategory, indexGroup=indexGroup,
                                                locationTile=locationTile, index=index, parent=parent)

        width, height = size
        self.rect = QtCore.QRectF(0, 0, width, height)
        self.colorFrame = QtGui.QColor(0, 0, 0, 255)
        self.colorFill = QtGui.QColor(0, 0, 0, 0)

        # flag
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, enabled=True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, enabled=True)
        self.setAcceptHoverEvents(True)

    def shape(self) -> QtGui.QPainterPath:

        path = QtGui.QPainterPath()
        path.addRect(self.rect)
        return path

    def boundingRect(self) -> QtCore.QRectF:

        expand = 1.0
        rect = self.rect
        if self.rect.width() >= 0 and self.rect.height() > 0:
            rect.adjust(-expand, -expand, expand, expand)
        if self.rect.width() < 0 and self.rect.height() >= 0:
            rect.adjust(expand, -expand, -expand, expand)
        if self.rect.width() <= 0 and self.rect.height() < 0:
            rect.adjust(expand, expand, -expand, -expand)
        if self.rect.width() < 0 and self.rect.height() >= 0:
            rect.adjust(-expand, expand, expand, -expand)
        return rect

    def paint(self, painter:QtGui.QPainter, option:QtWidgets.QStyleOptionGraphicsItem, widget:QtWidgets.QWidget=...):

        colorFrame = self.colorFrame
        if self.obvious:
            pass
        else:
            colorHsv = colorFrame.toHsv()
            colorFrame = colorHsv.fromHsvF(colorHsv.hueF(), 0.4 * colorHsv.saturationF(), colorHsv.valueF(), 1)
            colorFrame = colorFrame.toRgb()

        painter.setRenderHint(painter.Antialiasing)
        if option.state & QtWidgets.QStyle.State_MouseOver:
            colorBrush = QtGui.QColor(128, 255, 200, 60)
            pen = QtCore.Qt.NoPen
            if option.state & QtWidgets.QStyle.State_Sunken:
                pen = QtGui.QPen(QtGui.QColor(0, 255, 0))
        else:
            colorBrush = self.colorFill
            pen = QtGui.QPen(colorFrame)

        painter.setPen(pen)
        painter.setBrush(colorBrush)
        painter.drawRect(self.rect)

        if option.state & QtWidgets.QStyle.State_Selected:
            expand = 1
            rect =self.rect
            if self.rect.width() >= 0 and self.rect.height() > 0:
                return rect.adjust(expand, expand, -expand, -expand)
            if self.rect.width() < 0 and self.rect.height() >= 0:
                return rect.adjust(-expand, expand, expand, -expand)
            if self.rect.width() <= 0 and self.rect.height() < 0:
                return rect.adjust(-expand, -expand, expand, expand)
            if self.rect.width() < 0 and self.rect.height() >= 0:
                return rect.adjust(expand, -expand, -expand, expand)
            pen = QtGui.QPen(QtGui.QColor(255, 0, 0))
            brush = QtCore.Qt.NoBrush
            painter.setPen(pen)
            painter.setBrush(brush)
            painter.drawRect(rect)

    def mousePressEvent(self, event:QtWidgets.QGraphicsSceneMouseEvent):

        if event.button() is QtCore.Qt.LeftButton:
            self.update()
        # QtWidgets.QGraphicsItem.mousePressEvent(self, event)

    def mouseReleaseEvent(self, event:QtWidgets.QGraphicsSceneMouseEvent):

        self.update()
        QtWidgets.QGraphicsItem.mouseReleaseEvent(self, event)

    def mouseMoveEvent(self, event:QtWidgets.QGraphicsSceneMouseEvent):

        self.update()
        QtWidgets.QGraphicsItem.mouseMoveEvent(self, event)

    def setRect(self, rect:(tuple, list, QtCore.QRectF)):

        assert isinstance(rect, (tuple, list, QtCore.QRectF)), "rect Error"

        if isinstance(rect, (tuple, list)):
            rect = QtCore.QRectF(*rect)
        self.rect = rect

    def getWidth(self):

        return self.rect.width()

    def getHeight(self):

        return self.rect.height()

    def getSize(self):

        return self.rect.width(), self.rect.height()

    def setColorFrame(self, color:(int, QtGui.QColor)):

        if isinstance(color, list):
            assert len(color) == 4, "color length Error"
            self.colorFrame = QtGui.QColor(*color)
        elif isinstance(color, QtGui.QColor):
            self.colorFrame = color

    def getColorFrame(self):

        return self.colorFrame

    def setColorFill(self, color: (int, QtGui.QColor)):

        if isinstance(color, list):
            assert len(color) == 4, "color length Error"
            self.colorFill = QtGui.QColor(*color)
        elif isinstance(color, QtGui.QColor):
            self.colorFill = color

    def getColorFill(self):

        return self.colorFill


class NodeSingleMark(NodeMark):

    def __init__(self, radius=16, nameCategory="", indexGroup=-1, locationTile=(-1, -1), index=1, parent:QtWidgets.QGraphicsItem=None):

        if parent is None:
            super(NodeSingleMark, self).__init__(nameCategory=nameCategory, indexGroup=indexGroup,
                                           locationTile=locationTile, index=index)
        elif type(parent) is QtWidgets.QGraphicsItem:
            super(NodeSingleMark, self).__init__(nameCategory=nameCategory, indexGroup=indexGroup,
                                           locationTile=locationTile, index=index, parent=parent)
        else:
            assert False, "Parent Error"

        self.radius = radius
        self.colorMain = QtGui.QColor(0, 255, 255, 128)
        self.colorSub = QtGui.QColor(128, 128, 128, 128)
        self.setAcceptHoverEvents(True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, enabled=True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, enabled=True)
        self.setZValue(3)
        # motion

        # action

    def paint(self, painter:QtGui.QPainter, option:QtWidgets.QStyleOptionGraphicsItem, widget:QtWidgets.QWidget=...):

        colorMain = self.colorMain
        colorSub = self.colorSub
        if self.obvious:
            pass
        else:
            colorHsv = colorMain.toHsv()
            colorMain = colorHsv.fromHsvF(colorHsv.hueF(), 0.4 * colorHsv.saturationF(), colorHsv.valueF(), 1)
            colorMain = colorMain.toRgb()

            colorHsv = colorSub.toHsv()
            colorSub = colorHsv.fromHsvF(colorHsv.hueF(), 0.4 * colorHsv.saturationF(), colorHsv.valueF(), 1)
            colorSub = colorSub.toRgb()

        if option.state & QtWidgets.QStyle.State_MouseOver:
            gradient = QtGui.QRadialGradient(QtCore.QPointF(0, 0), self.radius)
            gradient.setColorAt(0, colorMain)
            gradient.setColorAt(1, colorSub)
            pen = QtCore.Qt.NoPen
            if option.state & QtWidgets.QStyle.State_Sunken:
                pen = QtGui.QPen(QtGui.QColor(0, 255, 0))
            if option.state & QtWidgets.QStyle.State_Selected:
                pen = QtGui.QPen(QtGui.QColor(255, 0, 0))
        else:
            gradient = QtGui.QRadialGradient(QtCore.QPointF(0, 0), self.radius)
            gradient.setColorAt(1, colorMain)
            gradient.setColorAt(0, colorSub)
            pen = QtCore.Qt.NoPen
            if option.state & QtWidgets.QStyle.State_Selected:
                pen = QtGui.QPen(QtGui.QColor(255, 0, 0))

        painter.setPen(pen)
        painter.setBrush(QtGui.QBrush(gradient))
        painter.setRenderHint(painter.Antialiasing)
        painter.drawEllipse(-self.radius / 2, -self.radius / 2, self.radius, self.radius)

    def mousePressEvent(self, event:QtWidgets.QGraphicsSceneMouseEvent):

        if event.button() is QtCore.Qt.LeftButton:
            self.update()

    def mouseReleaseEvent(self, event:QtWidgets.QGraphicsSceneMouseEvent):

        self.update()
        QtWidgets.QGraphicsItem.mouseReleaseEvent(self, event)

    def mouseMoveEvent(self, event:QtWidgets.QGraphicsSceneMouseEvent):

        self.update()
        QtWidgets.QGraphicsItem.mouseMoveEvent(self, event)


class YGraphicsScene(QtWidgets.QGraphicsScene):

    SignalPaintFinished = Signal()
    SignalNewNode = Signal(NodeMark)
    SignalDeleteNode = Signal(NodeMark)
    SignalMoveNode = Signal(NodeMark)
    SignalInsertNode = Signal(NodeMark)
    SignalNewRect = Signal(RectangleMark)
    SignalDeleteRect = Signal(RectangleMark)
    SignalMoveRect = Signal(RectangleMark)
    SignalColor = Signal(list)
    SignalCoordinate = Signal(list)

    def __init__(self, parent):

        super(YGraphicsScene, self).__init__(parent=parent)

        # feature
        self.imageNdBackground = None
        self.mode = SceneMode.Null
        self.colorMain = None
        self.nameCurrentCategory = ""
        self.indexCurrentGroup = -1
        self.xTile = -1
        self.yTile = -1
        self.nextIndex = -1
        self.nodeFirst = None
        self.nodeCurrent = None
        self.edgeCurrent = None
        self.sceneposContextMenu = None
        self.itemsGroup = {}

        # flag
        self.FlagKeys = {"Ctrl":False, "Alt":False, "Shift":False}
        self.FlagButtons = {"Left":False, "Middle":False, "Right":False}
        self.FlagPainting = False

        # action
        self.action_Delete = QtWidgets.QAction("Delete", self)
        self.action_Delete.setShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Delete))
        self.action_Delete.triggered.connect(self.slot_delete_item)
        self.action_Insert = QtWidgets.QAction("Insert", self)
        self.action_Insert.triggered.connect(self.slot_insert_item)

    def contextMenuEvent(self, event:QtWidgets.QGraphicsSceneContextMenuEvent):

        qMenu = QtWidgets.QMenu()
        qMenu.addAction(self.action_Delete)
        qMenu.addAction(self.action_Insert)
        qTransform = QtGui.QTransform(1, 0, 0, 1, 0, 0)
        item = self.itemAt(event.scenePos(), qTransform)
        if item is None:
            self.action_Delete.setEnabled(False)
            self.action_Insert.setEnabled(False)
        elif isinstance(item, NodeMark):
            self.action_Delete.setEnabled(True)
            self.action_Insert.setEnabled(False)
            item.setSelected(True)
        elif isinstance(item, RectangleMark):
            self.action_Delete.setEnabled(True)
            self.action_Insert.setEnabled(False)
            item.setSelected(True)
        elif isinstance(item, EdgePoly):
            self.action_Delete.setEnabled(False)
            self.action_Insert.setEnabled(True)
            self.sceneposContextMenu = event.scenePos()
            item.setSelected(True)
        qMenu.show()
        qMenu.exec_(event.screenPos())

    @Slot()
    def slot_delete_item(self):

        print("scene delete item")
        for item in self.selectedItems():
            # print("deleting item: ", item.getNameCategory(), item.getIndexGroup(), item.getIndex())
            if isinstance(item, NodeSingleMark):
                for childItem in self.items():
                    # print(childItem.getNameCategory(), childItem.getIndexGroup(), childItem.getIndex())
                    if isinstance(childItem, NodeSingleMark) and childItem.getNameCategory() == item.getNameCategory() and \
                            childItem.getIndexGroup() == item.getIndexGroup():
                        if childItem.getIndex() > item.getIndex():
                            childItem.setIndex(childItem.getIndex() - 1)
                            # print("change to: ", childItem.getNameCategory(), childItem.getIndexGroup(),
                            #       childItem.getIndex())
                self.SignalDeleteNode.emit(item)
            elif isinstance(item, RectangleMark):
                for childItem in self.items():
                    print(childItem.getNameCategory(), childItem.getIndexGroup(), childItem.getIndex())
                    if isinstance(childItem, RectangleMark) and childItem.getNameCategory() == item.getNameCategory() and \
                            childItem.getIndexGroup() == item.getIndexGroup():
                        if childItem.getIndex() > item.getIndex():
                            childItem.setIndex(childItem.getIndex() - 1)
                            print("change to: ", childItem.getNameCategory(), childItem.getIndexGroup(),
                                  childItem.getIndex())
                self.SignalDeleteRect.emit(item)
            elif isinstance(item, NodePolyMark):
                edgeFront:EdgePoly = item.getEdgeFront()
                edgeBack:EdgePoly = item.getEdgeBack()
                edgeFront.setLine(QtCore.QLineF(edgeFront.line().p1(), edgeBack.getNodeBack().scenePos()))
                edgeBack.getNodeBack().setEdgeFront(edgeFront)

                # change latter successor
                nodeNext: NodePolyMark = edgeBack.getNodeBack()
                while nodeNext is not self.nodeFirst:
                    nodeNext.setIndex(nodeNext.getIndex() - 1)
                    nodeNext = nodeNext.getEdgeBack().getNodeBack()
                self.removeItem(edgeBack)
                self.SignalDeleteNode.emit(item)
            self.removeItem(item)
    @Slot()
    def slot_insert_item(self):

        itemFocus = self.focusItem()
        if isinstance(itemFocus, EdgePoly):
            nodeFront: NodePolyMark = itemFocus.getNodeFront()
            nodeBack: NodePolyMark = itemFocus.getNodeBack()

            # generating
            node = NodePolyMark(2, nameCategory=nodeFront.getNameCategory(),
                                indexGroup=nodeFront.getIndexGroup(),
                                locationTile=nodeFront.getCoordinateTile(),
                                index=nodeFront.getIndex() + 1)
            node.setZValue(3)
            node.setPos(self.sceneposContextMenu)
            node.setColorMain(self.colorMain)
            # change reference
            itemFocus.setLine(QtCore.QLineF(nodeFront.scenePos(), self.sceneposContextMenu))
            itemFocus.setNodeBack(node)
            node.setEdgeFront(itemFocus)
            qline = EdgePoly(QtCore.QLineF(self.sceneposContextMenu, nodeBack.scenePos()))
            qline.setPen(QtGui.QPen(QtGui.QColor(64, 64, 64, 255), 2, QtCore.Qt.PenStyle.SolidLine,
                                        QtCore.Qt.PenCapStyle.RoundCap))
            node.setEdgeBack(qline)
            qline.setNodeFront(node)
            qline.setNodeBack(nodeBack)
            nodeBack.setEdgeFront(qline)
            self.addItem(qline)
            self.addItem(node)

            # emit SignalInsertNode
            self.SignalInsertNode.emit(node)


            # change latter successor
            # nodeBack.setIndex(nodeBack.getIndex() + 1)
            # nodeNext:NodePolyMark = nodeBack.getEdgeBack().getNodeBack()
            nodeNext = nodeBack
            while not nodeNext.isHead():
                nodeNext.setIndex(nodeNext.getIndex() + 1)
                nodeNext = nodeNext.getEdgeBack().getNodeBack()

    def mousePressEvent(self, event:QtWidgets.QGraphicsSceneMouseEvent):

        event.accept()
        scenePos = event.scenePos()
        if self.mode == SceneMode.DotAnnotation:
            QtWidgets.QGraphicsScene.mousePressEvent(self, event)
        elif self.mode == SceneMode.RectAnnotation:
            if self.FlagPainting == True:
                itemRect = self.focusItem()
                self.SignalNewRect.emit(itemRect)
                self.clearFocus()
                self.FlagPainting = False
            QtWidgets.QGraphicsScene.mousePressEvent(self, event)
        elif self.mode == SceneMode.PolygonAnnotion:
            if event.button() is QtCore.Qt.LeftButton:
                self.FlagButtons["Left"] = True
                if self.FlagPainting is True:
                    qTrans = QtGui.QTransform(1, 0, 0, 1, 0, 0)
                    itemHere = self.itemAt(scenePos, qTrans)
                    if itemHere is None:
                        if self.edgeCurrent is not None:
                            self.edgeCurrent.setLine(QtCore.QLineF(self.edgeCurrent.line().p1(), scenePos))
                            self.edgeCurrent.setPen(QtGui.QPen(QtGui.QColor(64, 64, 64, 192), 2, QtCore.Qt.PenStyle.SolidLine,
                                                        QtCore.Qt.PenCapStyle.RoundCap))
                        node = NodePolyMark(2, nameCategory=self.getCurrentNameCategory(),
                                indexGroup=self.getCurrentIndexGroup(),
                                locationTile=self.getCoordinateTile(),
                                index=self.getNextIndex())
                        node.setZValue(3)
                        node.setPos(scenePos)
                        node.setColorMain(self.colorMain)
                        if isinstance(self.edgeCurrent, EdgePoly):
                            node.setEdgeFront(self.edgeCurrent)
                            self.edgeCurrent.setNodeBack(node)
                        self.addItem(node)
                        self.SignalNewNode.emit(node)
                        self.setNextIndex(self.getNextIndex() + 1)
                        line = QtCore.QLineF(scenePos, scenePos)
                        qline = EdgePoly(line)
                        node.setEdgeBack(qline)
                        qline.setNodeFront(node)
                        self.addItem(qline)
                        self.edgeCurrent = qline
                    else:
                        if isinstance(itemHere, NodeMark):
                            if itemHere is self.nodeFirst:
                                if self.edgeCurrent is not None:
                                    self.edgeCurrent.setLine(QtCore.QLineF(self.edgeCurrent.line().p1(), self.nodeFirst.scenePos()))
                                    self.edgeCurrent.setPen(
                                        QtGui.QPen(QtGui.QColor(64, 64, 64, 192), 2, QtCore.Qt.PenStyle.SolidLine,
                                                   QtCore.Qt.PenCapStyle.RoundCap))
                                    self.nodeFirst.setEdgeFront(self.edgeCurrent)
                                    self.edgeCurrent.setNodeBack(self.nodeFirst)
                                self.FlagPainting = False
                                self.edgeCurrent = None
                                self.SignalPaintFinished.emit()
                        else:
                            if self.edgeCurrent is not None:
                                self.edgeCurrent.setLine(QtCore.QLineF(self.edgeCurrent.line().p1(), scenePos))
                                self.edgeCurrent.setPen(
                                    QtGui.QPen(QtGui.QColor(64, 64, 64, 192), 2, QtCore.Qt.PenStyle.SolidLine,
                                               QtCore.Qt.PenCapStyle.RoundCap))
                            print("p1: ", self.edgeCurrent.line().p1().toTuple())
                            print("scenePos: ", scenePos.toTuple())
                            self.clearFocus()
                            node = NodePolyMark(2, nameCategory=self.getCurrentNameCategory(),
                                                indexGroup=self.getCurrentIndexGroup(),
                                                locationTile=self.getCoordinateTile(),
                                                index=self.getNextIndex())
                            node.setZValue(3)
                            node.setPos(scenePos)
                            node.setColorMain(self.colorMain)
                            if self.edgeCurrent is not None:
                                node.setEdgeFront(self.edgeCurrent)
                                itemHere.setNodeBack(node)
                            self.addItem(node)
                            self.SignalNewNode.emit(node)
                            self.setNextIndex(self.getNextIndex() + 1)
                            line = QtCore.QLineF(scenePos, scenePos)
                            qline = EdgePoly(line)
                            # qline.setWidth(1)
                            node.setEdgeBack(qline)
                            qline.setNodeFront(node)
                            self.edgeCurrent = qline
                            self.addItem(qline)
                else: # not painting
                    qTrans = QtGui.QTransform(1, 0, 0, 1, 0, 0)
                    itemHere = self.itemAt(scenePos, qTrans)
                    if isinstance(itemHere, NodePolyMark):
                        self.nodeCurrent = itemHere
        elif self.mode == SceneMode.PolyRPPAnnotation:
            print("PolyRPPAnnotation")
            pass
        elif self.mode == SceneMode.DotSetAnnotation:
            print("DotSetAnnotation")
            pass
        elif self.mode == SceneMode.SplineAnnotation:
            print("SplineAnnotation")
            pass
        elif self.mode == SceneMode.Null:
            pass
        if event.button() == QtCore.Qt.LeftButton:
            self.FlagButtons["Left"] = True
            self.LocationLeftButtonPressed = event.scenePos()

        QtWidgets.QGraphicsScene.mousePressEvent(self, event)

    def mouseReleaseEvent(self, event:QtWidgets.QGraphicsSceneMouseEvent):

        if event.button() == QtCore.Qt.LeftButton:
            self.FlagButtons["Left"] = False
            self.LocationLeftButtonPressed = event.scenePos()
            # Select move
            self.LocationLeftButtonReleased = event.scenePos()
            for item in self.selectedItems():
                if isinstance(item, NodeSingleMark):
                    self.SignalMoveNode.emit(item)
                elif isinstance(item, RectangleMark):
                    self.SignalMoveRect.emit(item)
                elif isinstance(item, NodePolyMark):
                    self.SignalMoveNode.emit(item)
                    self.nodeCurrent = None
        QtWidgets.QGraphicsScene.mouseReleaseEvent(self, event)

    def mouseMoveEvent(self, event:QtWidgets.QGraphicsSceneMouseEvent):

        posDiff = event.scenePos() - event.lastScenePos()
        scenePos = event.scenePos()
        # color infomation display
        if self.imageNdBackground is not None:
            coordinate = scenePos.toTuple()
            if 0 <= coordinate[0] < self.imageNdBackground.shape[1] and 0 <= coordinate[1] < self.imageNdBackground.shape[0]:
                self.SignalCoordinate.emit([int(coordinate[1]), int(coordinate[0])])
                self.SignalColor.emit(list(self.imageNdBackground[int(coordinate[1]), int(coordinate[0])]))
        if self.FlagPainting == True:
            if self.mode == SceneMode.RectAnnotation:
                if self.FlagPainting == True:
                    item = self.focusItem()
                    item.setSubPoint(event.scenePos())
                    self.update()
            elif self.mode == SceneMode.PolygonAnnotion:
                if self.FlagButtons["Left"] == False:
                    if self.edgeCurrent is not None:
                        line = QtCore.QLineF(self.edgeCurrent.line().p1(), scenePos)
                        self.edgeCurrent.setLine(line)
                        self.update()
            elif self.mode == SceneMode.PolyRPPAnnotation:
                print("PolyRPPAnnotation")
                pass
            elif self.mode == SceneMode.DotSetAnnotation:
                print("DotSetAnnotation")
                pass
            elif self.mode == SceneMode.SplineAnnotation:
                print("SplineAnnotation")
                pass
            elif self.mode == SceneMode.Null:
                print("NullAnnotation")
                pass
        else:
            # move items (don't distinguish between classes)
            if self.FlagButtons["Left"]:
                for item in self.selectedItems():
                    if isinstance(item, (NodeSingleMark, RectangleMark)):
                        posLast = item.scenePos()
                        posCurrent = posLast + posDiff
                        item.setPos(posCurrent)
                    elif isinstance(item, NodePolyMark):
                        if item.obvious:
                            posLast = item.scenePos()
                            posCurrent = posLast + posDiff
                            item.setPos(posCurrent)
                            edgeFront = item.getEdgeFront()
                            edgeFront.setLine(QtCore.QLineF(edgeFront.line().p1(), scenePos))
                            edgeBack = item.getEdgeBack()
                            edgeBack.setLine(QtCore.QLineF(scenePos, edgeBack.line().p2()))

            # # move nodepoly
            # if self.FlagButtons["Left"] == True:
            #     if self.nodeCurrent is not None:
            #         edgeFront = self.nodeCurrent.getEdgeFront()
            #         edgeFront.setLine(QtCore.QLineF(edgeFront.line().p1(), scenePos))
            #
            #         edgeBack = self.nodeCurrent.getEdgeBack()
            #         edgeBack.setLine(QtCore.QLineF(scenePos, edgeBack.line().p2()))
        QtWidgets.QGraphicsScene.mouseMoveEvent(self, event)

    def mouseDoubleClickEvent(self, event:QtWidgets.QGraphicsSceneMouseEvent):

        scenePos = event.scenePos()
        if self.mode == SceneMode.DotAnnotation:
            print("DotAnnotation")
            qTrans = QtGui.QTransform(1, 0, 0, 1, 0, 0)
            itemHere = self.itemAt(scenePos, qTrans)
            if itemHere is None or type(itemHere) is not NodeSingleMark:
                node = NodeSingleMark(20, nameCategory=self.getCurrentNameCategory(),
                                      indexGroup=self.getCurrentIndexGroup(),
                                      locationTile=self.getCoordinateTile(),
                                      index=self.getNextIndex())
                node.setPos(scenePos)
                node.setColorMain(self.colorMain)
                self.addItem(node)
                self.SignalNewNode.emit(node)
                self.setNextIndex(self.getNextIndex() + 1)
                self.update()
        elif self.mode == SceneMode.RectAnnotation:
            print("RectAnnotation")
            qTrans = QtGui.QTransform(1, 0, 0, 1, 0, 0)
            itemHere = self.itemAt(scenePos, qTrans)
            if itemHere is None or isinstance(itemHere, RectangleMark):
                rect = RectangleMark((1, 1), nameCategory=self.getCurrentNameCategory(),
                                      indexGroup=self.getCurrentIndexGroup(),
                                      locationTile=self.getCoordinateTile(),
                                      index=self.getNextIndex())
                rect.setColorFrame(self.colorMain)
                rect.setPos(scenePos)
                rect.setFocus()
                self.addItem(rect)
                self.setNextIndex(self.getNextIndex() + 1)
                self.update()
                self.FlagPainting = True
        elif self.mode == SceneMode.PolygonAnnotion:
            print("PolygonAnnotation")
            qTrans = QtGui.QTransform(1, 0, 0, 1, 0, 0)
            itemHere = self.itemAt(scenePos, qTrans)
            if itemHere is None or isinstance(itemHere, RectangleMark):
                node = NodePolyMark(2, nameCategory=self.getCurrentNameCategory(),
                                    indexGroup=self.getCurrentIndexGroup(),
                                    locationTile=self.getCoordinateTile(),
                                    index=self.getNextIndex(),
                                    head=True)
                node.setZValue(3)
                node.setPos(scenePos)
                node.setColorMain(self.colorMain)
                self.nodeFirst = node
                self.addItem(node)
                self.SignalNewNode.emit(node)
                self.setNextIndex(self.getNextIndex() + 1)
                line = QtCore.QLineF(scenePos, scenePos)
                qline = EdgePoly(line)
                self.addItem(qline)
                node.setEdgeBack(qline)
                qline.setNodeFront(node)
                self.edgeCurrent = qline
                self.FlagPainting = True
        elif self.mode == SceneMode.PolyRPPAnnotation:
            print("PolyRPPAnnotation")
            pass
        elif self.mode == SceneMode.DotSetAnnotation:
            print("DotSetAnnotation")
            pass
        elif self.mode == SceneMode.SplineAnnotation:
            print("SplineAnnotation")
            pass
        else:
            pass

        QtWidgets.QGraphicsScene.mouseDoubleClickEvent(self, event)

    # self function
    # TODO
    # def addItem2Group(self, nameCategory, indexGroup, item):
    #
    #     if nameCategory in self.itemsGroup:
    #         if indexGroup in self.itemsGroup[indexGroup]:
    #             self.itemsGroup[nameCategory][indexGroup].append(item)
    #         else:
    #             self.itemsGroup[nameCategory][indexGroup] = [item]
    #     else:
    #         self.itemsGroup[nameCategory] = {indexGroup:[item]}
    #
    # def removeItem4Group(self, item):
    #
    def setCoordinateTile(self, location: (int, int)):

        assert isinstance(location, (tuple, list)) and len(location) == 2, "Location Error"
        self.xTile, self.yTile = location

    def getXCoordinateTile(self):

        return self.xTile

    def getYCoordinateTile(self):

        return self.yTile

    def getCoordinateTile(self):

        return self.xTile, self.yTile

    def setCurrentNameCategory(self, nameCategory: str):

        self.nameCurrentCategory = nameCategory

    def getCurrentNameCategory(self):

        return self.nameCurrentCategory

    def setCurrentIndexGroup(self, indexGroup: int):

        self.indexCurrentGroup = indexGroup

    def setCurrentCategoryGroup(self, nameCategory: str, indexGroup: int):

        self.nameCurrentCategory = nameCategory
        self.indexCurrentGroup = indexGroup

    def getCurrentIndexGroup(self):

        return self.indexCurrentGroup

    def getCurrentCategoryGroup(self):

        return self.nameCurrentCategory, self.indexCurrentGroup

    def setNextIndex(self, index: int):

        self.nextIndex = index

    def getNextIndex(self):

        return self.nextIndex

    def setMode(self, mode: SceneMode):

        assert mode in SceneMode, "Mode Error"
        self.mode = mode

    def setColorMain(self, color: list):

        self.colorMain = QtGui.QColor(*color)

    def drawBackground(self, painter: QtGui.QPainter, rect: QtCore.QRectF):

        if self.imageNdBackground is not None:
            painter.save()
            # print("Re: paint")
            qImg = qimage2ndarray.array2qimage(self.imageNdBackground)
            painter.drawImage(QtCore.QRectF(0, 0, self.imageNdBackground.shape[1],
                                            self.imageNdBackground.shape[0]), qImg)
            painter.restore()

    def setBGI(self, image):  # BGI = Back Ground Image

        assert isinstance(image, np.ndarray), "Error Image"

        self.imageNdBackground = image

    def drawBGI(self, image, width, height):

        assert isinstance(image, np.ndarray), "Error Image"

        self.setBGI(image)
        painter = QtGui.QPainter()
        self.drawBackground(painter, QtCore.QRectF(0, 0, width, height))


class YGraphicsView(QtWidgets.QGraphicsView):

    #Signal
    SignalScale = Signal(float)

    def __init__(self, **args):

        if len(args) == 0:
            super(YGraphicsView, self).__init__()
        elif len(args) == 1:
            assert "parent" in args, "Parameters Error"
            super(YGraphicsView, self).__init__(args["parent"])
        elif len(args) == 2:
            assert "parent" in args and "scene" in args, "Parameters Error"
            super(YGraphicsView, self).__init__(args["scene"], args["parent"])

        # feature
        # self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        # self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        # self.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)

        # Flag
        self.KeysFlag = {"Ctrl":False, "Alt":False, "Shift":False}
        self.ButtonsFlag = {"Left":False, "Middle":False, "Right":False}
        self.PosEvent = None
        self.setMouseTracking(True)



    def wheelEvent(self, event:QtGui.QWheelEvent):

        posCenter = QtCore.QPointF(self.width() / 2, self.height() / 2)
        posMouse = event.posF()
        xDiff, yDiff = (0.1 * (posMouse - posCenter)).toTuple()
        # print("diff: ", posDiff)
        # print("h max:{}  h min:{}, v max:{} v min:{}".format(self.horizontalScrollBar().maximum(),
        #                                                      self.horizontalScrollBar().minimum(),
        #                                                      self.verticalScrollBar().maximum(),
        #                                                      self.verticalScrollBar().minimum()
        #                                                     ))
        if event.delta() < 0:  # backward rolling
            factor = 0.9
            self.scale(factor, factor)
            hvalueNew = self.horizontalScrollBar().value() - xDiff
            if self.horizontalScrollBar().minimum() < hvalueNew < self.horizontalScrollBar().maximum():
                self.horizontalScrollBar().setValue(hvalueNew)
            vvalueNew = self.verticalScrollBar().value() - yDiff
            if self.verticalScrollBar().minimum() < vvalueNew < self.verticalScrollBar().maximum():
                self.verticalScrollBar().setValue(vvalueNew)
        else:  # forward rolling
            factor = 1.1
            self.scale(factor, factor)
            hvalueNew = self.horizontalScrollBar().value() + xDiff
            if self.horizontalScrollBar().minimum() < hvalueNew < self.horizontalScrollBar().maximum():
                self.horizontalScrollBar().setValue(hvalueNew)
            vvalueNew = self.verticalScrollBar().value() + yDiff
            if self.verticalScrollBar().minimum() < vvalueNew < self.verticalScrollBar().maximum():
                self.verticalScrollBar().setValue(vvalueNew)
        # event.accept()
        # QtWidgets.QGraphicsView.wheelEvent(self, event)
        self.SignalScale.emit(self.transform().m11())

    def mousePressEvent(self, event:QtGui.QMouseEvent):

        if event.button() == QtCore.Qt.MiddleButton:
            self.ButtonsFlag["Middle"] = True
            self.PosEvent = event.pos()
            self.setCursor(QtCore.Qt.ClosedHandCursor)
            # event.accept()
        QtWidgets.QGraphicsView.mousePressEvent(self, event)

    def mouseReleaseEvent(self, event:QtGui.QMouseEvent):

        if event.button() == QtCore.Qt.MiddleButton:
            self.ButtonsFlag["Middle"] = False
            # event.accept()
        self.setCursor(QtCore.Qt.ArrowCursor)

        QtWidgets.QGraphicsView.mouseReleaseEvent(self, event)

    def mouseMoveEvent(self, event:QtGui.QMouseEvent):

        if self.ButtonsFlag["Middle"] == True:
            posCurrent = event.pos()
            posDiff = posCurrent - self.PosEvent
            hScrollBar = self.horizontalScrollBar()
            vScrollBar = self.verticalScrollBar()
            hScrollBar.setValue(hScrollBar.value() - posDiff.x())
            vScrollBar.setValue(vScrollBar.value() - posDiff.y())
            self.PosEvent = posCurrent
            # event.accept()
        QtWidgets.QGraphicsView.mouseMoveEvent(self, event)

    def keyPressEvent(self, event:QtGui.QKeyEvent):

        if event.key() == QtCore.Qt.Key_Control:
            print("Ctrl True")
            self.KeysFlag["Ctrl"] = True
            self.setCursor(QtCore.Qt.OpenHandCursor)
            # self.setCursor(QtCore.Qt.DragMoveCursor)
            # self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
        QtWidgets.QGraphicsView.keyPressEvent(self, event)

    def keyReleaseEvent(self, event:QtGui.QKeyEvent):

        if event.key() == QtCore.Qt.Key_Control:
            print("Ctrl False")
            self.KeysFlag["Ctrl"] = False
            # self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
            # self.setCursor(QtCore.Qt.ArrowCursor)
        QtWidgets.QGraphicsView.keyPressEvent(self, event)



class MyRectItem(QtWidgets.QGraphicsRectItem):

    def __init__(self, parent, *rect):
        if rect is None:
            super(MyRectItem, self).__init__(parent=parent)
        else:
            if len(rect) == 4:
                super(MyRectItem, self).__init__(float(rect[0]), float(rect[1]), float(rect[2]), float(rect[3]), parent=parent)
        self.setBrush(QtGui.QBrush(QtGui.QColor(255, 0, 255, 128)))
        self.setVisible(True)
        self.ensureVisible()
        self.setAcceptTouchEvents(True)
        self.setAcceptHoverEvents(True)
        self.setAcceptDrops(True)

    def focusInEvent(self, event:QtGui.QFocusEvent):
        print("rect is focused.")
        print(event.reason())

    def focusOutEvent(self, event:QtGui.QFocusEvent):
        print("rect is out of control.")
        print(event.reason())

    def dragEnterEvent(self, event:QtWidgets.QGraphicsSceneDragDropEvent):
        self.acceptDrops()
        print("I am moving")
        print(event.pos())

    def hoverEnterEvent(self, event:QtWidgets.QGraphicsSceneHoverEvent):
        print("Hovering")
        print(event.pos())

    def hoverLeaveEvent(self, event:QtWidgets.QGraphicsSceneHoverEvent):
        print("Hovering Leave")
        print(event.pos())

    def contextMenuEvent(self, event:QtWidgets.QGraphicsSceneContextMenuEvent):
        menu = QtWidgets.QMenu()
        menu.addAction("Move")
        menu.addAction("Enlarge")
        menu.addSeparator()
        menu.addAction("Delete")
        selectedAction = menu.exec_(event.screenPos())

    def mousePressEvent(self, event:QtWidgets.QGraphicsSceneMouseEvent):
        print("Mouse is Here: ", event.pos())
        self.setFocus(QtCore.Qt.OtherFocusReason)
        print(self.hasFocus())


class MySquare(QtWidgets.QGraphicsItem):
    def __init__(self, size=100):
        super(MySquare, self).__init__()
        self.size = size
        self.posStartDrag = QtCore.QPointF()
        self.posSelf = QtCore.QPointF()
        self.setAcceptHoverEvents(True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, enabled=False)

    def boundingRect(self) -> QtCore.QRectF:
        makeup = 2.0
        bbox = QtCore.QRectF(-self.size / 2 - makeup, -self.size / 2 - makeup, self.size + makeup, self.size + makeup)
        return bbox

    def shape(self) -> QtGui.QPainterPath:
        path = QtGui.QPainterPath()
        path.addRect(-self.size / 2, -self.size / 2, self.size, self.size)
        return path

    def paint(self, painter:QtGui.QPainter, option:QtWidgets.QStyleOptionGraphicsItem, widget:QtWidgets.QWidget=...):
        painter.setBrush(QtGui.QBrush(QtGui.QColor(0, 255, 255, 150)))
        painter.drawRect(-self.size // 2, -self.size // 2, self.size, self.size)

        if option.state & QtWidgets.QStyle.State_MouseOver:
            gradient = QtGui.QLinearGradient(QtCore.QPointF(-self.size/2, -self.size/2),
                                             QtCore.QPointF(self.size/2, self.size/2))
            gradient.setColorAt(0, QtGui.QColor(0, 255, 255))
            gradient.setColorAt(1, QtGui.QColor(60, 60, 200))
            pen = QtCore.Qt.NoPen
            if option.state & QtWidgets.QStyle.State_Sunken:
                pen = QtGui.QPen(QtGui.QColor(255, 0, 255))
        else:
            gradient = QtGui.QLinearGradient(QtCore.QPointF(-self.size / 2, -self.size / 2),
                                             QtCore.QPointF(self.size / 2, self.size / 2))
            gradient.setColorAt(1, QtGui.QColor(0, 255, 255))
            gradient.setColorAt(0, QtGui.QColor(60, 60, 200))
            pen = QtCore.Qt.NoPen

        painter.setPen(pen)
        painter.setBrush(QtGui.QBrush(gradient))
        painter.drawRect(-self.size // 2, -self.size // 2, self.size, self.size)

    def setSize(self, size):
        self.size = size
        self.update()

    def hoverEnterEvent(self, event:QtWidgets.QGraphicsSceneHoverEvent):
        self.update()
        print("Hover in. Postion: {}, {}".format(event.scenePos().x(), event.scenePos().y()))
        QtWidgets.QGraphicsItem.hoverEnterEvent(self, event)

    def hoverLeaveEvent(self, event:QtWidgets.QGraphicsSceneHoverEvent):
        self.update()
        print("Hover out. Postion: {}, {}".format(event.scenePos().x(), event.scenePos().y()) )
        QtWidgets.QGraphicsItem.hoverLeaveEvent(self, event)

    def mousePressEvent(self, event:QtWidgets.QGraphicsSceneMouseEvent):
        # self.posStartDrag = event.scenePos()
        self.posSelf = self.scenePos()
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, enabled=True)
        self.update()
        print("Pressed.")
        QtWidgets.QGraphicsItem.mousePressEvent(self, event)

    def mouseReleaseEvent(self, event:QtWidgets.QGraphicsSceneMouseEvent):
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, enabled=False)
        self.update()
        print("Released.")
        QtWidgets.QGraphicsItem.mouseReleaseEvent(self, event)

    def mouseMoveEvent(self, event:QtWidgets.QGraphicsSceneMouseEvent):
        posDiff = event.pos() - event.lastPos()
        self.setPos(posDiff + self.posSelf)
        self.update()
        QtWidgets.QGraphicsItem.mouseMoveEvent(self, event)


class LineMark(ItemMark):

    def __init__(self, parent:QtWidgets.QGraphicsItem=None):

        if parent is None:
            super(LineMark, self).__init__()
        elif type(parent) is QtWidgets.QGraphicsItem:
            super(LineMark, self).__init__(parent)

        # feature
        self.line = QtCore.QLineF(QtCore.QPointF(0, 0), QtCore.QPointF(0, 0))
        self.colorMain = QtGui.QColor(0, 0, 0, 255)
        self.colorSub = QtGui.QColor(0, 0, 0, 0)
        self.width = 3


        # flag
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, enabled=True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, enabled=True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, enabled=False)
        self.setAcceptHoverEvents(True)

    def boundingRect(self) -> QtCore.QRectF:

        expand = 2.0
        makeup = self.width / 2
        extern = expand + makeup
        bbox = QtCore.QRectF(QtCore.QPointF(0, 0), self.pointSub)
        if 0 <= self.getAngle() < 90:
            bbox.adjust(-extern, -extern, extern, extern)
        elif 90 <= self.getAngle() < 180:
            bbox.adjust(extern, -extern, extern, -extern)
        elif 180 <= self.getAngle() < 270:
            bbox.adjust(extern, extern, -extern, -extern)
        elif 270 <= self.getAngle() < 360:
            bbox.adjust(-extern, extern, -extern, extern)
        return bbox

    def shape(self) -> QtGui.QPainterPath:

        pass

    def getAngle(self):

        return (360 - self.line.angle()) % 360  # which means maximum < 360

    def getLength(self):

        return self.line.length()

    def setSubPoint(self, point:(list, tuple, QtCore.QPointF)):

        if isinstance(point, (tuple, list)):
            point = QtCore.QPointF(*point)
        self.pointSub = point

    def getSubPoint(self):

        return self.pointSub

    def setColorFrame(self, color:(int, QtGui.QColor)):

        if isinstance(color, list):
            assert len(color) == 4, "color length Error"
            self.colorMain = QtGui.QColor(*color)
        elif isinstance(color, QtGui.QColor):
            self.colorMain = color

    def getColorFrame(self):

        return self.colorMain

    def setColorFill(self, color: (int, QtGui.QColor)):

        if isinstance(color, list):
            assert len(color) == 4, "color length Error"
            self.colorSub = QtGui.QColor(*color)
        elif isinstance(color, QtGui.QColor):
            self.colorSub = color

    def getColorFill(self):

        return self.colorSub


class EdgePoly(QtWidgets.QGraphicsLineItem):

    def __init__(self, line:QtCore.QLineF=None, parent:QtWidgets.QGraphicsItem=None):

        if line is None:
            if parent is None:
                super(EdgePoly, self).__init__()
            elif isinstance(parent, QtWidgets.QGraphicsItem):
                super(EdgePoly, self).__init__()
        elif line is not None:
            if parent is None:
                super(EdgePoly, self).__init__(line)
            elif isinstance(parent, QtWidgets.QGraphicsItem):
                super(EdgePoly, self).__init__(line, parent)
        self.width = 2
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, enabled=False)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, enabled=True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, enabled=False)
        self.setAcceptHoverEvents(False)
        self.setZValue(2)
        pen = QtGui.QPen(QtGui.QColor(128, 128, 128, 128), self.width, QtCore.Qt.PenStyle.DotLine, QtCore.Qt.PenCapStyle.RoundCap)
        self.setPen(pen)
        self.nodeFront = None
        self.nodeBack = None

    def setNodeFront(self, point:NodeMark):

        assert isinstance(point, NodeMark), "point Error"

        self.nodeFront = point

    def getNodeFront(self):

        return self.nodeFront

    def setNodeBack(self, point: NodeMark):

        assert isinstance(point, NodeMark), "point Error"

        self.nodeBack = point

    def getNodeBack(self):

        return self.nodeBack

    def setWidth(self, width:int):

        self.width = width

class NodePolyMark(NodeMark):

    def __init__(self, radius:int=20, nameCategory="", indexGroup=-1, locationTile=(-1, -1),
                 index=1, head: bool=False, parent:QtWidgets.QGraphicsItem=None):

        if parent is None:
            super(NodePolyMark, self).__init__(nameCategory=nameCategory, indexGroup=indexGroup,
                                           locationTile=locationTile, index=index)
        elif type(parent) is QtWidgets.QGraphicsItem:
            super(NodePolyMark, self).__init__(nameCategory=nameCategory, indexGroup=indexGroup,
                                           locationTile=locationTile, index=index, parent=parent)
        else:
            assert False, "Parent Error"

        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, enabled=False)

        # appearance
        self.radius = radius
        self.edgeFront = None
        self.edgeBack = None
        self.head = head


    def getEdgeFront(self):

        if self.edgeFront is not None:
            return self.edgeFront
        else:
            return None

    def setEdgeFront(self, edge:EdgePoly):

        if isinstance(edge, EdgePoly):
            self.edgeFront = edge

    def getEdgeBack(self):

        if self.edgeBack is not None:
            return self.edgeBack
        else:
            return None

    def setEdgeBack(self, edge: EdgePoly):

        if isinstance(edge, EdgePoly):
            self.edgeBack = edge

    def isHead(self):

        return self.head

    def mouseMoveEvent(self, event:QtWidgets.QGraphicsSceneMouseEvent):

        self.update()
        QtWidgets.QGraphicsItem.mouseMoveEvent(self, event)

    def mousePressEvent(self, event:QtWidgets.QGraphicsSceneMouseEvent):

        self.update()
        QtWidgets.QGraphicsItem.mousePressEvent(self, event)

    def mouseReleaseEvent(self, event:QtWidgets.QGraphicsSceneMouseEvent):

        self.update()
        QtWidgets.QGraphicsItem.mouseReleaseEvent(self, event)


class testEventFilter(QtCore.QObject):

    def __init__(self, state:bool):
        super(testEventFilter, self).__init__()
        self.state = state

    def eventFilter(self, watched:QtCore.QObject, event:QtCore.QEvent) -> bool:
        if self.state is not True:
            if event.type() == QtCore.QEvent.MouseMove:
                return True
        else:
            return QtCore.QObject.eventFilter(self, watched, event)


class TestScene(QtWidgets.QGraphicsScene):

    def __init__(self, parent:QtCore.QObject=None):

        if parent is None:
            super(TestScene, self).__init__()
        elif isinstance(parent, QtCore.QObject):
            super(TestScene, self).__init__(parent)
        self.polymode = True

    def mouseMoveEvent(self, event:QtWidgets.QGraphicsSceneMouseEvent):

        pass

    def mousePressEvent(self, event:QtWidgets.QGraphicsSceneMouseEvent):

        pass


class TStatusBar(QtWidgets.QStatusBar):

    def __init__(self, parent:QtWidgets.QWidget=None):

        if parent is None:
            super(TStatusBar, self).__init__()
        elif isinstance(parent, QtWidgets.QWidget):
            super(TStatusBar, self).__init__(parent=parent)

        self.scaleStatus = QtWidgets.QLabel("Magnification")
        self.scaleStatus.setToolTip("magnification")
        self.coordianteStatus = QtWidgets.QLabel("Coordinate")
        self.coordianteStatus.setToolTip("coordinate")
        self.coordianteStatus.setMinimumWidth(60)
        self.colorStatus = QtWidgets.QLabel("Color")
        self.colorStatus.setToolTip("color")
        self.filenameStatus = QtWidgets.QLabel("File's Name")
        self.addWidget(self.scaleStatus, 3)
        self.addWidget(self.coordianteStatus, 3)
        self.addWidget(self.colorStatus, 18)
        self.addWidget(self.filenameStatus, 4)

    def slot_show_coordiante(self, coordinate):

        self.coordianteStatus.setText("{}, {}".format(coordinate[0], coordinate[1]))

    def slot_show_color(self, color):

        if len(color) == 3:
            self.colorStatus.setText("{}  {}  {}".format(color[0], color[1], color[2]))
        if len(color) == 4:
            self.colorStatus.setText("{}  {}  {}  {}".format(color[0], color[1], color[2], color[3]))

    def slot_show_filename(self, filename):

        self.filenameStatus.setText(filename)


class AboutDialog(QtWidgets.QDialog):
    def __init__(self, parent:QtWidgets.QWidget=None):
        if parent is None:
            super(AboutDialog, self).__init__()
        elif isinstance(parent, QtWidgets.QWidget):
            super(AboutDialog, self).__init__(parent)
        else:
            raise Exception("parent Error")
        self.content = QtWidgets.QLabel("Ganned by <i>lansv</i>")
        self.content.setFont(QtGui.QFont("gothic", 11))
        self.version = QtWidgets.QLabel("<i><b>Version: <u>0.19.8.1</u></b></i>")
        self.version.setFont(QtGui.QFont("gothic", 14))
        self.version.setAlignment(QtCore.Qt.AlignHCenter)
        self.icon = QtWidgets.QLabel()
        self.icon.setPixmap(QtGui.QPixmap(":/images/icons/Image/justwe.png"))
        self.icon.setAlignment(QtCore.Qt.AlignHCenter)
        self.date = QtWidgets.QLabel("2019. 8. 25")

        layoutH = QtWidgets.QHBoxLayout()
        layoutH.addStretch(2)
        layoutH.addWidget(self.content)
        layoutH.addStretch(1)
        layoutH.addWidget(self.date)
        layoutH.addStretch(2)
        layoutV = QtWidgets.QVBoxLayout()
        layoutV.addStretch(2)
        layoutV.addWidget(self.icon)
        layoutV.addStretch(1)
        layoutV.addWidget(self.version)
        layoutV.addStretch(1)
        layoutV.addLayout(layoutH)
        layoutV.addStretch(2)
        self.setLayout(layoutV)

        self.setWindowTitle("About")
        self.setWindowIcon(QtGui.QIcon(":/icons/icons/Small/icon100_com_126.png"))
        self.setMinimumWidth(400)
        self.setMinimumHeight(300)


class MyMain(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyMain, self).__init__()
        base = QtWidgets.QWidget(self)
        self.viewer = YGraphicsView()
        self.viewer.setViewportUpdateMode(QtWidgets.QGraphicsView.FullViewportUpdate)
        self.setCentralWidget(self.viewer)
        # image = qimage2ndarray.imread("F:\\Lab\\laughman.jpg")
        # qImage = qimage2ndarray.array2qimage(image)
        qimage = QtGui.QImage("F:\\Lab\\laughman.jpg")
        self.Scene = QtWidgets.QGraphicsScene(self.viewer)
        self.Scene.setSceneRect(0, 0, 1000, 1000)

        # background layer
        painter = QtGui.QPainter()
        self.Scene.drawBackground(painter, QtCore.QRectF(0, 0, 600, 600))

        self.rect_0 = QtWidgets.QGraphicsRectItem()
        self.rect_0.setRect(0, 0, 50, 50)
        self.rect_0.setPos(175, 175)
        self.Scene.addItem(self.rect_0)

        self.point = NodeSingleMark(120)
        self.point.setObvious(True)
        self.point.setPos(400, 400)
        self.Scene.addItem(self.point)

        self.point2 = NodeSingleMark(100)
        self.point2.setObvious(False)
        self.point2.setPos(500, 500)
        self.Scene.addItem(self.point2)

        self.rect = RectangleMark()
        self.rect.setColorFrame([255, 0, 0, 255])
        self.rect.setColorFill([128, 255, 200, 255])
        self.rect.setObvious(True)
        self.rect.setSize((50, 50))
        self.rect.setPos(200, 200)
        self.Scene.addItem(self.rect)
        self.rect2 = RectangleMark()
        self.rect2.setColorFrame([255, 0, 0, 255])
        self.rect2.setColorFill([128, 255, 200, 255])
        self.rect2.setObvious(False)
        self.rect2.setSize((50, 50))
        self.rect2.setPos(100, 100)
        self.Scene.addItem(self.rect2)


        self.viewer.setScene(self.Scene)

        self.nodepoly = NodePolyMark(50)
        self.nodepoly.setObvious(False)
        self.nodepoly.setPos(355, 355)
        self.Scene.addItem(self.nodepoly)

        self.line = EdgePoly()
        self.line.setLine(75, 75, 275, 275)
        self.Scene.addItem(self.line)

        self.node = NodeMark(2)
        self.node.setObvious(False)
        self.node.setPos(275, 275)
        self.node.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
        self.Scene.addItem(self.node)

        self.rect = RectangleMark()
        self.rect.setSize((50, 50))
        self.rect.setPos(100, 50)
        self.Scene.addItem(self.rect)
        self.viewer.setSceneRect(QtCore.QRectF(0, 0, 500, 500))
        # self.viewer.update()
        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Push")
        self.button.clicked.connect(self.slot_)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(base)
        self.setLayout(layout)

    @Slot()
    def slot_(self):

        print("Polygon: ", self.poly.polygon)
        print("Shape: ", self.poly.shape())
        print("Bbox: ", self.poly.boundingRect())


if __name__ == "__main__":

    qapp = QtWidgets.QApplication()
    # mainwindow = MyMain()
    # mainwindow.show()
    dialog = AboutDialog()
    dialog.show()
    sys.exit(qapp.exec_())

