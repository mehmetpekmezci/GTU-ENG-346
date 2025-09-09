import mysql.connector
# sudo apt install libmysqlclient-dev
# pip3 install mysql mysql-client mysql-connector

mydb = mysql.connector.connect(
  host="localhost",
  user="denemeu",
  password="denemep",
  database="deneme",
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM deneme1 where id=0")

myresult = mycursor.fetchall()

for x in myresult:
  print(x[0])
  print(x[1])
