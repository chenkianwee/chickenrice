import pyqtgraph as pg
import pyqtgraph.opengl as gl
from pyqtgraph.parametertree import Parameter, ParameterTree
from pyqtgraph.Qt import QtGui, QtCore
import sys

class TestGui(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupGUI()
        
        self.params = Parameter.create(name='ParmX', type='group', children=[dict(name='Buttonx', type='action'), dict(name='Buttony', type='action')])
        self.tree.setParameters(self.params, showTop=False)
        self.params.param('Buttonx').sigActivated.connect(self.save_citygml)
        self.params.param('Buttony').sigActivated.connect(self.build_citygml)
        
    def setupGUI(self):
        self.layout = QtGui.QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)
        
        self.splitter = QtGui.QSplitter()
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.layout.addWidget(self.splitter)
        
        self.tree = ParameterTree(showHeader=False)
        self.splitter.addWidget(self.tree)

        self.view3d = gl.GLViewWidget()
        #self.view3d.opts['distance'] = 10000
        
        self.gx = gl.GLGridItem()
        self.gx.rotate(90, 0, 1, 0)
        self.gx.translate(-10, 0, 0)
        self.view3d.addItem(self.gx)
        self.gy = gl.GLGridItem()
        self.gy.rotate(90, 1, 0, 0)
        self.gy.translate(0, -10, 0)
        self.view3d.addItem(self.gy)
        self.gz = gl.GLGridItem()
        self.gz.translate(0, 0, -10)
        self.view3d.addItem(self.gz)
        self.splitter.addWidget(self.view3d)

    def build_citygml(self):
        pass

    def save_citygml(self):
        pass    