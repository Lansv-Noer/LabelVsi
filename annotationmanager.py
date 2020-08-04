# annotation item:
    # format: dict
    # first index: x num of tile > {first index:{}}
    # second index: y num of tile > {second index:{}}
    # third index: class / category index of annotation > {third index(name): {color, counter, type, []]}}
    # fourth index: Nth set of a class > [fourth index(int): [dot/dotset]]

from graphics import AnnotationType, SceneMode
from writer import MaskWriter

import xml.dom.minidom as minidom
from PySide2 import QtWidgets
from PySide2.QtCore import Signal, Slot
import multiresolutionimageinterface as mir


class TileAnnotationManager(object):

    def __init__(self, pathFile, categories, widthImage, heightImage, widthTile, heightTile,
                 mainwindow:QtWidgets.QMainWindow=None, numTileX=None, numTileY=None):

        super(TileAnnotationManager, self).__init__()
        self.pathFile = pathFile
        self.categories = categories
        self.heightTile = heightTile
        self.widthTile = widthTile
        self.widthImage = widthImage
        self.heightImage = heightImage
        self.mainwindow = mainwindow
        if numTileX is None:
            self.numTileX = self.widthImage // self.widthTile + \
                            int(self.widthImage % self.widthTile > 0)
        if numTileY is None:
            self.numTileY = self.heightImage // self.heightTile + \
                            int(self.heightImage % self.heightTile > 0)
        self.body = {}
        self.categoriesInfo = {}
        self.currentNameCategory = None
        self.currentIndexGroup = -1
        self.currentColor = []
        self.currentType = None

    def addCategory(self, categoryName=None, categoryColor=(0, 0, 255, 255), counter=0,
                    categoryType="Dot", categoryValue:int=-1):

        categoryInfo = [categoryColor, counter, categoryType, categoryValue]
        self.categoriesInfo[categoryName] = categoryInfo
        self.setCurrentNameCategory(categoryName)
        self.body[categoryName] = []  # [{x:{y:[count, [point]]}}]
        self.categories += 1

    def addGroup(self, nameCategory:str):

        assert nameCategory in self.categoriesInfo and nameCategory in self.body, "nameCategory Error"

        self.body[nameCategory].append({})
        self.categoriesInfo[nameCategory][1] += 1

    def addRect(self, nameCategory, indexGroup, locationTile: (int, int), sizeBlock: (int, int), rect):

        assert nameCategory in self.categoriesInfo and nameCategory in self.body, "nameCategory Error"
        assert 0 <= indexGroup < len(self.body[nameCategory]), "indexGroup Error"
        assert isinstance(locationTile, (tuple, list)) and len(locationTile) == 2, "location Error"
        assert isinstance(sizeBlock, (tuple, list)) and len(sizeBlock) == 2, "sizeBlock Error"
        assert isinstance(rect, (list, tuple)) or len(rect) == 4, "rect Error"  # rect:[x, y, width, height]

        xTile, yTile = locationTile

        if xTile not in self.body[nameCategory][indexGroup]:
            # self.body[nameCategory][indexGroup].append({xTile:{}})
            # self.body[nameCategory][indexGroup][xTile].append({yTile:[0, []]})
            self.body[nameCategory][indexGroup][xTile] = {yTile: [0, [], []]}
            self.body[nameCategory][indexGroup][xTile][yTile][1].append(list(rect))
            self.body[nameCategory][indexGroup][xTile][yTile][0] += 1
            self.body[nameCategory][indexGroup][xTile][yTile][2] = list(sizeBlock)
        else:
            if yTile not in self.body[nameCategory][indexGroup][xTile]:
                self.body[nameCategory][indexGroup][xTile][yTile] = [0, []]
                self.body[nameCategory][indexGroup][xTile][yTile][1].append(list(rect))
                self.body[nameCategory][indexGroup][xTile][yTile][0] += 1
                self.body[nameCategory][indexGroup][xTile][yTile][2] = list(sizeBlock)
            else:
                self.body[nameCategory][indexGroup][xTile][yTile][1].append(list(rect))
                self.body[nameCategory][indexGroup][xTile][yTile][0] += 1


    def addPoint(self, nameCategory, indexGroup, locationTile: (int, int), sizeBlock: (int, int), point):

        assert nameCategory in self.categoriesInfo and nameCategory in self.body, "nameCategory Error"
        assert 0 <= indexGroup < len(self.body[nameCategory]), "indexGroup Error"
        assert isinstance(locationTile, (tuple, list)) and len(locationTile) == 2, "location Error"
        assert isinstance(sizeBlock, (tuple, list)) and len(sizeBlock) == 2, "sizeBlock Error"
        assert isinstance(point, (list, tuple)) and len(point) == 2, "point Error" # point: [x, y]

        xTile, yTile = locationTile

        if xTile not in self.body[nameCategory][indexGroup]:
            # self.body[nameCategory][indexGroup].append({xTile:{}})
            # self.body[nameCategory][indexGroup][xTile].append({yTile:[0, []]})
            self.body[nameCategory][indexGroup][xTile] = {yTile: [0, [], []]}
            self.body[nameCategory][indexGroup][xTile][yTile][1].append(list(point))
            self.body[nameCategory][indexGroup][xTile][yTile][0] += 1
            self.body[nameCategory][indexGroup][xTile][yTile][2] = list(sizeBlock)
        else:
            if yTile not in self.body[nameCategory][indexGroup][xTile]:
                self.body[nameCategory][indexGroup][xTile][yTile] = [0, [], []]
                self.body[nameCategory][indexGroup][xTile][yTile][1].append(list(point))
                self.body[nameCategory][indexGroup][xTile][yTile][0] += 1
                self.body[nameCategory][indexGroup][xTile][yTile][2] = list(sizeBlock)
            else:
                self.body[nameCategory][indexGroup][xTile][yTile][1].append(list(point))
                self.body[nameCategory][indexGroup][xTile][yTile][0] += 1

    def addRects(self, nameCategory, indexGroup, locationTile: (int, int), sizeBlock: (int, int), *rects):

        assert nameCategory in self.categoriesInfo and nameCategory in self.body, "nameCategory Error"
        assert 0 <= indexGroup < len(self.body[nameCategory]), "indexGroup Error"
        assert isinstance(locationTile, (tuple, list)) and len(locationTile) == 2, "location Error"
        assert isinstance(sizeBlock, (tuple, list)) and len(sizeBlock) == 2, "sizeBlock Error"

        xTile, yTile = locationTile
        if xTile not in self.body[nameCategory][indexGroup]:
            self.body[nameCategory][indexGroup][xTile] = {yTile: [0, [], []]}
            # self.body[nameCategory][indexGroup][xTile].append({})
            for rect in rects:
                self.body[nameCategory][indexGroup][xTile][yTile][1].append(list(rect))
            self.body[nameCategory][indexGroup][xTile][yTile][0] += len(rects)
            self.body[nameCategory][indexGroup][xTile][yTile][2] = list(sizeBlock)
        else:
            if yTile not in self.body[nameCategory][indexGroup][xTile]:
                self.body[nameCategory][indexGroup][xTile][yTile] = [0, [], []]
                for rect in rects:
                    self.body[nameCategory][indexGroup][xTile][yTile][1].append(list(rect))
                self.body[nameCategory][indexGroup][xTile][yTile][0] += len(rects)
                self.body[nameCategory][indexGroup][xTile][yTile][2] = list(sizeBlock)
            else:
                for rect in rects:
                    self.body[nameCategory][indexGroup][xTile][yTile][1].append(list(rect))
                self.body[nameCategory][indexGroup][xTile][yTile][0] += len(rects)

    def addPoints(self, nameCategory, indexGroup, location: (int, int), sizeBlock: (int, int), *points):

        assert nameCategory in self.categoriesInfo and nameCategory in self.body, "nameCategory Error"
        assert 0 <= indexGroup < len(self.body[nameCategory]), "indexGroup Error"
        assert isinstance(location, (tuple, list)) and len(location) == 2, "location Error"
        assert isinstance(sizeBlock, (tuple, list)) and len(sizeBlock) == 2, "sizeBlock Error"

        xTile, yTile = location
        if xTile not in self.body[nameCategory][indexGroup]:
            self.body[nameCategory][indexGroup][xTile] = {yTile: [0, [], []]}
            for point in points:
                self.body[nameCategory][indexGroup][xTile][yTile][1].append(list(point))
            self.body[nameCategory][indexGroup][xTile][yTile][0] += len(points)
            self.body[nameCategory][indexGroup][xTile][yTile][2] = list(sizeBlock)
        else:
            if yTile not in self.body[nameCategory][indexGroup][xTile]:
                self.body[nameCategory][indexGroup][xTile][yTile] = [0, [], []]
                for point in points:
                    self.body[nameCategory][indexGroup][xTile][yTile][1].append(list(point))
                self.body[nameCategory][indexGroup][xTile][yTile][0] += len(points)
                self.body[nameCategory][indexGroup][xTile][yTile][2] = list(sizeBlock)
            else:
                for point in points:
                    self.body[nameCategory][indexGroup][xTile][yTile][1].append(list(point))
                self.body[nameCategory][indexGroup][xTile][yTile][0] += len(points)

    def insertRect(self, nameCategory, indexGroup, locationTile: (int, int), sizeBlock: (int, int), index, rect):

        assert nameCategory in self.categoriesInfo and nameCategory in self.body, "nameCategory Error"
        assert 0 <= indexGroup < len(self.body[nameCategory]), "indexGroup Error"
        assert isinstance(locationTile, (tuple, list)) and len(locationTile) == 2, "locationTile Error"
        xTile, yTile = locationTile
        assert xTile in self.body[nameCategory][indexGroup] and \
               yTile in self.body[nameCategory][indexGroup][xTile], "locationTile Error"
        assert 0 <= index < len(self.body[nameCategory][indexGroup][xTile][yTile][1]), "index Error"
        assert isinstance(rect, (tuple, list)) and len(rect) == 4, "rect Error"
        assert isinstance(sizeBlock, (tuple, list)) and len(sizeBlock) == 2, "sizeBlock Error"

        if xTile not in self.body[nameCategory][indexGroup]:
            # self.body[nameCategory][indexGroup].append({xTile:{}})
            # self.body[nameCategory][indexGroup][xTile].append({yTile:[0, []]})
            self.body[nameCategory][indexGroup][xTile] = {yTile: [0, [], []]}
            self.body[nameCategory][indexGroup][xTile][yTile][1].insert(index, list(rect))
            self.body[nameCategory][indexGroup][xTile][yTile][0] += 1
            self.body[nameCategory][indexGroup][xTile][yTile][2] = list(sizeBlock)
        else:
            if yTile not in self.body[nameCategory][indexGroup][xTile]:
                self.body[nameCategory][indexGroup][xTile][yTile] = [0, [], []]
                self.body[nameCategory][indexGroup][xTile][yTile][1].insert(index, list(rect))
                self.body[nameCategory][indexGroup][xTile][yTile][0] += 1
                self.body[nameCategory][indexGroup][xTile][yTile][2] = list(sizeBlock)
            else:
                self.body[nameCategory][indexGroup][xTile][yTile][1].insert(index, list(rect))
                self.body[nameCategory][indexGroup][xTile][yTile][0] += 1

    def insertPoint(self, nameCategory, indexGroup, locationTile: (int, int), sizeBlock: (int, int), index, point):

        assert nameCategory in self.categoriesInfo and nameCategory in self.body, "nameCategory Error"
        assert 0 <= indexGroup < len(self.body[nameCategory]), "indexGroup Error"
        assert isinstance(locationTile, (tuple, list)) and len(locationTile) == 2, "locationTile Error"
        xTile, yTile = locationTile
        assert xTile in self.body[nameCategory][indexGroup] and \
               yTile in self.body[nameCategory][indexGroup][xTile], "locationTile Error"
        assert 0 <= index < len(self.body[nameCategory][indexGroup][xTile][yTile][1]), "index Error"
        assert isinstance(point, (tuple, list)) and len(point) == 2, "point Error"
        assert isinstance(sizeBlock, (tuple, list)) and len(sizeBlock) == 2, "sizeBlock Error"

        if xTile not in self.body[nameCategory][indexGroup]:
            # self.body[nameCategory][indexGroup].append({xTile:{}})
            # self.body[nameCategory][indexGroup][xTile].append({yTile:[0, []]})
            self.body[nameCategory][indexGroup][xTile] = {yTile: [0, [], []]}
            self.body[nameCategory][indexGroup][xTile][yTile][1].insert(index, list(point))
            self.body[nameCategory][indexGroup][xTile][yTile][0] += 1
            self.body[nameCategory][indexGroup][xTile][yTile][2] = list(sizeBlock)
        else:
            if yTile not in self.body[nameCategory][indexGroup][xTile]:
                self.body[nameCategory][indexGroup][xTile][yTile] = [0, [], []]
                self.body[nameCategory][indexGroup][xTile][yTile][1].insert(index, list(point))
                self.body[nameCategory][indexGroup][xTile][yTile][0] += 1
                self.body[nameCategory][indexGroup][xTile][yTile][2] = list(sizeBlock)
            else:
                self.body[nameCategory][indexGroup][xTile][yTile][1].insert(index, list(point))
                self.body[nameCategory][indexGroup][xTile][yTile][0] += 1

    def deleteRect(self, nameCategory, indexGroup, locationTile: (int, int), index):

        assert nameCategory in self.categoriesInfo and nameCategory in self.body, "nameCategory Error"
        assert 0 <= indexGroup < len(self.body[nameCategory]), "indexGroup Error"
        assert isinstance(locationTile, (tuple, list)) and len(locationTile) == 2, "locationTile Error"
        xTile, yTile = locationTile
        assert xTile in self.body[nameCategory][indexGroup] and \
               yTile in self.body[nameCategory][indexGroup][xTile], "locationTile Error"

        print("poping rect {}".format(index))
        self.body[nameCategory][indexGroup][xTile][yTile][1].pop(index)
        self.body[nameCategory][indexGroup][xTile][yTile][0] -= 1

    def deletePoint(self, nameCategory, indexGroup, locationTile: (int, int), index):

        assert nameCategory in self.categoriesInfo and nameCategory in self.body, "nameCategory Error"
        assert 0 <= indexGroup < len(self.body[nameCategory]), "indexGroup Error"
        assert isinstance(locationTile, (tuple, list)) and len(locationTile) == 2, "locationTile Error"
        xTile, yTile = locationTile
        assert xTile in self.body[nameCategory][indexGroup] and \
               yTile in self.body[nameCategory][indexGroup][xTile], "locationTile Error"

        self.body[nameCategory][indexGroup][xTile][yTile][1].pop(index)
        self.body[nameCategory][indexGroup][xTile][yTile][0] -= 1

    def moveRect(self, nameCategory, indexGroup, locationTile: (int, int), index, pos):

        assert nameCategory in self.categoriesInfo and nameCategory in self.body, "nameCategory Error"
        assert 0 <= indexGroup < len(self.body[nameCategory]), "indexGroup Error"
        assert isinstance(pos, (list, tuple)) and len(pos) == 2, "pos Error"
        assert isinstance(locationTile, (tuple, list)) and len(locationTile) == 2, "locationTile Error"
        xTile, yTile = locationTile
        assert xTile in self.body[nameCategory][indexGroup] and \
               yTile in self.body[nameCategory][indexGroup][xTile], "locationTile Error"
        assert 0 <= index < len(self.body[nameCategory][indexGroup][xTile][yTile][1]), "index Error"

        self.body[nameCategory][indexGroup][xTile][yTile][1][index][:2] = pos

    def movePoint(self, nameCategory, indexGroup, locationTile: (int, int), index, pos):

        assert nameCategory in self.categoriesInfo and nameCategory in self.body, "nameCategory Error"
        assert 0 <= indexGroup < len(self.body[nameCategory]), "indexGroup Error"
        assert isinstance(pos, (list, tuple)), "pos Error"
        assert isinstance(locationTile, (tuple, list)) and len(locationTile) == 2, "locationTile Error"
        xTile, yTile = locationTile
        assert xTile in self.body[nameCategory][indexGroup] and \
               yTile in self.body[nameCategory][indexGroup][xTile], "locationTile Error"
        assert 0 <= index < len(self.body[nameCategory][indexGroup][xTile][yTile][1]), "index Error"

        posNew = list(pos) if isinstance(pos, tuple) else pos
        self.body[nameCategory][indexGroup][xTile][yTile][1][index] = posNew

    def changeName(self, newName, originalName=None):

        assert newName in self.categoriesInfo or newName != originalName, "NewName Error"
        if originalName is None:
            originalName = self.currentNameCategory
        else:
            assert originalName in self.categoriesInfo, "originalName Error"

        self.categoriesInfo[newName] = self.categoriesInfo.pop(originalName)
        self.body[newName] = self.body.pop(originalName)

    def changeColor(self, newColor, targetCategory=None):

        if targetCategory is None:
            targetCategory = self.currentNameCategory
        else:
            assert targetCategory in self.categoriesInfo, "targetCategory Error"

        self.categoriesInfo[targetCategory][0] = newColor

    def changeType(self, newType, targetCategory=None):

        if targetCategory is None:
            targetCategory = self.currentNameCategory
        else:
            assert targetCategory in self.categoriesInfo, "targetCategory Error"

        self.categoriesInfo[targetCategory][2] = newType

    def changeValue(self, newValue, targetCategory=None):

        if targetCategory is None:
            targetCategory = self.currentNameCategory
        else:
            assert targetCategory in self.categoriesInfo, "targetCategory Error"

        self.categoriesInfo[targetCategory][3] = newValue

    def setCurrentColor(self, color:str):

        assert isinstance(color, (list, tuple)) and len(color) == 4, "color Error"

        self.currentColor = color

    def setCurrentType(self, type:SceneMode):

        assert isinstance(type, SceneMode), "type Error"

        self.currentType = type

    def printInfo(self):

        print("image size:{}*{}    tile size:{}*{}    tile number:{}*{}".format(self.widthImage, self.heightImage,
                                                                                self.widthTile, self.heightTile,
                                                                                self.numTileX, self.numTileY))
        print("Categories: {}".format(self.categories))
        for key, value in self.categoriesInfo.items():
            print(key, end="\t")
            print(value)

    def getCategory(self, nameCategory: str, screenprint:bool=False):

        assert nameCategory in self.categoriesInfo, "nameCategory Error"

        dataTree = []
        print(nameCategory, "[{count}]: ".format(count=len(self.body[nameCategory]))) if screenprint else None
        for indexGroup, contentGroup in enumerate(self.body[nameCategory]):
            print("group[{}]:".format(indexGroup)) if screenprint else None
            dataTree.append({})
            for xTileIndex, xTileContent in contentGroup.items():
                for yTileIndex, yTileContent in xTileContent.items():
                    print("[{}, {}]".format(xTileIndex, yTileIndex)) if screenprint else None
                    print(yTileContent[1]) if screenprint else None
                    dataTree[indexGroup][xTileIndex, yTileIndex] = yTileContent[1]
        return dataTree

    def deleteCategory(self, nameCategory: str):

        assert nameCategory in self.categoriesInfo and nameCategory in self.body, "nameCategory Error"

        self.categoriesInfo.pop(nameCategory)
        self.body.pop(nameCategory)

    def getGroup(self, nameCategory: str, indexGroup: int, screenprint:bool=False):

        assert nameCategory in self.categoriesInfo and nameCategory in self.body, "nameCategory Error"
        assert 0 <= indexGroup < len(self.body[nameCategory]), "indexGroup Error"

        dataTree = {}
        print(nameCategory, " group[{indexGroup}]".format(indexGroup=indexGroup)) if screenprint else None
        for xTileIndex, xTileContent in self.body[nameCategory][indexGroup].items():
            for yTileIndex, yTileContent in xTileContent.items():
                print("[{}, {}]".format(xTileIndex, yTileIndex)) if screenprint else None
                print(yTileContent[1]) if screenprint else None
                dataTree[xTileIndex, yTileIndex] = yTileContent[1]
        return dataTree

    def deleteGroup(self, nameCategory: str, indexGroup: int):

        assert nameCategory in self.categoriesInfo and nameCategory in self.body, "nameCategory Error"

        self.categoriesInfo[nameCategory][1] -= 1
        self.body[nameCategory].pop(indexGroup)

    def getContentCategoryGroupTile(self, nameCategory: str, indexGroup: int, locationTile: (int, int), screenprint:bool=False):

        assert nameCategory in self.categoriesInfo and nameCategory in self.body, "nameCategory Error"
        assert 0 <= indexGroup < len(self.body[nameCategory]), "indexGroup Error"
        assert isinstance(locationTile, (tuple, list)) and len(locationTile) == 2, "locationTile Error"
        xTile, yTile = locationTile
        assert xTile in self.body[nameCategory][indexGroup] and \
               yTile in self.body[nameCategory][indexGroup][xTile], "locationTile Error"

        data = self.body[nameCategory][indexGroup][xTile][yTile][1]
        print(data) if screenprint else None
        return data

    def getCountCategoryGroupTile(self, nameCategory: str, indexGroup: int, locationTile: (int, int),
                                    screenprint: bool = False):

        assert nameCategory in self.categoriesInfo and nameCategory in self.body, "nameCategory Error"
        assert 0 <= indexGroup < len(self.body[nameCategory]), "indexGroup Error"
        assert isinstance(locationTile, (tuple, list)) and len(locationTile) == 2, "locationTile Error"
        xTile, yTile = locationTile
        assert xTile in self.body[nameCategory][indexGroup] and \
               yTile in self.body[nameCategory][indexGroup][xTile], "locationTile Error"
        return self.body[nameCategory][indexGroup][xTile][yTile][0]

    def getTileAnnotation(self, location: (int, int), screenprint: bool=False):

        assert isinstance(location, (tuple, list)) or len(location) == 2, "location Error"

        xTile, yTile = location
        print("[{}, {}]".format(xTile, yTile)) if screenprint else None
        dataTree = {}
        for nameCategory, contentCategory in self.body.items():
            for indexGroup, contentGroup in enumerate(contentCategory):
                if xTile in contentGroup and yTile in contentGroup[xTile]:
                    print(nameCategory, " [{indexGroup}]".format(indexGroup=indexGroup)) if screenprint else None
                    print(contentGroup[xTile][yTile][1]) if screenprint else None
                    if nameCategory not in dataTree:
                        dataTree[nameCategory] = {indexGroup:contentGroup[xTile][yTile][1]}
                    else:
                        dataTree[nameCategory][indexGroup] = contentGroup[xTile][yTile][1]
        return dataTree

    def getCategoryCount(self):

        return self.categories

    def setCurrentNameCategory(self, nameCategory:str):

        assert nameCategory in self.categoriesInfo

        self.currentNameCategory = nameCategory

    def setCurrentIndexGroup(self, indexGroup:str):

        # assert 0 <= indexGroup < len(self.categoriesInfo[self.getCurrentNameCategory()]), "indexGroup Error"
        ## index maybe out of the index ,so I annotate this assert

        self.currentIndexGroup = indexGroup

    def getCurrentNameCategory(self):

        return self.currentNameCategory

    def getCurrentIndexGroup(self):

        return self.currentIndexGroup

    def getCategoryColor(self, nameCategory:str):

        assert nameCategory in self.categoriesInfo, "nameCategory Error"

        return self.categoriesInfo[nameCategory][0] # list

    def getGroupsCount(self, nameCategory:str):

        assert nameCategory in self.categoriesInfo, "nameCategory Error"

        return self.categoriesInfo[nameCategory][1] # int

    def getCategoryType(self, nameCategory:str):

        assert nameCategory in self.categoriesInfo, "nameCategory Error"

        return self.categoriesInfo[nameCategory][2]

    def getCategoryValue(self, nameCategory:str):

        assert nameCategory in self.categoriesInfo, "nameCategory Error"

        return self.categoriesInfo[nameCategory][3]

    def getCurrentColor(self):

        return self.currentColor

    def getCurrentType(self):

        return self.currentType

    def addLocalBlock(self, x:int, y:int, category:str, content:list):

        pass

    def hasAnnotation(self, nameCategory, indexGroup, locationTile: (int, int)):

        assert isinstance(locationTile, (list, tuple)) and len(locationTile) == 2, "locationTile Error"

        xTile, yTile = locationTile
        if nameCategory in self.categoriesInfo:
            if indexGroup in self.categoriesInfo[nameCategory]:
                if xTile in self.body[nameCategory][indexGroup] and yTile in self.body[nameCategory][indexGroup][xTile]:
                    return True
        return False

    @Slot(str)
    def exportXml(self, pathFile:str):

        dom = minidom.getDOMImplementation().createDocument(None, "LabelU", None)
        all = dom.documentElement

        elementContent = dom.createElement("Content")

        elementNote = dom.createElement("Note")
        elementNote.appendChild(dom.createTextNode("Generated by LebelU"))

        elementInfo = dom.createElement("Information")
        elementInfo.setAttribute("Filepath", pathFile)
        elementInfo.setAttribute("HeightOfImage", str(self.heightImage))
        elementInfo.setAttribute("WidthOfImage", str(self.widthImage))
        elementInfo.setAttribute("HeightOfTile", str(self.heightTile))
        elementInfo.setAttribute("WidthOfTile", str(self.widthTile))
        elementInfo.setAttribute("YnumberOfTile", str(self.numTileY))
        elementInfo.setAttribute("XnumberOfTile", str(self.numTileX))

        elementBody = dom.createElement("Body")
        if len(self.categoriesInfo) > 0:
            for nameCategory, infoCategory in self.categoriesInfo.items():
                elementCategory = dom.createElement("Category")
                elementCategory.setAttribute("name", nameCategory)
                color = self.categoriesInfo[nameCategory][0][:3]
                alpha = self.categoriesInfo[nameCategory][0][3]
                elementCategory.setAttribute("color", hex(color[0]* 256 * 256 + color[1]* 256 + color[2]))
                elementCategory.setAttribute("alpha", hex(alpha))
                elementCategory.setAttribute("type", str(self.categoriesInfo[nameCategory][2]))
                elementCategory.setAttribute("number", str(self.categoriesInfo[nameCategory][1]))
                if len(self.body[nameCategory]) > 0:
                    for indexGroup, contentGroup in enumerate(self.body[nameCategory]):
                        elementGroup = dom.createElement("Group")
                        if len(self.body[nameCategory][indexGroup]) > 0:
                            for indexX in self.body[nameCategory][indexGroup]:
                                for indexY in self.body[nameCategory][indexGroup][indexX]:
                                    elementTile = dom.createElement("Tile")
                                    elementTile.setAttribute("XLocationTile", str(indexX))
                                    elementTile.setAttribute("YLocationTile", str(indexY))
                                    elementTile.setAttribute("WidthTile",
                                                             str(self.body[nameCategory][indexGroup][indexX][indexY][2][0]))
                                    elementTile.setAttribute("HeightTile",
                                                             str(self.body[nameCategory][indexGroup][indexX][indexY][2][1]))
                                    for index, item in enumerate(contentGroup[indexX][indexY][1]):
                                        if self.categoriesInfo[nameCategory][2] == "Dot" or \
                                                self.categoriesInfo[nameCategory][2] == AnnotationType.Dot:
                                            elementItem = dom.createElement("Point")
                                            elementItem.setAttribute("X", str(item[0]))
                                            elementItem.setAttribute("Y", str(item[1]))
                                        elif self.categoriesInfo[nameCategory][2] == "Rectangle" or \
                                                self.categoriesInfo[nameCategory][2] == AnnotationType.Rect:
                                            elementItem = dom.createElement("Rect")
                                            elementItem.setAttribute("X", str(item[0]))
                                            elementItem.setAttribute("Y", str(item[1]))
                                            elementItem.setAttribute("Width", str(item[2]))
                                            elementItem.setAttribute("Height", str(item[3]))
                                        elementItem.setAttribute("Index", str(index))
                                        elementTile.appendChild(elementItem)
                                    elementGroup.appendChild(elementTile)
                        elementCategory.appendChild(elementGroup)
                    elementBody.appendChild(elementCategory)

        elementContent.appendChild(elementNote)
        elementContent.appendChild(elementInfo)
        elementContent.appendChild(elementBody)

        all.appendChild(elementContent)

        with open(pathFile, "w", encoding="utf-8") as file:
            dom.writexml(file, addindent="\t", newl="\n", encoding="utf-8")

        print("Xml is written done.")

    @Slot(str)
    def exportMask(self, pathExport:str):

        writer = MaskWriter(mir.JPEG, 99)
        writer.writeMask(self, pathExport, channels=1)

if __name__ == '__main__':

    dic = TileAnnotationManager("abc", 0, 100000, 80000, 1024, 1024)
    dic.addCategory("Malignant", [255, 0, 0, 0], 0, AnnotationType.Dot)
    dic.addCategory("Benign", [255, 0, 255], 0, AnnotationType.DotSet)
    dic.addCategory(categoryColor=[129, 0, 0, 230], counter=0, categoryType=AnnotationType.Rect)
    dic.changeName("Normal")
    dic.changeColor([128, 128, 128, 128], "Benign")
    dic.addGroup("Benign")
    dic.addGroup("Benign")
    dic.addPoints("Benign", 1, (40, 41), (1000, 1000), (100, 120), (1, 3), (4,56))
    dic.addPoint("Benign", 1, (40, 41), (1000, 1000), (110, 120))
    dic.addPoint("Benign", 1, (40, 42), (1000, 800), (110, 120))
    dic.addPoint("Benign", 1, (30, 41), (1000, 1000), (45, 90))
    dic.addGroup("Normal")
    dic.addGroup("Normal")
    dic.addRect("Normal", 0, (1, 2), (1000, 1000), (123, 234, 34, 56))
    dic.addRects("Normal", 0, (40, 41), (1000, 1000), (23, 23, 235, 89), (46, 46, 123, 123), (69, 69, 456, 456))
    dic.addRects("Normal", 1, (40, 41), (1000, 1000), (24, 24, 34, 56), (48, 48, 56, 78), (96, 96, 89, 90))
    dic.moveRect("Normal", 1, (40, 41), 0, (100, 100))
    dic.printInfo()
    dic.getCategory("Benign")
    dic.getCategory("Normal")
    dic.getGroup("Benign", 1)
    body = dic.getTileAnnotation((40, 41))
    print("body: ", body)



