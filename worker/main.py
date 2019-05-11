# -*- coding: utf-8 -*-
import sys
from builtins import print
from queue import Queue
from PyQt5 import QtWidgets , QtCore ,QtGui , QtNetwork
from ma import Ui_MainWindow
import socket
import time

q=Queue(2)

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
        self.buff= 1024
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



class SlowTask(QtCore.QThread):
    updated = QtCore.pyqtSignal(int)
    Queue_up = QtCore.pyqtSignal(int)

    running = False

    def __init__(self, *args, **kwargs):
        super(SlowTask, self).__init__(*args, **kwargs)
        self.percent = 0
        self.running = True

    def run(self):
        while self.running:
            print(self.percent)
            self.percent += 1
            self.percent %= 100
            if q.full():
                self.Queue_up.emit(1)
                time.sleep(0.1)
            q.put(self.percent)

    def stop(self):
        self.running = False

class test_app(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.query = Queue()
        self.handle = QtCore.QThread()
        #self.receiver = MessageReceiver(queue)
        self.start.clicked.connect(self.start_t)
        self.stop.clicked.connect(self.close_t)

    def start_t(self):
        self.task = server(self)
        self.task.Queue_up.connect(self.t_update)
        self.task.start()
        print("+task")
        return 1

    def t_update(self):
        l=q.get()
        print("test.{}".format(l))

    def close_t(self):
        print("test start ")
        self.task.stop()
        return 1

def main():

    app=QtWidgets.QApplication(sys.argv)
    window=test_app()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()