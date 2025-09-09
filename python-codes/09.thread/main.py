import threading
from Node import Node

nodeList=[]
nodeList.append(Node("127.0.0.1","our_server"))
nodeList.append(Node("192.168.1.2","public_server1"))
nodeList.append(Node("192.168.1.2","public_server2"))
nodeList.append(Node("192.168.1.2","public_server3"))



threads=[]

for node in nodeList:
    #t = threading.Thread(target=node.checkSSH, args = (20222,))
    t = threading.Thread(target=node.checkSSH, args = (22,))
    threads.append(t)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()


for node in nodeList:
    if node.checkSSHResult :
        print("Node "+node.name+" is reachable through ssh port:"+str(node.sshport))
    else:   
        print("Node "+node.name+" is NOT reachable through ssh port:"+str(node.sshport))


