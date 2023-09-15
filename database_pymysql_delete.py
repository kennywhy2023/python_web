import pymysql

#连接数据库
db = pymysql.connect(
    host='10.13.2.4',
    port=3307,
    user='root',
    passwd='123456',
    database='mydb',
    charset='utf8')

#获取操作游标
cursor = db.cursor()
#数据库删除语句
sql = "delete from employeetest where age = %s" %(20)
try:
    #执行SQL语句
    cursor.execute(sql)
    #提交到数据库执行
    db.commit()
except:
    db.rollback()
    print('Error to delete data.')
#关闭数据库连接
db.close()

