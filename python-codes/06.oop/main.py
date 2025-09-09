#!/usr/bin/python3

from GWNode  import GWNode
from Node  import Node

def main():
  nodeList=[]

  try: 
   with open("hosts", "r") as f:
       data = f.read().splitlines()
  except FileNotFoundError :
       print("Can not find a ./hosts file containing "+
             "'ip,hostname' list of nodes")
       exit(1)
  for line in data:
      ip_and_name=line.split(',')
      ip=ip_and_name[0]
      name=ip_and_name[1]
      if ip.startswith("127"):
         nodeList.append(GWNode(ip,name,"gateway"))
      else:
         nodeList.append(Node(ip,name))
  for node in nodeList:
      print(f"Checking if we can reach {node.name} " +
            f"by {node.ip} at port 22 , this is a "+
            f"node of type :{node.getNodeType()}"
            )
      if node.checkSSH() :
          print(f"Yes we can reach {node.name} "+ 
                f"by {node.ip} at port 22 ")
      else:
          print(f"Sorry we can not reach {node.name} by "+ 
                f"{node.ip} at port 22")

       
if __name__ == '__main__':
 main()


