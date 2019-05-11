from multiprocessing import Process ,Queue
import  socket



class server():
    def __init__(self):
        self.q=Queue()
        self.socadd  = ("192.168.4.1", 989)
        self.soc = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    def run(self):
            print(self.soc.sendto(str.encode("sad"), self.socadd))
            while 1:
                msg = self.soc.recvfrom(1024)
                l = [float(i) for i in str(msg[0])[6:-4].split(";")]
                self.q.put(l)

if __name__ == '__main__':
    s=server()
    process_one = Process(target=s.run, args=())
    process_one.start()
    while 1:
        if s.q.empty():
            continue
        print(s.q.get())