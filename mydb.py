import mysql.connector

database=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password123'
)


#prepare a cursor object

cursorObject=database.cursor()

#create a database
cursorObject.execute("CREATE DATABASE mydb")

print('All Done')
