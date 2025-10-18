import sys
import os
import pickle

def main():
   if len(sys.argv) < 2 :
       print("Usage: python3 main.py <first_argument>")
       exit(1)
   FIRST_ARGUMENT=str(sys.argv[1])
   print(f"FIRST_ARGUMENT={FIRST_ARGUMENT}")
   path = FIRST_ARGUMENT
   dir_list = os.listdir(path)
   print("Files and directories in '", path, "' :")
   # prints all files
   print(dir_list)
   with open('filename.pickle', 'wb') as handle:
     pickle.dump(dir_list, handle, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
 main()


