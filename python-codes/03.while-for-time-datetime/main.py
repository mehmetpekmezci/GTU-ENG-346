#!/usr/bin/python3

import time
import datetime

def main():

   LIST1=[ 1,3,8,3,7,8,9,4 ]

   for value in LIST1 :
      print(f"{value}")

   for index in range(len(LIST1)) :
      print(f"LIST1[{index}]={LIST1[index]}")

   DICT1={"key1":"value1","key2":{"key2.1":"value2.1","key2.2":"value2.2"}}

   for key in DICT1.keys() :
      print(f"\nDICT1[{key}]={DICT1[key]}")

   i=0
   while i<5 :
       print(i)
       print("Current Time (human Readable) :"+str(datetime.datetime.now()))
       print("Current timestamp:"+str(time.time()))
       i=i+1
       time.sleep(1)

if __name__ == '__main__':
 main()


