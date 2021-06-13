import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="mysql_user",
  password="tajnehaslo"
)

print('Connection success')