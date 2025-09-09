#!/usr/bin/python3
import time

def main():
  while True:
   try:
     with open("deneme.txt", "r") as f:
       data = f.read().splitlines()
     print(data)
     if "exit" in data:
         exit(0)
   except FileNotFoundError:
     print("deneme.txt file not found...")
   time.sleep(1)

if __name__ == '__main__':
 main()


