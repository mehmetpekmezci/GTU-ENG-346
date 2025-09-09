import socket
import binascii
import time 
import traceback

class Multicaster :
    def __init__(self, multicast_ip, multicast_port):
        self.multicast_ip=multicast_ip
        self.multicast_port=int(multicast_port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        try:
          self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        except AttributeError:
          pass
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1)
        self.running=True

    def send(self):
        self.sock.sendto('Hello World!'.encode(), (self.multicast_ip, self.multicast_port))


    def receive(self):
       self.sock.bind((self.multicast_ip,self.multicast_port))
       while self.running:
        time.sleep(1)
        try:
           data, addr = self.sock.recvfrom(1024)
        except :
           traceback.print_exc()
        else:
           print ('Received Data = %s from %s' % (data.decode(),addr))

