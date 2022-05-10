from PySide6.QtCore import QSize
from PySide6 import QtWidgets
from PySide6.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib.figure import Figure
import matplotlib
from matplotlib import rcParams

# Ensure using PyQt5 backend
matplotlib.use('QT5Agg')

# Matplotlib canvas class to create figure
class MatplotlibCanvas(Canvas):
    def __init__(self):
        #  create widgets
        self.figure = Figure()
        self.axes = self.figure.subplots(2,2)
        Canvas.__init__(self, self.figure)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)


class MatplotlibWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.canvas = MatplotlibCanvas()
        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        self.vbl = QtWidgets.QVBoxLayout()  # Set box for plotting
        self.vbl.addWidget(self.toolbar)
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)

    def set_plot_params(self, title='', xlabel='', ylabel='',
                 xlim=None, ylim=None, xscale='linear', yscale='linear',
                 width=4, height=3, dpi=100):
        # self.canvas.axes.set_title(title)
        # self.canvas.axes.set_xlabel(xlabel)
        # self.canvas.axes.set_ylabel(ylabel)
        # if xscale is not None:
        #     self.canvas.axes.set_xscale(xscale)
        # if yscale is not None:
        #     self.canvas.axes.set_yscale(yscale)
        # if xlim is not None:
        #     self.canvas.axes.set_xlim(*xlim)
        # if ylim is not None:
        #     self.canvas.axes.set_ylim(*ylim)
        self.canvas.axes = self.canvas.figure.clear()
        self.canvas.axes = self.canvas.figure.subplots(1,1)
        # self.canvas.draw()
        # self.canvas.flush_events()


    # def sizeHint(self):
    #     return QSize(*self.get_width_height())

    # def minimumSizeHint(self):
    #     return QSize(10, 10)

if __name__=='__main__':
    import sys
    a = QtWidgets.QApplication(sys.argv)
    win = MatplotlibWidget()
    win.set_plot_params()
    win.show()
    sys.exit(a.exec())