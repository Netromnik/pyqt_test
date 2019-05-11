
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QBrush, QPen
from queue import Queue

from form import  Ui_MainWindow

import socket
import time

q=Queue(1)

class server(QtCore.QThread):

    updated = QtCore.pyqtSignal(int)
    Queue_up = QtCore.pyqtSignal(int)
    running = False

    def __init__(self, *args, **kwargs):
        super(server, self).__init__(*args, **kwargs)
        self.percent = 0
        self.soc()
        self.send()
        self.running = True

    def soc(self):
        self.socket = ("192.168.4.1", 989)
        # Create a UDP socket at client side
        self.UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        # Send to server using created UDP socket
    def send(self):
        self.mess= "hello"
        self.sendmess= str.encode(self.mess)
        self.UDPClientSocket.sendto(self.sendmess, self.socket)

    def run(self):
        while self.running:
            time.sleep(0.10)
            msgFromServer = self.UDPClientSocket.recvfrom(1024)
            msg = "{}".format(msgFromServer[0])
            l = [float(i) for i in str(msg)[6:-4].split(";")]
            if q.full():
                self.Queue_up.emit(1)
                time.sleep(0.1)
            q.put(l)
            print(l)

    def stop(self):
        self.running = False



class test_app(QtWidgets.QMainWindow,Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self._rotate=10
        self.setupUi(self)
        self.scen_x=QtWidgets.QGraphicsScene()
        self.scen_y=QtWidgets.QGraphicsScene()
        self.scen_z=QtWidgets.QGraphicsScene()
        self.xy.setScene(self.scen_x)
        self.yz.setScene(self.scen_y)
        self.xz.setScene(self.scen_z)
        self.xy.show()
        self.xz.show()
        self.yz.show()
        self.Gra_V= [self.xy, self.yz, self.xz]
        self.scen=[self.scen_x,self.scen_y,self.scen_z]

        #creat elipse
        [i.addEllipse(0,-100, self.yz.width()*2, self.yz.width()*2) for i in self.scen]

        #creat polka
        [i.addRect(0,0,self.yz.width()*2,2,brush=QBrush(QtCore.Qt.yellow),pen=QPen(QtCore.Qt.darkYellow)) for i in self.scen]

        #self._status_update_timer = QtCore.QTimer(self)
        #self._status_update_timer.setSingleShot(False)
        #self._status_update_timer.timeout.connect(lambda: self._update())
        #self._status_update_timer.start(50)
        #self.G_V.centerOn(self.G_V.width()/2, self.G_V.height()/2)


        self.handle = QtCore.QThread()
        #self.receiver = MessageReceiver(queue)
        self.ok.clicked.connect(self.start_t)
        self.end.clicked.connect(self.close_t)
        self.o_l=[float(0),float(0),float(0)]
    #def to timers
    def _update(self):
        self._rotate=self._rotate+0.1
        [i.rotate(self._rotate) for i in self.Gra_V]
        [i.update() for i in self.Gra_V]

    def start_t(self):
        self.task = server(self)
        self.task.Queue_up.connect(self.t_update)
        self.task.start()
        print("+task")
        return 1

    def t_update(self):
        l=q.get()

        self.xy.rotate(self.o_l[0]-l[0])
        self.xz.rotate(self.o_l[1]-l[1])
        self.yz.rotate(self.o_l[2]-l[2])
        [i.update() for i in self.Gra_V]
        self.o_l=l
    def close_t(self):
        print("test start ")
        self.task.stop()
        return 1


if __name__ == "__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    window=test_app()
    window.show()
    sys.exit(app.exec_())