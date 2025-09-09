import sys

def main():
   if len(sys.argv) < 2 :
       print("Usage: python3 main.py <first_argument>")
       exit(1)
   FIRST_ARGUMENT=float(sys.argv[1])
   COEFFICIENT=6.75
   RESULT=COEFFICIENT*FIRST_ARGUMENT
   print(f"RESULT={RESULT}")
   USER_INPUT=input("Enter Another VALUE: ")
   RESULT=COEFFICIENT*float(USER_INPUT)
   print(f"2. RESULT={RESULT}")

if __name__ == '__main__':
 main()


