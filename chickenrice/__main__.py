import sys

import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
from chickenrice.app import TestGui

def main(args=None):
    if args is None:
        args = sys.argv[1:]
        
    pg.mkQApp()
    win = TestGui()
    win.setWindowTitle("TestApp")
    win.show()
    win.resize(1100,700)
    
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

if __name__ == '__main__':
    main()
    