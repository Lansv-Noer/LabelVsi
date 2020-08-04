import bioformats
from bioformats import ImageReader
import bioformats.omexml as ome
import javabridge
import xml.dom.minidom as Minidom
import numpy as np


class VsiReader(bioformats.formatreader.ImageReader):
    def __init__(self, path, url=None, perform_init=True, tilesize=(1000, 1000)):
        javabridge.start_vm(class_path=bioformats.JARS)  # I code javabridge here, and maybe it will be proven wrong
        super(VsiReader, self).__init__(path, url, perform_init)
        self.channels = self.rdr.getSizeC()
        self.widthTile = tilesize[0]
        self.heightTile = tilesize[1]
        self.layersCount = self.rdr.getSeriesCount()
        self.currentLayer = 0
        self.rdr.setSeries(self.currentLayer)
        self.currentLayerWidth = self.rdr.getSizeX()
        self.currentLayerHeight = self.rdr.getSizeY()
        self.numTileX = self.currentLayerWidth // self.widthTile + \
                                     int(self.currentLayerWidth % self.widthTile > 0)
        self.numTileY = self.currentLayerHeight // self.heightTile + \
                                     int(self.currentLayerHeight % self.heightTile > 0)
        self.metadata = bioformats.get_omexml_metadata(path=path)

    def __delete__(self):
        pass
        javabridge.kill_vm()  # I code javabridge here, and maybe it will be proven wrong TODO
        pass

    def getMetadata(self):
        return self.metadata   # a str of xml

    def setLayer(self, layerIndex:int):
        assert layerIndex < self.layersCount, "Layer is out of the range"

        self.currentLayer = layerIndex
        self.rdr.setSeries(self.currentLayer)
        self.currentLayerWidth = self.rdr.getSizeX()
        self.currentLayerHeight = self.rdr.getSizeY()
        self.numTileX = self.currentLayerWidth // self.widthTile + \
                        int(self.currentLayerWidth % self.widthTile > 0)
        self.numTileY = self.currentLayerHeight // self.heightTile + \
                        int(self.currentLayerHeight % self.heightTile > 0)

    def getCurrentLayer(self):

        return self.currentLayer

    def getCurrentSize(self):

        return self.currentLayerWidth, self.currentLayerHeight

    def getSize(self, layer=-1):

        if layer < 0:
            return self.getCurrentSize()
        else:
            series_origin = self.rdr.getSeries()
            self.rdr.setSeries(layer)
            width = self.rdr.getSizeX()
            height = self.rdr.getSizeY()
            self.rdr.setSeries(series_origin)
            return width, height

    def setTileSize(self, tileSize:tuple):
        """
        (width, height)
        """
        assert len(tileSize) == 2, "tileSize error"
        self.widthTile = tileSize[0]
        self.heightTile = tileSize[1]
        self.numTileX = self.currentLayerWidth // self.widthTile + \
                        int(self.currentLayerWidth % self.widthTile > 0)
        self.numTileY = self.currentLayerHeight // self.heightTile + \
                        int(self.currentLayerHeight % self.heightTile > 0)

    def getTileSize(self):

        return self.widthTile, self.heightTile

    def getNumTile(self):

        return self.numTileX, self.numTileY

    def getTile(self, indexTileX, indexTileY):

        assert (0 <= indexTileX < self.numTileX) and (0 <= indexTileY < self.numTileY), "index of tile is out of range"

        if indexTileX < self.numTileX - 1:
            if indexTileY < self.numTileY - 1:
                widthTile = self.widthTile
                heightTile = self.heightTile
                bytes_image = self.rdr.openBytesXYWH(0, indexTileX * self.widthTile, indexTileY * self.heightTile,
                                                       widthTile, heightTile)
                image = bytes_image.reshape(heightTile, widthTile, self.channels)
            else:
                heightTile = self.currentLayerHeight - (self.currentLayerHeight // self.heightTile) * self.heightTile
                widthTile = self.widthTile
                bytes_image = self.rdr.openBytesXYWH(0, indexTileX * self.widthTile, indexTileY * self.heightTile,
                                                       widthTile, heightTile)
                image = bytes_image.reshape(heightTile, widthTile, self.channels)
        else:
            if indexTileY < self.numTileY - 1:
                heightTile = self.heightTile
                widthTile = self.currentLayerWidth - (self.currentLayerWidth // self.widthTile) * self.widthTile
                bytes_image = self.rdr.openBytesXYWH(0, indexTileX * self.widthTile, indexTileY * self.heightTile,
                                                       widthTile, heightTile)
                image = bytes_image.reshape(heightTile, widthTile, self.channels)
            else:
                heightTile = self.currentLayerHeight - (self.currentLayerHeight // self.heightTile) * self.heightTile
                widthTile = self.currentLayerWidth - (self.currentLayerWidth // self.widthTile) * self.widthTile
                bytes_image = self.rdr.openBytesXYWH(0, indexTileX * self.widthTile, indexTileY * self.heightTile,
                                                       widthTile, heightTile)
                image = bytes_image.reshape(heightTile, widthTile, self.channels)

        return image, ((indexTileX * self.widthTile, indexTileY * self.heightTile), (widthTile, heightTile))

    def getImage(self, sizeC, sizeZ, sizeT, series):

        series_origin = self.rdr.getSeries()
        self.rdr.setSeries(series)
        image = self.read(sizeC, sizeZ, sizeT, series)
        self.rdr.setSeries(series_origin)

        return np.array((image * 255).astype(np.uint8))

class XmlParser(object):
    def __init__(self, xml):
        assert isinstance(xml, str), "xml must be a str"
        self.strXml = xml

    def vsi_infoextract(self):
        domTree = Minidom.parseString(self.strXml)
        elementInstrument = domTree.getElementsByTagName("Instrument")
        elementsImage = domTree.getElementsByTagName("Image")

        listImagesinfo = list()
        for index, elementImage in enumerate(elementsImage):
            imageinfo = {}
            imageinfo.setdefault("Name", elementImage.getAttribute("Name"))
            nodelistDate = elementImage.getElementsByTagName("AcquisitionDate")
            nodelistBasic = elementImage.getElementsByTagName("Pixels")

            # Basic Info Part 1
            imageinfo.setdefault("SizeY", nodelistBasic[0].getAttribute("SizeY"))
            imageinfo.setdefault("SizeX", nodelistBasic[0].getAttribute("SizeX"))

            # Extral Info
            if nodelistDate.length == 0:
                imageinfo.setdefault("AcquisitionDate", "-")
                imageinfo.setdefault("PhysicalSizeY", "-")
                imageinfo.setdefault("PhysicalSizeX", "-")
            else:
                imageinfo.setdefault("AcquisitionDate", nodelistDate[0].firstChild.nodeValue)
                imageinfo.setdefault("PhysicalSizeY", nodelistBasic[0].getAttribute("PhysicalSizeY"))
                imageinfo.setdefault("PhysicalSizeX", nodelistBasic[0].getAttribute("PhysicalSizeX"))

            # Basic Info Part 2
            imageinfo.setdefault("DimensionOrder", nodelistBasic[0].getAttribute("DimensionOrder"))
            imageinfo.setdefault("Type", nodelistBasic[0].getAttribute("Type"))
            imageinfo.setdefault("SizeZ", nodelistBasic[0].getAttribute("SizeZ"))
            imageinfo.setdefault("SizeC", nodelistBasic[0].getAttribute("SizeC"))
            imageinfo.setdefault("SizeT", nodelistBasic[0].getAttribute("SizeT"))
            imageinfo.setdefault("BigEndian", nodelistBasic[0].getAttribute("BigEndian"))
            imageinfo.setdefault("SignificantBits", nodelistBasic[0].getAttribute("SignificantBits"))

            listImagesinfo.append(imageinfo)

        return listImagesinfo

if __name__ == "__main__":

    reader = VsiReader(path="J:\\yyc\\1733479-2.vsi")
    strXml = reader.getMetadata()
    parser = XmlParser(strXml)
    info = parser.vsi_infoextract()
    domTree = Minidom.parseString(strXml)
    collection = domTree.documentElement
    infoImages = domTree.getElementsByTagName("Image")
    for infoImage in infoImages:
        if infoImage.hasAttribute("Name"):
            print("Name: ", infoImage.getAttribute("Name"))
    print("Done.")



