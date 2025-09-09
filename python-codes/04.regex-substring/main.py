#!/usr/bin/python3
import re

def main():

   my_string = 'We are roots of havelsan :)'

   company = my_string[16:24]  

   print(company)
 
   print(my_string.split())

   if "root" in my_string:
       print("This string contains root word")

   if my_string.startswith("We"):
       print("This string starts with 'We'")

   if my_string.endswith(":)"):
       print("This string ends with ':)'")

   print(re.findall("^We.*havelsan", my_string)) 
   print(re.findall("^We.*havelsan$", my_string)) 
   print(re.findall("havelsan", my_string)) 
   print("My ip adress is 10.0.15.256 and yours is 10.0.5.13") 
   print(re.findall("(?:[0-9]{1,3}\.){3}[0-9]{1,3}",
         "My ip adress is 10.0.15.256 and yours is 10.0.5.13")) 
if __name__ == '__main__':
 main()


