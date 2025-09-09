def main():
   LIST1=[ 1,3,8,4 ]
   print(f"LIST1:{LIST1}")
   print(f"len(LIST1):{len(LIST1)}")
   LIST1.append("abc")
   print(f"LIST1:{LIST1}")
   print(f"LIST1[4]:{LIST1[4]}\n")
   
   DICT1={
          "key1":"value1",
          "key2":{
          "key2.1":"value2.1","key2.2":"value2.2"}
          }
   print(f"DICT1:{DICT1}")
   print(f"DICT1.keys():{DICT1.keys()}")
   print(f"DICT1[key1]:{DICT1['key1']}")
   DICT1["key3"]="value3"
   print(f"DICT1:{DICT1}")

if __name__ == '__main__':
 main()


