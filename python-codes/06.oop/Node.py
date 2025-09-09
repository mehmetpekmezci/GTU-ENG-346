import socket 

class Node :
    def __init__(self, ip, nodeName):
        self.name=nodeName
        self.ip=ip
        self.sshport=22
        self.timeout=5 # seconds

    def checkSSH(self, alternative_port_non_mandatory_argument=None):
      try:
        socket.setdefaulttimeout(self.timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if alternative_port_non_mandatory_argument is not None:
        
         s.connect(
           (self.ip,alternative_port_non_mandatory_argument)
          )
        else:
         s.connect((self.ip,self.sshport))
        
      except OSError as error:
        return False
      else:
        s.close()
        return True

    def getNodeType(self):
         return "Standard Node"
