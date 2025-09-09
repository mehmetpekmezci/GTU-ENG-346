import socket

class Node :
    def __init__(self, ip, nodeName):
        self.name=nodeName
        self.ip=ip
        self.timeout=5 # seconds
        self.sshport=22
    ## her fonksiyon self 'i alir, ama cagirirken bunu vermeyiz : node.checkSSH() gibi
    def checkSSH(self,port=22):
      self.sshport=port

      try:
        socket.setdefaulttimeout(self.timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.sshport))
      except OSError as error:
        self.checkSSHResult=False
      else:
        s.close()
        self.checkSSHResult=True


