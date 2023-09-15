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
#数据库更新语句
sql = "update employeetest set age = age + 2 where sex = '%c'" %('M')
try:
    #执行SQL语句
    cursor.execute(sql)
    #提交到数据库执行
    db.commit()
except:
    db.rollback()
    print('Error to update data.')
#关闭数据库连接
db.close()

