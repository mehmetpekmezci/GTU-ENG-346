import socket
import binascii
import time 
import traceback
from Logger import Logger
import logging

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
        self.logger=Logger("Mulicaster")

    def send(self):
        self.sock.sendto('Hello World!'.encode(), (self.multicast_ip, self.multicast_port))
        self.logger.debug(f"Sent Message : Helleo World!")


    def receive(self):
       self.logger.warn("We are starting to bind :"+self.multicast_ip+":"+str(self.multicast_port))
       self.sock.bind((self.multicast_ip,self.multicast_port))
       counter=0
       while self.running:
        self.logger.debug(f"Counter={counter}")
        counter+=1
        time.sleep(1)
        try:
           #data, addr = sock.recvfrom(1024) ## ERROR CASE
           data, addr = self.sock.recvfrom(1024)
        except :
           self.logger.error("We have an error while self.sock.recvfrom")
           traceback.print_exc()
           if counter > 10 :
              counter=0
              self.logger.critical("We have an error while self.sock.recvfrom for 10 seconds !!!")

        else:
           self.logger.info('Received Data = %s from %s' % (data.decode(),addr))

