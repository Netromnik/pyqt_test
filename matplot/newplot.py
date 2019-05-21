import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from form import Ui_MainWindow
import random
import time


class canva_Mat(FigureCanvas):
    """This class pronting 3 graphic for acran"""
    N=25
    def __init__(self, parent=None):
        self.start_time = time.time()
        self.fig = Figure()
        self.axes_y = self.fig.add_subplot(4,1,1)
        self.axes_p = self.fig.add_subplot(4,1,3)
        self.axes_r = self.fig.add_subplot(4,1,4)
        self.data_y = [0] * self.N
        self.data_p = [0] * self.N
        self.data_r = [0] * self.N
        self.time = [0] * self.N
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def setDate_y(self, x):
        self.data_y = self.data_y[1:self.N]
        self.data_y.append(x)
        self.paint()


    def setDate_p(self, x):
        self.data_p = self.data_p[1:self.N]
        self.data_p.append(x)
        self.paint()

    def setDate_r(self, x):
        self.data_r = self.data_r[1:self.N]
        self.data_r.append(x)
        print(x)
        self.paint()
    def setTime(self):
        self.time = self.time[1:len(self.time)]
        self.time.append(time.time() - self.start_time)

    def setDate(self,yaw,pitch,roll):
        self.data_y = self.data_y[1:self.N]
        self.data_p = self.data_p[1:self.N]
        self.data_r = self.data_r[1:self.N]
        self.data_y.append(yaw)
        self.data_p.append(pitch)
        self.data_r.append(roll)
        self.paint()

    def paint(self):
        self.setTime()
        self.axes_r.clear()
        self.axes_y.clear()
        self.axes_p.clear()
        self.axes_y.plot(self.time, self.data_y)
        self.axes_p.plot(self.time, self.data_p)
        self.axes_r.plot(self.time, self.data_r)
        FigureCanvas.draw(self)

class GUI(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(GUI, self).__init__(parent)
        self.i = 0
        self.setupUi(self)
        self.sc = canva_Mat(self.widget)
        self.gridLayout.addWidget(self.sc, 0, 1, 1, 1)
        self._status_update_timer = QtCore.QTimer(self)
        self._status_update_timer.setSingleShot(False)
        self._status_update_timer.timeout.connect(self.graf_update)
        self._status_update_timer.start(10)

    def graf_update(self):
        self.i += 1
        # self.sc.update((random.random(), random.random(), random.random()))
        #self.sc.update()
        self.sc.setDate(random.random(),random.random(),random.random())


if __name__ == '__main__':
    start_time = time.time()
    app = QApplication(sys.argv)
    prog = GUI()
    prog.showMaximized()
    sys.exit(app.exec_())
