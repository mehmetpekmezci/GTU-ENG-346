#!/usr/bin/python3

def main():
  ## PREFER THIS
  with open("deneme.txt", "r") as f:
       data = f.read().splitlines()
  print(data)
  for line in data:
      print(line)
  print("\n\n--------------------------\n\n")
  with open("deneme.txt", "r") as f:
       data = f.readlines()
  print(data)
  for line in data:
      print(line)

  record_file = open("./deneme1.txt", "w")
  record_file.write("We are roots of Havelsan 1\n")
  record_file.write("We are roots of Havelsan 2\n")
  record_file.close()

  
  record_file = open("./deneme1.txt", "r")
  print(record_file.read())
  record_file.close()


  print("\n\n--------------------------\n\n")

  record_file = open("./deneme1.txt", "w")
  record_file.write("We are roots of Havelsan 3\n")
  record_file.write("We are roots of Havelsan 4\n")
  record_file.close()

  record_file = open("./deneme1.txt", "r")
  print(record_file.read())
  record_file.close()

  print("\n\n--------------------------\n\n")


  record_file = open("./deneme1.txt", "a")
  record_file.write("We are roots of Havelsan 5\n")
  record_file.write("We are roots of Havelsan 6\n")
  record_file.close()

  record_file = open("./deneme1.txt", "r")
  print(record_file.read())
  record_file.close()

if __name__ == '__main__':
 main()


