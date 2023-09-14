import pymysql

db = pymysql.connect(
    host='10.13.2.4',
    port=3307,
    user='root',
    passwd='123456',
    db='mydb')
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print("database version: %s" % data)
db.close()
