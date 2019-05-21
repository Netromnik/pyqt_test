from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import  time
from multiprocessing import Process  ,pool
from PyQt5.QtWidgets import  QSizePolicy
import random

class canva_Mat(FigureCanvas):
    """This class pronting 3 graphic for acran"""
    N=100
    def __init__(self, parent=None):
        self.start_time = time.time()
        self.fig = Figure(dpi=100)
        self.axes_p = self.fig.add_subplot(3,1,1)
        self.axes_r = self.fig.add_subplot(3,1,2)
        self.axes_y = self.fig.add_subplot(3,1,3)
        self.data_y = [0] * self.N
        self.data_p = [0] * self.N
        self.data_r = [0] * self.N
        self.time = [0] * self.N
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

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


    def Prepaint(self):
            self.setTime()
            self.axes_r.clear()
            self.axes_y.clear()
            self.axes_p.clear()
            self.axes_y.plot(self.time, self.data_y,marker='+',linewidth=1,linestyle='dashed')
            self.axes_p.plot(self.time, self.data_p,marker='+',linewidth=1,linestyle='dashed')
            self.axes_r.plot(self.time, self.data_r,marker='+',linewidth=1,linestyle='dashed')
            self.style()
    def paint(self):
        self.Prepaint()
        FigureCanvas.draw(self)

    def style(self):
        self.axes_y.set_ylabel('yaw')
        self.axes_p.set_ylabel('pitch')
        self.axes_r.set_ylabel('roll')
        self.axes_p.set_xlabel('tik')
        self.axes_p.grid(True)
        self.axes_y.grid(True)
        self.axes_r.grid(True)
