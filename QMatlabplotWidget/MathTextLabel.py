from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtCore import Qt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MathTextLabel(QtWidgets.QWidget):

    def __init__(self, mathText="",fontscale=1, dpi=80, **kwargs):
        super().__init__(**kwargs)
        self.setText(mathText, fontscale, dpi, **kwargs)

    def __init__(self, parent, **kwargs):
        super().__init__(**kwargs)
        self.setParent(parent)

    def setText(self, mathText="", fontscale=1.0, dpi=80,**kwargs):
        self.fontscale = fontscale
        self.dpi = dpi
        l=QVBoxLayout(self)
        l.setContentsMargins(0,0,0,0)
        r,g,b,a=self.palette().base().color().getRgbF()
        if self.parent():
            r,g,b,a=self.parent().palette().color(QtGui.QPalette.Window).getRgbF()
        self._figure=Figure(edgecolor=(r,g,b), facecolor=(r,g,b))
        self._canvas=FigureCanvas(self._figure)
        l.addWidget(self._canvas)
        self._figure.clear()
        text=self._figure.suptitle(
            mathText,
            x=0.0,
            y=1.0,
            horizontalalignment='left',
            verticalalignment='top',
            backgroundcolor=(r,g,b,a),
            # size=QtGui.QFont().pointSize()*fontscale,
            **kwargs
            #color='red'
        )
        self._canvas.draw()
        (x0,y0),(x1,y1)=text.get_window_extent().get_points()
        w=x1-x0; h=y1-y0
        self._figure.set_size_inches(w/dpi, h/dpi)
        self.setFixedSize(w,h)

if __name__=='__main__':
    from sys import argv, exit

    class Widget(QtWidgets.QWidget):
        def __init__(self, **kwargs):
             super().__init__(**kwargs)

             l=QVBoxLayout(self)
             mathText=r'$X_k = \sum_{n=0}^{N-1} x_n . e^{\frac{-i2\pi kn}{N}}$'
             mlabel = MathTextLabel(mathText)
             l.addWidget(mlabel, alignment=Qt.AlignHCenter)
             # mlabel.setText(r'$\alpha=\beta$')

    a=QtWidgets.QApplication(argv)
    win = QtWidgets.QWidget()
    mathText=r'$X_k = \sum_{n=0}^{N-1} x_n . e^{\frac{-i2\pi kn}{N}}$'
    mlabel = MathTextLabel(win)
    mlabel.setText(mathText, color='red')
    mlabel.move(100,100)
    win.show()
    # mlabel = MathTextLabel(mathText)
    # mlabel.setParent(win)
    # mathText = r"$\alpha = \beta$"
    # mlabel.setText(mathText)
    # w=Widget()
    # w.show()
    #w.raise_()
    exit(a.exec())