#!/usr/bin/python3

from CarFile import CarClass

def main():
  carObject_1=CarClass("BLUE","1956",120)
  carObject_2=CarClass("BLUE","1924",50)

  carObject_1.accelerate(50)
  carObject_1.accelerate(50)
  carObject_1.accelerate(50)

  carObject_1.decelerate(50)
  carObject_1.decelerate(50)
  carObject_1.decelerate(50)
  carObject_1.decelerate(50)

  carObject_2.accelerate(50)
  carObject_2.accelerate(50)
       
if __name__ == '__main__':
 main()


